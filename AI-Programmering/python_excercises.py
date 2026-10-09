#2-1. Simple Message: Assign a message to a variable, and then print that message
message = "Hvid Monster er overrated!"
print(message)

#2-2. Simple Messages: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
message = "Booster er meget bedre!"
print(message)

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
name = "Preben"
print(f"Hello {name}, did you pray today?")

#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name = "Jonas"
print(name.lower())
print(name.upper())
print(name.title())

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
quote = "Counting or not counting gang violence."
author = "Mr. Kirk"
print(f"{author} once said, {quote.lower()}")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
famous_person = "Mr. Kirk"
quote = "Counting or not counting gang violence."
message = f"{famous_person} once said, {quote.lower()}"
print(message)

#2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name after striping the whitespace.
name = " peter "
print(name.rstrip())
print(name.lstrip())
print(name.strip())

print("\n\tPeter\n\tPeter")

#2-8. File Extension: Use a variable to represent a file name, and then print the file name with its extension. Then change the value of the variable to represent a different file name, and print the new file name with its extension.
moodle_url = "https://moodle.aau.dk/"
simple_moodle = moodle_url.removeprefix("https://")
print(simple_moodle)

Moodle = "moodle_skema.txt"
print(Moodle.removesuffix(".txt"))

#2-9. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results.
print(4+4)
print(12-4)
print(4*2)
print(16/2)

#2-10. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.
favorite_number = "27"
print(f"My favorite number is {favorite_number}!")

import this

#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ["Preben", "Alexander", "Åse"]
print(names[0])
print(names[1])
print(names[2])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but this time, print a message to each person. The text of each message should be the same, but each message should be personalized with the person’s name.
names = ["Preben", "Alexander", "Åse"]
print(f"Hello {names[2]}, did you speak to {names[0]} today?")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
cars = ["bmw", "audi", "mercedes"]
message = f"I would like to own a {cars[0].title()} some day!"
print(message)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guest_list = ["Steve Jobs", "Charlie Kirk", "Kanye West"]
print(f"Hello {guest_list[0]}, would you like to attend my dinner party? {guest_list[1]} and {guest_list[2]} is also comming")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
guest_list[1] = "Mr.Beast"
print(guest_list)
print(f"Hello {guest_list[0]}, Charlie Kirk can't make it to the dinner party, but {guest_list[1]} is coming instead. {guest_list[2]} is also comming")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
guest_list.insert(0, "Nissefar")
guest_list.insert(2, "Søren Pind")
guest_list.append("Rocket Man")
print(guest_list)

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
popped_guest = guest_list.pop(0)
print(f"Sorry {popped_guest}, I have to remove you from the dinner party...")
popped_guest2 = guest_list.pop(2)
print(f"Sorry {popped_guest2}, I have to remove you from the dinner party...")
popped_guest3 = guest_list.pop(1)
print(f"Sorry {popped_guest3}, I have to remove you from the dinner party...")
del guest_list[2]
del guest_list[1]
del guest_list[0]
print(guest_list)

#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
places = []

