import serial
import datetime
import ephem
from math import degrees as deg
import requests
format = "%Y-%m-%d %H:%M"
# Local latitude, longitude coordinates - decimal degrees
# latitude is +ve in Northern hemisphere, longitude is +ve east of Greenwich
home_lat = 37.87060
home_lon = -4.77860

home = ephem.Observer()
home.lat, home.lon = str(home_lat), str(home_lon)
home.date = datetime.datetime.utcnow()

sun, moon = ephem.Sun(), ephem.Moon()

sun.compute(home)
sun_az  = round(deg(float(sun.az)),1)
sun_al = round(deg(float(sun.alt)),1)
sunrise  = home.previous_rising(sun)
sunset   = home.next_setting(sun)

moon.compute(home)
moon_az  = round(deg(float(moon.az)),1)
moon_al = round(deg(float(moon.alt)),1)
moon_illum = round(moon.phase,1)
moonrise = ephem.localtime(home.next_rising(moon)).strftime(format)
moonset  = ephem.localtime(home.next_setting(moon)).strftime(format)
full_moon = ephem.localtime(ephem.next_full_moon(home.date)).strftime(format)

sol = round(23/(360/sun_az))
luna = round(23/(360/moon_az))

arduino = serial.Serial('/dev/serial0', 9600)

while True:
  comando = sol
  arduino.write(comando)
arduino.close()

print(sol)
print(luna)
print(sun_az)
print(moon_az)
