"""
Name: Time Format
Purpose: Quick function to convert seconds to minutes and seconds format (mm:ss)
Author: Yoav Amitai
"""

def time_format(duration: int) -> str:
    """Generate a readable song duratin (mm:ss)

    Args:
        duration (int): duration of song in seconds

    Returns:
        str: duration of song in mm:ss format
    """
    minutes = duration // 60
    return "%02d:%02d" % (minutes, duration % 60)