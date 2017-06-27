# gitlab-issues

Script to export issues from a gitlab project to a csv file for dissemination/reporting.

Issues can be filtered by state (opened/closed/reopened) or by label.

Defaults to the project defined in `settings.py`, but this can be changed on the command line.
Requires a file `_credentials.py` in the same directory containing a USERNAME and PASSWORD for the server given in `settings.py`. For simplicity, a sample file is included which can be edited and renamed.

## Installation
Clone, install the requirements (python-gitlab) and off you go!

```
git clone git@gitlab.cs.cf.ac.uk:scm2mjc/gitlab-issues-reports.git
cd gitlab-issues-reports
pip install -r REQUIREMENTS.txt
```

Remember to create a file `_credentials.py` with your gitlab username and password!

## Usage

```
usage: export_issues.py [-h]
                        [-s [{opened,closed,reopened} [{opened,closed,reopened} ...]]]
                        [-f FILENAME] [-p PROJECT] [-l [LABELS [LABELS ...]]]

Process and export issues from a gitlab project

optional arguments:
  -h, --help            show this help message and exit
  -s [{opened,closed,reopened} [{opened,closed,reopened} ...]], --state [{opened,closed,reopened} [{opened,closed,reopened} ...]]
                        export only issues with the given state
  -f FILENAME, --filename FILENAME
                        specify filename for output
  -p PROJECT, --project PROJECT
                        specify the project to export issues from
  -l [LABELS [LABELS ...]], --labels [LABELS [LABELS ...]]
                        specify a list of labels to filter by
```
