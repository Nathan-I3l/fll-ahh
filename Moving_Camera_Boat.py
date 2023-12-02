from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()


hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
left_wheel= Motor(Port.F,Direction.COUNTERCLOCKWISE)
right_wheel=Motor(Port.B, Direction.CLOCKWISE)
dt=DriveBase(left_wheel,right_wheel,56,84)
dt.settings(477,477,477)
#dt.distance_control.pid(1000,0,200)
at = Motor(Port.E, Direction.CLOCKWISE)
at1 = Motor(Port.A, Direction.COUNTERCLOCKWISE)
adt=DriveBase(at, at1, 56, 84)


dt.straight(425)
at.run_angle(450, 100)
dt.straight(-200)
at.run_angle(450, -150)
dt.straight(-250)
