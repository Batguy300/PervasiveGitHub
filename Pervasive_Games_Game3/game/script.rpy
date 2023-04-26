# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define greg = Character("Greg")
define unknown = Character("unknown")

image Store_front:
    "store_front.png"
    zoom 0.8

image Store_front_blurred:
    "store_front_blurred.png"
    zoom 0.8

image Greg:
    "greg.png"
    zoom 0.5



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Store_front

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    play music "audio/Paitently_Waiting.mp3"

    "Another boring day at work..."

    "I wonder who the next looney's gonna be to walk through the door..."

    "..."

    "HA! Not a customer in sight - finally I can catch a break from these degenerates... "

    $ renpy.music.set_pause(True, channel="music")

    unknown "...eughh....mhm..."

    $ renpy.music.set_pause(False, channel="music")

    "What the hell was that?"

    $ renpy.music.set_pause(True, channel="music")

    unknown "AWWW FUCK...ehhugh"


    $ renpy.music.set_pause(False, channel="music")

    "HEY...CAN I HELP YOU??!"

    scene Store_front_blurred

    show Greg
    with dissolve

    greg "...eughh....mhm.."

    $ renpy.music.set_pause(False, channel="music")

    "The man walks into the store, allowing the sea breeze and smoke to come in."
    "Once the door closes, the sea is gone but the smoke lingers."

    greg "I need a paper fork."

    "Do you want any food with that?"

    greg "No, no. I just need a paper fork. I have my own food"
    greg "It was supposed to be such a nice evening..."

    "He stares past you, unblinking. His hand slowly curls into a fist, shaking violently."

    menu:
        "We don't have paper forks" :
            jump plasticForks

        "Ask him to leave" :
            jump leave
        
        "Inquire about the smoke" :
            jump smoke

        "Coffee?" :
            jump coffee


    greg "I need a fork."

    "Do you want any food with that?"

    greg "No, no I just need a paper fork. I have my own food. It was supposed to be such a nice evening…” The man stares past you, unblinking. His eyes are red and bloodshot and his hands, balled at his sides, are shaking violently"

    label fork_1:
        menu:
            "We don’t sell packets but I have individual plastic forks I could give you":
                jump fork_4
            "I’m afraid I’m going to have to ask you to leave":
                jump fork_3A
            "Man, you stink!":
                jump fork_2A
            "Are you sure you don’t want something, maybe a coffee? It’s only a dollar":
                greg "Nah I told you, come on. Rhymes with vapour stork. ” He is clearly upset by the suggestion."
                jump fork_1

    label fork_2:
        "Are you alright? You smell like a charcoal oven."
    label fork_2A:
        greg "Yeah sorry about that mate, there’s been a bit of an incident, but I had to go somewhere. I don’t want to get into it, but as a bit of a hint I can divulge that it might get a lot better if I just had a paper fork."
        jump fork_1

    label fork_3:
        "I don’t have any spare change, please leave"
    label fork_3A:
        greg "Aw don’t give me that, I’m here for a reason! Look, I just needed… I just do need a paper fork. It has to be paper, that's all I’m here for."
        jump fork_1


    label fork_4:
        greg "“What the- nah, I don’t need a plastic fork! Can you just pay attention here, I’m using words and you ain’t listening.” His bloodshot eyes roll in his skull, but when you manage to meet his gaze for a split second you see his desperation."
        menu:
            "Respectfully, are you baked out of your mind?":
                greg "If only I knew how to bake I wouldn’t be in this mess right now. I just wanted some hot food."
                jump fork_4
            "Here, just take this” *Offer him a plastic fork":
                greg "Stop trying to sell me crap I didn’t ask for. I’m trying to tell you what I want here but you ain’t really paying attention at all are you. That’s the problem with shops these days, you’re not here to get me what I want, this all just some big game to you isn’t it."
                jump fork_4
            "If you aren’t going to buy anything then please leave.":
                greg "Aw come on really? You really gonna be like that?"
                jump fork_4C
            "Is it really just a fork you’re after?":
                jump fork_4D

    label fork_4C:
        menu:
            "Yes":
                jump fork_end
            "No":
                jump fork_4

    label fork_4D:
        greg "W-what do you mean, by that?"
        menu:
            "You need help, I’m going to call the authorities":
                jump fork_5
            "I think you’re after something else entirely":
                jump fork_6
            "I think you’re just messing with me":
                jump fork_5C

    label fork_5:
        greg "Don’t be like that, come on I’m right as rain. I’ve got a real trustworthy face you know, I’ve been told that."
        menu:
            "I’m calling them now":
                greg "Alright alright, fine I’ll go. You ain’t cool at all."
                jump fork_end
            "Alright fine, you can stay":
                jump fork_5C

    label fork_5C:
        greg "Ay I knew you were alright"
        jump fork_4D

    label fork_6:
        greg "Hey you didn’t hear that from me, I don’t know what you’re talking about. You’re totally crazy, what would it even be that I could want?"
        menu:
            "A smoke detector":
                greg "If there’s one thing I need less of in my life, it’s smoke detectors. I get it I’ll pay more attention next time you don’t have to whine about it so loud."
            "Finger food":
                greg "piss off!"
            "A microwave":
                "you know, you cant put metal in microwaves. Maybe next time keep you fork in your mouth. What I think you really need, is a Microwave"
                greg "You smartass...I guess your right actually. Hey thanks!"
            "Spare change":
                greg "Come on I don’t need spare change, my parents actually own a large toothbrush factory. We have a nice house. Or we did."

    label fork_end:
        "bye."
    # This ends the game.

    return
