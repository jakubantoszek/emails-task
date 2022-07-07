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

    print("Found emails with '" + text + "' in email (" + str(len(matches)) + "):")
    for matched_email in matches:
        print("    " + str(matched_email))


def group_by_domain(correct_emails):
    dictionary = {}
    for email in correct_emails:
        if email.domain in dictionary:
            dictionary[email.domain].append(str(email))
        else:
            dictionary[email.domain] = [str(email)]

    for domain in sorted(dictionary.keys()):
        print('Domain ' + domain + ' (' + str(len(dictionary[domain])) + '):')
        for email in sorted(dictionary[domain]):
            print("    " + email)
