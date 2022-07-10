import os
import sys

import email
import file
import parser
from utils import check_arguments

if __name__ == '__main__':
    try:
        dir_list = os.listdir('emails')  # list all files from directory
    except IOError:
        print('Cannot find directory with email files')
        sys.exit()

    emails_list = []

    for file_path in dir_list:  # reading all files from directory
        f = file.File(file_path)
        f.get_emails_from_file(emails_list)

    correct_emails = []
    correct_emails_text = []  # additional array to check duplicates
    incorrect_emails = []

    for email_text in emails_list:
        email_obj = email.Email(email_text)
        if email_obj.correct:
            if email_text not in correct_emails_text:  # remove duplicates
                correct_emails.append(email_obj)
                correct_emails_text.append(email_text)
        else:
            incorrect_emails.append(email_obj)

    # parse arguments to program if they are correct
    if check_arguments():
        cli_parser = parser.Parser()
        cli_parser.call_functions(correct_emails, incorrect_emails)  # call function that matches to program args
    else:
        print('Type -h or --help as argument to check correct commands')
