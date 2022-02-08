---
layout: default
---

# Weasleys Clock
The Weasleys Clock s a magical clock from the Harry Potter books owned by the Weasleys family which individually monitored each of their whereabouts. Located in the living room at The Burrow, the clock had nine golden hands, one for every member of the household. In place of hours on the clock's face were a series of possible locations, including "home," "school", "work", "travelling", "lost", "hospital", "prison", and "mortal peril".

## Basic Ideas

The main ideas came from this blog https://www.instructables.com/Build-Your-Own-Weasley-Location-Clock/ by http://www.patpeters.org 

## The clock

I took an old mechanical wooden clock that I found on Ebay because I wanted to reuse as many parts as possible from the old mechanics and the original pointers. But combining the old gears with modern ones and the motors was kind of tricky in the end as is still not working perfectly.

## The motors

I wanted to reuse an old Raspberry Pi type B I decided to use stepper motors instead of servo motors. Main reason was that the Joy-It motors with the board was a perfect fit: https://joy-it.net/de/products/RB-Moto2 . To drive the old mechanical clock gears with the motor I used belts and gears that were made for 3D Printers.

## The mobile app

The [Owntracks App](https://owntracks.org/) is a perfect fit to send MQTT protocol based location information to the raspberry pi.

## The MQTT Server

I did not manage to install a local MQTT server on my Raspberry Pi. Unfortunately it became quite hard to find a free MQTT server on the internet. What worked for me is the offering from [HiveMQ](https://www.hivemq.com/) offering a free MQTT server hosted on AWS that allows 3 concurrent connections. Just enough to connect 2 mobile devices and the Raspberry Pi.

## The Software 

Receiving the MQTT information and sending it to a small Python program that manages the motors is really simple with a node-red flow https://nodered.org/   I created two separated flows for the 2 pointers.

![](/assets/img/node-red.png)