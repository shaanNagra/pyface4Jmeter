#!/usr/bin/env python

# INTERNAL IMPORTS
from .internal.base_element import BaseElem
from .internal.constants import THINK_TIME

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////


# ------------------------------------------
#
# ------------------------------------------
class ThinkTime(BaseElem):
    def __init__(self, name='think time'):
        super().__init__(THINK_TIME, name)
