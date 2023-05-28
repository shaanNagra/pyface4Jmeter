# pyface4Jmeter
A python interface to create jmeter scripts in JMX format

> NOTE: This project was initially a small tool in a larger research project.   </br>
> The interface was used by an automated load testing application to build the  </br>
> jmeter scripts. The project was archived back in 2021.

## Version Requirements


## Implemented Components

Jmeter offers alot of different components for creating tests. However, not     </br>
every component was required for our use. The list below shows the currently    </br>
implemented components.

### Samplers
*  [JSR223 Sampler](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Sampler)

### Logic Controllers
* [Simple Controller](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Controller)
* [Once Only Controller](https://jmeter.apache.org/usermanual/component_reference.html#Once_Only_Controller)
* [Random Controller](https://jmeter.apache.org/usermanual/component_reference.html#Random_Controller)
* [Module Controller](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller)

### Listeners
* No Listeners have been implemented yet.
### Cofiguration Elements
* No Configuration Elements have been implemented yet.
### Assertations
* No Assertation Elements have been implemented yet.
### Timers
* [Uniform Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Uniform_Random_Timer)

### Pre Processors
* No Pre Processors have been implemented yet.
### Post Processors
* No Post Processors have been implemented yet.
### Miscelaneous Features
* [Test Plan](https://jmeter.apache.org/usermanual/component_reference.html#Test_Plan)
* [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group)
* [Test Fragment](https://jmeter.apache.org/usermanual/component_reference.html#Test_Fragment)

### Extensions

Components that are extensions for Jmeter

#### Logic Controllers
* [Blazemeters Weighted Switch Controller]()