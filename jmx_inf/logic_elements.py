#!/usr/bin/env python

# EXTERNAL IMPORTS
import lxml.etree as ET

# INTERNAL IMPORTS
from jmx_inf.internal.base_element import BaseElem
from jmx_inf.internal.constants import (BZM_WEIGHTED_SWITCH_CONTROLLER,
                                        SIMPLE_CONTROLLER,
                                        RANDOM_CONTROLLER,
                                        ONCE_ONLY_CONTROLLER,
                                        MODULE_CONTROLLER)

"""This module contains classes for some JMX logical controllers. 

Classes: 
    WeightedSwitchController:
    SimpleController:
    RandomController:
    OnceOnlyContoller:
    ModuleController:


"""


class WeightedSwitchController(BaseElem):
    """The JMX Element for the Weighted Switch Controller.
    
    The weighted switch controller is a JMeter extension created by 
    https://www.blazemeter.com/. The weighted switch controller allows users to 
    define probability value of the subelements.
    SRC: https://github.com/Blazemeter/jmeter-bzm-plugins/tree/master/wsc


    Attributes:
        name: the name value of the JMX Elemnt (default 'wsc')

    Methods:
        addCase(caseName, weight): adds switch case to controller with given weight
    """
    def __init__(self, name='wsc'):
        # self.cases = list(dict())
        super().__init__(BZM_WEIGHTED_SWITCH_CONTROLLER, name)


    def addCase(self, caseName, weight):
        """Add case to list with given probability

        Parameters:
            caseName: the name of the case (used as ID)
            weight: the probability of case being selected (e.g. 75)
        """
        collProp = ET.Element('collectionProp', name=caseName+'Props')

        nameProp = ET.Element('stringProp', name=caseName+"Name")
        nameProp.text = caseName

        weightProp = ET.Element('stringProp', name=caseName+'Weight')
        weightProp.text = str(weight)

        enableProp = ET.Element('stringProp', name=caseName+'Enabled')
        enableProp.text = self.bool_2_bool(True)

        collProp.append(nameProp)
        collProp.append(weightProp)
        collProp.append(enableProp)

        self.Element.find(
            './/collectionProp[@name="Weights"]'
            ).append(collProp)


class SimpleController(BaseElem):
    """The JMX Element for a Jmeter GenericContoller

    """
    def __init__(self, name='simple controller'):
        super().__init__(SIMPLE_CONTROLLER, name)


class RandomController(BaseElem):
    """The JMX Element for a Random Controller.
    
    The Random Logic Controller acts similarly to the Interleave Controller, 
    except that instead of going in order through its sub-controllers and 
    samplers, it picks one at random at each pass.

    Attribute:

    Methods:
        configRC_ignoreSubcontrollerBlocks(Ignore=False): Set flag ignore 
        sub-controller blocks.
    """
    def __init__(self, name='Random Controller'):
        super().__init__(RANDOM_CONTROLLER, name)

    def configRC_ignoreSubcontrollerBlocks(self, Ignore=False):
        """Set flag ignore sub-controller blocks.
        
        If checked, the interleave controller will treat sub-controllers like single request 
        elements and only allow one request per controller at a time.

        Parameters: 
            Ignore: to ignore sub-controller blocks
        """
        flag = 1

        if Ignore is True:
            flag = 0

        self.Element.find(
            './/intProp[@name="InterleaveControl.style"]'
            ).text = flag

        return


class OnceOnlyController(BaseElem):
    """The JMX Element for a Once Only Controller

    The Once Only Logic Controller tells JMeter to process the controller(s) 
    inside it only once per Thread, and pass over any requests under it during 
    further iterations through the test plan.

    Attribute:

    Methods:

    """
    def __init__(self, name='Once Only Controller'):
        super().__init__(ONCE_ONLY_CONTROLLER, name)



class ModuleController(BaseElem):
    """The JMX Element for a Module Controller

    The Module Controller provides a mechanism for substituting test plan 
    fragments into the current test plan at run-time.

    Attributes:

    Methods:
        add_path:
    """
    def __init__(self, name='Module Controller'):
        super().__init__(MODULE_CONTROLLER, name)

    def add_path(self, path):
        path_elem = self.Element.find(
            './/collectionProp[@name="ModuleController.node_path"]'
            )
        old_path = path_elem.getchildren()
        if old_path is None:
            for item in old_path:
                path_elem.remove(item)

        for item in path:
            newElem = ET.Element('stringProp', name=item+"PathProp")
            newElem.text = item
            path_elem.append(newElem)


# test = ModuleController()
# test.add_path(['the','path','lol'])
# test.print()
