import machine
import neopixel
import utime

STREIFEN_ANZAHL = 3
PER_STREIFEN = 5

np = neopixel.NeoPixel(machine.Pin(13), STREIFEN_ANZAHL * PER_STREIFEN)

def mapTo5(input):
	if input < -85:
		return 1

	elif input < -80:
		return 2

	elif input < -75:
		return 3

	elif input < -70:
		return 4

	elif input > -65 and input < 0:
		return 5

	else:
		return 0


def drawLights(nr):
	if nr < 1 or nr > 5:
		draw_error()
		return

	for streifen_index in range(STREIFEN_ANZAHL):
		for led_in_streifen_index in range(PER_STREIFEN):
			if streifen_index % 2 == 0:
				led_index = streifen_index * 5 + led_in_streifen_index
			else:
				led_index = (streifen_index+1) * 5 - led_in_streifen_index -1

			r, g, b = map(nr, led_in_streifen_index)

			np[led_index] = (r, g, b)

	np.write()	
	np.write()
	np.write()

def map(nr, led_index):
	if led_index < nr: #1 <= nr <= 5; 0 <= led_index <= 4
		#beleuchtet
		return color_of(nr)
	else:
		return 0, 0, 0 #led dunkel

def color_of(nr):
	if nr == 1:
		return 255, 0, 0
	if nr == 2:
		return 255, 64, 0
	if nr == 3:
		return 255, 128, 0
	if nr == 4:
		return 128, 255, 0
	if nr == 5:
		return 0, 128, 255

	return 100, 100, 100

def draw_error():
	for streifen_index in range(STREIFEN_ANZAHL):
		for led_in_streifen_index in range(PER_STREIFEN):
			led_index = streifen_index * 5 + led_in_streifen_index

			np[led_index] = (255, 255, 255)

def run_loading_animation():
	while True:
		for nr in range(5):
			drawLights(nr +1)
			utime.sleep_ms(500)