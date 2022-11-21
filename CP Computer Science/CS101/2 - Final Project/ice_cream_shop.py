import time


# function to print choices
def print_choices(a_dict):
	for i in a_dict:
		print(i, a_dict[i])


print("Welcome to the game! Try to buy the ice cream!")
print("==========================")
time.sleep(2)
print("Hello! What is your name?")
name = input("YOU: My name is ")
print("Well hello,", name, "!")
print("What can I get you today?")
choice_1 = {1: "chocolate ice cream", 2: "strawberry ice cream", 3: "sandwiches", 4: "nothing"}
print_choices(choice_1)
c_1 = input("YOU: I want number ")
# check if the answer is a valid answer
while c_1 not in str(list(choice_1.keys())):
	print("What? We don't have that at all! What do you want??")
	print_choices(choice_1)
	c_1 = input("YOU: I want number ")
c_1 = int(c_1)
print(f"Hmm you want {choice_1[c_1]}, huh?")
time.sleep(2)
if c_1 == 1:
	print(f"Well here ya go! One {choice_1[c_1]}")
	time.sleep(2)
	print(f"That's our last one, these {choice_1[c_1]} practically sell themselves")
	time.sleep(2)
	print("==", "\n", "  ==", "\n", "    ==", "\n", "      ==", "\n", "CONGRATULATIONS YOU WON")

elif c_1 == 2:
	print(f"Well here ya go! One {choice_1[c_1]}")
	time.sleep(2)
	print("I remember that time when my missus used to go out and buy these strawberry ice cream...")
	time.sleep(3)
	print("2 HOURS OF TALKING LATER")
	time.sleep(1)
	print("... and s-she... she just left me and got ANOTHER flavour!? U-unbelievable!!")
	time.sleep(2)
	print("==", "\n", "  ==", "\n", "    ==", "\n", "      ==", "\n", "THE SELLER IS TOO SAD TO SELL", "\n", "YOU LOST THE GAME")

elif c_1 == 3:
	print("What do you think this is huh?")
	time.sleep(2)
	print("Get out of here punk")
	time.sleep(2)
	print("==", "\n", "  ==", "\n", "    ==", "\n", "      ==", "\n", "YOU GOT THE WRONG ORDER", "\n", "YOU LOST THE GAME")

elif c_1 == 4:
	print("Then why are you here??")
	time.sleep(2)
	print("Go mess with someone else!")
	time.sleep(2)
	print("==", "\n", "  ==", "\n", "    ==", "\n", "      ==", "\n", "WHAT DO YOU WANT?!", "\n", "YOU LOST THE GAME")
time.sleep(5)
print("\n", "If you wish to try again please restart the program.")
