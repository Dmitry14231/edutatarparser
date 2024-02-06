from flask import Flask, request, jsonify
import subprocess
import requests


app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def process_data():
    try:
        data = request.json  
        if data is not None:
            print(data)
            print('запрос получен!')
            ID = data["id"]
            dcoin=int(data["dcoin"])
            subprocess.run(["python3", "parser.py",  ID, dcoin])
             
        else:
            print('JSON NULL')

        return "OK"
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
