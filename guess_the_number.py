import os
import random
os.system("")
def game():
	stored_number = random.randint(1,1000)
	class color:
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
	print(color.bold,color.lightcyan,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(color.bold,color.lightcyan, "          | Made By @'Cybernetic' !!! |")
	print(color.bold,color.lightcyan,"===============================================")
	print(color.bold, color.blue, "\t\tHi, Welcome to Game")
	print(color.bold, color.blue, "     You have to guess a number b/w [1-1000]")
	print(color.orange, "            You have only {15} Attempts")
	print(color.green,"\t      Press 'Q' to quit Anytime!")
	print(color.bold,color.green,"===============================================")
	while (attempt<=15):
		print(color.purple," Enter a Number <<<<<<<< >>>>>>>: ", end="")
		user_input = input().upper()
		if user_input=="Q":
			print("  -----------------------------------------------")
			print("  Good Bye......!")
			print("  See You Next Time....")
			exit()
		elif not user_input.isdigit():
			print(color.red,color.bold,"-----------------------------------------------")
			print(color.red, " You Entered Something Wrong!!!")
			print(color.bold, color.red, "Please! Enter An Integer Value Not Anyother....")
			print(color.red,color.bold,"-----------------------------------------------")
			continue
		elif int(user_input) < stored_number:
			print(color.gold, " Enter Greater  > | > from",user_input,"{ Attempts:", 15-attempt,"}")
		elif int(user_input) > stored_number:
			print(color.red, " Enter Lesser   < | < from",user_input,"{ Attempts:", 15-attempt,"}")
		else:
			print(color.green," -----------------------------------------------")
			print(color.green," Your Number:",user_input,            "  ====|==== Hidden Number:",stored_number)
			print(color.green," Congratulations!!!     |      { You Guessed","}")
			print(color.green," -----------------------------------------------")
			print(color.green," You guessed the number in",attempt,"Attempts")
			print(color.green," -----------------------------------------------")
			again()
			break
		attempt = attempt + 1
	if (attempt>15):
		print(color.cyan,color.bold,"-----------------------------------------------")
		print(color.cyan,color.bold,"    Sorry!!!                    You Lose!!!")
		print(color.cyan,color.bold,"-----------------------------------------------")
		print(color.cyan,color.bold, "{ Game Over!!! }       |     { Game Over!!!","}")
		print(color.cyan,color.bold,"-----------------------------------------------")
		print("  Hidden Number Was ----------->   {",stored_number,"}")
		print(color.cyan,color.bold,"-----------------------------------------------")
		again()
def again():
	class color1:
		bold='\033[01m'
		green='\033[32m'
	print("  Do You Want To Play or Quit [Y/N]: ",end="")
	user_decision = input().upper()
	if user_decision == 'Y':
			print(color1.bold,color1.green,"\n -------------------------------------------------\n    >>>>>>>>>   { New Game Started }   <<<<<<<<<")
			game()
	elif user_decision == 'N':
		print("  -----------------------------------------------")
		print("  Good Bye......!")
		print("  See You Next Time....")
	else:
		print("  Warning! please select only [ Y or N ]")
		print("  -----------------------------------------------")
		again()
game()