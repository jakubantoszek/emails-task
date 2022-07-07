def show_incorrect_emails(incorrect_emails):
    print("Invalid emails (" + str(len(incorrect_emails)) + "):")
    for email in incorrect_emails:
        print("    " + str(email))
