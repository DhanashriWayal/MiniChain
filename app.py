from flask import Flask, jsonify, request
from blockchain import MiniChain

app = Flask(__name__)
blockchain = MiniChain()

@app.route('/mine', methods=['POST'])
def mine():
    transactions = request.json.get('transactions', [])
    block = blockchain.mine_block(transactions)
    response = {
        'message': 'New block mined!',
        'index': block.index,
        'transactions': block.transactions,
        'hash': block.hash,
        'previous_hash': block.previous_hash
    }
    return jsonify(response), 201

@app.route('/transaction', methods=['POST'])
def new_transaction():
    sender = request.json['sender']
    receiver = request.json['receiver']
    amount = request.json['amount']
    transaction = blockchain.add_transaction(sender, receiver, amount)
    response = {'message': 'Transaction added to pending', 'transaction': transaction}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.to_dict(),
        'length': len(blockchain.chain),
        'valid': blockchain.is_chain_valid()
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)