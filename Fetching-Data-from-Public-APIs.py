import requests

def get_random_cat_fact():
    """Fetch a random cat fact from the cat fact API."""
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    if response.status_code == 200:
       
        print(f"Full JSON Response: {response.json()}")

        joke_data = response.json()
        return joke_data['fact']
    else:
        return "Failed to retrieve cat facts."
    

def main():
    print("Welcome to the Random cat fact Generator!")


    while True:
        user_input = input("Press Enter to get a new catfaact, or type 'q'/'exit' to quit: ").strip().lower()

        if user_input in ('q', 'exit'):
            print("GoodBye!")
            break

        joke = get_random_cat_fact()
        print(joke)

if __name__ == "__main__":
    main()