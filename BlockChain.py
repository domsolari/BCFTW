# Import the part "Block" from Block.py module
from Block import Block
# Import time module
import time


class BlockChain:
    """This class defines functions that are the building blocks of creating a block chain"""
    blocks = list()
    # define blocks as empty list

    def __init__(self):
        """Define the method _init_(self) to assign values to properties of the class BlockChain"""
        # Assign a value to an initial hash "genesis_hash" (genesis_hash consists 64 times a zero)
        genesis_hash = '0' * 64
        # Assign a block containing the genesis_hash, indexed at 0
        genesis_block = Block(genesis_hash, 0)
        # Append the created block genesis_hash to the block chain
        self.blocks.append(genesis_block)
        # Print out message that block chain creation was successful
        print("Blockchain was created")

    def get_current_block(self):
        """Define the function get_current_block(self) to access the current block"""
        return self.blocks[-1]

    def _create_block(self):
        """Define the method create_block(self) that creates another block (any after genesis_block)"""
        # Assign the current block to the variable prev_block
        prev_block = self.get_current_block()
        # Assign the hash of the current block to the variable prev_hash
        prev_hash = prev_block.get_hash()
        # Get the maximum index in the current list by getting the list length
        index = len(self.blocks)
        # Create a new block by calling the class "Block" and assign it to the variable next_block
        next_block = Block(prev_hash, index)
        # Append the new block to the existing list
        self.blocks.append(next_block)

    def add_transaction(self, transaction):
        # Define the method add_transaction(self, transaction) that adds transactions to a block in the chain
        # Get the current block and assign it to current_block
        current_block = self.get_current_block()
        # Add a transaction to the current block by appending it to the transactions list
        current_block.transactions.append(transaction)
        # Print message informing user about amount added
        print("Transaction of {0} added".format(transaction))
        # Print the transactions of the current block by calling the method print_transactions() defined in Block.py
        current_block.print_transactions()

    def mine_new_block(self):
        # Define the method mine_new_block(self) that mines the current block and subsequently creates a new block
        # Print message that mining is ongoing
        print("Start mining...")
        # Assign the time at the start of the mining process to the variable start
        start = time.time()
        # Get the current block
        current_block = self.get_current_block()
        # Get the previous hash of the current block and assign it to the variable previous_hash
        prev_hash = current_block.prev_hash
        # Create a new hash and assign it to the variable new_hash
        new_hash = str()
        # Require five zeros at the beginning of the hash, note, this value can be changed
        required_len: int = 5
        while new_hash[:required_len] != prev_hash[:required_len]:
            # Here we check whether the current Hash starts with 5 zeros, if this is not the case,
            # we use the increase_nonce method from Block.py and hash the current block with a new
            # nonce again. This will be done as long as the hash starts not with 5 zeros. This process
            # is called mining
            current_block.increase_nonce()
            new_hash = current_block.get_hash()
        end = time.time()
        duration = end - start
        print("Block mined in {0}s".format(round(duration)))
        self._create_block()
        self.print_blocks()

    def print_blocks(self):
        # Define the function print_blocks(self) that prints the blocks in the block chain
        # for each block in the blocks list print the transactions stored in it
        for block in self.blocks:
            block.print_transactions()
