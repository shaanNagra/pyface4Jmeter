#!/usr/bin/env python

# INTERNAL IMPORTS
from .internal.base_element import BaseElem
from .internal.constants import UNIFORM_RANDOM_TIMER

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////


# ------------------------------------------
#
# ------------------------------------------
class UniformRandom(BaseElem):
    def __init__(self, name='think time'):
        super().__init__(UNIFORM_RANDOM_TIMER, name)

    def set_offset(self, delay):
        elem = self.Element.find('.//stringProp[@name="ConstantTimer.delay"]')
        elem.text = delay

    def set_range(self, range):
        elem = self.Element.find('.//stringProp[@name="RandomTimer.range"]')
        elem.text = range
