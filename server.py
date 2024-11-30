from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/alphabetizer', methods=['POST'])
def alphabetizer():
    json_names = request.get_json()

    sorted_names = dict(sorted(json_names.items()))

    json_names = json.dumps(sorted_names)

    return json_names

if __name__ == "__main__":
    app.run(debug=True, port=5002)