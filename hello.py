# Ask Users for their name.
name = input("What is your name? ").strip().title()

# I can also use name = name.strip() for managing user's extra spaced inputs & name = name.title() to capatlize small charactered input.

# If I want to call the user by only their first name or to singh ji by their last name.

first, last = name.split()

# Say hello to the users.

print(f"Oh hello, {first}")
age= input("What's your age duh? ")

# Remove's Blank or WhiteSpaces From User's Abnormal Spaced Input.
age = age.strip()
print(f"Cool, {age}")

# Asking User If they have a Girlfriend Or Boyfriend.
Partner = input("Gotta Partner? ").strip()
print("cool bruvh")

# Ask User If he wants to make a Million Dollars
input("Want's to make 1 million $? ")
print("Cool we'll learn to code then. ", end="")

input("Sound's good to you? ")
print("Then go and start working right now")

