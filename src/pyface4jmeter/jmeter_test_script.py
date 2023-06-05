#!/usr/bin/env python

# EXTERNAL IMPORTS
import lxml.etree as ET

# INTERNAL IMPORTS
from .internal.constants import HASH_TREE

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////

class JmeterTestPlan:
    """The Class that represents the JMeter Element 'Wrapper'.

    Attributes: 
        version:
        properties:
        jmeter:

    Methods:
        append(Element): Appends Element as child to this one.
        toString: Returns element content as a string.
        print(): Prints JMX of element.
        enable(enable=True): Sets the enable flag of JMX element.
        bool_2_bool: Returns string of Boolean value.
    """
    def __init__(self, version, properties, jmeter):
        self.__header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

        self.Element = ET.Element('jmeterTestPlan')
        self.Element.set('version', version)
        self.Element.set('properties', properties)
        self.Element.set('jmeter', jmeter)
        self.hashTree = ET.fromstring(HASH_TREE)
        self.Element.append(self.hashTree)

    def append(self, elem):
        """ Appends given element as subelement.

        Parameter:
            elem: The Element object to append as subelement.
        """
        self.hashTree.extend(elem)
        return

    def print(self):
        """Print string content of element and any sibling elements.
        """
        print(ET.tostring(self.Element))
        return

    def toString(self):
        """Returns element content as a string.

        Returns:
            String: JMX Element content.
        """
        return ET.tostring(self.Element)

    def enable(self, enable=True):
        """Sets enable flag of a JMX Elements.
        """
        self.Element.set('enabled', self.Bool2Bool(enable))
        return

    def Bool2Bool(self, bool):
        """Returns String of Boolean value.

        Returns:
            string: "false" or "true"
        """
        if bool is False:
            return "false"
        elif bool is True:
            return "true"
