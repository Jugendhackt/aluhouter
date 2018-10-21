<readme>

	<microcontroller>

		You can use every microcontroller. WiFi capabiltities of esp32 are not nesseccary.

		It's written in micropython.

		<pin configuration>

			WS2812 controll pin:  Pin 13

			Serial communication: RX0 and TX0

		</pin configuration>

	</microcontroller>

	connect router with microcontroller with serial communication. The most routers have an usb port or at least serial pins on the PCB

	<router>

		The router is flashed and got the Freifunk Firmware. For further instructions, visit their website. The firmware depends on the local Freifunk group at your city.

		Berlin Freifunk page: https://berlin.freifunk.net/index_en/

		German version:       https://berlin.freifunk.net/

		On the router, there is a Shellscript transmitting data. It can be found at ./router_shellscript.

	</router>

<readme>
