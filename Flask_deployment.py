import pickle as pk
from flask import Flask, request, jsonify


app = Flask('Pneumonia Detector')
@app.route('/predict', methods=['POST'])
def predict():
    return 'Pinging model application'

if __name__ == '__main__':
    app.run(debug=True)