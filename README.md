# gitlab-issues

Script to export issues from a gitlab project to a csv file for dissemination/reporting.

Defaults to the project defined in `settings.py`, but this can be changed on the command line
Requires a file `_credentials.py` in the same directory containing a USERNAME and PASSWORD for the server given in `settings.py`

```
usage: export_issues.py [-h]
                        [-s [{opened,closed,reopened} [{opened,closed,reopened} ...]]]
                        [-f FILENAME]
                        [-p PROJECT]

Process and export issues from a gitlab project

optional arguments:
  -h, --help            show this help message and exit

  -s [{opened,closed,reopened} [{opened,closed,reopened} ...]], --state [{opened,closed,reopened} [{opened,closed,reopened} ...]]
                        export only issues with the given state

  -f FILENAME, --filename FILENAME
                        specify filename for output

  -p PROJECT, --project PROJECT
                        specify the project to export issues from
```
