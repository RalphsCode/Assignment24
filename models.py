"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.String(50), nullable = False)

    description = db.Column(db.String(150), nullable = True)

    # Relationship with reference table
    plylst_2_refTbl = db.relationship('PlaylistSong', backref='refTbl_2_plylst')


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    title = db.Column(db.String, nullable = False)

    artist = db.Column(db.String, nullable = False)

    # Relationship with reference table
    song_2_refTbl = db.relationship('PlaylistSong',  backref='refTbl_2_song')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    playlist_id = db.Column(db.Integer, ForeignKey('playlists.id'), nullable=False)

    song_id = db.Column(db.Integer, ForeignKey('songs.id'), nullable=False)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
