from ham_dev.rotator import spid3, spid_serial3
from time import sleep
import sys
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    myRak=spid3()
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