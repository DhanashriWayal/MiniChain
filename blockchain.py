import hashlib
import json
from time import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class MiniChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 5  # Number of leading zeros for PoW (e.g., '00000')

    def create_genesis_block(self):
        return Block(0, [], time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_block(self, transactions):
        index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        timestamp = time()
        nonce = 0
        block = Block(index, transactions, timestamp, previous_hash, nonce)

        # Proof-of-Work: Find nonce so hash starts with '0' * difficulty
        while block.hash[:self.difficulty] != "0" * self.difficulty:
            nonce += 1
            block.nonce = nonce
            block.hash = block.calculate_hash()

        print(f"Block mined! Nonce: {nonce}")
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        # In a real app, validate transactions here
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        self.get_latest_block().transactions.append(transaction)
        return transaction

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def to_dict(self):
        return [vars(block) for block in self.chain]