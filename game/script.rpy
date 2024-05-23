# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# maake a date character template
define date = Character()


define gb = Character("Gabriel")
define mama = Character("mama!!!!")
define ash = Character("Ash")
define lb = Character("Ladybird")
define qt = Character("Sephirah")
define dg = Character("Dragon")

#change the args on this to make it a subtitle chant that auto advances
define chant = Character("gabriel")

python:
    name = renpy.input("Your name?")
    name = name.strip() or "Kevin"

define mc = Character("tony")
define mc_polite = Character()


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
    jump qdate

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

    jump ash

    return

label where_to:
    menu:
        "Where should I take my date to?"
        "Fancy restaurant":
            "Yes, yes! The fanciest restaurant I can think of!"
        "Coffee shop":
            "Of course! What better coffee shop than McCafe!"
        "Beach":
            "The beach...?"
            "Ehh... but I hate sweating."
            "I'm sure my date will appreciate a meal from the greatest American restaurant---"
            "that's McDonald's, of course---"
            "MUCH more than sweating on some sandy beach."
            "I'm a GENIUS!"
    
    "I should take everyone to this venue!"
    return

#region Gabriel interludes
label afterq:
    gb "What happened?"
    mc "__ lost __ pronouns."
    gb "Oh wow."
    gb "That must be so tough for __."
    mc "__ can't even refer to __ in the first person."
    gb "Damn that fucking sucks."


    return

label afterlb:

    gb "Ha!"
    gb "Nice try."

    return


#endregion Gabriel interludes


#region Dates

label ladybird:
    mc "And for the LAST time, I'm onlty looking to date GIRLS!! NOT men."
    lb "Can I be included in that designation?"
    lb "Girls and Ladybird, if it's not too much trouble."

    return

label qdate:
    qt "Ok. First question:"
    qt "What are your pronouns?"
    "gabes really resting my pasticence with all ofthe curveballs hes throwing me."
    "first analie,n. now a LIBERAL"
    "I HAVE TO STAND MY GROUND."
    mc "I don't {i}do{/i} pronouns."
    qt "No pronouns?"
    mc "No."
    qt "So if I were to use he/him for you, that would be misgendering..."
    mc "No, it- {nw=0.5}"
    qt "No pronouns..."
    mc "wait a minute-{nw=0.5}"
    $ renpy.notify("Pronouns lost!")
    qt "...got it."

    qt "Alright, second question."
    qt "Hypothetically." 
    qt "If __ girlfriend were a worm, would __ still love her?"
    mc "What?"
    qt "If __ girlfriend were a worm,"
    qt "would __ still love her?"
    mc "Would who still love her?"
    qt "__, Tony! __!!"
    mc "HOW are you doing that with your mouth???"
    qt "__ didn't answer my question."
    mc "Well of course __ would love __ hypothetical girlfriend"
    "..."
    "hold on"
    mc "__ would love __ hypothetical girlfriend"
    mc "what is goin g on"
    qt "Oh, __ said __ didn't do pronouns."
    qt "So I took em. {w}No pronouns for __!"
    #tony D:    

    qt "Okay. Last question."
    qt "If __ were put in an elementary school and __ couldn't escape, how many fifth graders do __ think __ could take out before dying?"
    mc "{w=0.9}Like in CoD zombies?"
    qt "Yeah"
    mc "Easily 300 rounds."
    qt "Really?????"
    mc "Yeah. Like __ easily got 300 rounds in blops 3 zombies. on every map"
    qt "Oh wow! Isn't that world record?"
    qt "Wait I'm looking that up right now..."
    "whats she doing"
    mc "jsyk __ records orent on thwe leaderboards yet tho hteyre still beeing verified"
    qt "Says highest possible round is 255..."
    mc "yeah but"
    qt "Higher rounds aren't possible without mods..."
    qt "Yeah gonna have to doubt on the fifth graders question :/"
    mc "__ could do it!"
    qt "Excuse me, are __ modding my fifth graders question?"
    mc ""

    qt "anyway."
    qt "Still can't believe the whole \"no pronouns\" thing."
    qt "Me personally, my pronouns are just she cuz I can't be her"
    qt "(Her is my girlfriend)"
    mc "You have a GIRLFRIEND?"
    qt "Oh yeah I do"
    qt "We're not really looking for a third, though."
    mc "So why are you here?"
    qt "Oh I just thought it'd be funny lol"
    mc "So you're g-"
    #q fades away



    return

