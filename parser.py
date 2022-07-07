import argparse
from utils import *


class Parser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser()

        self.add_arguments()
        args = self.__parser.parse_args()

        # add commands variables
        self.__ic = args.incorrect_emails

    def add_arguments(self):
        self.__parser.add_argument('--incorrect-emails', '-ic',
                                   action='store_true',
                                   help='show incorrect emails')

    def call_functions(self, correct_emails, incorrect_emails):
        if self.__ic:
            show_incorrect_emails(incorrect_emails)
