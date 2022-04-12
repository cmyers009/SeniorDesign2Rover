import paho.mqtt.client as mqtt

BROKER_HOST = "test.mosquitto.org"
BROKER_PORT = 1883
TOPIC = "TEST"

def on_connect(client,user_data,rc):
    if rc==0:
        print("connected successfully")
    else:
        print("Connection failed. rc= "+str(rc))
def on_publish(client,user_data,mid):
    print("Message "+str(mid)+" published.")

mqttclient = mqtt.Client()
mqttclient.connect(BROKER_HOST,BROKER_PORT)

mqttclient.on_connect=on_connect
mqttclient.on_publish=on_publish

#mqttclient.publish(TOPIC,"Communication")
#mqttclient.publish(TOPIC,"Is")
#mqttclient.publish(TOPIC,"Working!!!!")

def publish_data(data_code,data):
    mqttclient.publish(data_code,data)
