from flask import Flask, render_template, request, jsonify
from blockchain import MiniChain
import json

app = Flask(__name__)
blockchain = MiniChain()

# === FRONTEND ===
@app.route('/')
def index():
    return render_template('index.html')

# === API ENDPOINTS ===
@app.route('/api/chain', methods=['GET'])
def api_chain():
    return jsonify({
        'chain': blockchain.to_dict(),
        'length': len(blockchain.chain),
        'valid': blockchain.is_chain_valid()
    })

@app.route('/api/transaction', methods=['POST'])
def api_transaction():
    data = request.json
    tx = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message': 'Transaction added!', 'tx': tx}), 201

@app.route('/api/mine', methods=['POST'])
def api_mine():
    block = blockchain.mine_block([])
    return jsonify({
        'message': 'Block mined!',
        'block': vars(block)
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)