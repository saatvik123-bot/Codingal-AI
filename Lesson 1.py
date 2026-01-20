print("Hello! I am AI bot !! What's your name : ")

name = input()

print( f"Nice to meet you, {name} !")

print("How are you feeling (good/bad): ")

mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!!")
elif mood == "bad":
    print("It's ok no problem!!")
else:
    print("I understand that you cant say your feelings!!")

print("Thank You So much have a great day !!")