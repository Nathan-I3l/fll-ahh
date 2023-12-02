from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch








hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
dt=DriveBase(Motor(Port.F,Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE),56,84)
dt.settings(977,977,977)
am=Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
am1=Motor(Port.A, positive_direction=Direction.CLOCKWISE)
adt=DriveBase(am, am1, 56, 84)
hub.speaker.volume(100)
dt.use_gyro(True)


dt.straight(190)
dt.turn(-15)
dt.straight(140)
dt.turn(50)
dt.turn(-50)
dt.straight(-300)
