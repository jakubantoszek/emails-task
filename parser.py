import argparse
from utils import *


class Parser:
    # TODO wyjatek - za duzo podanych argumentow
    # TODO wyjatek - niepoprawny argument
    def __init__(self):
        self.__parser = argparse.ArgumentParser()

        self.add_arguments()
        args = self.__parser.parse_args()

        # add commands variables
        self.__ic = args.incorrect_emails
        self.__search = args.search

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

    def call_functions(self, correct_emails, incorrect_emails):
        if self.__ic:
            show_incorrect_emails(incorrect_emails)
        if self.__search is not None:
            search_by_text(correct_emails, self.__search)
