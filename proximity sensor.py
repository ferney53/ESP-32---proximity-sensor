from machine import Pin, ADC, PWM
from utime import sleep, sleep_ms
from hcsr04 import HCSR04
import network, time, urequests

def conectaWifi(red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect('ASUS_X00PD', 'ferney53')         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
     return True




sensor = HCSR04(trigger_pin=14, echo_pin=33)
led1 = Pin(18, Pin.OUT)
led2 = Pin(5, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(2, Pin.OUT)
led5 = Pin(15, Pin.OUT)
buzzer=PWM(Pin(25))

notas =[261, 293, 329, 349, 392 ]


if conectaWifi("Wokwi-GUEST", ""):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/distancia/with/key/hQCqP3sqC4tJ-zGMRHDeKWWK3eTYgLcECFgeBXw5hgd?"






    while True:
        distancia= sensor.distance_cm()
        print("distancia:{:.1f}cm".format(distancia))
        
        if distancia >201 and distancia <250:
            led1.on()
            led2.off()
            led3.off()
            led4.off()
            led5.off()
            buzzer.freq(3135)
            for sonido in range(0,1023):
                buzzer.duty(sonido)
            
        

        elif distancia >151 and distancia <200:
            led1.off()
            led2.on()
            led3.off()
            led4.off()
            led5.off()
            buzzer.freq(3322)
            for sonido in range(0,1023):
                buzzer.duty(sonido)
            

        elif distancia >101 and distancia <150:
            led1.off()
            led2.off()
            led3.on()
            led4.off()
            led5.off()
            buzzer.freq(3520)
            for sonido in range(0,1023):
                buzzer.duty(sonido)

        elif distancia >51 and distancia <100:
            led1.off()
            led2.off()
            led3.off()
            led4.on()
            led5.off()
            buzzer.freq(3729)
            for sonido in range(0,1023):
                buzzer.duty(sonido)

        elif distancia >0 and distancia <50:
            led1.off()
            led2.off()
            led3.off()
            led4.off()
            led5.on()
            buzzer.freq(3951)
            for sonido in range(0,1023):
                buzzer.duty(sonido)

            respuesta = urequests.get(url+"&value1="+str(distancia))      
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
           

        else:
            led1.off()
            led2.off()
            led3.off()
            led4.off()
            led5.off()
            buzzer.duty(0)
            buzzer.freq(1)


else:
       print ("Imposible conectar")
       miRed.active (False)
   
        


        
   