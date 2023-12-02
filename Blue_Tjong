from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis
from pybricks.robotics import DriveBase,
from pybricks.tools import wait, StopWatch




hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
dt=DriveBase(Motor(Port.F,Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE),56,84)
dt.settings(577,577,577)
#dt.distance_control.pid(1000,0,200)
am=Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
am1=Motor(Port.A, positive_direction=Direction.CLOCKWISE)
adt=DriveBase(am, am1, 56, 84)




dt.straight(300)
wait(50)
dt.straight(105)
wait(20)
dt.turn(19)
wait(400)
dt.turn(26)
dt.straight(-200)
dt.turn(-70)
wait(20)
dt.straight(-150)
dt.turn(70)
dt.straight(-100)
