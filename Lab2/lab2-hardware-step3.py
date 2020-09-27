# The Hardware I'm using are Raspberry pi and a SenseHat
from sense_hat import SenseHat
import time

s = SenseHat()
# Get the raw information of the compass
raw = s.get_compass_raw()

# Assign the compass values to x, y, and z
x = raw["x"]
y = raw["y"]
z = raw["z"]

# Dispaly the result on the screen
s.show_message(str(int(x)))
time.sleep(1)
s.show_message(str(int(y)))
time.sleep(1)
s.show_message(str(int(z)))
