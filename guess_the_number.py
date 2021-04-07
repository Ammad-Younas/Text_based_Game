import os
import random
os.system("")
def game():
	stored_number = random.randint(1,1000)
	class color:
		underline='\033[04m'
		bold='\033[01m'
		blue='\033[34m'
		orange='\033[33m'
		gold='\033[33m'
		red='\033[31m'
		green='\033[32m'
		cyan='\033[36m'
		purple='\033[35m'
		darkgrey = '\033[90m'
		lightcyan='\033[96m'
	attempt = 1
	try:
		Bold ='\033[01m'
		Blue ='\033[34m'
		O='\033[33m'
		Gold ='\033[33m'
		R ='\033[31m'
		Green ='\033[32m'
		C ='\033[36m'
		P ='\033[35m'
		Darkgrey = '\033[90m'
		Lightcyan='\033[96m'
		color_list = [Bold, Blue, O, Gold, R, Green, C, P, Darkgrey, Lightcyan]
		choice_color = random.choice(color_list)
		print(color.bold,choice_color,"===============================================")
		print(color.darkgrey, "              Made By @Cybernetic !!!")
		print(color.bold, color.blue, "\t\t  Welcome to Game")
		print(color.bold, color.blue, "     You have to guess a number b/w [1-1000]")
		print(color.orange, "            You have only {15} Attempts")
		print(color.bold,choice_color,"===============================================")
		while (attempt<=15):
			print(color.purple," Enter a Number <<<<<<<< >>>>>>>: ", end="")
			user_input = float(input(""))
			if user_input < stored_number:
				print(color.gold, " Enter Greater Number > | >  { Attempts:", 15-attempt,"}")
			elif user_input > stored_number:
				print(color.red, " Enter Lesser Number  < | <  { Attempts:", 15-attempt,"}")
			else:
				print(color.green," -----------------------------------------------")
				print(color.green," Congratulations!!!     |    { You Guessed","}")
				print(color.green," -----------------------------------------------")
				print(color.green," You guessed the number in",attempt,"Attempts")
				print(color.green," -----------------------------------------------")
				again()
				break
			attempt = attempt + 1
		if (attempt>15):
			print(color.cyan,color.bold,"-----------------------------------------------")
			print(color.cyan,color.bold, "{ Game Over!!! }       |     { Game Over!!!","}")
			print(color.cyan,color.bold,"-----------------------------------------------")
			print("  Hidden Number Was ----------->   {",stored_number,"}")
			print(color.cyan,color.bold,"-----------------------------------------------")
			again()
	except Exception:
		print(color.red,color.bold,"-----------------------------------------------")
		print(color.red, " You Entered Something Wrong!!!")
		print(color.bold, color.red, "Please! Enter An Integer Value Not Anyother....")
		print(color.red,color.bold,"-----------------------------------------------")
		again()
def again():
	print("  Do You Want To Play Again or Quit [Y/N]: ",end="")
	user_decision = input().upper()
	if user_decision == 'Y':
			print("\n")
			game()
	elif user_decision == 'N':
		print("  -----------------------------------------------")
		print("  Good Bye......!")
		print("  See You Next Time....")
	else:
		print("  Please! Select only [ Y or N ]")
		print("  -----------------------------------------------")
		again()
game()