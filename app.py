from flask import Flask, jsonify, request
import random

app = Flask(_name_)

# Load dataset from file
with open('cerpen.txt', 'r') as file:
    cerpen_dataset = file.read().split('\n\n')

@app.route('/generate_cerpen', methods=['POST'])
def generate_cerpen():
    # Mendapatkan jumlah cerpen yang akan di-generate dari front end
    jumlah_cerpen = int(request.json['jumlah_cerpen'])

    # Mengacak cerpen dari dataset
    cerpen_terpilih = random.sample(cerpen_dataset, jumlah_cerpen)

    return jsonify({'cerpen': cerpen_terpilih})

if _name_ == '_main_':
    app.run(debug=True)