"""
utils.py

This module provides utility functions to improve app functionality
"""


import time
import os
import platform
from datetime import datetime



def delay(n=6):
    """
    Artificial delay simulator.

    Args:
        n: The number of dots that are displayed.

    Prints:
        Prints a series of dots in an interval of half a second.
    
    """

    for _ in range(n):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("")



def get_current_date():
    """Returns the current date"""
    date = datetime.now().strftime("%d-%m-%Y")
    return date



def clear_screen(n=0.8):
    """
    Clear the terminal

    Args:
        n: The number of seconds before the screen is cleared
    """
    
    time.sleep(n)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")