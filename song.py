"""
Name: Song
Purpose: Class that represents a song, containing metadata and the audio file itself
"""
from tinytag import TinyTag
import os
from PIL import Image
from io import BytesIO

class Song:
    """
    Represents a song.

    Args:
        self: The Song instance.
        path (str): The path to the song file.

    Attributes:
        title (str): The title of the song.
        artist (str): The artist of the song.
        duration: The duration of the song.
        genre: The genre of the song.
        year: The year the song was released.
    """

    def __init__(self, path: str) -> None:
        song_metadata: TinyTag = TinyTag.get(path, image=True)
        self.title = song_metadata.title
        self.artist = song_metadata.artist
        self.duration = song_metadata.duration
        self.genre = song_metadata.genre
        self.year = song_metadata.year
        self.path = os.path.abspath(path)
        self.album_art = Image.open(BytesIO(song_metadata.get_image())).resize((20,20)) # type: ignore
