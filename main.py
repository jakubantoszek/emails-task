import os
import file

if __name__ == '__main__':
    dir_list = os.listdir('emails')
    emails_list = []

    for file_path in dir_list:
        f = file.File(file_path)
        f.get_emails_from_file(emails_list)
