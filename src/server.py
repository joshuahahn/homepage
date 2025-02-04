# Imports
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

from datetime import date
from collections import defaultdict

app = Flask(__name__)

# Variables
daily_listens = defaultdict(list)
album_listens = defaultdict(int)
artist_listens = defaultdict(int)
total_listens = 0

# Page Rendering
@app.route('/')
def home():
    return render_template('home.html', data=[])

@app.route('/contributions')
def contributions():
    return render_template('contributions.html', data=[])


@app.route('/music')
def album_diary():
    return render_template('in-progress.html')

    global daily_listens
    global album_listens
    global artist_listens
    global total_listens

    album_data = [len(album_listens), len(artist_listens), total_listens,
                  daily_listens, album_listens, artist_listens]
    return render_template('album-diary.html', data=album_data)

@app.route('/math')
def math():
    return render_template('in-progress.html')

# Helper Functions
def process_album_list():
    global daily_listens
    global album_listens
    global artist_listens
    global total_listens

    with open('data/albums', 'r') as f:
        data = f.readlines()

    n = len(data)
    i = 0

    while i < n:
        #month, day, year = data[i].strip().split('-')
        #day = date(2000+int(year), int(month), int(year))
        i += 1

        while i < n and data[i]!= '\n':
            artist, album = data[i].strip().split('\\')
            daily_listens[data[i-1]].append((artist, album))
            album_listens[album] += 1
            artist_listens[artist] += 1
            total_listens += 1
            i += 1
        i += 1

if __name__ == '__main__':
    process_album_list()
    app.run(debug=True)
