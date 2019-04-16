import paho.mqtt.client as mqtt
import time

first_topic = "/i0t1md/data1"
second_topic = "/i0t1md/data2"
broker_url = "iot.eclipse.org"

def mqtt_client_connect():
    print("connected to: ", broker_url)
    client.connect(broker_url)
    client.loop_start()

client = mqtt.Client("client_name")
mqtt_client_connect()

n = 0

while True:
	print("Publishing on {} data 1: {}").format( first_topic, str(n) )
	print("Publishing on {} data 2: {}").format( second_topic, str(n+1) )

	client.publish(first_topic, n)
	client.publish(second_topic, n+1)
	n = n + 1
	time.sleep(5)