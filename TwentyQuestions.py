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
    vol.setVolume(0.9)
    
    # writing topics' qichat code as text strings (end-of-line characters are important!)
    topic_content_1 = ('topic: ~greetings()\n'
                   'language: enu\n'
                   'concept:(greetings) ["Good Morning" "Good Afternoon" "Good Evening" Hello Hi Hey "Whats up" ]\n'
                   'concept:(names) [Nathan Megan Christina]\n'
                   
                    'u:(~greetings) Hello human what is your name\n'
                    'u:(my name is _~names) nice to meet you $1 $name=$1 ^gotoReactivate(games)\n'
                    '''u:(what is my name) ^first["your name is $name" "I dont know"]\n
                        u1:(no) Ok ^clear(name) \n'''
                    'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) O Hello!\n'                
                   
                    '''proposal: %games Would you like to play a game with me?
                     u1:(yes) Great! We can play, Simon says, story time, or 20 Questions\n
                         u2:(20 Questions) OK ^gotoReactivate(start) \n
                     u1:(no) Aww too bad \n'''
                     
                     '''proposal: %start Lets play, ok think of an animal and I will ask questions to try and see if I can guess. Do you have an animal in mind?\n
                         u1:(Yes) ^gotoReactivate(Mammal)
                         u1:(No) Alright I'll give you more time to think \n'''
                         
                     '''u:(Guess what animal) %Mammal Hmm ok let me see. Are you thinking of a mammal?\n
                             u1:(yes) Is it big or small?
                                 u2:(big) Does it eat meat?
                                    u3:(no) Does it live in Africa?
                                        u4:(no) Does it have a trunk?
                                            u5:(yes) Are you thinking of an elephant?
                                                u6: (yes) Great that was fun, do you want to play again?
                                                    u7:(yes) ^gotoReactivate(start)
                                                    u7:(no) Ok maybe we can do something else.
                                u2:(small) Does it eat meat?
                                    u3:(no) Does it swim?
                                        u4:(yes) Does it lay eggs?
                                            u5:(yes) Are you thinking of a playtapus?
                                                u6:(yes) Great that was fun, do you want to play again?
                                                    u7:(yes) ^gotoReactivate(start)
                                                    u7:(no) Ok maybe we can do something else. \n'''
#                                            u5:(no) Does it have a flat tail?
#                                                u6:(yes) Are you thinking of a beaver?
#                                                    u7:(yes) Great that was fun, do you want to play again?
#                                                        u8:(yes) ^gotoReactivate(start)
#                                                        u8:(no) Ok maybe we can do something else.\n'''
                    )
    
    
#    topic_content_2 = ('topic: ~Play20Questions()\n'
#                       'language: enu\n'
                        
#                        '''u:({Nao} Guess the animal) Hmm ok let me see. Are you thinking of a mammal?\n''')
#                                 u1:(yes) Is it big or small?
#                                     u2:(big) Does it eat meat?
#                                        u3:(no) Does it swim?
#                                            u4: (no) Does it have a trunk?
#                                                u5: (yes) Are you thinking of an elephant?
#                                                    u6: (yes) Great that was fun, do you want to play again?
#                                                        u7:(yes) ^gotoReactivate(start)
#                                                        u7:(no) Ok maybe we can do something else.
#                                    u2:(small) Does it eat meat?
#                                        u3:(no) Does it swim?
#                                            u4:(yes) Does it lay eggs?
#                                                u5:(yes) Are you thinking of a playtapus?
#                                                    u6:(yes) Great that was fun, do you want to play again?
#                                                        u7:(yes) ^gotoReactivate(start)
#                                                        u7:(no) Ok maybe we can do something else.
#                                                u5:(no) Does it have a flat tail?
#                                                    u6:(yes) Are you thinking of a beaver?
#                                                        u7:(yes) Great that was fun, do you want to play again?
#                                                            u8:(yes) ^gotoReactivate(start)
#                                                            u8:(no) Ok maybe we can do something else.
#                                u1:(no) Is it a bird?
#                                    u2:(yes) Does it fly?
#                                        u3:(no) Can it swim?
#                                            u4:(no) Is it big or small?
#                                                u5:(big) Are you thinking of an ostrich?
#                                                    u6:(yes) Great that was fun, do you want to play again?
#                                                        u7:(yes) ^gotoReactivate(start)
#                                                        u7:(no) Ok maybe we can do something else.'''
#                                )

 # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content_1)
#    topic_name_2 = ALDialog.loadTopicContent(topic_content_2)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)
#    ALDialog.activateTopic(topic_name_2)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('20Questions')

    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
    
        ALDialog.unsubscribe('20Questions')

        # Deactivating all topics
        ALDialog.deactivateTopic(topic_name_1)
#        ALDialog.deactivateTopic(topic_name_2)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(topic_name_1)
#        ALDialog.unloadTopic(topic_name_2)


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
                
