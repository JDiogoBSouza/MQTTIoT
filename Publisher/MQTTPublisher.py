import paho.mqtt.client as mqtt
import time
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 23

temperatura_topic = "/i0t1md/temperatura"
umidade_topic = "/i0t1md/umidade"
broker_url = "iot.eclipse.org"

def mqtt_client_connect():
    print("conectando ao broker: ", broker_url)
    client.connect(broker_url)		#Conecta ao broker de mensagens
    client.loop_start()				#Inicia loop

client = mqtt.Client("Raspberry") #Cria nova instancia
mqtt_client_connect()			 	#Chama funcao para conectar ao broker

n = 0

while True:
	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	# Note that sometimes you won't get a reading and
	# the results will be null (because Linux can't
	# guarantee the timing of calls to read the sensor).
	# If this happens try again!
	if humidity is not None and temperature is not None:
		print("Publicando no Topico {} : {}*C").format( temperatura_topic, temperature )
		print("Publicando no Topico {} : {}%").format( umidade_topic, humidity )

		client.publish(temperatura_topic, temperature)		#publica o dado no topico 1
		client.publish(umidade_topic, humidity)			#publica o dado no topico 2
	else:
    		print('Failed to get reading. Try again!')

	time.sleep(10)