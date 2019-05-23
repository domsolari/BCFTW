from BlockChain import BlockChain
from actions import prompt_action, run_action

is_running = True
# Store True

block_chain = BlockChain()
# Calls the BlockChain class


while is_running:
	action = prompt_action()
	# prompt_action delivers the user's choice, store it
	if action is None:
		# If the user entered an invalid input
		is_running = False
		print("Invalid Input, please restart the program")
		break
		# break terminates the current loop
	run_action(block_chain, action)
	# run_action is executed when user enters a valid input
	print()
	input("[Hit enter to do something] ")
