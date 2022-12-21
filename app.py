from flask import Flask, jsonify, request, render_template
from db import get_songs, add_songs

app = Flask(__name__)

@app.route('/songs', methods=['POST', 'GET'])
def songs():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        add_songs(request.get_json())
        return 'Song Added'

    return get_songs()    

@app.route('/')
def home():
    return render_template('index.html')

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
