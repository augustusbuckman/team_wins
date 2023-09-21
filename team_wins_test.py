import os.path
import sys
from unittest import TestCase

from team_wins import main
from tud_test_base import *

def test_team_wins():
    try:
        exist = os.path.exists("team_wins.py")
        assert exist == True
    except:
        sys.exit()

    set_keyboard_input(['cfb05_s_e.txt', 'C Missouri'])
    main()
    output = get_display_output()
    assert output == [
        "This program reads a file for a sport's teams results.",
        "Enter file name: ",
        "Enter team name: ",
        "wins: 1",
        "losses: 0",
        "win percentage: 100.0"
    ]
