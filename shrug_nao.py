#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: PoseInit - Small example to make Nao go to an initial position."""

import qi
import argparse
import sys


def main(session):
    """
    PoseInit: Small example to make Nao go to an initial position.
    """
    # Get the services ALMotion & ALRobotPosture.

    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand Init
    posture_service.goToPosture("StandInit", 0.5)

    # Go to rest position
    motion_service.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)

# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.345108, [3, -0.433333, 0], [3, 0.216667, 0]], [0.16563, [3, -0.216667, 0], [3, 0.183333, 0]], [0.16563, [3, -0.183333, 0], [3, 0.266667, 0]], [0.177902, [3, -0.266667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.0199001, [3, -0.433333, 0], [3, 0.216667, 0]], [0.0199001, [3, -0.216667, 0], [3, 0.183333, 0]], [0.0199001, [3, -0.183333, 0], [3, 0.266667, 0]], [0.0199001, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[-1.23023, [3, -0.433333, 0], [3, 0.216667, 0]], [-1.19034, [3, -0.216667, 0], [3, 0.183333, 0]], [-1.50481, [3, -0.183333, 0], [3, 0.266667, 0]], [-1.11978, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[-0.94652, [3, -0.433333, 0], [3, 0.216667, 0]], [-1.55705, [3, -0.216667, 0.20568], [3, 0.183333, -0.174037]], [-2.08567, [3, -0.183333, 0.0141319], [3, 0.266667, -0.0205555]], [-2.10622, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.024, [3, -0.433333, 0], [3, 0.216667, 0]], [0.024, [3, -0.216667, 0], [3, 0.183333, 0]], [0.024, [3, -0.183333, 0], [3, 0.266667, 0]], [0.7268, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.929562, [3, -0.433333, 0], [3, 0.216667, 0]], [0.837522, [3, -0.216667, 0], [3, 0.183333, 0]], [0.943368, [3, -0.183333, 0], [3, 0.266667, 0]], [0.613558, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.107338, [3, -0.433333, 0], [3, 0.216667, 0]], [0.056716, [3, -0.216667, 0.0155104], [3, 0.183333, -0.0131242]], [0.0214341, [3, -0.183333, 0], [3, 0.266667, 0]], [0.292952, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[-0.119694, [3, -0.433333, 0], [3, 0.216667, 0]], [0.151824, [3, -0.216667, 0], [3, 0.183333, 0]], [-0.0844119, [3, -0.183333, 0.214779], [3, 0.266667, -0.312406]], [-1.42973, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[1.29474, [3, -0.433333, 0], [3, 0.216667, 0]], [1.38524, [3, -0.216667, -0.0196651], [3, 0.183333, 0.0166397]], [1.40365, [3, -0.183333, 0], [3, 0.266667, 0]], [0.967996, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[1.03541, [3, -0.433333, 0], [3, 0.216667, 0]], [1.0937, [3, -0.216667, -0.0582922], [3, 0.183333, 0.0493242]], [2.08567, [3, -0.183333, -0.011965], [3, 0.266667, 0.0174036]], [2.10307, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.0248001, [3, -0.433333, 0], [3, 0.216667, 0]], [0.0248001, [3, -0.216667, 0], [3, 0.183333, 0]], [0.0248001, [3, -0.183333, 0], [3, 0.266667, 0]], [0.6864, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[1.03396, [3, -0.433333, 0], [3, 0.216667, 0]], [0.92351, [3, -0.216667, 0.00906451], [3, 0.183333, -0.00766997]], [0.91584, [3, -0.183333, 0.00766997], [3, 0.266667, -0.0111563]], [0.627448, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[0.0398421, [3, -0.433333, 0], [3, 0.216667, 0]], [0.110406, [3, -0.216667, 0], [3, 0.183333, 0]], [0.030638, [3, -0.183333, 0.0289566], [3, 0.266667, -0.0421187]], [-0.10282, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1.25, 1.9, 2.45, 3.25])
keys.append([[-0.113558, [3, -0.433333, 0], [3, 0.216667, 0]], [-0.10282, [3, -0.216667, 0], [3, 0.183333, 0]], [-0.10282, [3, -0.183333, 0], [3, 0.266667, 0]], [1.13972, [3, -0.266667, 0], [3, 0, 0]]])

  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
motion = ALProxy("ALMotion", IP, 9559)
  # motion = ALProxy("ALMotion")
motion.angleInterpolationBezier(names, times, keys)

