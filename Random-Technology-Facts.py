import requests
from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset = True)

url = "https://api.chucknorris.io/jokes/random"



def chuck_norris_jokes():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(Fore.BLUE +"Did you know?" + Fore.YELLOW +fact_data['value'])
    else:
        print(Fore.RED +"Failed to fetch fact")

chuck_norris_jokes()
while True:
    user_input = input(Fore.GREEN +"Press Enter to get a open food facts or type 'q' to quit...")
    if user_input.lower() == 'q':
        print(Fore.YELLOW +"Good Bye!")
        break
    chuck_norris_jokes()