#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import serial
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import time
from datetime import datetime


plotly.tools.set_credentials_file(username="fjblau", api_key="UqWW0QabemCegQnB2mV2")
arduino = serial.Serial('/dev/cu.usbserial-DN04QYYO', 9600, timeout=.1)
arduino.flushInput()
arduino.flush()
arduino.flushOutput()

Lx = []
Ly = []
ln = 0
for n in range (1,30):
	time.sleep(1)
	#print(n)
	
	data = arduino.readline()[:-2].decode("utf-8")  #the last bit gets rid of the new-line chars
	print (data)
	if n > 10:
		if data[:1]=="$":
			ln = ln + 1
			
			Lx.append(datetime.now().strftime('%H:%M:%S'))
			Ly.append(float(data.split(",")[9][data.split(",")[9].find("=")+1:]))

print (Lx)
print (Ly)

plotdata = [
	go.Scatter(
	x = Lx,
	y = Ly
	)
	]

plot_url = py.plot(plotdata, filename='light-data-plot')

		


