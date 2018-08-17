#!/usr/bin/python

import serial
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import time
from datetime import datetime


plotly.tools.set_credentials_file(username="fjblau", api_key="UqWW0QabemCegQnB2mV2")
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

Lx = []
Ly = []
ln = 0
for n in range (1,30):
	time.sleep(1)
	#print(n)
	
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	print data
	if n > 10:
		if data[:1]=="$":
			ln = ln + 1
			#for i in range (1,15):
			#print data.split(",")[15][data.split(",")[15].find("=")+1:]
			#print "\n"
			Lx.append(datetime.now().strftime('%H:%M:%S'))
			Ly.append(float(data.split(",")[13][data.split(",")[13].find("=")+1:]))

print (Lx)
print (Ly)

plotdata = [
	go.Scatter(
	x = Lx,
	y = Ly
	)
	]

plot_url = py.plot(plotdata, filename='light-data-plot')

		


