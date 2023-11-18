"""
Name: Player
Purpose: The CLI UI component
Author: Yoav Amitai
"""

from rich.layout import Layout
from rich.align import Align
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich import box

from util.theme import Theme

###   Think about using rich-pixels
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
            Layout(name="song_list", size=10), Layout(name="media_buttons")
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
