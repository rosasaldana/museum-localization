from marvelmind import MarvelmindHedge
from time import sleep
import sys

def main():
    hedge = MarvelmindHedge(tty = "/dev/tty.usbmodem1411", adr=10, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    while True:
        try:
            sleep(1)
            print('IMU Data:')
            print(hedge.valuesImuData)
            print('Raw IMU Data:')
            print (hedge.valuesImuRawData) # get last position and print
            print('Position Raw:')
            print (hedge.position()) # get last position and print
            print('Position:')
            hedge.print_position()
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()
