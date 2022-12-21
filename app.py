from flask import Flask, jsonify, request, render_template
from db import get_songs, add_songs

app = Flask(__name__)

@app.route('/create', methods=['POST', 'GET'])
def create_song():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        genre = request.form['genre']

        if not title:
            flash('Title is required!')
        elif not artist:
            flash('Artist is required!')
        elif not genre:
            flash('Genre is required!')
        else:
            add_songs({"title":title, "artist":artist, "genre":genre})
            return redirect(url_for('index'))
    return render_template('create.html')        

@app.route('/')
def home():
    songs = get_songs()
    return render_template('index.html', songs=songs)

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
