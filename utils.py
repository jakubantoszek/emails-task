import sys


def show_incorrect_emails(incorrect_emails):
    print("Invalid emails (" + str(len(incorrect_emails)) + "):")
    for email in incorrect_emails:
        print("    " + str(email))


def search_by_text(correct_emails, text):
    # find emails that match the text
    matches = []
    for email in correct_emails:
        if text in str(email):
            matches.append(email)

    if len(matches) > 0:
        print("Found emails with '" + text + "' in email (" + str(len(matches)) + "):")
        for matched_email in matches:
            print("    " + str(matched_email))
    else:
        print("Emails with '" + text + "' not found")


def group_by_domain(correct_emails):
    dictionary = {}  # domain is key, list of emails is value
    for email in correct_emails:
        if email.domain in dictionary:
            dictionary[email.domain].append(str(email))
        else:
            dictionary[email.domain] = [str(email)]

    for domain in sorted(dictionary.keys()):
        print('Domain ' + domain + ' (' + str(len(dictionary[domain])) + '):')
        for email in sorted(dictionary[domain]):
            print("    " + email)


def find_emails_not_in_logs(correct_emails, path):
    logs_emails = []
    not_found_emails = []

    try:
        with open(path) as logs_file:
            # read all emails from logs file
            lines = logs_file.read().splitlines()
            for line in lines:
                logs_emails.append(line[47:-2])  # get only e-mail from line (everything before it has constant length)

        for email in correct_emails:
            if str(email) not in logs_emails:
                not_found_emails.append(str(email))

        print("Emails not sent (" + str(len(not_found_emails)) + "):")

        for nf_email in sorted(not_found_emails):
            print("    " + nf_email)
    except IOError:
        print('Cannot open the file, make sure the path is correct')


def check_arguments():
    # check if arguments given to program are correct
    args = sys.argv

    if len(args) == 1:
        print('There are no commands')
        return False
    if len(args) > 3:
        print('There are too much commands or arguments')
        return False
    if args[1] in ['--incorrect-emails', '-ic', '--group-by-domain', '-gbd']:
        if len(args) == 3:
            print('There are too much commands or arguments')
            return False
        return True
    if args[1] in ['--search', '-s', '--find-emails-not-in-logs', '-feil']:
        if len(args) == 2:
            print('You must add argument to command')
            return False
        elif args[2][0] == '-':
            print("Wrong argument to command, - can't be first character")
            return False
        return True
    elif args[1] not in ['--help', '-h']:
        print('Wrong commands')
        return False

    return True
