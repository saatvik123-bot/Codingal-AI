safe_message = [
    "Hi good morning!", "Good Evening!", "Do your homeworks"
]

spam_message = [
    "Click the link to win a new iphone", "Enter the otp to get 2.5 billion dollors",
    "Click the link to get new BMW "
]

user_input = input("Give the message over here to check if the message was safe or spam: ")

if user_input == safe_message:
  print("This is a safe message")
elif user_input == spam_message:
  print("This is a spam message")
else:
  print("Sorry can't identify!!!")