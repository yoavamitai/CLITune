"""
Name: Player
Purpose: The CLI UI component
Author: Yoav Amitai
"""

from typing import List

from rich import box
from rich import table
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

from song import Song
from util.theme import Theme
from util.time_format import time_format


class UIPlayer:
    """Player
    The UI Component of the music player
    """

    def __init__(self, theme: Theme) -> None:
        self.layout: Layout = self.draw_ui(Layout())
        self.theme: Theme = theme

    def draw_ui(self, layout: Layout) -> Layout:
        """Refresh the current player UI

        Args:
            layout (Layout): Current Layout attribute

        Returns:
            Layout: updated layout
        """
        # Split main areas
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", size=25),
            Layout(name="footer", size=3),
        )

        # Update Header
        layout["header"].update(
            Panel(
                Align.center("[bold][#feff6e] ♪ CLITune[/#feff6e][/bold]"),
                border_style=self.theme.panel_border,
            )
        )

        # Update Main
        layout["main"].split_column(
            Layout(name="now_playing", size=3),
            Layout(name="media_album", size=22),
        )

        layout["media_album"].split_row(
            Layout(name="media_controls"), Layout(name="album")
        )

        layout["media_controls"].split_column(
            Layout(name="playlist", size=10), 
            Layout(name="media_buttons")
        )

        layout["media_buttons"].update(
            Panel(
                Align.center(
                    "[bold][#feff6e]Pre(v) (P)lay/Pause (S)top"
                    " (N)ext  (R)epeat  (Q)uit (+)Vol (-)Vol [/#feff6e][/bold]"
                ),
                title="Controls",
                border_style=self.theme.panel_border,
            )
        )

        # Update footer
        layout["footer"].update(
            Panel(
                Align.center(
                    "[bold][#feff6e] Created with [#ff2b2b]♥  [/#ff2b2b] "
                    "by Yoav Amitai [/#feff6e][/bold]"
                ),
                border_style=self.theme.panel_border,
            )
        )
        return layout

    def draw_playlist(self, playlist: List[Song], currently_playing_idx: int) -> Panel:
        curr_song: Song = playlist[currently_playing_idx]
        
        playlist_table = Table(
            show_lines=False,\
            box=box.SIMPLE,
            border_style=self.theme.panel_border
        )
        playlist_table.add_column("Title", style="cyan")
        playlist_table.add_column("Artist", style="white")
        playlist_table.add_column("Duration", justify="right", style="green")
        
        for song in playlist:
            playlist_table.add_row(song.title, song.artist, time_format(song.duration)) # type: ignore
        
        return Panel(
            table,
            border_style=self.theme.panel_border,
            title="[#feff6e]Queue"
        )