# jira-comments - See recent JIRA comments inside a project

## Quickstart

```bash
virtualenv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
python jira-comments.py --help
```

### Authenticate to JIRA

Even if you use single sign on to authenticate to JIRA normally, you also have
a regular username and password. You can set it by going to
`Profile -> Change Password`. Once you have your password, you can authenticate
on the command-line.

```bash
>python jira-comments.py auth --server https://my-jira-host --username my-username@my-domain.com --password my-password
Successfully connected to: https://my-jira-host
Version: 7.8.0
Connected as: Your Name
Wrote credentials to ~/.jirarc
```

If successful, the credentials will be cached in `~/.jirarc` so that you don't
need to provide them again.


#### Query for Recent Comments

TODO

## Settings

You can create a `settings_override.py` file, and populate the following
settings:

### JIRA_BASE_URL, JIRA_USERNAME, JIRA_PASSWORD

The URL of your JIRA instance. This can be used instead of using `auth`
and creating a `~/.jirarc` file.

```python
JIRA_BASE_URL = 'https://my-jira-host'
JIRA_USERNAME = 'my-username@my-domain.com'
JIRA_PASSWORD = 'my-password'
```

### JIRA_BOARD_ID

The JIRA sprint board ID, from the sprint board URL 'RapidView' argument.

```python
JIRA_BOARD_ID = 1234
```
