## Basic Ideas

The main ideas came from this blog https://www.instructables.com/Build-Your-Own-Weasley-Location-Clock/ by http://www.patpeters.org 

## The clock

I took an old mechanical wooden clock that I found on Ebay because I wanted to reuse as many parts as possible from the old mechanics and the original pointers. But combining the old gears with modern ones and the motors was kind of tricky in the end as is still not working perfectly.

## The motors

I wanted to reuse an old Raspberry Pi type B I decided to use stepper motors instead of servo motors. Main reason was that the Joy-It motors with the board was a perfect fit: https://joy-it.net/de/products/RB-Moto2 . To drive the old mechanical clock gears with the motor I used belts and gears that were made for 3D Printers.

## The mobile app

The Owntracks App is a perfect fit to send MQTT Protocoll based location information to the Rasbperry.

## The MQTT Server

I did not manage to install a local MQTT server on my Raspberry Pi. Unfortunately it became quite hard to find a free MQTT server on the internet. What worked for me is the offering from https://www.hivemq.com/ offering a free MQTT server hosted on AWS that allows 3 concurrent connections. Just enough to connect 2 mobile devices and the Raspberry Pi.

## The Software 

Receiving the MQTT information and sending it to a small Python program that manages the motors is really simple with a node-red flow https://nodered.org/   I created two separated flows for the 2 pointers

![](/Users/d028779/Desktop/node-red.png)





 