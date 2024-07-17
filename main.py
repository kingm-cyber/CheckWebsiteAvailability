import requests


def take_user_website_list(filename):
    print(f"Type one website per line, and press ENTER when finished:\n\n")
    lines = []

    while True:
        try:
            line = input()

            if line == "":
                break
            if not line.startswith("https://") or line.startswith("http://"):
                line = "https://" + line

            lines.append(line)

        except EOFError:
            break

    with open(filename, 'w') as file:
        file.write(f"\n".join(lines) + "\n")

    with open(filename, 'r') as file:
        file.read()


def check_website_availability(filename):
    with open(filename, 'r') as file:
        websites = file.read().splitlines()

    for website in websites:
        try:
            response = requests.get(website)
            print(f"Website: {website} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Website Error: {e}")


user_list = "websites.txt"
take_user_website_list(user_list)
check_website_availability(user_list)