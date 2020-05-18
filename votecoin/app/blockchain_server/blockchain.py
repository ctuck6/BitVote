import time

class Blockchain(object):
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_block(0, '00') # Creates genesis block

    def create_block(self, nonce, previous_hash):
        block = {
            "block_number" : len(self.chain) + 1,
            "timestamp": time.strftime("%c", time.gmtime()),
            "transactions": self.transactions,
            "nonce": nonce,
            "hash": "",
            "previous hash": previous_hash,
        }

        # Reset list of TXs
        self.transactions = []
        self.chain.append(block)