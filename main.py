spam_keywords = ["win", "free", "offer", "money", "click", "buy now", "lottery", "congratulations", "prize", "wow", "won"]

def is_spam(message):
    message = message.lower()
    for word in spam_keywords:
        if word in message:
            return True
    return False

messages = [
    "Congratulations! You have won a free iPhone!",
    "Hey, can we meet tomorrow?",
    "Limited offer!! Earn money from home.",
    "Please submit the assignment",
    "Click here to claim your prize now"
]

print("----- Spam Classification -----")
for msg in messages:
    if is_spam(msg):
        print(f"Message: \"{msg}\" --> SPAM")
    else:
        print(f"Message: \"{msg}\" --> NOT SPAM")

user_msg = input("\nEnter a message to check: ")
if is_spam(user_msg):
    print("Result: SPAM")
else:
    print("Result: NOT SPAM")
