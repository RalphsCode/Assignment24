from app import app
from models import db, Song, PlaylistSong, Playlist

with app.app_context():
    db.drop_all()
    db.create_all()

# Add Songs
s1 = Song(title="Beautiful Sounds", artist="We B Jammin")
s2= Song(title="The Remix", artist="Not Done Yet")
s3 = Song(title = "Am I?", artist="Who")
s4 = Song(title="Nothin' Better Than the Butta'", artist = "Making Sourdough")
s5 = Song(title="Enough Already", artist="Finalist")

db.session.add_all([s1,s2,s3,s4,s5])
db.session.commit()

# Add Playlists 
p1 = Playlist(name="Slow Jams")
p2 = Playlist(name = "Hate ya", description="Breakup songs")
p3 = Playlist(name="workout", description="Songs to stop the boredom")

db.session.add_all([p1,p2,p3])
db.session.commit()

# Add Songs To Playlist
l1 = PlaylistSong(playlist_id=1, song_id=3)
l2 = PlaylistSong(playlist_id=2, song_id=3)
l3 = PlaylistSong(playlist_id=1, song_id=4)
l4 = PlaylistSong(playlist_id=1, song_id=1)

db.session.add_all([l1,l2, l3, l4])
db.session.commit()

# Testing
print('----------------------------------')
print("Songs on the ", p1.name, "playlist:")
# SELECT * FROM playlists_songs WHERE playlist_id = 1;
jams_list_songs = p1.plylst_2_refTbl 
# for all the song_id's on that playlist
for song in jams_list_songs:
    # Get the title of the song from the song table
    print('- ', song.refTbl_2_song.title)
print('----------------------------------')