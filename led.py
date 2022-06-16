import paho.mqtt.client as mqtt
from led import LED

led = LED()
def connect_result(client,userdata,flags,rc):
    if rc ==0 :
        client.subscribe("test/#")
        print("연결")
    else:
        print("연결실패")

def on_message(client,userdata,message):
    myval = message.payload.decode("utf-8")
    print(myval)
    if myval =="on":
        led.led_on()
        print("on")
    elif myval == "off":
        led.led_off()
        print("off")

try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message

    mqttClient.connect("172.20.10.8",1883,60)
    mqttClient.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    pass