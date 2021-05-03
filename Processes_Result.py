import sys
import time
from PIL import Image
from naoqi import ALProxy
import random

def Processes_Result(IP, PORT):
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    o = open("output.txt", "r")
    lineList = o.readlines()
    o.close()
    correct_pose = lineList[-1]

    
    

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.96])
    keys.append([-0.161711])

    names.append("HeadYaw")
    times.append([1.96])
    keys.append([0])

    names.append("LAnklePitch")
    times.append([1.96])
    keys.append([0.0786058])

    names.append("LAnkleRoll")
    times.append([1.96])
    keys.append([-0.107048])

    names.append("LElbowRoll")
    times.append([1.96])
    keys.append([-0.411273])

    names.append("LElbowYaw")
    times.append([1.96])
    keys.append([-1.21504])

    names.append("LHand")
    times.append([1.96])
    keys.append([0.298925])

    names.append("LHipPitch")
    times.append([1.96])
    keys.append([0.126938])

    names.append("LHipRoll")
    times.append([1.96])
    keys.append([0.117724])

    names.append("LHipYawPitch")
    times.append([1.96])
    keys.append([-0.179657])

    names.append("LKneePitch")
    times.append([1.96])
    keys.append([-0.0910475])

    names.append("LShoulderPitch")
    times.append([1.96])
    keys.append([1.71496])

    names.append("LShoulderRoll")
    times.append([1.96])
    keys.append([0.290432])

    names.append("LWristYaw")
    times.append([1.96])
    keys.append([0.100201])

    names.append("RAnklePitch")
    times.append([1.96])
    keys.append([0.0786057])

    names.append("RAnkleRoll")
    times.append([1.96])
    keys.append([0.107044])

    names.append("RElbowRoll")
    times.append([1.96])
    keys.append([0.401101])

    names.append("RElbowYaw")
    times.append([1.96])
    keys.append([1.20957])

    names.append("RHand")
    times.append([1.96])
    keys.append([0.294017])

    names.append("RHipPitch")
    times.append([1.96])
    keys.append([0.126938])

    names.append("RHipRoll")
    times.append([1.96])
    keys.append([-0.117718])

    names.append("RHipYawPitch")
    times.append([1.96])
    keys.append([-0.179657])

    names.append("RKneePitch")
    times.append([1.96])
    keys.append([-0.0910475])

    names.append("RShoulderPitch")
    times.append([1.96])
    keys.append([1.5242])

    names.append("RShoulderRoll")
    times.append([1.96])
    keys.append([-0.250043])

    names.append("RWristYaw")
    times.append([1.96])
    keys.append([0.0925942])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", IP, PORT)
      #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

    if (correct_pose == "Y"):
        tts.say("Correct!")
    else:
        tts.say("Sorry, that was incorrect!")
    
    o.close()
	
if __name__ == '__main__':
  IP = "192.168.86.237"  # Replace here with your NaoQi's IP address.
  PORT = 9559

  # Read IP address from first argument if any.
  if len(sys.argv) > 1:
    IP = sys.argv[1]
    
  Processes_Result(IP,PORT)