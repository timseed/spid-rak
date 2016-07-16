 '''
 This is a test program for the Alfaspid RAK controller and
 is written in Python 2.7

 The program was written for demonstration purposes only and as
 a template for users to fashion any custom software project
 they may be attempting.

 Before using this program, the user must:
   1.  Install python2 followed by the pyserial module on the computer to
       be used.
   2.  Install and set-up the RAK Rotator and Controller in accordance
       with the Alfaspid RAK Manual and ensure that it is working with the
       manual controls on the controller.
   3.  Obtain a controller program such as Ham Radio Deluxe or N1MM to
       confirm that the RS232 or USB connection between the Computer
       and Controller are fully functional.

 Obtain a copy of file "Program_format-Komunicacji-2005-08-10.pdf"
 from the Alfaradio website to fully understand this program.

 This program was developed on a DELL 610 Laptop with Windows XP and
 tested on a computers running Windows 7, Debian Linux and OSX 10.10

 No warranty is stated nor implied by Alfaradio for this program's use.


This module was converted to Python3 by Tim Seed a45wg@sy-edm.com
There are no known issues in using this module


Please note The SPID rotator uses 1200 Baud !!

Working:
    MoveTo
    Status

ToDo:
   check stop functions

'''

from time import sleep
import logging
from .spid_serial3 import spid_serial3

class spid3(object):
    '''
    get the Comm Port information
    input_variable = raw_input ("Enter comm port: (Default /dev/cu.usbserial-A104FZJ8 ")
    if len(input_variable) < 5:
    input_variable="/dev/cu.usbserial-A104FZJ8"
    '''

    def __init__(self, port="/dev/tty.usbserial-A104FZJ8", speed=1200, timeout=10):
        '''
        Initialize the SPID Rotator Class
        :param port: The name of the port i.e. /dev/tty.usbserial-A104FZJ8
        :param speed: I think this always has to be 1200 - so you can leave it blank and it will be 1200
        :param timeout: Devault value is 10
        :return:
        '''

        self.port = port
        self.speed = speed
        self.timeout = timeout
        # define constants.
        self.loop = 1
        self.zero5 = chr(0) *5
        self.logger = logging.getLogger(__name__)

        # Open Comm Port
        try:
            if self.logger:
                self.logger.debug("Trying to Open Port " + port)
            self.ser = spid_serial3(self.port, self.speed, self.timeout)
            if self.logger:
                self.logger.Info("Port " + port + " With no error")
        except  AttributeError:
            #If no logger defined we will get an error here
            print("%W: No logger defined")
        except Exception as err:
            self.logger.error(str.format("Err: {} {} Unable to open device {} ", str(err),type(err),port))

    def stop(self):
        '''
        Stop the Movement of the Rotator
        :return: Current Bearing in Degrees
        '''
        out = chr(87) + self.zero5 + self.zero5 + chr(15) + chr(32)
        x = self.ser.write(out)
        # Wait for answer from controller
        sleep(0.5)
        azs=self.status()
        print(("Rotator currently at %3d " % (azs) + "Degrees"))
            return azs

    def status(self):
        # Build the status command word.
        out = chr(87) + self.zero5 + self.zero5 + chr(31) + chr(32)
        x = self.ser.write(out)
        # Wait for answer from controller
        sleep(0.5)

        data = self.ser.read(5)
        # once all 5 characters are received, decode location.
        if len(data) >= 5:
            s1 = ord(data[1].encode('latin-1'))
            s2 = ord(data[2].encode('latin-1'))
            s3 = ord(data[3].encode('latin-1'))
            azs = s1 * 100 + s2 * 10 + s3
            # Since the controller sends the status based on 0 degrees = 360
            # remove the 360 here
            azs = azs % 360
            print(("Rotator currently at %3d " % (azs) + "Degrees"))
            return azs

    def moveto(self, az):
            # send command to rotator controller to move rotator
            # to the desired azimuth.
            az=int(az)
            # test to see if azimuth is in the range of 0 to 360 Degrees
            if (az < 0 or az > 360):
                self.logger.error("Invalid Azimuth")
                return
            else:
                # Convert Azimuth to number required by controller
                az = az + 360
                # Build message to be sent to controller
                out = chr(87) + str(az) + chr(48) + chr(1) + self.zero5 + chr(47) + chr(32)
                # Send message to Controller
                x = self.ser.write(out)

    def __del__(self):
            self.ser.flushInput()
            self.ser.flushOutput()
            self.ser.close()
            sleep(3)
            try:
                if self.ser.is_open():
                    print("Trying to close for 2nd time")
                    self.ser.flushInput()
                    self.ser.flushOutput()
                    self.ser.close()
                if self.ser.is_open():
                    print("Failed to correctly close the serial Port - a machine restart will probably be needed.")
            except:
                print('Closing ')
