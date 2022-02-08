---
layout: default
---

# Weasley Clock
The Weasleys Family Clock s a magical clock from the Harry Potter books owned by the Weasleys family which individually monitored each of their whereabouts. Located in the living room at The Burrow, the clock had nine golden hands, one for every member of the household. My version has just the 2 original pointers.

![](/assets/img/UhrFront.jpg)
## Basic Ideas

The main ideas came from this [blog](https://www.instructables.com/Build-Your-Own-Weasley-Location-Clock/) by [ppeters0502](https://www.instructables.com/member/ppeters0502/).

## The clock

I took an old mechanical wooden clock that I found on Ebay because I wanted to reuse as many parts as possible from the old mechanics and the original pointers. But combining the old gears with modern ones and the motors was kind of tricky in the end as is still not working perfectly.

![](/assets/img/Antrieb2.jpg)
## The motors

I wanted to reuse an old Raspberry Pi type B and decided to use stepper motors instead of servo motors. Main reason was that the Joy-It motors coming together with the board were a perfect fit: [Joy-IT RB-Motors](https://joy-it.net/de/products/RB-Moto2). To drive the old mechanical clock gears with the motor I used belts and gears that were made for 3D Printers.

![](/assets/img/Antrieb3.jpg)
## The mobile app

The [Owntracks App](https://owntracks.org/) is perfect to send MQTT protocol based location information to the raspberry pi.

## The MQTT Server

I did not manage to install a local MQTT server on my Raspberry Pi. Unfortunately it became quite hard to find a free MQTT server on the internet. What worked for me is the offering from [HiveMQ](https://www.hivemq.com/) offering a free MQTT server hosted on AWS that allows 3 concurrent connections. Just enough to connect 2 mobile devices and the Raspberry Pi in the clock.

## The Software 

Receiving the MQTT information and sending it to a small Python program that manages the motors is really simple with a node-red flow https://nodered.org/.   I created two separated flows for the 2 pointers. The nodes are mainly configured the same way as described by [ppeters0502](https://www.instructables.com/Build-Your-Own-Weasley-Location-Clock/). I just added some debug nodes and took the "location" only from events of _type "transition" and not from _type "location" to get them only once.  See the Owntracks [manual](https://owntracks.org/booklet/tech/json/)

![](/assets/img/node-red.png)

The python code can be found [here](/Uhr.py).