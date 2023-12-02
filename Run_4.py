from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
dt=DriveBase(Motor(Port.F,Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE),56,84)
#dt.settings(277,277,277)
#dt.distance_control.pid(1000,0,200)
am=Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
am1=Motor(Port.A, positive_direction=Direction.CLOCKWISE)
adt=DriveBase(am, am1, 56, 84)
dt.use_gyro(True)


#Mission 1
dt.straight(50)
dt.turn(45)
dt.straight(98)
dt.turn(-45)
dt.straight(555)
dt.turn(45)
dt.straight(163)
dt.turn(-90)
dt.straight(200)
dt.straight(-150)
dt.straight(150)
#Mission 2
dt.straight(-250)
dt.turn(135)
dt.straight(225)
dt.turn(-90)
dt.straight(30)
adt.straight(-290)
adt.straight(290)
dt.straight(-30)
#Mission 3
dt.turn(90)
dt.straight(300)
dt.turn(-90)
dt.straight(160)
dt.turn(215)
dt.turn(-35)
dt.straight(160)
#Mission 4
dt.turn(-90)
dt.straight(450)
dt.turn(-50)
dt.straight(190)
#Mission 5
dt.straight(-100)
dt.turn(120)
dt.straight(600)


