# spid-rak
Python3 Spid Rotator controller

In early 2015 I received a SPID RAK Rotator with the Computer Control module. After installing I then set around to try and control it from the Linux/Mac software I use - but I could not find anything specific - instead of putting the controller into emulation mode (it can pretend to be a Yaesu as well as other types I believe) - I looked for the programming manual for this controller and set to work in Python.

#Python 2.x

If you are running this version of Python - and most Linux Distro's have this as their base version then there is already a good set of utils you can use [Utils for Controlling](http://alfaradio.ca/downloads/program_info/).

However, if you develop in Python3 - then this will not work.


#Python 3.x

As I develop in a multi-language enviroment I always use UTF-8 based development tools, however the "low-down" data data transfer mechanism is often still byte oriented - so you end up putting countless encode, decode method into your code.

I therefore took the base Python2.x code set - and gave it a slight update. Nothing too major, overriding some of the default serial method to auto encode/decode plus update the docstrings.


#How do I use it ?

Download and there should a tester.py file - 


```bash
python tester.py <Device Name in Full> <TestNumber>
```

##Device Name

In Linux/Mac it will appear in /dev


```bash
ls /dev | grep -i USB
```

Will give you a list of the possible device names.


## Test Number

There are 2 simple tests.

  - 1 
    -  Get your heading move +10 Degress, and Move Back 
  - 2
    -  Get your heading move +90 degress, but **STOP** and then return to original

#What next ?

Up to you - it is about 2 minutes work to add a command line option so you can control your spid from a terminal window.

