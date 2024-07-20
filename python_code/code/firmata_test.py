from pyfirmata import Arduino ,SERVO,util
from time import sleep

port ='COM5'
pin1 = 6
pin2 = 7
board = Arduino(port)

board.digital[pin1].mode=SERVO
board.digital[pin2].mode=SERVO


def rotateservo(pin,angle):
    board.digital[pin].write(angle)

    # sleep(0.015)

while True:
    x=input("angle:")
    y=input("angle2:")
    # if x=="1":
    #     for i in range(0,180):
    rotateservo(pin1,x)
    rotateservo(pin2,y)