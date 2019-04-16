import paho.mqtt.client as mqtt #import the client1
import time

#broker_url="192.168.1.184" 
broker_url="iot.eclipse.org"

first_topic = "/i0t1md/temperatura"
second_topic = "/i0t1md/umidade"
broker_url = "iot.eclipse.org"

############
def on_message(client, userdata, message):

	fMessage = str(message.payload.decode("utf-8"))

	#print("Mensagem '{}' Recebida do Topico {}.").format(fMessage, message.topic)

	if message.topic == "/i0t1md/temperatura":
		print("Temperatura {}*C").format(fMessage)
	elif message.topic == "/i0t1md/umidade":
		print("Umidade {}%").format(fMessage)
	else:
		print("Topico nao subscrito")

	#Dados adicionais pra usar
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
########################################

print("Criando nova instancia de cliente.")
client = mqtt.Client("P1") #cria nova instancia

client.on_message=on_message #atribuindo funcao de callback

print("conectando ao broker")
client.connect(broker_url) #conecta ao broker

#client.loop_start() #inicia um loop

print("Subscrevendo no topico {}").format(first_topic)
client.subscribe(first_topic)	#subscreve no topico 1

print("Subscrevendo no topico {}").format(second_topic)
client.subscribe(second_topic)	#subscreve no topico 2

#time.sleep(10)

#client.loop_stop() #termina o loop
client.loop_forever() #forever in the loop