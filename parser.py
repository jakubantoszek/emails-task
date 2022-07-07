import argparse

from utils import *


class Parser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser()

        self.add_arguments()
        args = self.__parser.parse_args()

        # add commands variables
        self.__ic = args.incorrect_emails
        self.__search = args.search
        self.__gbd = args.group_by_domain
        self.__feil = args.find_emails_not_in_logs

    def add_arguments(self):
        self.__parser.add_argument('--incorrect-emails', '-ic',
                                   action='store_true',
                                   help='show incorrect emails')
        self.__parser.add_argument('--search', '-s',
                                   metavar='str',
                                   action='store',
                                   type=str,
                                   help='search emails by text')
        self.__parser.add_argument('--group-by-domain', '-gbd',
                                   action='store_true',
                                   help='group emails by domain')
        self.__parser.add_argument('--find-emails-not-in-logs', '-feil',
                                   metavar='path_to_logs_file',
                                   action='store',
                                   type=str,
                                   help='find emails that are not in the logs file')

    def call_functions(self, correct_emails, incorrect_emails):
        if self.__ic:
            show_incorrect_emails(incorrect_emails)
        if self.__search is not None:
            search_by_text(correct_emails, self.__search)
        if self.__gbd:
            group_by_domain(correct_emails)
        if self.__feil is not None:
            find_emails_not_in_logs(correct_emails, self.__feil)
