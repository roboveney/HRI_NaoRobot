#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import qi
import argparse
import sys

def main(session):
    # Getting the service ALDialog
    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")
    vol = session.service("ALTextToSpeech")
    vol.setVolume(0.6)
    
    # writing topics' qichat code as text strings (end-of-line characters are important!)
    topic_content_1 = ('topic: ~Begin()\n'
                       'language: enu\n'
                       'concept:(stories)["Little Red Riding Hood" "King Arthur" "or Flash Gordon"]\n'
                       
                       'u:(Test Function) ^topicTagReactivate(Hood, info)\n'
                       
                       'u: ({Nao} Tell me a story) Ok I know several stories ^gotoReactivate(Choices)\n'

                       '''proposal: %Choices Would you like to hear about ^enumerate(~stories)\n
                        u1:(Hood) Great! ^topicTagReactivate(Hood,who)
                        u1:(Arthur) Awesome
                        u1:(Gordon) Cool'''
                        
                        '''proposal: %Another Would you like to hear another story?
                       u1:(yes) Ok ^gotoReactivate(Choices)
                       u1:(no) OK, have a good day'''
                        )

    topic_content_2 = ('topic: ~Hood()\n'
                       'language: enu\n'
                       'concept:(names) [Megan Christina]\n'
                       
                       'u:(Nao Restart) Ok lets start over ^gotoReactivate(Begin,Choices)\n'
                       
                       '''proposal: %who Would you like to be the main character in the story?\n
                       u1:(yes) ^gotoReactivate(info)
                       u1:(no) Ok then, are you sitting comfortable good, then we will begin.^gotoReactivate(start)'''
                       
                       '''proposal: %info What name would you like me to call you in the story?\n
                       u:({My name is} _~names) Ok $1 $Name=$1 ^goto(start)'''
                       
                       '''proposal: %start Little Red Riding Hood is going to deliver supplies to her grandmother in the woods. She notices some pretty flowers and fruits. Does she rest to smell the flowers and have a snack, or continue along the path?\n
                       u1:(Rest) Ok she decides to rest ^gotoReactivate(startRest)
                       u1:(Continue) ^gotoReactivate(startContinue)'''
                       
                       #1
                       '''proposal: %startRest As she takes a rest, a wolf appears. Does she talk with the wolf or run away?\n
                       u1:(Talk) ^gotoReactivate(restTalk)
                       u1:(Run) ^gotoReactivate(restRun)'''
                       
                       #2
                       '''proposal: %startContinue She continues along the path to ["his $Pronoun==He" "her $Pronoun==She" "their $Pronoun==They"] grandma's house. Grandma is baking cookies! Does $Pronoun stay to help her bake, 
                       or does $Pronoun head back home after delivering the supplies?\n
                       u1:(Stay) ^gotoReactivate(continueStay)
                       u1:(Leave) ^gotoReactivate(continueLeave)'''
                       
                       #1-1
                       '''proposal: %restTalk She decides to talk to the wolf who says he's on his way to visit an old lady. Does she go with the wolf or go by herself?\n
                       u1:(Wolf) ^gotoReactivate(talkWolf)
                       u1:(Alone) ^gotoReactivate(talkAlone)'''
                       
                       #1-2
                       '''proposal: %restRun Little Red Riding Hood tries to continue to Grandma's house, but she doesnt remember which way to go! Does she go down the
                       path to the left or the right?\n
                       u1:(left) ^gotoReactivate(runLeft)
                       u1:(right) ^gotoReactivate(runRight)'''
                       
                       #1-1-1
                       '''proposal: %talkWolf She goes with the wolf to the old lady's house. The house turns out to be her grandma's! It also turns out that the wolf, who introduces 
                       himself as Mr. Lupin, is the local milk man! He deliver's grandma's milk and grandma invites both of them in for milk and cookies. The end. Did you enjoy the story?\n
                       u1:(yes) I'm glad! You helped make it an interesting story ^topicTagReactivate(Begin, Another)
                       u1:(no) I'm sorry ^topicTagReactivate(Begin, Another)'''
                       
                       #1-2-2
                       '''proposal: %runRight She goes down the right path and ends up by a beautiful lake! The water is blue, the sun is warm and she is feeling a little hungry from all
                       the walking. She decides to have a delicious snack under a tree by the lake and take a nap. Little Red Riding Hood had a great day but unfortunately her Grandma never got the supplies that she
                       needed, oh no! ...The end, Did you enjoy the story?\n
                       u1:(yes) I'm glad you helped make it an interesting story
                       u1:(no) I'm sorry ^topicTagReactivate(storySetup, Another)'''
                       )
        # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content_1)
    topic_name_2 = ALDialog.loadTopicContent(topic_content_2)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)
    ALDialog.activateTopic(topic_name_2)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('Story_Time')

    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
    
        ALDialog.unsubscribe('Story_Time')

        # Deactivating all topics
        ALDialog.deactivateTopic(topic_name_1)
        ALDialog.deactivateTopic(topic_name_2)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(topic_name_1)
        ALDialog.unloadTopic(topic_name_2)


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