"""
Name: Theme
Purpose: Class defining a UI color scheme
"""
from dataclasses import dataclass

@dataclass
class Theme:
    """Defines a UI theme
    """
    panel_border: str
    spectro_color: str
