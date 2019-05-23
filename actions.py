from enum import Enum
from BlockChain import BlockChain
from Transaction import Transaction
import sys # Is needed for the sys.exit command


class Action(Enum):
    """The inputs (1,2,3,x) are matched with their options"""
    ADD_TRANSACTION = str(1)
    MINE_BLOCK = str(2)
    SHOW_CHAIN = str(3)
    EXIT_PROGRAM = "x"


def prompt_action() -> Action:
    """Defining the options the user will be given when entering the program"""
    options = ["[1] Add Transactions to the current Block", "[2] Mine Block", "[3] Show Blockchain", "[x] Exit"]
    print("Choose what you want to do?")
    for what_to_do in options:
        print(what_to_do)
        # This loop will print all possible options, so we do not have to write them all line by line
    index = input('')
    # The user can enter what he wants to do
    try:
        return Action(index)
    except ValueError:
        return None
    # Checks whether the user entered a valid input, this will be used in main.py


def run_action(block_chain: BlockChain, action: Action):
    """This function calls the required methods which are needed for the user's input """
    if action == Action.ADD_TRANSACTION:
        transaction = Transaction()
        block_chain.add_transaction(transaction)
    if action == Action.MINE_BLOCK:
        block_chain.mine_new_block()
    if action == Action.SHOW_CHAIN:
        block_chain.print_blocks()
    if action == Action.EXIT_PROGRAM:
        sys.exit("See ya later alligator, we hope you enjoyed our small Blockchain application")
