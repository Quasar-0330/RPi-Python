import subprocess
import re
import i2clcda as lcd
import psutil
from time import sleep

lcd.lcd_init()

while True:
	sleep(1)
	cmd = "sudo vcgencmd measure_temp"
	temp = subprocess.check_output(cmd.split())
	cpuusage = psutil.cpu_percent(interval=0)
	temp = temp.decode("utf-8")
	temp = re.sub("temp=|'C|\n", "", temp)
	lcd.lcd_string("CPU Temp {}'C".format(temp), lcd.LCD_LINE_1)
	lcd.lcd_string("CPU Usage {}%".format(cpuusage), lcd.LCD_LINE_2)
