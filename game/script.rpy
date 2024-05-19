# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define gb = Character("Gabriel")
define mama = Character("mama!!!!")
define ash = Character("Ash")

#change the args on this to make it a subtitle chant that auto advances
define chant = Character("also gabe")

python:
    name = renpy.input("Your name?")
    name = name.strip() or "Kevin"

define mc = Character("tony")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    e "TIME JUMP!!"
    jump gabeintro

    # These display lines of dialogue.


    # This ends the game.

    return

label notifytest:
    mama "so you will date me...?"
    mc "No I hate aliens"
    $ renpy.notify("Hunting license revoked.")

    mc "wtf"
    return

label gabeintro:

    "I did agree to meet thiss gabriel guy to set up these dates."
    "so where is he?"
    "all I see is a really tall woman wlaiking toward me..."
    gb "Hi. I'm Gabriel."
    "SE-{nw=0.3}"
    gb "Is there... something you would like to say to me...?"
    mc "Oh osorry... it's just that.. you remind me of this guy from this video game."
    gb "I get that a lot."
    mc "are you a \[KEYWORD\] parody?"
    gb "..."

    menu:
        gb "Who the hell is \[KEYWORD\]?"
        "Don't say ligma balls":
            pass
        "Don't say ligma balls":
            pass
        "Don't say ligma balls":
            pass
    
    mc "ligma balls"
    "god"
    "dammit"
    gb "Oh. So it's like that, huh..."

    #fake game over screen

    mc "Oh god. for a second there I thought I doied"
    gb "That was mercy."
    gb "Act up again and justice will come later."
    "kowai desu ne :("
    gb "Of course, there will be no need for justice if you simply do the right thing from the start!"
    mc "which is?"
    gb "Before you are seven beautiful women."
    "Hot damn! I'm excited!!!!!"
    gb "Your mission is to be normal around them. {w=0.3} Can you handle that?"
    mc "Course I can! I'm the normalest guy there is, {nw=0.2}" 
    mc "I'm so normal they used to call me Average Joe and I got the superlative for Most Normalest Guy in the yearbook {nw=0.2}"
    gb "SHut the fuck up"
    gb "Please."
    #gabriel fades away
    "oh."
    "he vanished."

    return

label ash:
    $ fav_soda = ""

    #the date branches to give you a different ending based on whether or not you like PiBB Xtra
    menu soda:
        "What's your favorite kind of soda?"
        "Dr Pepper":
            ash "Oh, great! Glad you agree."
            call why_gamer
        "PiBB Xtra":
            $ fav_soda = "pibb"
            call why_pibb
            return
    return

label why_gamer:
    mc "I mean, I SUPPOSE I could put up with you bieng a {i}gamer{/i}..."
    mc "Let's make plans for another date."
    ash "Huh? Hell nah lmfao you broke asf taking me to this janky ass McDonald's 😂"
    ash "Thanks for the meal tho"
    "What!? She left?"
    "And after all I DID for her? Women are so ungrateful... grrrrr"
    return

label why_pibb:
    ash "What the..."
    ash "Why would you drink a PiBB Xtra when Dr Pepper is right there...?"
    mc "it's a cherry coola that was meant to compete with but not taste exactly like dr pepper"
    mc "You see the coca cola company (coke for short) understood, after the faliure of new coke, {nw=0.3}"
    mc "that in competeing with pepsico, they should not attempt to directly imitate their products 
        in order to avoid alienating their core audience in Atlanta. {nw=0.3}"
    ash "Um- {nw=0.3}"
    mc "that was actually one of many such run-ins with attempting to mimic pepsico. in fact the wretched pepsico {nw=0.3}"
    mc "had forced the coke company to change the original name already. anyway. {nw=0.3}"
    mc "PiBB Xtra is a refreshing spiced cherry cola for when you need a delicious pick-me-up from any Coke product-carrying retailer. {nw=0.3}"
    ash "TONY."
    ash "If I wanted to drink a cherry cola from the Coca-Cola company, I would just drink a Cherry Coke!"
    mc "It's NOT a cherry cola it is a SPICED cherry cola, there's a whole WORLD of difference!"
    mc "But that may be a bit too nuanced for your female brain..."
    return


#region Endings

label killing_chant
    chant "The divine power vested in me must only be used for good, for justice, to strike down evil."
    chant "The title Mother was bestowed upon me and may be retracted at any time."
    chant "I must at all times serve and be in servitude of the common man, for the good of humanity."
    chant "Be sure and be true; the power of Mother will be used in this moment, in this moment," 
    chant "in truth and good faith, in truth and good conscience."
    chant "If I should falter, the heavens may strike me down."

    return


label endingcheck:

    mc "Oh thank goodness you're here gabe. It was TERRIBLE,."
    mc "those girls... they were so WEIRD! "
    gb "So you're telling me you fumbled all of them."
    gb "All seven women, in a row."
    mc "How could I fumble if I'm the prize?"
    #gabriel grimaces with his eyes wide.

    if fav_soda == "pibb":
        jump regularending
    elif fav_soda == "pepper":
        jump sodaending
    else:
        #block of code to run
    return

label regularending:

    
    return

label failsafeending:
    gb "That's weird..."
    mc "Is something wrong?"
    gb "um..."
    jump regularending
    #ending continues as normal. should be unreachable by the player
    return

label sodaending:

    gb "ok who the FUCK drinks mr pibb"
    mc "it's called PiBB Xtra and it's a spiced cherry cola thats"
    gb "I'm killing you. {w=0.4} I'm killing you"

    #you died :(
    return
#endregion
