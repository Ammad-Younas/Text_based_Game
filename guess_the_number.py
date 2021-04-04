import os
import random
os.system("")
def game():
	stored_number = random.randint(0, 1000)
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
		print(color.darkgrey, "              Made By @Cybernetic !!!")
		print(color.bold, color.blue, "Welcome to Guess the Number Game  b/w  1 to 1000")
		print(color.orange, "            You have only 15 attempts")
		while (attempt<=15):
			print(color.purple," Enter a Number: ", end="")
			user_input = int(input(""))
			if user_input < stored_number:
				print(color.gold, " Enter Greater Number and attempt left:", 15-attempt)
			elif user_input > stored_number:
				print(color.red, " Enter Lesser Number and attempt left:", 15-attempt)
			else:
				print(color.green ," Congratulation ! You Win the Game In", attempt, "Attempt")
				again()
				break
			attempt = attempt + 1
		if (attempt>15):
			print(color.cyan, "           Game over")
			print(color.cyan, " You Have Run Out Of Attempts")
			print("  The Number Was", [stored_number])
			again()
	except Exception:
		print(color.lightcyan, " You Entered Wrong Input")
		print(color.bold, color.lightcyan, "Please !!! Enter An Integer Value Not String....")
		again()
def again():
	print("  Do You Want To Play Again or Quit [Y/N]: ", end="")
	user_decision = input().upper()
	if user_decision == 'Y':
			print("\n")
			game()
	elif user_decision == 'N':
		print("\n")
		print("  Good Bye......!")
		print("  See You Next Time....")
	else:
		again()
game()
