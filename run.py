from blockchain import MiniChain

# Create blockchain
blockchain = MiniChain()

# Add some transactions
blockchain.add_transaction("Alice", "Bob", 50)
blockchain.add_transaction("Bob", "Charlie", 30)

# Mine a block
blockchain.mine_block([])  # Mine with pending transactions

# Add more and mine again
blockchain.add_transaction("Charlie", "Alice", 20)
blockchain.mine_block([])

# Validate
print("Chain valid?", blockchain.is_chain_valid())
print("Full chain:", blockchain.to_dict())