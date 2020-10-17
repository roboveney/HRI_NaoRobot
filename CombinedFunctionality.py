#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
import qi
import argparse
import sys
import time
import greetAndGameChoice.py as Convo

def main(session):
    # Establish services to be used
    posture_service = session.service("ALRobotPosture")
    motion_service = session.service("ALMotion")
    tracker_service = session.service("ALTracker")
    asr_service = session.service("ALSpeechRecognition")
    asr_service.setLanguage("English")
    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")





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
