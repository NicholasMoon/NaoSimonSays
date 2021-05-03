import sys
import time
from PIL import Image
from naoqi import ALProxy
import random



def getNaoImage(IP, PORT):
#  First get an image from Nao, then show it on the screen with PIL.


  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  resolution = 2    # VGA
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  naoImage = camProxy.getImageRemote(videoClient)
  print('naoImage taken')
  t1 = time.time()

  # Time the image transfer.
  print "acquisition delay ", t1 - t0

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  #print("array = ",array)

  # Create a PIL Image from our pixel array.
  im = Image.frombytes("RGB", (imageWidth, imageHeight), array) #fromstring("RGB", (imageWidth, imageHeight), array)

  # Save the image.
  im.save("input.png", "PNG")


def Simon_Says(IP, PORT):

    session = open("session.txt", "a")
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    num_poses = 3

    say_simon = random.randint( 0, 1 )
    if (say_simon):
        tts.say("Simon says")
        
    pose = random.randint( 0, num_poses - 1)
    if (pose == 0):
        tts.say("Raise your right hand")
        if (say_simon):
            session.write("\nR")
        else:
            session.write("\nD")
            
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.96])
        keys.append([-0.169378])

        names.append("HeadYaw")
        times.append([1.96])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.96])
        keys.append([0.0845001])

        names.append("LAnkleRoll")
        times.append([1.96])
        keys.append([-0.105746])

        names.append("LElbowRoll")
        times.append([1.96])
        keys.append([-0.417841])

        names.append("LElbowYaw")
        times.append([1.96])
        keys.append([-1.19997])

        names.append("LHand")
        times.append([1.96])
        keys.append([0.291937])

        names.append("LHipPitch")
        times.append([1.96])
        keys.append([0.126938])

        names.append("LHipRoll")
        times.append([1.96])
        keys.append([0.11865])

        names.append("LHipYawPitch")
        times.append([1.96])
        keys.append([-0.176982])

        names.append("LKneePitch")
        times.append([1.96])
        keys.append([-0.0872551])

        names.append("LShoulderPitch")
        times.append([1.96])
        keys.append([1.43955])

        names.append("LShoulderRoll")
        times.append([1.96])
        keys.append([0.223222])

        names.append("LWristYaw")
        times.append([1.96])
        keys.append([0.105193])

        names.append("RAnklePitch")
        times.append([1.96])
        keys.append([0.0844999])

        names.append("RAnkleRoll")
        times.append([1.96])
        keys.append([0.105742])

        names.append("RElbowRoll")
        times.append([1.96])
        keys.append([0.403045])

        names.append("RElbowYaw")
        times.append([1.96])
        keys.append([1.18997])

        names.append("RHand")
        times.append([1.96])
        keys.append([0.291937])

        names.append("RHipPitch")
        times.append([1.96])
        keys.append([0.126938])

        names.append("RHipRoll")
        times.append([1.96])
        keys.append([-0.118644])

        names.append("RHipYawPitch")
        times.append([1.96])
        keys.append([-0.176982])

        names.append("RKneePitch")
        times.append([1.96])
        keys.append([-0.0872551])

        names.append("RShoulderPitch")
        times.append([0.1, 1.96])
        keys.append([1.44339, -0.905857])

        names.append("RShoulderRoll")
        times.append([1.96])
        keys.append([-0.186345])

        names.append("RWristYaw")
        times.append([1.96])
        keys.append([0.0905791])

        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          motion = ALProxy("ALMotion", IP, PORT)
          #motion = ALProxy("ALMotion")
          motion.angleInterpolation(names, keys, times, True)
        except BaseException, err:
          print err

    elif (pose == 1):
        tts.say("Raise your left hand")
        if (say_simon):
            session.write("\nL")
        else:
            session.write("\nD")
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.1, 1.96])
        keys.append([-0.161711, -0.161711])

        names.append("HeadYaw")
        times.append([0.1, 1.96])
        keys.append([0, 0])

        names.append("LAnklePitch")
        times.append([0.1, 1.96])
        keys.append([0.0786058, 0.0786058])

        names.append("LAnkleRoll")
        times.append([0.1, 1.96])
        keys.append([-0.107048, -0.107048])

        names.append("LElbowRoll")
        times.append([0.1, 1.96])
        keys.append([-0.422097, -0.410763])

        names.append("LElbowYaw")
        times.append([0.1, 1.96])
        keys.append([-1.20471, -1.20471])

        names.append("LHand")
        times.append([0.1, 1.96])
        keys.append([0.298925, 0.298925])

        names.append("LHipPitch")
        times.append([0.1, 1.96])
        keys.append([0.126938, 0.126938])

        names.append("LHipRoll")
        times.append([0.1, 1.96])
        keys.append([0.117724, 0.117724])

        names.append("LHipYawPitch")
        times.append([0.1, 1.96])
        keys.append([-0.179657, -0.179657])

        names.append("LKneePitch")
        times.append([0.1, 1.96])
        keys.append([-0.0910475, -0.0910475])

        names.append("LShoulderPitch")
        times.append([0.1, 1.96])
        keys.append([1.53387, -0.585729])

        names.append("LShoulderRoll")
        times.append([0.1, 1.96])
        keys.append([0.260202, 0.226437])

        names.append("LWristYaw")
        times.append([0.1, 1.96])
        keys.append([0.100201, 0.100201])

        names.append("RAnklePitch")
        times.append([0.1, 1.96])
        keys.append([0.0786058, 0.0786058])

        names.append("RAnkleRoll")
        times.append([0.1, 1.96])
        keys.append([0.107044, 0.107044])

        names.append("RElbowRoll")
        times.append([0.1, 1.96])
        keys.append([0.413868, 0.413868])

        names.append("RElbowYaw")
        times.append([0.1, 1.96])
        keys.append([1.19819, 1.19819])

        names.append("RHand")
        times.append([0.1, 1.96])
        keys.append([0.294017, 0.294017])

        names.append("RHipPitch")
        times.append([0.1, 1.96])
        keys.append([0.126938, 0.126938])

        names.append("RHipRoll")
        times.append([0.1, 1.96])
        keys.append([-0.117718, -0.117718])

        names.append("RHipYawPitch")
        times.append([0.1, 1.96])
        keys.append([-0.179657, -0.179657])

        names.append("RKneePitch")
        times.append([0.1, 1.96])
        keys.append([-0.0910475, -0.0910475])

        names.append("RShoulderPitch")
        times.append([0.1, 1.96])
        keys.append([1.40732, 1.40732])

        names.append("RShoulderRoll")
        times.append([0.1, 1.96])
        keys.append([-0.213162, -0.213162])

        names.append("RWristYaw")
        times.append([0.1, 1.96])
        keys.append([0.0925941, 0.0925941])

        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          motion = ALProxy("ALMotion", IP, PORT)
          #motion = ALProxy("ALMotion")
          motion.angleInterpolation(names, keys, times, True)
        except BaseException, err:
          print err

    elif (pose == 2):
        tts.say("Raise your both your hands")
        if (say_simon):
            session.write("\nB")
        else:
            session.write("\nD")
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.1, 1.96])
        keys.append([-0.161711, -0.161711])

        names.append("HeadYaw")
        times.append([0.1, 1.96])
        keys.append([0, 0])

        names.append("LAnklePitch")
        times.append([0.1, 1.96])
        keys.append([0.0786058, 0.0786058])

        names.append("LAnkleRoll")
        times.append([0.1, 1.96])
        keys.append([-0.107048, -0.107048])

        names.append("LElbowRoll")
        times.append([0.1, 1.96])
        keys.append([-0.422098, -0.410345])

        names.append("LElbowYaw")
        times.append([0.1, 1.96])
        keys.append([-1.20471, -1.20471])

        names.append("LHand")
        times.append([0.1, 1.96])
        keys.append([0.298925, 0.298925])

        names.append("LHipPitch")
        times.append([0.1, 1.96])
        keys.append([0.126938, 0.126938])

        names.append("LHipRoll")
        times.append([0.1, 1.96])
        keys.append([0.117724, 0.117724])

        names.append("LHipYawPitch")
        times.append([0.1, 1.96])
        keys.append([-0.179657, -0.179657])

        names.append("LKneePitch")
        times.append([0.1, 1.96])
        keys.append([-0.0910475, -0.0910475])

        names.append("LShoulderPitch")
        times.append([0.1, 1.96])
        keys.append([1.42558, -0.60565])

        names.append("LShoulderRoll")
        times.append([0.1, 1.96])
        keys.append([0.249758, 0.224686])

        names.append("LWristYaw")
        times.append([0.1, 1.96])
        keys.append([0.100201, 0.100201])

        names.append("RAnklePitch")
        times.append([0.1, 1.96])
        keys.append([0.0786057, 0.0786057])

        names.append("RAnkleRoll")
        times.append([0.1, 1.96])
        keys.append([0.107044, 0.107044])

        names.append("RElbowRoll")
        times.append([0.1, 1.96])
        keys.append([0.414976, 0.401152])

        names.append("RElbowYaw")
        times.append([0.1, 1.96])
        keys.append([1.19865, 1.18804])

        names.append("RHand")
        times.append([0.1, 1.96])
        keys.append([0.294017, 0.294017])

        names.append("RHipPitch")
        times.append([0.1, 1.96])
        keys.append([0.126938, 0.126938])

        names.append("RHipRoll")
        times.append([0.1, 1.96])
        keys.append([-0.117718, -0.117718])

        names.append("RHipYawPitch")
        times.append([0.1, 1.96])
        keys.append([-0.179657, -0.179657])

        names.append("RKneePitch")
        times.append([0.1, 1.96])
        keys.append([-0.0910475, -0.0910475])

        names.append("RShoulderPitch")
        times.append([0.1, 1.96])
        keys.append([1.40732, -0.59593])

        names.append("RShoulderRoll")
        times.append([0.1, 1.96])
        keys.append([-0.216628, -0.189636])

        names.append("RWristYaw")
        times.append([0.1, 1.96])
        keys.append([0.0925942, 0.0925942])

        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          motion = ALProxy("ALMotion", IP, PORT)
          # motion = ALProxy("ALMotion")
          motion.angleInterpolation(names, keys, times, True)
        except BaseException, err:
          print err
          
    session.close()
    time.sleep(3)
    getNaoImage(IP,PORT)
    # run pose recognition


if __name__ == '__main__':
  IP = "192.168.86.237"  # Replace here with your NaoQi's IP address.
  PORT = 9559

  # Read IP address from first argument if any.
  if len(sys.argv) > 1:
    IP = sys.argv[1]
    
  Simon_Says(IP,PORT)
