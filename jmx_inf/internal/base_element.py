#!/usr/bin/env python

# EXTERNAL IMPORTS
import lxml.etree as ET

# INTERNAL IMPORTS
from .constants import HASH_TREE

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////


# ------------------------------------------
#
# ------------------------------------------
class BaseElem:
    """The parent class for creating Jmeter elements.


    Attributes:
        Element: JMX ElementTree.
        TempRoot: Temporary ElementTree to act as root to Element.

    Methods:
        append(Element): Appends Element as child to this one.
        get_elem(): Returns ElementTree Element.
        print(): Prints JMX of element.
        enable(enable=True): Sets the enable flag of JMX element.
        bool_2_bool: Returns string of Boolean value.
    """
    def __init__(self, element, name):
        """Constructs parent attributes for JMX Element object.
        
        Parameters:
            element: The string that represent a JMX Element.
            name: The name of JMX Element.  
        """
        self.Element = ET.fromstring(element)
        self.Element.set('testname', name)
        self.TempRoot = ET.Element('temproot')
        self.TempRoot.append(self.Element)
        self.Element.addnext(ET.fromstring(HASH_TREE))
        pass

    def append(self, elem):
        """Appends given element as subelement.

        Parameter:
            elem: The Element object to append as subelement.
        """
        self.Element.getnext().extend(elem)
        return

    def get_elem(self):
        """Returns subelements of TempRoot Element.

        Returns:
            subelements of temporary root.
        """
        return self.TempRoot.getchildren()

    def print(self):
        """Print string content of element and any sibling elements.
        """
        print(ET.tostring(self.Element))
        print(ET.tostring(self.Element.getnext()))
        return

    def enable(self, enable=True):
        """Sets enable flag of a JMX Elements.
        """
        self.Element.set('enabled', self.Bool2Bool(enable))
        return

    def bool_2_bool(self, bool):
        """Returns String of Boolean value.

        Returns:
            string: "false" or "true"
        """
        if bool is False:
            return "false"
        elif bool is True:
            return "true"
