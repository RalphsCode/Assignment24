from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import exists, not_, and_
from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()
    # POST Route
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            if form.description.data:
                description = form.description.data
                new_playlist = Playlist(name=name, description=description)
            else:
                new_playlist = Playlist(name=name)
            db.session.add(new_playlist)
            db.session.commit()
            return redirect('/playlists')
    # GET Route
    return render_template('new_playlist.html', form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    # POST Route
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            artist = form.artist.data
            new_song = Song(title=title, artist=artist)
            db.session.add(new_song)
            db.session.commit()
            return redirect("/songs")
    # GET Route
    return render_template('new_song.html', form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    # Songs not on playlist
    songs_to_add = Song.query.filter(
    not_(
        Song.id.in_(
            db.session.query(PlaylistSong.song_id)
            .filter(PlaylistSong.playlist_id == playlist_id)
            .subquery()
        )   )
        ).all()

    # Turn Query results into a list of tuples and send to form
    form.song.choices = [(song.id, song.title) for song in songs_to_add]
    print('###### playlist_id:', playlist_id)
    for song in form.song.choices:
        print (song)
    # POST Route
    if request.method == 'POST':
        if form.validate_on_submit():
            new_song = form.song.data
            add_song = PlaylistSong(playlist_id=playlist_id, song_id = new_song)
            db.session.add(add_song)
            db.session.commit()

            return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
