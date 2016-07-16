
import serial


class spid_serial3(serial.Serial):
    '''
    Wrap the standard Serial class in a python3 super-class. So I do not have to worry about
    casting data to and from bytes.

    Please note: This has only been tested with read, write throughly - and only with the RAKSpid device.

    Author: Tim Seed
    E-Mail: a45wg@sy-edm.com
    url:
    '''

    def __init__(self,port,speed,timeout):
        '''
        Generic Init routine
        :param port: Serial Port Name
        :param speed: Baud Rate
        :param timeout: Timeout
        :return: Nothing
        '''
        super().__init__(port=port,baudrate=speed,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,timeout=timeout)

    def write(self, cmd):
        '''
        Write utf-8 data to serial device. This will auto convert to bytes prior to sending.
        :param cmd: The command to be send
        :return: The lenth of the data sent
        '''
        cmd = bytes(cmd.encode('utf-8'))
        sent=super(spid_serial3, self).write(cmd)
        return sent

    def read(self, size=1):
        '''
        Read byte data from Serial device and auto convert to utf-8 prior to returning the data.
        :param size: Number of bytes to read
        :return: utf-8 string of the data
        '''
        data = super(spid_serial3, self).read(size=size)
        return data.decode('utf-8')

    def read_all(self):
        data = super(spid_serial3, self).read_all()
        return data.decode('utf-8')

    def read_line(self):
        data = super(spid_serial3, self).readline()
        return data.decode('utf-8')