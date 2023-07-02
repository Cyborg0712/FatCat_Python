name = input("Hello! What is your name? ")
print("Hi "+name+", good to see you!")
feeling = input("How are you? ")

if "not" in feeling:
    print("Sorry to hear that!")
elif ("I' fine" in feeling) or ("fine" in feeling) or ("good" in feeling) or ("Fine" in feeling):
    print("Me too!")

favcolour = input("What is your favorite colour? ")

if ("Red" in favcolour or "Green" in favcolour or "Blue" in favcolour or "Orange" in favcolour):
    print("We have a lot in common")
else:
    print("My favorite colour is Blue")

