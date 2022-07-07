import os
import email
import file
import parser
from utils import check_arguments

if __name__ == '__main__':
    dir_list = os.listdir('emails')
    emails_list = []

    for file_path in dir_list:
        f = file.File(file_path)
        f.get_emails_from_file(emails_list)

    correct_emails = []
    incorrect_emails = []
    for email_text in emails_list:
        email_obj = email.Email(email_text)
        if email_obj.correct:
            correct_emails.append(email_obj)
        else:
            incorrect_emails.append(email_obj)

    if check_arguments():
        cli_parser = parser.Parser()
        cli_parser.call_functions(correct_emails, incorrect_emails)
