import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
try:
	while True:
		for x in range(0, 5):
			GPIO.output(17, 1)       # set GPIO24 to 1/GPIO.HIGH/True  
			time.sleep(0.5)   
			GPIO.output(17,0)
			time.sleep(0.4) #Each for loop takes 100ms to iterate so there is no need to sleep for the full 500 ms. This apply to all of the following loops
		for x in range(0,50):
			# The read_adc function will get the value of the specified channel (0-7)self.
			lightLevel = mcp.read_adc(0)
			if lightLevel > 600:
				print("Light " + str(lightLevel))
			else:
				print("Dark " + str(lightLevel))
		for x in range(0, 4):
			GPIO.output(17, 1)       # set GPIO24 to 1/GPIO.HIGH/True  
			time.sleep(0.2)   
			GPIO.output(17,0)
		for x in range(0,50):
			# The read_adc function will get the value of the specified channel (0-7)self.
			soundLevel = mcp.read_adc(1)
			if soundLevel > 100:
				GPIO.output(17,0)
				print("Ambient " + str(lightLevel))
			else:
				print("Loud " + str(lightLevel))
				GPIO.output(17, 1) 
				x += 1
			time.sleep(0.1) 
		for x in range(0, 4):
			GPIO.output(17, 1)       # set GPIO24 to 1/GPIO.HIGH/True  
			time.sleep(0.2)   
			GPIO.output(17,0)
			time.sleep(0.1)             # wait half a second  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
	GPIO.cleanup()                 # resets all GPIO ports used by this program  
