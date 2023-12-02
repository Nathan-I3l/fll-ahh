from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis




hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
dt=DriveBase(Motor(Port.F,Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE),56,84)
dt.settings(577,577,577)
#dt.distance_control.pid(0,0,0)
am=Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
am1=Motor(Port.A, positive_direction=Direction.CLOCKWISE)
adt=DriveBase(am, am1, 56, 84)
hub.speaker.volume(100)
dt.use_gyro(True)




#am.run_target(900,0)
dt.straight(230)
dt.turn(-45)
dt.straight(275)
am.run_target(900,-360)
dt.straight(-100)
dt.straight(-300)
am.run_target(900,0)


am.run_target(900,0)
dt.turn(45)
dt.straight(-200)
