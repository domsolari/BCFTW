import hashlib


# This package is needed for the hash function

class Block:
    """The following Class determines our Block"""
    nonce = 0
    # The nonce, which will be changed during the hash process, is set to zero originally
    index: int
    # Index of the block is an integer
    prev_hash: str
    # the hash from the previous block is also included in the current block, that is the idea of the
    # safety mechanism of a block chain
    transactions: list

    # The transaction of the block are stored in a list

    def __init__(self, prev_hash, index):
        self.prev_hash = prev_hash
        self.index = index + 1
        # Our first block should be Block 1 and not Block 0, thus we add 1 to the index
        self.transactions = list()

    def __str__(self):
        """This method returns the string representation of the object"""
        return "prev_hash:{0}|nonce:{1}|transactions:{2}".format(self.prev_hash, self.nonce, self.transactions)

    def get_hash(self):
        """This method converts the content of the block into an hash"""
        data = str(self).encode("utf - 8")
        # Convert the data into set of bytes which is required for the hash process
        return hashlib.sha256(data).hexdigest()
        # The data will be hashed and the hash is returned

    def increase_nonce(self):
        """At every iteration, we add 1 to the nonce and store the sum within the same step"""
        self.nonce += 1

    def print_transactions(self):
        """This method will print Information about the Block number and its content"""
        print("Block {0}: {1}".format(self.index, self.transactions))
