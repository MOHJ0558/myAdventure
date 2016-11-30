	# myAdventure v1.0
# By Andy Chen

from random import randint
from sys import exit

# settings

def win():
	print "You won the game!"
	exit(0)

def lose():
	print "You lose the game!"
	exit(0)

def unknown():
	print "I don't know what are you doing. STOP."
	exit(0)

def error():
	print "Error! Try again."
	exit(1)

determinator = randint(1, 2)



# main
def path1():
	print "You walked on the path, and it break into 2 branches. Where will you go?"
	print "1. Go left."
	print "2. Go right."

	where1 = raw_input('> ')

	if where1 == "1":
		monster()

	if where1 == "2":
		sea()
	else:
		unknown()
		path1()

def monster():
	print "You walked and suddenly encountered an evil monster. What will you do?"
	print "1. Flee."
	print "2. Fight."
	print "3. Fight and flee as well(retreat)."

	monster = raw_input('> ')

	if monster == "1":
		print "The monster is faster than you and then eat you."
		lose()

	elif monster == "2":
		if determinator == 1:
			print "You finally fought back and killed the monster. But then you suddenly dropped by a hole."
			maze()
		else:
			print "You tried but you can't. The monster eat you."
			lose()

	elif monster == "3":
			print "You successfully retreated, but not paying attention to the portal behind you and you are transported to another room."
			computer()

	else:
		unknown()

def sea():
	print "You arrived at a vast sea. What will you do?"
	print "1. Swim."
	print "2. Take a boat."

	sea = raw_input('> ')

	if sea == "1":	
		if determinator == 1:
			print "You are energectic on swimming and finally got on the shoreline. There's a bus there, and you ride it."
			accident()
			
		else:
			print "You feebly tried to get across, but you can't. The sea devoured you."
			lose()

	elif sea == "2":
		if determinator == 1:
			print "The boat traveled smmothly and you reached the end. You walked on."
			maze()
		else:
			print "The boat didn't steer very well, but it turned over instead, and you are drowned."
			lose()

	else:
		unknown()
			


def path2():
	print "You walked on the path, and it break into 3 branches. Where will you go?"
	print "1. Go left."
	print "2. Go right."

	where2 = raw_input('> ')

	if where2 == "1":
		accident()
	elif where2 == "2":
		maze()
	else:
		unknown()
		path2()

def accident():
	print "You ride a bus and suddenly encountered an accident. What will you do?"
	print "1. Flee from top."
	print "2. Flee from window."
	print "3. Flee from doors."
	print "4. SOS."

	accident = raw_input('> ')

	if accident == "1":
		print "You escaped and found that you are at the original place where you started."
		main()
	elif accident == "2":
		if determinator == 1:
			print "You hammered at the window. It shattered and you escaped. You run away."
			maze()
		else:
			print "You can't escape because the window is too hard to break."
			lose()
	elif accident == "3":
		print "The door stuck by something heavy, so you can't escape."
		lose()
	elif accident == "4":
		if determinator == 1:
			print "You asked for help, and someone immediately saved you from disaster."				
			win()
		else:
			print "You asked for help, but they'd ignored you and flee for their own life."
			lose()
	else:
		unknown()


def maze():
	print "You are in front of a maze."
	print "1. Head into the maze."
	print "2. Look around."
	print "3. Call your friends to play with you."		

	maze = raw_input('> ')

	if maze == "1": 
		print "You are a genius! You quickly found the way out and walked on."
		computer()
	elif maze == "2":
		print "You looked and looked but couldn't find a way out. You are stuck here."
		lose()
	elif maze == "3":
		if determinator == 1:
			print "Your guys managed to get out of the maze. Teamwork is the best! You thanked your friends and walked on."
			sea()
		else:
			print "You called your friends, but they leaved you here at the maze. You can't get out."
			lose()
	else:
		unknown()



def path3():
	print "You walked on the path, and it break into 2 branches. Where will you go?"
	print "1. Go Left."
	print "2. Go right."

	where3 = raw_input('> ')

	if where3 == "1":
		computer()
	elif where3 == "2":
		maze()
	else:
		unknown()	

		
def computer():
	print "You are sitting in front of a computer."
	print "1. Try to unlock the Computer."
	print "2. Break the computer."

	computer = raw_input('> ')

	if computer == "1":
		print "The code is 1 digit, less than 4. You have only 1 chance."
		code = "%d" % (randint(1, 3))
		
		guess = raw_input("[keypad]> ")

		if guess == code:
			print "You successfully logged in, and as you play it, you suddenly dropped into an enormous hole."
			sea()
		else:
			print "The computer explodes and crush you to jelly."
			lose()

	if computer == "2":
		print "The computer explodes and crush you to jelly."
		lose()

	else:
		unknown()

def main():
	print "This is where all begins..."
	print "There's 3 branches of the road. Where will you go?"
	print "1. Go left."
	print "2. Go right."
	print "3. Go straight forward."

	where0 = raw_input('> ')

	if where0 == "1":
		path1()

	elif where0 == "2":
		path2()

	elif where0 == "3":
		path3()

	else:
		unknown()


if __name__ == '__main__':
	main()


