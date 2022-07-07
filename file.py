import os.path
import pandas as pd


class File:
    def __init__(self, file_path):
        self.__path = file_path

        split_path = os.path.splitext(file_path)
        self.__extension = split_path[1]

    def get_emails_from_file(self, emails_list):
        if self.__extension == '.txt':
            with open('emails/' + self.__path) as txt_file:
                lines = txt_file.read().splitlines()
                for line in lines:
                    emails_list.append(line)

        if self.__extension == '.csv':
            data = pd.read_csv('emails/' + self.__path, sep=';')
            for row in data['email']:
                emails_list.append(row)
