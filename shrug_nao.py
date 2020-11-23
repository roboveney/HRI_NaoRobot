#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: PoseInit - Small example to make Nao go to an initial position."""

import qi
import argparse
import sys

# Choregraphe bezier export in Python.
names1 = list()
times1 = list()
keys1 = list()

names1.append("HeadPitch")
times1.append([1.92, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.162646, -0.162646, -0.162646, -0.162646, -0.162646, -0.144238, -0.144238, -0.144238])

names1.append("HeadYaw")
times1.append([1.92, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.01845, -0.354396, 0.216252, 0.478566, 0.0674542, 0.05825, 0.05825, -0.227074])

names1.append("LAnklePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.093532, 0.091998, 0.091998, 0.091998, 0.091998, 0.091998, 0.091998, 0.0827939])

names1.append("LAnkleRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.121144, -0.122678, -0.122678, -0.122678, -0.122678, -0.121144, -0.121144, -0.12728])

names1.append("LElbowRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.605888, -0.62583, -0.62583, -0.62583, -1.02314, -1.00013, -1.00013, -0.975581])

names1.append("LElbowYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-1.38524, -0.955723, -1.38524, -1.91601, -0.584497, -0.633584, -0.633584, -0.627448])

names1.append("LHand")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.2884, 0.2884, 0.2884, 0.2884, 0.2884, 0.294, 0.294, 0.294])

names1.append("LHipPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.130432, 0.130432, 0.130432, 0.130432, 0.130432, 0.12583, 0.12583, 0.128898])

names1.append("LHipRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0966839, 0.0966839, 0.0966839, 0.0966839, 0.0966839, 0.0951499, 0.0951499, 0.099752])

names1.append("LHipYawPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.1733, -0.1733, -0.170232])

names1.append("LKneePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.092082, -0.092082, -0.092082, -0.092082, -0.092082, -0.0923279, -0.0923279, -0.0859461])

names1.append("LShoulderPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.638103, 0.539926, 0.51845, 0.532256, 0.326699, 0.414139, 0.414139, 0.481634])

names1.append("LShoulderRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.151824, -0.07214, 0.381923, 0.777696, 0.306757, 0.263807, 0.263807, 0.254602])

names1.append("LWristYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0981341, -0.368202, -0.329852, -0.273093, -1.09072, -1.00941, -1.00941, -1.00328])

names1.append("RAnklePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0951499, 0.090548, 0.090548, 0.090548, 0.0890141, 0.092082, 0.092082, 0.0874801])

names1.append("RAnkleRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.130432, 0.128898, 0.128898, 0.128898, 0.128898, 0.121228, 0.121228, 0.128898])

names1.append("RElbowRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.618244, 0.595234, 0.779314, 0.817664, 0.817664, 0.794654, 0.794654, 0.774711])

names1.append("RElbowYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([1.26551, 1.42351, 1.43425, 0.951039, 0.613558, 0.845191, 0.845191, 0.83292])

names1.append("RHand")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.2904, 0.2904, 0.2904, 0.2904, 0.2904, 0.2876, 0.2876, 0.2876])

names1.append("RHipPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.121144, 0.122678, 0.122678, 0.122678, 0.122678, 0.121144, 0.121144, 0.11961])

names1.append("RHipRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.091998, -0.091998, -0.091998, -0.091998, -0.091998, -0.101202, -0.101202, -0.107338])

names1.append("RHipYawPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.1733, -0.1733, -0.170232])

names1.append("RKneePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0923279, -0.0923279, -0.0904641])

names1.append("RShoulderPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.558418, 0.570689, 0.552281, 0.426494, 0.346725, 0.423426, 0.423426, 0.461776])

names1.append("RShoulderRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.151908, -0.481718, 0.0812599, 0.263807, 0.0904641, -0.39428, -0.39428, -0.38661])

names1.append("RWristYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0889301, 0.151824, 0.0889301, 0.593616, 0.895815, 0.851328, 0.851328, 0.842125])


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
    motion_service.angleInterpolationBezier(names1, times1, keys1)

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


