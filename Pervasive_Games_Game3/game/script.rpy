# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define greg = Character("Greg")
define dylan = Character("Dylan")
define martha = Character("Martha")
define unknown = Character("Unknown")

image Store_front:
    "store_front.png"
    zoom 0.8

image Store_front_blurred:
    "store_front_blurred.png"
    zoom 0.8

image Greg:
    "greg.png"
    zoom 0.5

image Martha:
    "martha.png"
    zoom 0.5

image Dylan:
    "dylan.png"
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

    "What the hell was that?"

    unknown "AWWW FUCK...ehhugh"

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

    greg "No, no. I just need a paper fork. I have my own food."
    greg "It was supposed to be such a nice evening..."

    "He stares past you, unblinking. His hand slowly curls into a fist, shaking violently."

    label fork_1:
        menu:
            "We don’t sell packets but I have individual plastic forks I could give you":
                jump fork_4
            "I’m afraid I’m going to have to ask you to leave":
                jump fork_3
            "Man, you stink!":
                jump fork_2
            "Are you sure you don’t want something, maybe a coffee? It’s only a dollar":
                greg "Nah I told you, come on. Rhymes with vapour stork."
                "He is clealy upset by the suggestion"
                jump fork_1

    label fork_2:
        "Are you alright? You smell like a charcoal oven."
        greg "Yeah sorry about that mate, there’s been a bit of an incident, but I had to go somewhere."
        greg "I don’t want to get into it, but as a bit of a hint I can divulge that it might get a lot better if I just had a paper fork."
        jump fork_1

    label fork_3:
        "I don’t have any spare change, please leave"
        greg "Aw don’t give me that, I’m here for a reason! Look, I just needed… I just do need a paper fork. It has to be paper, that's all I’m here for."
        jump fork_1


    label fork_4:
        greg "What the- nah, I don’t need a plastic fork! Can you just pay attention here, I’m using words and you ain’t listening."
        "His bloodshot eyes roll in his skull, but when you manage to meet his gaze for a split second you see his desperation."
    label fork_4_menu:
        menu:
            "Respectfully, are you baked out of your mind?":
                greg "If only I knew how to bake I wouldn’t be in this mess right now. I just wanted some hot food."
                jump fork_4_menu
            "Here, just take this” *Offer him a plastic fork":
                greg "Stop trying to sell me crap I didn’t ask for. I’m trying to tell you what I want here but you ain’t really paying attention at all are you."
                greg "That’s the problem with shops these days, you’re not here to get me what I want, this all just some big game to you isn’t it."
                jump fork_4_menu
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
                jump fork_4_menu

    label fork_4D:
        greg "W-what do you mean, by that?"
    label fork_4D_menu:
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
        jump fork_4D_menu

    label fork_6:
        greg "Hey you didn’t hear that from me, I don’t know what you’re talking about. You’re totally crazy, what would it even be that I could want?"
        menu:
            "A smoke detector":
                greg "If there’s one thing I need less of in my life, it’s smoke detectors. I get it I’ll pay more attention next time you don’t have to whine about it so loud."
            "Finger food":
                greg "piss off!"
            "A microwave":
                "You know, you cant put metal in microwaves. Maybe next time keep you fork in your mouth. What I think you really need, is a microwave"
                greg "You smartass...I guess your right actually. Hey thanks!"
                jump pre_fork_end
            "Spare change":
                greg "Come on I don’t need spare change, my parents actually own a large toothbrush factory. We have a nice house. Or we did."

    label pre_fork_end:
        "No problem. Enjoy your day"
    label fork_end:
        greg "Bye."
        hide Greg
        with dissolve
    
    scene Store_front

    "Well, that's that idiot dealt with."

    "Now I'll just..."

    "Oh for Christ's sake!"

    scene Store_front_blurred
    show Martha
    with dissolve

    "The sea breeze comes back, but only for a brief moment."

    martha "Oh, hello there son. Can you help me with something?"

    "Uh, sure... What are you looking for?"

    martha "I need some margarine, cucumbers, and string. Do you have those items in stock?"

    "Sure do! Follow me."

    martha "Oh, no no no."

    martha "No no no."

    label fork_8:
        martha "Oh no. This string wont do! It'll snap within an instant!"
        menu:
            "It'll be fine!":
                martha "The wire is thinner than paper, it won't hold!"
            "That's the good wire though!":
                martha "A shame... I thought this store would have what i needed..."
            "May i interest you in some fishing wire instead?":
                martha "Certianly, Cucumbers are so heavy nowadays! That'll help me so much!"
                jump fork_8A

    label fork_8A:
        "uhhhh, sure... Is there anything else you need ms?"
    # This ends the game.

    return
