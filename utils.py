import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import re
from urllib.parse import urlparse, parse_qs
import os
from dotenv import load_dotenv

# Load environment variables from .env (if using .env)
load_dotenv()

# Access the environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

def convert_spotify_track(spotify_track_url):
    match = re.search(r"track/([a-zA-Z0-9]+)", spotify_track_url)
    if not match:
        return "Invalid Spotify track URL"
    
    track_id = match.group(1)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0cf6b535ba6147409e6fe4aca8d08d93",
                                                client_secret="43933069bc8f4e81b1637c5a8fa87004",
                                                redirect_uri="https://open.spotify.com/",scope="user-library-read"))
    track = sp.track(track_id)
    track_name = track['name']

    album = track['album']['name']
    artists = [artist['name'] for artist in track['artists']]
    print(f"{track_name} {album} {' '.join(artists)}")
    ytmusic = YTMusic()
    results = ytmusic.search(f"{track_name} album: {album}", filter='songs', limit=1)
    url = f"https://music.youtube.com/watch?v={results[0]['videoId']}" if "videoId" in results[0] else "N/A"
    return url



