import requests
from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset = True)

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"



def get_random_technology_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(Fore.BLUE +"Did you know?" + Fore.YELLOW +fact_data['text'])
    else:
        print(Fore.RED +"Failed to fetch fact")

get_random_technology_facts()
while True:
    user_input = input(Fore.GREEN +"Press Enter to get a random technology fact or type 'q' to quit...")
    if user_input.lower() == 'q':
        print(Fore.YELLOW +"Good Bye!")
        break
    get_random_technology_facts()
