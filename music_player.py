"""
Name: Music Player
Purpose: The main music player class, contains the UI player and the audio manager.
Author: Yoav Amitai
"""
import glob
from itertools import chain
import os
from typing import List, NoReturn

import keyboard as kb

from audio_manager import AudioManager
from song import Song
from ui_player import UIPlayer
from util.theme import Theme
from util.play_state_enum import PlayStateEnum


class MusicPlayer:
    """Music Player class."""

    def __init__(self, music_folder_path: str) -> None:
        """
        Initializes a MusicPlayer object.

        Args:
            self: The MusicPlayer instance.
            music_folder_path (str): The path to the music folder.

        Attributes:
            music_folder_path (str): The path to the music folder.
            player (UIPlayer): The UIPlayer instance.
            audio_manager (AudioManager): The AudioManager instance.
        """

        self.music_folder_path: str = music_folder_path
        self.player: UIPlayer = UIPlayer(
            Theme(panel_border="#D7D5D4", spectro_color="#0FFF50")
        )
        self.audio_manager: AudioManager = AudioManager()
        self.state: PlayStateEnum = PlayStateEnum.PAUSED
        self.current_song: int = 0
        self.playlist: List[Song] = []
        self.__load_songs()
        self.__add_keyboard_shortcuts()

    def __load_songs(self) -> None:
        """
        Loads songs from the music folder path.

        Args:
            self: The MusicPlayer instance.

        Returns:
            None
        """
        types = ["*.mp3", "*.wav"]
        all_files = chain.from_iterable(
            glob.glob(f"{self.music_folder_path}/{t}" for t in types)  # type: ignore
        )
        self.playlist = [Song(song_path) for song_path in all_files]

    def __add_keyboard_shortcuts(self) -> None:
        """
        The function adds keyboard shortcuts for various actions in a music player.
        """
        kb.add_hotkey("p", self.toggle_pause)
        # kb.add_hotkey("r", lambda: PLAYER.music.rewind())
        # kb.add_hotkey("s", lambda: PLAYER.music.stop())
        kb.add_hotkey("v", self.prev_track)
        kb.add_hotkey("n", self.next_track)
        kb.add_hotkey("+", self.increase_volume)
        kb.add_hotkey("-", self.decrease_volume)
        kb.add_hotkey("q", self.exit_player)

    def toggle_pause(self) -> None:
        """
        The function toggles music pause/unpause.
        """
        self.audio_manager.toggle_pause(self.state)

    def rewind(self) -> None:
        """
        The function rewinds the current song.
        """
        self.audio_manager.rewind()

    def stop(self) -> None:
        self.audio_manager.stop()

    def prev_track(self) -> None:
        if self.current_song - 1 <= 0:
            return
        self.current_song -= 1
        self.audio_manager.prev_track(self.playlist[self.current_song])

    def next_track(self) -> None:
        if self.current_song + 1 >= len(self.playlist) - 1:
            return
        self.current_song += 1
        self.audio_manager.next_track(self.playlist[self.current_song])

    def increase_volume(self) -> None:
        """
        The function increases the volume of the music using the audio manager.
        """
        self.audio_manager.increase_volume()

    def decrease_volume(self) -> None:
        """
        The function decreases the volume of the music using the audio manager.
        """
        self.audio_manager.decrease_volume()

    def exit_player(self) -> NoReturn:
        """
        The function "exit_player" is used to exit the music player program.
        """
        os._exit(0)
