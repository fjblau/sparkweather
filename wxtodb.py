#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import serial
import time
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="172.104.235.199",
  user="wx1",
  passwd="group1",
  database="wx1"
)

mycursor = mydb.cursor()

arduino = serial.Serial('/dev/cu.usbserial-DN04QYYO', 9600, timeout=.1)
arduino.flushInput()
arduino.flush()
arduino.flushOutput()

for x in range(0, 20):
	data = arduino.readline()
	print ("ignore - ", data)

while (True):
	time.sleep(2)
	data = arduino.readline()[:-2].decode("utf-8")
	if data[:1]=="$":
		data = "("+data[2:-2]+")"
		print ("use - ", data)
		sql = "INSERT INTO wx(winddir, windspeedmph, windgustmph, windgustdir, windspdmph_avg2m, humidity, tempf, rainin, dailyrainin, pressure, light_lvl)" \
		" VALUES " + data
		print (sql)
		mycursor.execute(sql)
		mydb.commit()