#region Just Ash...
label ash:
    $ fav_soda = ""

    "The next date should be arriveing soon... she better be good."
    ash "Oh hey! Are you Tony?"
    mc "That's my name, dont' wear it out."
    ash "Ooookay."
    ash "How are ya?"
    mc "I'm fine, thanks for asking."
    ash ""
    mc ""
    ash "(is he not gonna ask how i'm doing...?)"
    ash "So what do you do for fun?"
    mc "mmm, cna't flex too hard or I\"ll scare her away... keep it humble..."
    mc "Eh, nothing too flashy, just flexing my intellectual muscles pondering the meaning of life while benchinig 450lbs with one arm..."
    "nailed it"
    ash "You work out, huh?"
    mc "Yep. If you need some tips, just hit me up{nw=0.5}"
    ash "It doesn't look like you work out!"
    ash "Ah, let me not judge."
    ash "Personally, I'm super into sports, but on the weekends I like to chill and play video games for a few hours."
    mc "You mean you're a... {w=0.3}a...{w=0.3} a gamer...?"
    ash "Yes...?"
    mc "A REAL girl gamer?"
    ash "I'm an adult but yeah. I guess you could call me a gamer."
    "heh... I'll be the judge of thar."
    mc "I jsut have a couple quesions for you.. since you SAY you're a gamer."
    ash "You're not gonna do one of theose nerrd cred questionnaires where I have to answer trivia about 80s- and 90s-era video games,"
    ash "are you?"
    mc ""
    mc "well"
    mc "say"
    mc "for the sake of argument,"
    ash "*sigh*"
    ash "Super Mario Bros. was released in 1985"
    ash "The player character in the Legend of Zelda is named Link (although in most games you can rename him)"
    ash "And in all other territories the SEGA Genesis is called the Mega Drive."
    ash "That do it?"
    "how'd she even know..."
    "Wowza... she's good."
    ash "Do you need more time to come up with different riddles?"
    mc "I'm just... honestly, milady..."
    ash "\"Milady.\""
    mc "True gamer girls, such as yourself, are a rare treat in the landscape of fakes."
    mc "Those unscrupulous fake girl gamers have always attempted to seduce us REAL gamers with their siren songs and cleavage..."
    ash "huh"
    mc "But an honest gamer girl as yourself is truly invested in the beauty of games...!"
    ash "Do you think games are art?"
    mc "no"
    ash ""
    ash "So."
    ash "Have you come up with that new quesiton yet...?"
    mc "As a matter facy, I have."
    mc "Ahem."
    mc "What are your favorite positions and are you wearing a bra?"
    ash "?"
    ash "I always wear a bra and I'm a striker."
    mc "" # uh
    ash "oh you meant like. {w=1.0}sex positions?"
    ash "Well to be honest I could really do without sex." 
    ash "...but that damn Dr Pepper a whole different story... "
    ash "Elixir of the GODS, yo!"
    ash "Wanna see my favorite sodas?"

    #menu is timed
    menu:
        "Yes":
            pass
        "No":
            pass
    
    # the soda cutscene, which is a recorded twitch vod of maru (as ash) rating every soda while being heckled by chat



    #the date branches to give you a different ending based on whether or not you like PiBB Xtra
    menu yoursoda:
        "What's your favorite kind of soda?"
        "Dr Pepper":
            $ fav_soda = "pepper"
            ash "Oh, great! Glad you agree."
            jump ashend
        "PiBB Xtra":
            $ fav_soda = "pibb"
            jump why_pibb
            
    jump endingcheck
    return


label ashend:

    "She's salmost doen with her meal. I have to make a decision soon..."
    "This is a tough decision."
    "ON one hand she is atually very nice and sweet and cool and firendly."
    "On the other, hwer friendlyness reminfs me of a male friend, and not a woman..."
    "on ONE hand she is a strange animal furry mammal person..."
    "one the other, hot damn she"
    $ renpy.notify("We've censored Tony's remarks for the sake of decency.")
    mc_polite "Tony finds Ash very beautiful and aesthetically pleasing."
    "I can't possibly turn up my nose at a real life girl gamer!"
    "I think sh'ell make a fine gf."
    "why's she getting up"
    mc "Where are you going?"
    ash "I gotta get home. It's late"
    mc "Wait!"
    mc "Let's make plans for another date."
    ash "Huh?"
    ash "Hell nah lmfao you broke asf taking me to this janky ass McDonald's 😂"
    ash "Thanks for the meal tho"
    "And after all I DID for her? Women are so ungrateful... grrrrr"
    jump endingcheck
    # replace ending check with next date
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
    ash "Oh, misogyny. I'm out"
    "No way she left!"
    "That wasn't misogyny it was just a keen observation from my large brain! grrr....."
    jump endingcheck
    # replace ending check with next date
    return
#endregion Just Ash...

label dragon:
    "I'm hoping the next one is a REAL catch this time."
    "Oh, she's almost here."
    dg "Hello!"


    mc "*sight*"
    mc "all right"
    mc "what's the catch."
    dg "Oh, no catch!"
    dg "But I am technically a dragon."
    "So many women, and not a single one dateable."


    return

#endregion Dates


#region Endings

label killing_chant:
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
    mc "And some of them weren't even girls!"
    mc "I TRUSTED you to bring me girls!!"
    gb "\"Girls?\" Like, children?"
    mc "Gabe!!! Obviously by \"girls,\" the English word for female children, I meant \"adult women.\""
    mc "EVERYONE knows tha.t"
    gb "Uh-huh."
    gb "You are not permitted to call me \"Gabe,\" by the way."
    gb "So have you decided on who you'd like to continue pursuing?"
    mc "Nah, you gotta set up some more dates. They all left and I can't figure out why :/"
    gb "You-"
    gb "You're telling me you fumbled all of them?"
    gb "All of them, in a row?"
    mc "I didn't fumble; I'm the prize!"
    #gabriel grimaces with his eyes wide.

    if fav_soda == "pibb":
        jump sodaending
    elif fav_soda == "pepper":
        jump regularending
    else:
        jump failsafeending
        #block of code to run
    return

label regularending:
    gb "*breathes in*"
    call killing_chant
    mc "What?"
    gb "You're going to hell."
    gb "Goodbye."
    #you died :(

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
    mc "it is no longer called MISTRE PIBB it's called PiBB Xtra and it's a spiced cherry cola thats"
    gb "I'm killing you. {w=0.4} I'm killing you"

    #you died :(
    return
#endregion
