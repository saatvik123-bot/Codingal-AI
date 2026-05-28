import random

def random_story_generator():
    characters = ["A Knight", "A Astranaut", "A Wizzard", "A boy"]
    place = ["A Forest", "On Mars", "A Castel", "A Mountain"]
    action = ["Foght a Monster", "Found Alien's World", "Made a curing Medicine for the village", "Found Tressure"]

    character = random.choice(characters)
    places = random.choice(place)
    actions = random.choice(action)

    story = f"Once upon a time there was a {character} who was in a {places} and one day he {actions}"
    print(story)
    
random_story_generator()