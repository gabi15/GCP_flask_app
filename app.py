from flask import Flask, jsonify, request, render_template, json, redirect, url_for, flash
from db import get_songs, add_songs
import google.cloud.logging
import logging
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()


@app.route('/create', methods=['POST', 'GET'])
def create_song():
    if request.method == 'POST':
        logging.info("Start processing song post")
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
            add_songs({"title": title, "artist": artist, "genre": genre})
            logging.info("End processing song post")
            return redirect(url_for('home'))
    return render_template('create.html')        


@app.route('/')
def home():
    logging.info("Start getting songs")
    songs = get_songs()
    logging.info("End getting songs")
    return render_template('index.html', songs=songs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
