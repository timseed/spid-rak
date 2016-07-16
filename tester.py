from ham_dev.rotator import spid3, spid_serial3
from time import sleep
import sys
import logging

if __name__ == "__main__":
    if len(sys.argv)==3:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        test_type=int(sys.argv[2])
        if test_type==1:
            myRak=spid3(sys.argv[1])
            pos=myRak.status()
            print(str.format('Current Position is {}',pos))
            sleep(2)
            ipos=int(pos)
            print(str.format("Now Moving from {} to {}",ipos,ipos+10))
            myRak.moveto(ipos+10)
            sleep(4)
            pos=myRak.status()
            print(str.format('Current Position is {}',pos))
            print(str.format("Moving back to {}",pos))
            sleep(4)
            myRak.moveto(ipos)
            sleep(4)
            print("RAK Test finished")

        elif test_type==2:
            myRak=spid3(sys.argv[1])
            pos=myRak.status()
            print(str.format('Current Position is {}',pos))
            print("Long Move & Stop Test")
            sleep(2)
            ipos=(int(pos)+90)%360
            print(str.format("Now Moving from {} to {}",pos,ipos))
            myRak.moveto(ipos)
            sleep(5)    #It will not have got there yet
            print("Stopping Move")
            stoppedpos=myRak.stop()
            print(str.format("Rak Stopped at {}",stoppedpos))
            sleep(2)
            print("Returning to Start Position")
            myRak.moveto(pos)
    else:
        print("Usage: python tester.py <DeviceName> <TestNumber>")
        print("\n\n")
        print("device name looks like: /dev/tty.usbserial-A104FZJ8")
        print("test can be :  ")
        print("               1: Simple 10 degree swing and back")
        print("               2: Simple 30 degree stop, and swing back")
        print("i.e. python tester.py /dev/tty.usbserial-A104FZJ8 1")


