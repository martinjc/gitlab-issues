#stdlib imports
import os
import csv
import argparse

# external lib imports
import gitlab

# internal project imports          # settings.py stores project and server info
from settings import *              # credentials contains USERNAME and PASSWORD
from _credentials import *          # of user with permission to access the
                                    # project listed in settings

FIELDS = ['id', 'title', 'description', 'due_date', 'milestone', 'milestone_duedate', 'labels', 'web_url', 'author', 'assignees', 'last_updated', 'state']

def init():
    # initialise gitlab object and authorise for use
    gl = gitlab.Gitlab(COMSC_GITLAB_SERVER, email=USERNAME, password=PASSWORD, api_version=4)
    gl.auth()
    # make sure we have somewhere to output to
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    return gl


def issue_to_dict(issue):
    """
    Convert an issue to a dictionary suitable for outputting to csv
    """
    issue_data = {}
    issue_data['id'] = issue.id
    issue_data['title'] = issue.title
    issue_data['description'] = issue.description
    issue_data['due_date'] = issue.due_date
    issue_data['labels'] = '; '.join(issue.labels) if len(issue.labels) > 0 else ''
    issue_data['web_url'] = issue.web_url
    issue_data['author'] = issue.author.name
    issue_data['assignees'] = '; '.join([a['name'] for a in issue.assignees]) if len(issue.labels) > 0 else ''
    issue_data['last_updated'] = issue.updated_at
    issue_data['state'] = issue.state
    if issue.milestone:
        issue_data['milestone'] = issue.milestone.title
        issue_data['milestone_duedate'] = issue.milestone.due_date
    return issue_data

def export_issues(gl, project=PROJECT, state=None, labels=None, filename='issues.csv'):

    issues_data = []

    project = gl.projects.get(project)

    for issue in project.issues.list():
        # are we filtering by state or label?
        if state or labels:
            # if we're filtering by both, state must be correct and label must be in labels
            if state and labels and issue.state in state and set(issue.labels) & set(labels):
                issues_data.append(issue_to_dict(issue))
            # if we're filtering just by state then state must be correct
            elif state and not labels and issue.state in state:
                issues_data.append(issue_to_dict(issue))
            # if we're filtering by label then label must be in labels
            elif not state and labels and set(issue.labels) & set(labels):
                issues_data.append(issue_to_dict(issue))
        # if we're not filtering
        elif not state and not labels:
            issues_data.append(issue_to_dict(issue))

    with open(os.path.join(OUTPUT_DIRECTORY, 'issues.csv'), 'w') as output_file:

        writer = csv.DictWriter(f=output_file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(issues_data)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Process and export issues from a gitlab project")
    parser.add_argument('-s', '--state', action='store', nargs='*', default=None, choices=['opened', 'closed', 'reopened'], help="export only issues with the given state")
    parser.add_argument('-f', '--filename', action='store', default=None, help="specify filename for output")
    parser.add_argument('-p', '--project', action='store', default=PROJECT, help='specify the project to export issues from')
    parser.add_argument('-l', '--labels', action='store', nargs='*', default=None, help='specify a list of labels to filter by')
    args = parser.parse_args()

    gl = init()
    export_issues(gl, args.project, args.state, args.labels, args.filename)
