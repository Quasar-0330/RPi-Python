from gpiozero import Buzzer
from time import sleep
import subprocess
import re

bz = Buzzer(18)

while True:
	sleep(1)
	cmd = "sudo vcgencmd measure_temp"
	temp = subprocess.check_output(cmd.split())
	temp = temp.decode("utf-8")
	temp = re.sub("temp=|'C|\n", "", temp)
	if float(temp) >= 70:
		bz.on()
