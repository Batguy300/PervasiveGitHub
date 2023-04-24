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

    unknown "...eughh....mhm..."

    $ renpy.music.set_pause(True, channel="music")

    unknown "AWWW FUCK...ehhugh"

    $ renpy.music.set_pause(False, channel="music")


    scene Store_front_blurred

    show Greg

    greg "...eughh....mhm.."

    # This ends the game.

    return
