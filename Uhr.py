import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 24 # pink
coil_A_2_pin = 4 # orange
coil_B_1_pin = 23 # blau
coil_B_2_pin = 25 # gelb
coil2_A_1_pin = 18 # pink
coil2_A_2_pin = 22 # orange
coil2_B_1_pin = 17 # blau
coil2_B_2_pin = 27 # gelb

StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

GPIO.setup(coil2_A_1_pin, GPIO.OUT)
GPIO.setup(coil2_A_2_pin, GPIO.OUT)
GPIO.setup(coil2_B_1_pin, GPIO.OUT)
GPIO.setup(coil2_B_2_pin, GPIO.OUT)

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def setStepHour(w1, w2, w3, w4):
   GPIO.output(coil2_A_1_pin, w1)
   GPIO.output(coil2_A_2_pin, w2)
   GPIO.output(coil2_B_1_pin, w3)
   GPIO.output(coil2_B_2_pin, w4)

def setStepMinute(w1, w2, w3, w4):
   GPIO.output(coil_A_1_pin, w1)
   GPIO.output(coil_A_2_pin, w2)
   GPIO.output(coil_B_1_pin, w3)
   GPIO.output(coil_B_2_pin, w4)

def forwardMinute(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStepMinute(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def forwardHour(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStepHour(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def backwardsMinute(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStepMinute(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def backwardsHour(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStepHour(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

 # This opens the previous location file and reads each line into the list, then closes it
try:
  file=open('pointerpos.txt','r')
#  print("Sucess open file!")
  list = file.readlines()
  file.close()
#  print("File: %s" % list)
  CurrentPositionHourMotor = int(list[0])
  CurrentPositionMinuteMotor = int(list[1])
except:
   CurrentPositionHourMotor = 0
   CurrentPositionMinuteMotor = 0

print("CurrentHour: %s" % CurrentPositionHourMotor)
print("CurrentMinute: %s" % CurrentPositionMinuteMotor)

person = sys.argv[1]
location = sys.argv[2]
print("Person: %s" % person)
print("Location: %s" % location)

#12 locations  on the clock face
location_list = ['home','school','travel','orchester','sohani','yoga','flamenco','erlenbach','kochendorf','music','town','baseball']

try:
  loc_index = location_list.index(location)
#  print("Location Index: %s" % loc_index)
except:
  loc_index = 0
  print("Default Location Index: %s" % loc_index)

if (person == '1'):
  # Calculate the difference to the next position Hour (Jakob)
  TargetPositionHourMotor = loc_index
  if loc_index == 0:
    deltaHourMotor = CurrentPositionHourMotor
    delay = 10 
    steps = 34 * deltaHourMotor
    backwardsHour(int(delay) / 1000.0, int(steps))  
    print("Person 1 is back home")
    # No change for minute pointer
    TargetPositionMinuteMotor  = CurrentPositionMinuteMotor   
  else:
    if TargetPositionHourMotor >= CurrentPositionHourMotor:
      deltaHourMotor = TargetPositionHourMotor - CurrentPositionHourMotor
    elif TargetPositionHourMotor < CurrentPositionHourMotor:
       deltaHourMotor = 12 - CurrentPositionHourMotor + TargetPositionHourMotor
    delay = 10
    if deltaHourMotor <= 6:
      # Hour pointer move forward 
      steps = 34 * deltaHourMotor
      forwardHour(int(delay) / 1000.0, int(steps))
    elif deltaHourMotor > 6:
      # Hour pointer move backward 
      steps = 34*(12-deltaHourMotor)
      backwardsHour(int(delay) / 1000.0, int(steps))   
    print("Person 1 moved to: %s" % TargetPositionHourMotor)  
    # No change for minute pointer
    TargetPositionMinuteMotor  = CurrentPositionMinuteMotor       
else:
  # Calculate the difference to the next position Minute
  TargetPositionMinuteMotor = loc_index
  if loc_index == 0:
    deltaMinuteMotor = CurrentPositionMinuteMotor
    delay = 10 
    steps = 40 * deltaMinuteMotor
    backwardsMinute(int(delay) / 1000.0, int(steps))  
    print("Person 0 is back home")
    # No change for hourpointer
    TargetPositionHourMotor  = CurrentPositionHourMotor   
  else:
    if TargetPositionMinuteMotor >= CurrentPositionMinuteMotor:
      deltaMinuteMotor = TargetPositionMinuteMotor - CurrentPositionMinuteMotor
    elif TargetPositionMinuteMotor < CurrentPositionMinuteMotor:
      deltaMinuteMotor = 12 - CurrentPositionMinuteMotor + TargetPositionMinuteMotor      
    delay = 10
    if deltaMinuteMotor <= 6:
      # Minute pointer move forward  
      steps = 40 * deltaMinuteMotor 
      forwardMinute(int(delay) / 1000.0, int(steps)) 
    elif deltaMinuteMotor > 6:  
      # Minute pointer move backward
      steps = 40*(12-deltaMinuteMotor)
      backwardsMinute(int(delay) / 1000.0, int(steps))       
    print("Person 0 moved to: %s" % TargetPositionMinuteMotor)
    # No change for hour pointer
    TargetPositionHourMotor  = CurrentPositionHourMotor

try:
  file=open('pointerpos.txt','w')
  file.write(str(TargetPositionHourMotor))
  file.write('\n')
  file.write(str(TargetPositionMinuteMotor))
  file.close()
except:
  print("Write to file failed!")