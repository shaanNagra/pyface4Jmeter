#!/usr/bin/env python

# EXTERNAL IMPORTS
import lxml.etree as ET

# INTERNAL IMPORTS
from ..internal.base_element import BaseElem
from ..internal.constants import (TEST_PLAN,
                                  THREAD_GROUP,
                                  TEST_FRAGMENT,
                                  )


class TestPlan(BaseElem):
    def __init__(self, name='Test Plan'):
        super().__init__(TEST_PLAN, name)

    def configTestPlan(
            self,
            comments,
            func_mode=False, teardown=False, s_tg=False):

        self.Element.find(
            './/stringProp[@name="TestPlan.comments"]').text = comments

        self.Element.find(
            './/boolProp[@name="TestPlan.functional_mode"]'
            ).text = self.Bool2Bool(func_mode)

        self.Element.find(
            './/boolProp[@name="TestPlan.tearDown_on_shutdown"]'
            ).text = self.Bool2Bool(teardown)

        self.Element.find(
            './/boolProp[@name="TestPlan.serialize_threadgroups"]'
            ).text = self.Bool2Bool(s_tg)
        return

class threadGroup(BaseElem):
    def __init__(self, name='Thread Group'):
        
        super().__init__(THREAD_GROUP, name)

    def config_loopCount(self, count, infinite=False):

        if infinite is False:
            newElem = ET.Element('stringProp', name='LoopController.loops')
            newElem.text = str(count)
        else:
            newElem = ET.Element('intProp', name='LoopController.loops')
            newElem.text = str(-1)

        if self.Element.find(
             './/intProp[@name="LoopController.loops"]'
             ) is None:
            elem = self.Element.find(
                './/stringProp[@name="LoopController.loops"]'
                )

        else:
            elem = self.Element.find(
                './/intProp[@name="LoopController.loops"]'
                )

        elem.addnext(newElem)
        parent = elem.getparent()
        parent.remove(elem)
        return

    def config_onSampleError(self, Action=0):
        """Sets action to be taken after a Sampler error

        Parameters:
            Action: Flag of which action to select. (0 = Continue ,
            1 = Start Next Thread Loop, 2 = Stop Thread, 3 = Stop Test,
            4 = Stop Test Now)

        Returns:
            Boolean: True if action was set
        """
        selectable = ['continue','startnextloop','stopthread',
                      'stoptest','stoptestnow']
        if 0 <= Action < len(selectable):
            on_sample_err_prop = self.Element.find(
                './/stringProp[@name="ThreadGroup.on_sample_error"]'
                )
            on_sample_err_prop.text = selectable[Action]
            return True
        return False

    def config_Lifetime(self, toggle=False, Duration="", StartupDelay=""):
        schedElem = self.Element.find(
            './/boolProp[@name="ThreadGroup.scheduler"]'
            )
        duratElem = schedElem.getnext()
        delayElem = duratElem.getnext()
        if toggle is False:
            schedElem.text = self.Bool2Bool(toggle)
            duratElem.text = ''
            delayElem.text = ''
        else:
            schedElem.text = self.Bool2Bool(toggle)
            duratElem.text = str(Duration)
            delayElem.text = str(StartupDelay)
        return

    def config_other(self, sameUserOnIter=False, numThreads=1, rampTime=1):
        numThreadsElem = self.Element.find(
            './/stringProp[@name="ThreadGroup.num_threads"]'
            )
        rampTimeElem = numThreadsElem.getnext()
        sameUserElem = self.Element.find(
            './/boolProp[@name="ThreadGroup.same_user_on_next_iteration"]'
            )
        numThreadsElem.text = str(numThreads)
        rampTimeElem.text = str(rampTime)
        sameUserElem.text = self.Bool2Bool(sameUserOnIter)
        return


class TestFragment(BaseElem):

    def __init__(self, name):
        super().__init__(TEST_FRAGMENT, name)

    def configTestFragment(self, comments):
        pass
