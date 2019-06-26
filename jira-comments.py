import argparse
from collections import defaultdict
from datetime import datetime, timedelta

import colorama
import lib_jira
import settings


def kwargs_or_default(setting_value):
    if setting_value:
        return dict(default=setting_value)
    return dict(required=True)


def auth(args):
    lib_jira.test_auth(
        server=args.server,
        username=args.username,
        password=args.password)
    lib_jira.save_credentials()


def _get_since(days_ago):
    since = datetime.now() - timedelta(days=days_ago)
    return str(since)


def get_comments(args):
    sprint = lib_jira.get_current_sprint(args.board)
    if not sprint:
        raise Exception('No active sprint found')
    since = _get_since(args.days)
    for issue in lib_jira.get_issues(sprint.id):
        comments = list(lib_jira.get_comments(issue.id, since))
        if len(comments) == 0:
            continue
        print '%s%s' % (colorama.Fore.CYAN, issue.fields.summary)
        print '%s%s/browse/%s' % (colorama.Fore.CYAN, settings.JIRA_BASE_URL, issue.key)
        for comment in comments:
            print ' %s%s%s: %s' % (colorama.Style.BRIGHT, comment.author, colorama.Style.NORMAL, comment.body.strip())
        print ''


if __name__ == '__main__':
    colorama.init(autoreset=True)

    parser = argparse.ArgumentParser(prog='jira-comments')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_auth = subparsers.add_parser('auth', help='Authenticate to JIRA')
    parser_auth.add_argument('--server', help='JIRA Server URL',
        **kwargs_or_default(settings.JIRA_BASE_URL))
    parser_auth.add_argument('--username', help='JIRA username',
        **kwargs_or_default(settings.JIRA_USERNAME))
    parser_auth.add_argument('--password', help='JIRA password',
        **kwargs_or_default(settings.JIRA_PASSWORD))
    parser_auth.set_defaults(func=auth)

    parser_report = subparsers.add_parser('list', help='List recent comments')
    parser_report.add_argument('--board', help='JIRA Board ID',
        **kwargs_or_default(settings.JIRA_BOARD_ID))
    parser_report.add_argument('--days', help='Days ago', type=int)
    parser_report.set_defaults(func=get_comments)

    args = parser.parse_args()
    args.func(args)
