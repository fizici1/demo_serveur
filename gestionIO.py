#-*-coding:utf-8-*

import grovepi
import wiringpi2 as wiringPi
import json

relay_pin = 2
DHT_pin = 3
RGB_pin = 4
US_pin = 7
PIR_pin = 8
PWM_GPIO = 18

def setupIO():
    # Initialisation des entrées sorties sur le GrovePi #
    grovepi.pinMode(relay_pin,"OUTPUT")
    grovepi.pinMode(RGB_pin,"OUTPUT")
    grovepi.pinMode(PIR_pin, "INPUT")
    grovepi.chainableRgbLed_init(RGB_pin,8)
    
    # On génère un PWM hardware de fréquence 50Hz #
    # La largeur de l'impulsion est entre 0,8 et 2ms #
    wiringPi.wiringPiSetupGpio()
    wiringPi.pinMode(PWM_GPIO, 2)
    wiringPi.pwmSetMode(0)
    wiringPi.pwmSetClock(384)
    wiringPi.pwmSetRange(1024)
    wiringPi.pwmWrite(PWM_GPIO,75)

def readData():
    try:
        json_obj = json.dumps({
                'temp' : grovepi.dht(DHT_pin,1)[0],
                'hum' : grovepi.dht(DHT_pin,1)[1],
                'lum' : grovepi.analogRead(0),
                'dist' : grovepi.ultrasonicRead(US_pin),
                'pot' : grovepi.analogRead(1),
                'pir' : grovepi.digitalRead(PIR_pin)
                }) 
        return json_obj
    except IOError:
        print "Erreur d'entrée/sortie"

def controle(nom, etat):
    if nom == 'lampe':
        grovepi.digitalWrite(relay_pin, etat)
    if nom == 'servo':
        wiringPi.pwmWrite(PWM_GPIO,etat)

def RGB(rouge, vert, bleu):
    grovepi.storeColor(rouge, vert, bleu)
    grovepi.chainableRgbLed_pattern(RGB_pin, 2, 5)

def lumiere(SB, SH, active):
    grovepi.appliLumiere(SB, SH, active)
