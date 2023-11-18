"""
Name: Music Player
Purpose: Controls the music
Author: Yoav Amitai
"""

import contextlib

with contextlib.redirect_stdout(None):
    from pygame import mixer
from song import Song
from util.play_state_enum import PlayStateEnum

class AudioManager:
    """Controls the music playing"""

    def __init__(self) -> None:
        """Initiates the music player and controls the audio"""
        mixer.init()

    def __load_song(self, song: Song) -> None:
        """
        The function loads a song using the path provided.
        
        :param song: Song instance to load
        """
        mixer.music.load(song.path)
    
    def increase_volume(self) -> None:
        """
        The function increases the volume of the music being played by 5%, up to a maximum of 1.
        """
        curr_vol = mixer.music.get_volume()
        if curr_vol + 0.05 >= 1:
            curr_vol = 1
        else:
            curr_vol += 0.05
        mixer.music.set_volume(curr_vol)
    
    def decrease_volume(self) -> None:
        """
        The function decreases the volume of the music being played by 5%, or sets it to 0% if it
        is already at or below 5%.
        """
        curr_vol = mixer.music.get_volume()
        if curr_vol - 0.05 <= 0:
            curr_vol = 0
        else:
            curr_vol -= 0.05
        mixer.music.set_volume(curr_vol)
    
    def toggle_pause(self, current_state: PlayStateEnum) -> None:
        """
        The function toggles between pausing and unpausing the music based on its current state.
        
        :param current_state: The current state of the music player, represented by the PlayStateEnum
        enumeration
        """
        if mixer.music.get_busy():
            mixer.music.pause()
            current_state = PlayStateEnum.PAUSED
        else:
            mixer.music.unpause()
            current_state = PlayStateEnum.PLAYING
    
    def stop(self) -> None:
        """
        The function stops the currently playing music.
        """
        mixer.music.stop()

    def next_track(self, track: Song) -> None:
        self.__load_song(track)
        mixer.music.play()
    
    def prev_track(self, track: Song) -> None:
        self.__load_song(track)
        mixer.music.play()

    def rewind(self) -> None:
        """
        The function rewinds the currently playing music.
        """
        mixer.music.rewind()