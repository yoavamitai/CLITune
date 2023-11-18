"""
Name: CLITune
Purpose: A cool CLI music player
Author: Yoav Amitai
"""
import argparse
from argparse import Namespace
from music_player import MusicPlayer


def get_args() -> Namespace:
    """Parse the arguments when running the program

    Returns:
        Namespace: passed arguments
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", type=str, required=True, help="Path to the music folder to play"
    )
    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """main
    Run the Music Player
    """
    arguments = get_args()
    music_player = MusicPlayer(music_folder_path=arguments.path)


if __name__ == "__main__":
    main()
