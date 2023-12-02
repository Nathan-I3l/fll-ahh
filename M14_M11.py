from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
dt=DriveBase(Motor(Port.F,Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE),56,84)
dt.settings(577,577,977)
#dt.distance_control.pid(1000,0,200)
at = Motor(Port.E, Direction.CLOCKWISE)
at1 = Motor(Port.A, Direction.COUNTERCLOCKWISE)
adt=DriveBase(at, at1, 56, 84)


dt.curve(-500,90, wait=True)
dt.straight(-280)
dt.curve(-75,-90)
dt.straight(-50, wait=True)
dt.turn(10)
dt.straight(-50,wait=True)
dt.straight(125)
dt.turn(5)
dt.straight(35)
at.run_time(900,5000)
at.run_time(900,3500)
dt.straight(-70)
dt.turn(72)
dt.curve(-500,-100)
dt.straight(-350)
