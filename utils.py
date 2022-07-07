def show_incorrect_emails(incorrect_emails):
    print("Invalid emails (" + str(len(incorrect_emails)) + "):")
    for email in incorrect_emails:
        print("    " + str(email))


def search_by_text(correct_emails, text):
    matches = []
    for email in correct_emails:
        if text in str(email):
            matches.append(email)

    print("Found emails with '" + text + "' in email (" + str(len(matches)) + "):")
    for matched_email in matches:
        print("    " + str(matched_email))
