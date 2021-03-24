import random

class TempSensor:
    
  def __init__(self):
    self.currentTemp = random.randint(10,90)  # works in farenheit

  def getTemp(self, mode):
    f = self.currentTemp
    if mode == 'm':  # m is metric. switch to centrigrade
        c = (f - 32) * 5/9
        return str(int(c)) + '°c'
    else:
        return str(int(f)) + '°f'

#ts = TempSensor()
#print(ts.getTemp('e'))

#ts = TempSensor()
#print(ts.getTemp('m'))

