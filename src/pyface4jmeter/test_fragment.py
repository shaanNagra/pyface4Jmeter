#!/usr/bin/env python

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////


from .internal.base_element import BaseElem
from .internal.constants import TEST_FRAGMENT


# ------------------------------------------
#
# ------------------------------------------
class TestFragment(BaseElem):

    def __init__(self, name):
        super().__init__(TEST_FRAGMENT, name)

    def configTestFragment(self, comments):
        pass
