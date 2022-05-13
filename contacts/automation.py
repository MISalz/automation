import re


def clean(number_string):
    # cleaned_number = number_string.replace('(', '')
    # cleaned_number = number_string.replace(')', '-')
    # cleaned_number = number_string.replace('.', '-')
    number_string = re.sub(r"\(", '', number_string)
    number_string = re.sub(r"\)", '-', number_string)
    number_string = re.sub(r"\.", '-', number_string)

    if len(number_string) == 8:
        number_string = "206-" + number_string

    return number_string


def validate_phone():
    phone_pattern = re.compile(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

    with open("assets/potential-contacts.txt") as numbers:
        lines = numbers.read()

    match_numbers = re.findall(phone_pattern, lines)

    cleaned = []

    for x in match_numbers:
        cleaned.append(clean(x))

    cleaned.sort()
    print(cleaned)
    report = "\n".join(cleaned)

    with open("contacts/phone_numbers.txt", "w+") as phone_list:
        phone_list.write(report)


validate_phone()


def validate_email():
    email_pattern = re.compile(r"[a-zA-Z\d._-]+@[a-zA-Z\d._-]+\.[a-zA-Z\d_-]+")

    with open("assets/potential-contacts.txt") as emails:
        lines = emails.read()

    match_emails = re.findall(email_pattern, lines)

    match_emails.sort()
    # print(match_emails)

    email_report = "\n".join(match_emails)

    with open("contacts/emails.txt", "w+") as email_string:
        email_string.write(email_report)


validate_email()
