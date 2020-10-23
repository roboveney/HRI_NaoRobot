s#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
import qi
import argparse
import sys

def gameConvo(session):
    # Getting the service ALDialog
    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")

    # writing topics' qichat code as text strings (end-of-line characters are important!)
    topic_content_1 = ('topic: ~greetings()\n'
                       'language: enu\n'
                       'concept:(greetings) ["Good Morning" "Good Afternoon" "Good Evening" Hello Hi Hey "Whats up" ]\n'
                       'concept:(names) [Nathan Megan Christina]\n'
                       
                       'u: (~greetings) Hello human what is your name\n'
                       'u:(my name is _~names) nice to meet you $1 $name=$1 ^nextProposal\n'
                       '''u:(what is my name) ^first["your name is $name" "I dont know"]\n
                           u1:(no) Ok ^clear(name)'''
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) O Hello!\n'
                       
                       
                       '''proposal: Would you like to play a game with me?
                        u1:(yes) Great! ^topicTag(games_topic,listgames)
                        u1:(no) Aww too bad''')

    topic_content_2 = ('topic: ~games_topic()\n'
                       'language: enu\n'
                       'concept:(games) We can play ["Simon says" "story time" "chess"]\n'
                       'proposal: %listgames ^enumerate(~games)\n'
                       'u:(What is your favorite game) I like story time\n')

    # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content_1)
    topic_name_2 = ALDialog.loadTopicContent(topic_content_2)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)
    ALDialog.activateTopic(topic_name_2)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('games_dialog')

    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
    
        ALDialog.unsubscribe('games_dialog')

        # Deactivating all topics
        ALDialog.deactivateTopic(topic_name_1)
        ALDialog.deactivateTopic(topic_name_2)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(topic_name_1)
        ALDialog.unloadTopic(topic_name_2)


#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
#    parser.add_argument("--port", type=int, default=9559,
#                        help="port number, the default value is OK in most cases")
#
#    args = parser.parse_args()
#    session = qi.Session()
#    try:
#        session.connect("tcp://{}:{}".format(args.ip, args.port))
#    except RuntimeError:
#        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
#               " Run with -h option for help.\n".format(args.ip, args.port))
#        sys.exit(1)
#    main(session)
