import os

if __name__ == '__main__':
    dir_list = os.listdir('emails')
    for file in dir_list:
        print(file)