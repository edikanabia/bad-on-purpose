# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

#region all characters named
define gb = Character("Gabriel", image="gabriel")
define nc = Character("Niecy", image="niecy")
define mama = Character("mama", image="mama")
define ash = Character("Ash", image="ash")
define lb = Character("Ladybird", image="ladybird")
define qt = Character("Sephirah", image="q")
define dg = Character("Dragon", image="aizeer")
define jl = Character("Jules", image="jules")
define ox = Character("Onyx", image="onyx")
define mc = Character("tony", image="tony")
define mc_thought = Character(image="tony") #tony's thoughts are colored and italicized
define mc_polite = Character() #different font, probably times new roman lol

#endregion

#change the args on this to make it a subtitle chant that auto advances
define chant = Character()


#region images linked

#tony
image side tony jawdrop = "images/portraits/tony_jawdrop.png"
image side tony rage = "images/portraits/tony_rage.png"
image side tony sensitive = "images/portraits/tony_sensitive.png"
image side tony smug = "images/portraits/tony_smug.png"
image side tony conservative = "images/portraits/tony_conservative.png"
image side tony genius = "images/portraits/tony_genius.png"
image side tony awooga = "images/portraits/tony_awooga.png"
image side tony neutral = "images/portraits/tony_neutral.png"

#gabriel
image gabriel neutral = "images/portraits/gabriel_neutral.png"
image gabriel happy = "images/portraits/gabriel_happy.png"
image gabriel shocked = "images/portraits/gabriel_shocked.png"
image gabriel annoyed = "images/portraits/gabriel_annoyed.png"
image gabriel thinking = "images/portraits/gabriel_thinking.png"
image gabriel tired = "images/portraits/gabriel_tired.png"
image gabriel annoyed closed = "images/portraits/gabriel_annoyed_closed.png"
image gabriel threaten = "images/portraits/gabriel_threaten.png"
image gabriel nervous = "images/portraits/gabriel_nervous.png"
image gabriel worried = "images/portraits/gabriel_worried.png"
image gabriel confused = "images/portraits/gabriel_confused.png"
image gabriel unamused = "images/portraits/gabriel_unamused.png"

#jules
image jules neutral = "images/portraits/jules_neutral.png"
image jules happy = "images/portraits/jules_happy.png"
image jules sad = "images/portraits/jules_sad.png"
image jules angry = "images/portraits/jules_angry.png"
image jules sideeye = "images/portraits/jules_sideeye.png"
image jules shocked = "images/portraits/jules_shocked.png"
image jules neutral happy = "images/portraits/jules_neutral_happy.png"
image jules smitten = "images/portraits/jules_smitten.png"

#mama
image mama happy = "images/portraits/mama_happy.png"
image mama neutral = "images/portraits/mama_neutral.png"
image mama confused = "images/portraits/mama_confused.png"
image mama sad = "images/portraits/mama_sad.png"
image mama happy monster = "images/portraits/wing_mama.png"
image mama smitten = "images/portraits/wing_mama_smitten.png"
image mama sad monster = "images/portraits/wing_mama_sad.png"
image mama worried = "images/portraits/wing_mama_worried.png"

#ladybird
image ladybird happy = "images/portraits/ladybird_happy.png"
image ladybird sad = "images/portraits/ladybird_sad.png"
image ladybird neutral = "images/portraits/ladybird_neutral.png"
image ladybird thinking = "images/portraits/ladybird_thinking.png"
image ladybird sideeye  = "images/portraits/ladybird_sideeye.png"
image ladybird shocked = "images/portraits/ladybird_shocked.png"
image ladybird eyeup = "images/portraits/ladybird_eyeup.png"

#niecy
image niecy neutral = "images/portraits/niecy_neutral.png"
image niecy happy = "images/portraits/niecy_happy.png"
image niecy sad = "images/portraits/niecy_sad.png"
image niecy solemn = "images/portraits/niecy_solemn.png"
image niecy devious = "images/portraits/niecy_devious.png"
image niecy shocked = "images/portraits/niecy_shocked.png"
image niecy worried = "images/portraits/niecy_worried.png"

#ash
image ash happy = "images/portraits/ash_happy.png"
image ash neutral = "images/portraits/ash_neutral.png"
image ash shocked = "images/portraits/ash_shocked.png"
image ash pepper = "images/portraits/ash_elixir.png"
image ash disgusted = "images/portraits/ash_disgusted.png"
image ash worried = "images/portraits/ash_worried.png"
image ash annoyed = "images/portraits/ash_annoyed.png"

#aizeer
image aizeer neutral = "images/portraits/aizeer_neutral.png"
image aizeer happy = "images/portraits/aizeer_happy.png"
image aizeer shocked = "images/portraits/aizeer_shocked.png"
image aizeer worried = "images/portraits/aizeer_worried.png"

#onyx
image onyx neutral = "images/portraits/onxy_neutral.png"
image onyx happy = "images/portraits/onxy_happy.png"
image onyx sad = "images/portraits/onxy_sad.png"
image onyx angry = "images/portraits/onxy_angry.png"
image onyx shocked = "images/portraits/onxy_shocked.png"
image onyx worried = "images/portraits/onxy_worried.png"
image onyx confused = "images/portraits/onxy_confused.png"

#q
image q neutral = "images/portraits/q_neutral.png"
image q smitten = "images/portraits/q_smitten.png"
image q yap = "images/portraits/q_yap.png"
image q smug = "images/portraits/q_smug.png"
image q shocked = "images/portraits/q_shocked.png"
image q angry = "images/portraits/q_angry.png"

#misc
image server = "images/portraits/server.png"

#backgrounds
image bg gabriel room = "images/backgrounds/gabriel_room.png"
image bg home = "images/backgrounds/home.png"
image bg drive thru = "images/backgrounds/drivethrough.png"
image bg mcdonalds = "images/backgrounds/mcdonalds_interior.png"
image bg mcdonalds hazy = "images/backgrounds/hazy_mcdonalds_interior.png"
image bg black = Solid("000")
image bg white = Solid("fff")

#tierlist 
image tierlist = "images/funnies/soda_teirlist.png"

#cgs
image cg spying neutral = "images/cgs/cg_spying2.png"
image cg spying worried = "images/cgs/cg_spying1.png"
image cg death = "images/cgs/cg_killing_blow.png"

#endregion

#region Pre-defined transforms

#positions
transform move_to_right:
    linear 0.8 xalign 0.85
    yalign 1.0
    
transform move_to_center:
    linear 0.8 xalign 0.5 
    yalign 1.0

transform move_to_left:
    linear 0.8 xalign 0.1
    yalign 1.0

transform person_a:
    xalign 0.15
    yalign 1.0

transform person_b:
    xalign 0.3
    yalign 1.0

transform person_c:
    xalign 0.5
    yalign 1.0

transform person_d:
    xalign 0.7
    yalign 1.0

transform person_e:
    xalign 0.82
    yalign 1.0


#transitions
define dissolve_fast = Dissolve(0.2)
define dissolve_slow = Dissolve(0.8)
define jumpcut = Dissolve(0.07)
define new_day = Fade(0.5, 0.2, 0.5)
define alien_reveal = Fade(2.0, 0.1, 2.5, color="#FFF")
define lightning_flash_1 = Fade(0.01,0,0.01, color="#98C0DB")
define lightning_flash_2 = Fade(0.01,0,1.0, color="#98C0DB")
define fade_near_instant = Fade (0, 1.0, 0.8, color="#000")

#animations

#lightning flash
#transformation flash
#fall asleep
#screen shake

#endregion

#region Sound

#endregion




#all flags
define bird_fail = True
define normal_points = 0
define where = ""
define leave_early = False
define game_over_scene = "game_over"

# The game starts here.

label start:

    python:
        name = renpy.input("Name the protagonist! (We recommend not giving him the name of someone or something you like.)")
        name = name.strip() or "Kevin"
        

    "Looks like your name issssssssssss"
    "[name], is it?"
    "all right... let's do it."

    jump gabeintro

    return

label transform_tests:
    show gabriel neutral at person_b
    show niecy happy at person_d
    "Hi Gabriel, Hi niecy."

    return



label gabeintro:
    #scene: Gabriel's room
    scene bg gabriel room
    mc_thought "I did agree to meet thiss gabriel guy to set up these dates."
    mc_thought "so where is he?"
    mc_thought "all I see is a really tall woman wlaiking toward me..."
    show gabriel neutral at person_c with dissolve_fast

        
    gb "Hi. I'm Gabriel. You must be [mc]."
    menu:
        "Why is my name Tony":
            pass
    "Heh..."
    "You'll be glad we saved you the trouble."
    "Moving on."
    mc_thought jawdrop "SEPH-{nw=0.5}"
    gb "Is something wrong...?"
    mc smug "Oh osorry... it's just that.. you remind me of this guy from this video game."
    gb thinking "I get that a lot."
    mc "are you a \[KEYWORD\] parody?"
    gb neutral "..."

    menu:
        gb tired "Who the hell is \[KEYWORD\]?"
        "Don't say ligma balls":
            pass
        "Don't say ligma balls":
            pass
        "Don't say ligma balls":
            pass
    
    mc "ligma balls"
    mc_thought rage "god"
    mc_thought "dammit"
    gb happy "Oh. So it's like that, huh..."
    show screen expression game_over_scene pass (False, True) with fade_near_instant
    #fake game over screen

    mc smug "Oh god. for a second there I thought I doied"
    gb annoyed "That was mercy."
    gb "Act up again and justice will come later."
    mc_thought sensitive "kowai desu ne :("
    gb thinking "Of course, there will be no need for justice if you simply do the right thing from the start!"
    mc smug "which is?"
    gb neutral "Before you are several beautiful women. My assistant gathered them."
    mc_thought smug "Hot damn! I'm excited!!!!!"
    gb "Your mission is to be normal around them. {w=0.3} Can you handle that?"
    mc genius "Course I can! I'm the normalest guy there is, {nw=0.2}" 
    mc smug "I'm so normal they used to call me Average Joe and I got the superlative for Most Normalest Guy in the yearbook {nw=0.2}"
    gb tired "SHut the fuck up"
    gb "Please."
    mc conservative "ok."
    mc "*raises hand*"
    gb "What."
    mc "Is my mission just to be normal because to be honest I\"m really tryna fuck so{nw=0.5}"
    gb thinking "Listen. Tony."
    gb "As a recovering misogynist myself, no one wants to hear you say that."
    gb neutral "But to answer your question, these are actually functions of the same thing."
    mc "Man if it's theat easy I wouldev had a gf alaready... i feel like you're lying."
    gb unamused "Because you're so normal?"
    mc smug "Yeah!"
    gb "Yeah we'll see about that."
    hide gabriel with dissolve_slow
    #gabriel fades away
    mc_thought conservative "oh."
    mc_thought "he vanished."
    mc_thought smug "well! I should get going."


    jump day_one

    return

label where_to:
    mc_thought "I'vev got a long week ahead of me. But first I have to make an important decision!"

    menu:
        mc_thought "Where should I take my date to?"
        "Fancy restaurant":
            mc_thought genius "Yes, yes! The fanciest restaurant I can think of!"
            mc_thought "McDonald's!"
            $ where = "fancy restaurant"
        "Coffee shop":
            mc_thought genius "Of course!" 
            mc_thought "And What better coffee shop {cps=*0.3}than...{/cps} McCafe!"
            $ where = "coffee shop"
        "Beach":
            mc_thought smug "The beach...?"
            mc_thought "Ehh... but I hate sweating."
            mc_thought "I'm sure my date will appreciate a meal from the greatest American restaurant---"
            mc_thought genius "that's McDonald's, of course---"
            mc_thought smug "MUCH more than sweating on some sandy beach."
            mc_thought genius "I'm a GENIUS!"
    
    mc_thought "I should take everyone to this venue!"

    return

#region Gabriel interludes

label interlude:
    #scene: gabriel room
    scene bg gabriel room with fade
    mc rage "Gabriel!"
    show niecy happy at person_b with dissolve
    show gabriel neutral at person_d with dissolve

    nc "Hello white man!"
    mc conservative "Who's this?"
    gb "My assistant, Niecy."
    nc "Nice to meet you!"
    mc "Okay."
    nc solemn "(\"Okay?\" Not \"The pleasure's all mine\" or \"Nice to meet you too?\")"
    gb thinking "(I told you you wouldn't like him.)"
    gb neutral "How goes it?"
    mc rage "Not great!"

    if bird_fail == False:
        mc "How comes, yesterday, you had me do all that only for the lady to turn out to be a dude!?"
        nc shocked "What? I thought men were okay!" 
        nc "You had the text in your bio that said,\"I have a soft spot for pretty men.\""
        mc jawdrop "Whhaaaaaaaaaaat who put that there?"
        gb "And we told you ahead of time... that Ladybird is a man."
        mc_thought smug "...it's true. it was on my phone. they texted me"
        mc smug "Well he wasn't cool anyway!"
    else:
        mc "Why do you keep pickin out weirdos for me!"
        mc "The first girl was obsessed with her ex and the second didn't get how a McDonald's date functioned!"
        gb tired "Well we all saw how you treated them."
        gb "No need to complain after the fact. You got your point across."
    nc neutral "It usually takes a couple dates to find someone you click with."
    nc happy "We'll find someone for you! Don't worry too much."
    mc smug "Tbh, I'm trying to keep faith in your guys' choices of girl, but these ppl arenn't my thing at all!"
    nc shocked "I'm so sorry!!"
    nc "I really tried my hardest to find as many women with unmatched beauty and attractive personalities as I could."
    nc sad "Just like you put in your description..."
    mc rage "Well you're not doing a very good job!"
    mc smug "I was so miffed from that first one I actually called over another girl to finish out the night."
    gb happy "Well look at you, coming out of your shell."
    mc conservative "Yeah, she was happy to date m e but I got closer and she was kinda fat and old so I had to tell her no."
    gb confused "Fumble tbh"
    nc devious "Fat and old!? Yo send her my way!"
    #gabriel niecy high five cg, if there's time.

    mc neutral "Now that i think about it, she kinda looked like you Gabe!"
    mc "White hair, purple eyes, everything."
    gb "Huh? A woman who looked like me? who's chubby and old?"
    gb "You met my landscaper?"
    nc neutral "But she doesn't look anything like you, does she? Besides the white hair and purple eyes."
    gb neutral "Yeah lot's of people have white hair and purple eyes, Tony." 
    gb thinking "You'll have to be more specific than that."
    mc "She had white hair and purple eyes, but curly hair instead of straight, and she was a bit tan...."
    nc "Well, Orion has curly hair, but she's not short or fat..."
    gb neutral "She's short to me." 
    gb happy "But that's because I'm 6'6 :)"
    gb thinking "I can't think of a single person who matches that description."
    nc sad "..."
    nc "Gabriel, doesn't that sound like... like it could be..."
    gb "..."

    gb "Tony..." 
    gb "Be honest."
    gb threaten "What did you really say to her?" #gabriel's really close to the screen now.
    menu:
        "Answer":
            nc shocked "Tony don't answer that!"
            menu:
                "Listen to Niecy and shut your yap":
                    pass

                "Double down":
                    nc worried "Gabriel stop him! Save him!!"
                    gb thinking "From himself?"
                    gb happy "Hahaha..."
                    gb thinking "Go ahead and finish."
                    menu:
                        "Tell Gabriel what you said despite the ominous laugh":
                            jump earlyend
                        "Cede the battle to Niecy and sit this one out":
                            pass

        "Do not":
            pass
    
    mc smug "Uh you know uh normal stuff."
    mc neutral "I didn't say anything mean."
    mc smug "I was, like, super nice to her. And stuff."
    gb thinking "You hurt her feelings."
    nc solemn "I'm more curious as to why you passed up on the opportunity to fuck his mom."
    nc "Even if you weren't interested."
    gb "You win some, you lose some, I guess."
    mc "wait"
    mc jawdrop"THat was your MOM?"
    nc shocked "💀" #skull emoji
    gb "You've still got more dates lined up, so don't-"
    gb tired "Don't fuck it up."
    gb thinking "I was going to say \"don't count yourself out just yet,\" but."
    gb annoyed closed "I have  no reason to say that."
    nc happy "That's not really your style, anyway."
    gb thinking "No, no it isn't." 
    gb happy "You're right, Niecy! You always are <3"
    gb annoyed "Now GET OUT OF MY SIGHT!"
    
    jump ash
    #and scene!
    return


#activates after gaining a certain amount of normal points
label afterq:

    gb "What happened?"
    mc "__ lost __ pronouns."
    gb "Oh wow."
    gb "That must be so tough for __."
    mc "__ know, right? __ can't even refer to __ in the first person."
    mc "Why is that????"
    #gabriel stares at the camera
    gb "It's a mystery."
    mc "YOu set me up."
    gb "I didn't plan that."
    mc "Man Gabe,"
    gb "__ are not permitted to call me that, by the way."
    gb "I neglected correct __ earlier. But I should have."
    mc "Man Gabriel, this date stuff is annoying."
    mc "Is it easier to date men?"
    gb "Shouldn't __ have asked __ that when __ went on the dates with men?"
    mc "Well __ didn't realize it then!"
    gb "Realize what?"
    mc "...you're pwetty."
    mc "I don't care that you're a man."
    gb "Don't go developing on me {i}now,{/i} __'ve been so terrible so far..."
    mc "Gabe- um- Gabriel?"
    mc "Do you think __ could ever be with a man?"
    gb "I can't answer that for __."
    mc "...could __ be with you?"
    gb "I'm married."
    "here's how tony can still win:" #I need like death note copycat music here
    mc "Is your marriage open"
    mc "cuz you seem like an open marriage guy."
    mc "I'm not against being the third."
    gb "(...This isn't good.)"
    gb "(If he comes out as bisexual now, we'll never be taken seriously again...)"
    gb "(Think of what this will do to the community...!)"
    gb "My marriage is only open to women."
    gb "Extra men aren't partners... they're accessories."
    "Guh...! That objectifying gaze...! It's almost too much to bear!"
    "__ can feel him queering my gender!"
    "Wait... if __ play my cards right, __ can clutch this counter and live with a sliver of health...!"
    mc "__ LIKE WHEN WOMEN ARE MEAN TO __!!"
    gb "*snort*"
    gb "__ don't mean that."
    menu:
        "I don't":
            gb "Thought so."
            "That was a close one. __ could have died."
            "__'m not ready to be bisexual..."
            gb "(Good... he's giving that look that says,\"I'm not ready to be bisexual.\")"
            mc "Gabriel __ don't think __'m ready for this. That kind of love is too powerful."
            mc "You can't set __ up with another man, okay?"
            gb "oh bad news"
            mc "what?"
            gb "hahahahhahahahahhahahahahahhahahahahahahahahahahahahahahahahahahahaha{nw}"

        "I do":
            gb "...__'re squirming in __ seat."
            mc "nuh-uh!"
            gb "I've been keeping a secret from __, Tony."
            gb "I may be a man."
            gb "But I'm also a woman!"
            "What!? But that means..."
            "He's been objectifying me using a female gaze!?"
            "No...! I hate when women are powerful!!"
            "NOOOOOOOOOOOOOOOOOOOO!!!!!!"

    #deathnote copycaat music fades away
    gb "Anyway."
    gb "The next person is almost here."
    gb "I should leave soon."
    mc "WAIT!!"
    gb "What is it?"
    mc "Can I have my pronouns back?"
    gb "No."
    #gabriel leaves.


    return



#endregion Gabriel interludes

#region Days 
#all of the days are in tony's room.
label day_one:
    scene bg home with fade
    mc_thought smug "I'd better get ready for my first date."
    call where_to
    jump jules
    return

label night_one:
    $ alien = ""
    scene bg home with fade
    mc_thought conservative "man..."
    mc_thought "tonight was CRAZY."
    mc_thought "I never expected someone so tall to be unable to take a RESL intellectual conversation..."
    if leave_early == True:
        $ alien = "weird"
    else:
        $ alien = "alien"
    mc_thought "and the [alien] lady afterward!"
    mc_thought "just my luck isn't it."
    if leave_early == False:
        mc_thought smug "they were wrong tho... I'm not the freak"
    else:
        pass
    mc_thought "Sheesh... I should head to bed."
    jump day_two
    return


label day_two:
    scene bg home with fade
    #it's the next day and tony's up bright and early because gabe 
    #said he has to show out and be gentle for the next date.
    mc_thought neutral "Another day?"
    mc_thought awooga"Another HAWT BABE! woohoo!"
    mc_thought conservative "Gabriel said for this one that I have to have to treat this next one with \"gentleness and care.\""
    mc_thought smug "No need ot remind me, Im' the gentlest gy there is."
    mc_thought "I evemm have my yearbook superlative for gentlest guy..."
    mc_thought genius "Of cours,e I mean my middle shchool yearbook."
    mc_thought smug "This should be EASY!"
    jump ladybird
    return

label night_two:
    scene bg home with fade
    #tony's gonna plan to show up at gabriel's room angry, feeling set up.
    if bird_fail == True:
        mc_thought neutral "Gabriel was soooooo mad at me."
        mc_thought "Like wow gabe."
        mc_thought "If you like him that much..."
        mc_thought smug "Why don't you go after him yourself!"
        "Does he know!?"
    else:
        mc_thought rage "Tuh. a MAN named LADYbird? riDICKulous."
        mc_thought "whose idea was that anyway!!?"

    mc_thought conservative "Tomorrow morning I'm gonna show Gabriel a pizza my mind."
    mc_thought "But first?"
    mc_thought sensitive "A MAN's man's gotta get to his 9pm bedtimies!"
    mc_thought "Nighty night!"
    jump interlude

    return

label night_three:
    scene bg home with fade
    #return here after onyx. last time's a charm.
    mc_thought conservative "Another resounding... failuer."
    mc_thought "The girl could be cute, and I'll JUST start to overlook her flaws..."
    mc_thought rage "And then there's always a catch!"
    mc_thought "The Universe is so CRUEL to me!!"
    mc_thought smug "guess i'll just go to bed and try to prepare for tomorrow..."
    jump dragon
    return

label night_four:
    scene bg home with None
    mc_thought conservative "So many women and not a single one of them dateable."
    mc_thought "Damn."
    mc_thought smug "I guess tomorrow I'm gonna have to tell Gabriel to send some more myway."
    mc_thought conservative "And to tell his assistant to stop ffffmucking it up for me..."
    jump endingcheck
    return


#endregion Days

#region Dates

label jules:
    scene bg mcdonalds with new_day
    #just a normal date from someone who can't get over her ex...
    show jules happy at person_c with dissolve_fast
    jl "Hey!"
    mc conservative "Hello."
    jl neutral happy "How are ya?"
    mc "I'm pretty good."
    jl "Cool! I'm Jules."
    mc "It's tony."
    jl "Nice to meet you!"
    jl "Sorry I'm late, I didn't have time to button my shirt."
    mc "Hey, I'm not complainin."
    jl happy "*laughs*"
    mc smug "So? What do you thinkof the venue huh? preddy cool isn't it?"
    jl neutral "I don't love this place, actually."
    jl neutral happy "But I mean it's all right for a casual thing, you know? With your friends."
    jl neutral "When we first came to the city, Bo and I used to come here just to be somewhere that wasn't outside."
    mc neutral "Who's Bowen Eye?"
    jl smitten "Oh, Bo is... a lot to me! But, you know... we're supposed to be on break."
    jl neutral "He's not anyone you have to worry about."
    "(silence)"
    jl neutral happy "So um, what do you for fun!"
    mc smug "Usually I play video games, very intellectual exercise."
    jl "It's a very expensive exercise, too. But I hear they're good for cognition and reflexes."
    mc genius "Are you perhasp as cultured as I am?"
    jl smitten "Me? Oh, I don't really play. Growing up, there was really one person I knew who had one of those..."
    jl shocked"Gaming consoles?"
    jl happy "Bo and I would go visit him from time to time."
    jl neutral "But he and his mom ended up moving away..."
    jl happy "They look fun, though. Changed a lot, haven't they?"
    jl shocked "What kinds of games do you play?"
    mc genius "Erm, I odn't simply play one Kind, of game."
    jl angry "I figured! That's... why I asked, \"what kind{b}s{/b}.\""
    mc smug "Well, everything, I guess!"
    jl happy neutral "So you can help me out a bit! Cuz I started to get really into these, like..."
    jl neutral "I think they're called adventure games?"
    mc conservative "Oh those don't count"
    jl shocked "wh"
    jl "Why not?"
    mc "Cuz they don't have enough gameplay. Like you're just clickin on stuff and reading it."
    jl "Are all games not just clicking on stuff?"
    mc neutral "Well when I use my custom Ubuntu distro on my Raspberry Pi am I playing video games?"
    jl "You could be! I don't know what raspberry pies have to do with anything!"
    mc smug "Well I'm much more well-versed on the topic than you are!"
    jl neutral happy "Okay! Enlighten me."
    mc "There's an objective definition for a game. A game must meet multiple criteria..."
    mc "There must be a win condiiton and a loss condition,"
    mc "There must be explicit rules,"
    mc "AND it must require significant skill or physical activity to complete."
    jl neutral "Huh, okay."
    jl "So Candyland isn't a game."
    mc "It-"
    jl shocked "Is it?"
    mc_thought rage "WHO Does she think she is!?"
    jl happy "I'm not trying to catch you in a bind or anything, I promise!"
    jl neutral happy "I just wanna understand you."
    mc neutral "It is a game,"
    jl shocked "Even htough it's effectively predetermined?" 
    jl "It doesn't require any skill at all. To pick a card from a deck."
    jl "I used to play the damn thing with Bo all the time."
    jl smitten "He'd say I was cheating cuz he rarely ever won. But he always let me go first, so..."
    mc "You talk about this Bo guy a LOT."
    jl sad "*sigh* Is it that obvious?"
    jl "We grew up together, so everything reminds me of him."
    mc conservative "I see. I see you."
    mc "You can't imagine a world without him because your small mind doesn't allow your schemas to develop."
    jl shocked "What!?"
    mc smug "It's the nature of a woman, from a small town especially, to have that experience, Julia."
    mc genius "But because I'm {i}very{/i} open-minded,..."
    mc smug "Even though you can't carry a conversation on MY turf..."
    mc "I can DEFINITELY carry one on yours."
    mc "For example, EYE read a book for the first time."
    jl sad "Oh, I totally get you. I've been so distracted with everything going on, I barely have time to read either."
    jl neutral happy "I haven't finished a good book in so long."
    jl neutral "..."
    jl shocked "I'm sorry, did you say you read a book for the first time?"
    mc "Yeah"
    jl "Like ever?"
    mc "Yeah, it was tough but I got through it."
    jl "You've never read a book before?"
    mc "No, is that weird?"
    jl sideeye "It's a little weird, yeah."
    jl neutral "I don't wanna judge or anything, though."
    jl neutral happy "What book was it?"
    mc "Cat in the Hat"
    jl shocked "Like {w=0.7}by Dr. Seuss?"
    mc "Yeah"
    jl "How did you find the {w=0.6}you know, {w=0.4}the experience?"
    mc "was alright. I liekd the pictures"
    jl neutral "he's, yanno. he's a good artist"
    jl "um"
    jl "rhymes are good too"
    mc jawdrop"there's rhymes?"
    jl sideeye"..."
    jl happy "If you liked that story, might I suggest Green Eggs and Ham next?"
    mc smug "Woah there... I appreciate an intellectual, especially a woman who's an intellectual-"
    mc "though not as intellectual as me-"
    mc "but there's no need to be a show off."
    jl sad "It's... y'know, it's whatever."
    jl "I think I should go now."
    mc neutral "What? But... you agreed to meet! I still have approximately three hours of quality time with you left!"
    jl neutral happy"{cps=*0.2}Nyeahhhhhhhhhhhhh{/cps} I changed my mind."
    mc sensitive "But what did I doooooooo actually what did I do!"
    jl neutral "Okay, well, uh, you got my name wrong, after I told it to you."
    jl sad "You called me small-minded? Over, essentially, nothing."
    jl sideeye "I'm just getting the overall vibe that you wouldn't really respect or appreciate me."
    mc neutral "I thought we were having a respectful, intellectual exchange!" 
    jl sad "*sigh* Okay, well,"
    jl "Even if we hit it out of the park, I just don't know. About us. I don't know"
    jl smitten "It's my fault, partly. I really, REALLY miss my ex."
    jl sideeye "But the, um. Elitism? Chauvinism? There's a word for it..."
    jl "It's not helping."
    mc neutral "Well jeez!"
    mc "I had no idea you were so sensitive!"
    jl sad "(I knew this was a bad idea...)"
    jl angry "Tony? Is it Tony?"
    mc "Yees..."
    jl sideeye "It was uh, nice meeting you."
    mc rage "Fine!! Be that way!!"
    mc "I hope I never see you again!!"
    jl sad "(Yeah I'm getting outta here.)"
    hide jules with dissolve_fast
    #jules leaves.

    jump mamad
    
    return

label mamad:
    #mama from a distance cg
    $ leave_early = False

    mc_thought rage "Letting a broad walk out on me.. I woulda stopped her if she wasn't six feet tall."
    mc_thought "There's no way I'm going home without a proper date"
    mc_thought neutral "I gotta find someone else! So I don't let my time go to waste."
    #sees mama
    show mama neutral at person_e with dissolve
    mc_thought awooga "Hey, there's a looker!"
    mc_thought "damn she's thicc!"
    mc awooga "Hello? Hello? Hello beautiful woman?"
    "???" "Are you referring to me as a beautiful woman!?"
    mc "You wanna come over here?"
    "???" "WEll I must approach, if I am being summoned..."
    show mama:
        move_to_center
    mc_thought neutral "hm...."
    mc_thought "Now that Im up cloase n personal..."
    $ renpy.notify("She's literally stunning.")
    mc_thought conservative "Shes... not that hot. Too tubby."
    mc neutral "How old are you mama?"
    mama happy "The destruction of your pplanet predates me!"
    mama neutral "Yet, I outrank every member of your species!"
    mama happy "In terms of the numbers, I am ranked the highest at 6,689,243rd!"
    mc "How are you ranked that low?"
    mama "On the contrary! It's the highest in the world!"
    mc "But there aren't even that many players om WoW Classic."
    mama neutral "I beg your pardon?"
    mc "WoW Classic."
    mama confused ":3?"
    mc "The video game????"
    mama "I am confused as to why you brought up video games seeing as you asked me how old I am!"
    mama neutral "I was borne from a thought around six million years ago, eight billion years in the future!"
    mc jawdrop "Damn!!"
    mama sad "Is that, a turned off...?"
    menu:
        "Yeah":
            #premature date end
            mc conservative "It totally is."
            mama "Oh... I'm sorry!"
            mama "I thought... I thought... since you called out to me..."
            mc "Nah. I'm going home"
            $ leave_early = True
            jump night_one
        "Nah":
            $ normal_points = normal_points + 1

    mc smug "Nahhhhh mama where ar eyou from?"
    mama neutral "I am from the mass of deepspace that obstructs the corners of the universe!"
    mama "I was cursed to live on Earth! But Earth is no curse at all! Not to me!!"
    mama "I traveled the universe in search of love..."
    mama happy "You called me over, and it must be because you love me!"
    mama "Show me some love!! Yes, let us create love!!"
    mc neutral "WOAH."
    mc "Back off, lady. You're a 6. at best"
    mc_thought smug "Man. It's always the ugly girls that are so forward..."
    mama sad "Ahh!!"
    mama "That... wasn't very nice!"
    mc_thought neutral "..."
    mc_thought "you know what?"
    mc_thought neutral "That Julia chick was wrong. I'm SO oen minded."
    mc "I guess I can give you a CHANCE."
    mama confused "so you will date me after all...?"
    mc "Yeaaaaaahhhhh I gueeeeesssssss"
    mama happy"Wow! I am so happy, I could... I could..."
    show mama happy monster with alien_reveal
    #wing monster mama
    mc jawdrop "WOAH WHAT THE-"
    mc_thought jawdrop "what the HECK is that?"
    mc_thought "some kind of WING MONSTER?"
    mama worried "Ohhhh..."
    mama "I did it again..."
    mama "this always happens when I get excited...."
    mama smitten "I have been deigning to tell you..."
    mama "In simple terms..."
    mama "I am an alien from outerspace..."
    mama "You do not ahte me for this, do you?"
    mama "It is something I cannot change..."

    menu:
        "I don't hate you":
            $ normal_points += 1
        "I hate aliens":
            pass

    $ renpy.notify("Hunting license revoked.")
    mc "No I think you're disgusting"
    mama worried "w..."
    mama sad monster "WAAAAAAAAAAAAAHHHHHHHHHHHHHHHH!!"
    #mama runs away
    hide mama with dissolve
    "another customer" "what the hell was that man?"
    mc smug "I know she was such a freak"
    "another customer" "nah man, YOU'RE the freak!"
    "customers" "freak! freak! freak! freak! freak!"
    #you need to leave!
    mc rage "NUH-UH!!! NUH-UH!! NO U!!! NUH-UH!!"
    mc_thought rage "Oh no... my attacks! they're bouncung off!"
    mc_thought "I-I gotta get outta here!"

    jump night_one

    return

label ladybird:
    scene bg black with dissolve
    #ladybird (sier) is expecting a proper date
    #step 1: pick him up at his house
    #scene: all black
    "..."
    gb "The first step is for Tony to pick up Ladybird at his residence."
    nc "Easy stuff!"
    gb "Let's see how he does."
    mc_thought "*knock* *knock* *knock"
    mc neutral "Hellloooooooo!"
    #open door
    show ladybird neutral at center with dissolve_fast
    lb "Hello."
    mc "I'm here to pick you up."
    lb "I am excited to be a passenger in one of those earthly machines... what were they called..."
    lb happy "Automobiles!"
    lb neutral "...where is it?"
    mc "where's what"
    lb "The car. Even I know what a car is."
    mc "*shrugs*"
    mc "Don't have one."
    lb "How are are we supposed to get to the restaurant then?"
    mc rage "Well damn Lady, it's not like I can carry you there!"
    mc "Th- the restaurant isn't even that far."
    lb thinking "*sigh* okay."
    hide ladybird with dissolve_slow
    #walking 
    gb "There's no misogyny yet, but... horrible start so far."
    nc "It can only go up from here!"
    nc  "...Hey, why can't we drive them?"
    gb "I'm curious to see how Tony handles this."
    $ renpy.notify("Mission: Handle this!")
    scene bg white with dissolve
    show ladybird happy at center with dissolve_fast
    lb "You're in luck that i'm so, \"walkpilled,\" today."
    mc smug "It's a beautiful day."
    lb "I know I am, thank you!"
    mc neutral "uh."
    menu:
        "Clarify what you said":
            mc "FOR your information, I wasn't talking about you."
            mc "YOU are FAR TOO TALL for my liking....."
            mc "I think EYE Will be the decider of whether or noot you are worthy of my admiration"
            jump ladybird_fail
        "Let it go":
            pass
    "They continue walking." #footsteps.
    lb neutral "How long until we get to the place, anyway? And where are we going?"
    mc smug "It's a surprise."    
    scene bg drive thru with dissolve
    show ladybird happy at person_d with dissolve_fast
    lb "oh! I bet it's behind that McDonald's."
    mc neutral "Erm... It is the McDonald's."
    lb neutral "umm..."
    show cg spying neutral with dissolve
    gb "You've got to be fucking kidding me."
    nc "I guess he's not good enough for Taco Bell."
    hide cg spying neutral with dissolve
    mc smug "Wanna go in?"
    lb "I suppose..."
    mc "After you."
    scene bg mcdonalds with dissolve
    show ladybird happy at right with dissolve_fast
    mc "..."
    mc "What are you doing?"
    lb neutral "Waiting to be seated...?"
    menu:
        "Wonder who waits to be seated at a McDonald's.":
            $ normal_points += 1
            mc_thought neutral "...who waits to be seated at a McDonald's?"
            pass
        "Who waits to be seated at a McDonald's!?":
            mc smug "Ummmm Ladybird!"
            mc "This {i}fine establishment{/i} allows you to go directly to the counter to order your food!"
            mc genius "Everyone with a BRAIN knows that."
            lb sad "Are.. are you saying I...?"
            mc "It's okay, Miladybird."
            mc "I don't expect you to understand."
            mc "Allow me to educate you. It will be the basis of a healthy and stable relationship"
            jump ladybird_fail
    show cg spying neutral with dissolve_fast
    gb "did he just wait to be seated at a damn McDonald's"
    nc "SHHHHHHH!"
    gb "why are you shushing me we can't fucking hear them"
    hide cg spying with dissolve_fast
    mc "I think it's okay if we just go straight to the countrer."
    show ladybird happy:
        linear 0.8 person_d
    show server at offscreenleft
    show server:
        linear 0.8 person_b
    
    lb "So! What do you recommend?"
    mc neutral "uhhhhh"
    lb "Ooooh, that quarter pounder looks scrumptious!"
    lb "Do you think the quarters come separately?"
    mc "We should start with some fries."
    lb "Okay!"
    "server" "Hi, welcome to McDonalds may I take your order"
    mc smug "Ladybirds first...!"
    mc_thought genius "hehe"
    lb "Can I get a large fry? The largest you have."
    lb "Perhaps thumb-sized, if possible, or- Oh! Oh! Do you have any fries the size of my arm?"
    "server" "*sigh* No sir. We do not."
    "server" "a large fry refers to the size of the container."
    mc "You know what. we could just get a soundwich. like a nice cheeseburger."
    lb "*gasp*!! {w=0.5} A quarter pounder with CHEESE! Great idea!"
    lb shocked "Oh, hm, why not get the double quarter pounder?"
    "server" "I hear it's double the fun."
    lb "Maybe I'll even get two of them."
    mc_thought neutral "For someone who thought this was gonna be fancier than it is..."
    mc_thought genius "She sure is excited."
    mc_thought neutral "But I'm getting kinda"
    mc_thought rage "TIRED"
    mc_thought neutral "of how indecisive she is!!"
    menu: 
        "I'm gonna tell her what's up":
            mc rage "WILL YOU HUrry up and pick something already!!"
            show server:
                linear 0.8 offscreenleft
            hide server with dissolve_fast
            mc "I've been STANDING for TWO MINUTES!!"
            mc sensitive "my feetsies hurt :("
            lb sad "I... I'm sorry..."
            jump ladybird_fail
        "I can't yet, I've got to hold it in...":
            $ normal_points += 1
            pass

    mc_thought neutral "She's really the yapper huh."
    "..."
    "..."
    lb shocked "Tony!!"
    mc "Hunh!?"
    lb neutral "What are you getting?"
    menu:
        "One cheeseburger":
            mc rage "ONE cheeseburger like a CIVILIZED HUMAN WHO CAN MODERATE THEIR POTIONS!!!"
            mc smug "I mean portions."
            lb sad "Oh..."
            "server" "gah dam."
            show server:
                linear 0.8 offscreenleft
            jump ladybird_fail
        "Two cheeseburgers":
            mc neutral "TWO cheeseburgers."
            mc "Because my stomach is GROWLING."
            lb "It is? Let's hurry up and eat, then!"
            mc rage "NEXT TIME, don't make me WAIT so long for my FOOD," 
            mc "B***H!!"
            show ladybird shocked with dissolve_fast
            pause 3.0
            show server:
                linear 0.8 offscreenleft
            jump ladybird_fail
        "Three cheeseburgers":
            $ normal_points += 1
            pass
        "Four cheeseburgers":
            mc  smug "Fffffour cheeseburgers."
            lb happy "Oh wow!"
            lb neutral "Do you usually get four cheeseburgers?"
            mc neutral "Uh...."
            mc_thought rage "I-I-I don't like that she called my bluff!"
            mc "YOU DRESS WEIRD!!"
            lb shocked "Wh..."
            lb sad "No I don't..."
            "server" "I don't wanna be here for this."
            show server:
                linear 0.8 offscreenleft
            jump ladybird_fail
    mc smug "THReeeeeee cheeseburgers."
    mc rage "SINCE the McRibb is gone..."
    "server" "Oh, dude-"
    "server" "The McRibb came back, bro."
    mc neutral "What? No it isn't."
    "server" "???"
    "server" "yes it is???"
    mc genius "No it's not I would know I'm really really smart"
    "server" "Oh boy."
    show cg spying neutral with dissolve_fast
    gb "What's going on?"
    nc "They're taking a long time to order..."
    gb "He's arguing with the server?"
    nc "Oh god, he's hopeless."
    "..."
    nc "Hey, he just said Taco Bell!"
    gb "You can read lips, Niecy? What are they saying now?"
    nc "Ah, I just really like Taco Bell. Can't do much beyond that."
    gb "Huh. They're really going at it."
    gb "...Yeah, they're {i}really{/i} going at it."
    nc "Should we do something?"
    gb "Mmmmmmmm"
    gb "nah"
    gb "It should be fine."
    nc "Oh hey, looks like things are settling down."
    hide cg spying neutral with dissolve_fast

    mc neutral "OKAY FINE. The quarter pounder with cheese."
    "server" "will that be all"
    lb eyeup "Of course not! No meal would be complete without a dessert!"
    mc_thought smug "Of course he's gonna say the chocolate chip cookie."
    lb happy "I'd like one ice cream please!"
    show cg spying worried with vpunch
    gb "HE WENT FOR THE ICE CREAM!?"
    hide cg spying worried with dissolve_fast
    "server" "..."
    "server" "I'm so sorry sir,"
    "server" "Ice cream machine broke."
    show ladybird shocked
    pause 3.0
    lb "It... it CAN'T be!"
    "server" "*crsshhh* management, we got a customer on suicide watch *crshh* over"
    mc_thought sensitive "She's having that reaction because she doesn't know any better..."
    mc_thought genius "Now's my chance to clinch this and bring it home...!"
    menu:
        "The ice cream machine is always broken":
            $ normal_points += 1

        "The ice cream machine is always broken":
            mc genius "The ice cream machine is always broken," 
            mc rage "{w=0.5}IDIOT"
            show ladybird sad
            mc "NOBODY EVEN LIKES ICE CREAM LIKE THATANYWAY."
            "server" "yo chill out lil bro"
            mc smug "Hang on, I'm not done."
            mc rage "IT'S ALL CURD AND SLOP!!"
            mc "You're DISGUSTING!!"
            "server" "yeesh..."
            show server:
                linear 0.8 offscreenleft
            lb "..."
            jump ladybird_fail
    mc genius "The ice cream machine is always broken, Miladybird."
    mc "Might I suggest, "
    "server" "the apple pie"
    mc "the ch-"
    mc rage "who said the apple pie."
    "server" "brother can you just pay for your order."
    mc "FINE"

    $ renpy.notify("Mission: Date handled!")
    scene bg black with dissolve_fast
    "Tony and Ladybird get through the arduous task of ordering a meal."
    "Now, they finally sit down to eat it..."
    scene bg mcdonalds with dissolve_fast
    show ladybird happy at center with dissolve_fast
    lb "I'm so excited to eat these."
    mc neutral "Big meal, huh"
    lb "Of course! I'm a growing boy, as they say."
    mc_thought neutral "\"Boy...\""

    mc smug "Wait." 
    mc jawdrop "You're a man?"
    lb happy "I think so!"
    mc "I thought you were a girl!!"
    lb neutral "Oh, no. I'm not educated enough to be a girl, yet."
    lb thinking "But I'm working toward my BFA (Bachelor of Femme Arts)"
    mc "Huh!? I thought... with a name like {i}Lady{/i}bird..."
    lb happy "You might not believe this, but my mononym penname is not, in fact, my true name!"
    mc rage "What the heck!! I asked them for beautiful girls with attractive personalities!"
    lb neutral "Oh, no. Definitely not a girl."
    lb happy "But I'd like to be included in that designation, one day."
    lb "Girls and Ladybird. Has a nice ring to it."
    lb neutral "Do you at least find my personality attractive...?"
    mc "I-"
    mc sensitive "well"
    lb thinking "Aha... :)"
    lb happy "Good bye, Tony. I hope it works out for you someday."
    $ bird_fail = False
    

    jump night_two

    return

label ladybird_fail:
    $ bird_fail = True
    show cg spying worried with dissolve
    gb "The hell did he just say to him!?"
    nc "Uh oh. Looks likek it's going south..."
    gb "Hang on. I'll fix this..."
    hide cg spying worried with dissolve
    #scene is whatever the previous scene was
    show gabriel happy at right with dissolve_fast
    gb "Excuse me, for a moment!"
    show ladybird happy:
        move_to_left
    show gabriel happy:
        move_to_center
    lb happy "Oh...! Tiny, your compatriot."
    show gabriel annoyed with vpunch
    gb annoyed "TONY!! WHAT are you DOING!"
    mc smug "Just being honest!!!"
    gb "I TOLD YOU-"
    show ladybird sideeye with dissolve_fast
    show gabriel shocked with dissolve_fast
    pause 4.0
    show gabriel annoyed with dissolve_fast
    #ladybird looks at him funny
    gb "(Have you no tact? I told you, gentleness and care!)"
    mc "I was being gentle! I got this I promise!"
    show gabriel annoyed:
        zoom 3.0
        xalign 0.6
        yanchor 1.0
        ypos 3000
    
    gb "I'll be \"gentle\" when I tear you limb from limb if you don't scurry your sorry lil white ass home you paper pale worthless pile of sawdust."
    hide gabriel
    show gabriel annoyed closed with dissolve_fast
    gb "I swear to god."
    mc_thought jawdrop "Yikes!"
    mc_thought "I'm outta here!"
    #tony skidaddles
    show gabriel neutral:
        linear 0.8 person_d
    show ladybird neutral:
        linear 0.8 person_b

    gb "He wasn't too mean to you, was he?"
    lb sad "I mean, people have been cruel to me before."
    gb "Don't worry."
    gb happy "I'll treat you right."
    #so if you fail ladybird he isn't going to talk to you, and it should lock you out of Gaybriel too.


    jump night_two

    return

# gabriel interrupts here to ask how it's going so far

#region Just Ash...
label ash:
    scene bg mcdonalds
    $ fav_soda = ""
    "I don't believe gabriel whe he says the dates falling thru are my fautl."
    if where != "":
        "I've beeen taking my dates to the greatest [where] in the world..."
    else:
        "I've been saving them from the horrors of going to the beach...outside..."
        "where it's hot and dangerous..."
    
    "I've been showing them kindness by being honest..."
    "And they're just walking out on me left and right."
    "It makes no sense!"
    "The next date should be arriveing soon... she better be good."

    show ash 

    ash happy "Oh hey! Are you Tony?"
    mc jawdrop "Wh- you're not even human!"
    ash annoyed "Get over it"
    mc conservative "ok."
    mc "Yeah. I'm Tony."
    mc "That's my name, dont' wear it out."
    ash neutral "Ooookay."
    ash "How are ya?"
    mc smug "I'm fine, thanks for asking."
    ash worried ""
    mc ""
    ash disgusted "(is he not gonna ask how i'm doing...?)"
    ash neutral "So what do you do for fun?"
    "mmm, cna't flex too hard or I\"ll scare her away... gotta keep it humble..."
    mc "Eh, nothing too flashy, just flexing my intellectual muscles pondering the meaning of life while benchinig 450lbs with one arm..."
    "nailed it"
    ash neutral "You work out, huh?"
    mc "Yep. If you need some tips, just hit me up{nw=0.5}"
    ash worried "It doesn't look like you work out.."
    ash worried "Ah, let me not judge."
    ash neutral "Personally, I'm super into sports, but on the weekends I like to chill and play video games for a few hours."
    mc "You mean you're a... {w=0.3}a...{w=0.3} a gamer...?"
    ash disgusted "Yes...?"
    mc "A REAL girl gamer?"
    ash worried "I'm an adult but yeah. I guess you could call me a gamer."
    "heh... I'll be the judge of thar."
    mc "I jsut have a couple quesions for you.. since you SAY you're a gamer."
    ash annoyed "You're not gonna do one of theose nerrd cred questionnaires where I have to answer trivia about 80s- and 90s-era video games,"
    ash "are you?"
    mc ""
    mc "well"
    mc "say"
    mc "for the sake of argument,"
    ash "*sigh*"
    ash "Super Mario Bros. was released in 1985{nw=0.5}"
    ash "The player character in the Legend of Zelda is named Link (although in most games you can rename him){nw=0.5}"
    ash "And in all other territories the SEGA Genesis is called the Mega Drive.{nw=0.5}"
    ash "That do it?"
    "how'd she even know..."
    "Wowza... she's good."
    ash worried "Do you need more time to come up with different riddles?"
    mc "I'm just... honestly, milady..."
    ash disgusted "\"Milady.\""
    mc "True gamer girls, such as yourself, are a rare treat in the landscape of fakes."
    mc "Those unscrupulous fake girl gamers have always attempted to seduce us REAL gamers with their siren songs and cleavage..."
    ash worried "huh"
    mc "But an honest gamer girl as yourself is truly invested in the beauty of games...!"
    ash neutral "Do you think games are art?"
    mc "no"
    ash disgusted ""
    ash "So."
    ash worried "Have you come up with that new quesiton yet...?"
    mc "As a matter facy, I have."
    mc "Ahem."
    mc "What are your favorite positions and are you wearing a bra?"
    ash shocked "?"
    ash disgusted "I always wear a bra and I'm a striker."
    mc "" # uh
    ash neutral "oh you meant like. {w=1.0}sex positions?"
    ash "Well to be honest I could really do without sex." 
    ash happy "...but that damn Dr Pepper a whole different story... "
    ash pepper "Elixir of the GODS, yo!"
    ash happy "Wanna see my favorite sodas?"

    #menu is timed
    menu:
        "Yes":
            pass
        "No":
            pass
    

    show ash:
        xalign 0.5
        move_to_right
    
    show tierlist behind ash:
        xalign 0.5
        yalign 0.25

    # the soda cutscene, which is a recorded twitch vod of maru (as ash) rating every soda while being heckled by chat
    #OR: show the tier list
    ash happy"alright so to start us off, Coke and Pepsi"
    ash neutral "they are the most basic of the bunch and are typically the most common of all the sodas" 
    ash "so for that reason C tier"
    ash happy "next we got sprite, an absolute classic of a drink"
    ash "B tier, since it's not that great but a good drink all together "
    ash disgusted "now this one is a bit controversial but 7up gets easy B tier"
    ash happy "It's because it's essentially just a sprite but a but more carbonation imo"
    ash neutral "now the cherry version of both coke and pepsi is just objectively better since it actually has flavor now"
    ash happy "B tier, easy"
    ash neutral "Fanta flavors are genuinely all good around the board, but grape is the most lacking"
    ash happy "Orange and Pineapple are definitely B tier"
    ash worried "Ill give grape C tier however since it's honestly just not it"
    ash disgusted "Okay, crush is in a similar boat, but is overall just worse!"
    ash neutral "Crush grape and strawberry are the only ones to really make note of"
    ash disgusted "I will say the Crush version of Strawberry definitely beats Fanta's, but still not that great."
    ash "C tier overall, orange will get D tier for being kinda bleh"
    ash annoyed "and also Fanta Strawberry goes there too for being relatively mid"
    ash disgusted "Sunkist would be last when it comes to fruit flavored sodas, and that shit is GARBAGE"
    ash neutral "listen chat,"
    ash worried "Sunkist is only something people enjoy when they are little babies who will drink anything with sugar in it."
    ash annoyed "Don't you DARE come in here spilling some nonsense that it's good EVER!"
    ash "Sunkist - F TIER, MODS, GET HIM OUT"
    ash neutral "achem, moving on"
    ash worried "gonna say it, Vanilla coke is honestly mid, not as good as the og"
    ash annoyed "get that ass banned to D tier"
    ash disgusted "okay so chat. Imma get a bit controversial again..."
    ash "Mountain Dew is one of the biggest hit or miss soft drinks to ever be put on the market"
    ash neutral "for that reason alone i'm gonna have to split them up a bit"
    ash disgusted "the OG is honestly one of the WORST possible flavors to drink"
    ash "Straight up just battery acid, no one wants to touch that shit."
    ash worried "D teir. Only because it's not Sunkist"
    ash neutral "Now listen folks, I get it, I'm a gamer-"
    ash happy "- emphasis on the gay part - "
    ash annoyed "But Code red is honestly kinda doo doo water!"
    ash disgusted "It's a bit better than the OG so i'm not gonna be nearly as harsh, but you will not see me drinking this in the club"
    ash neutral "and finally, with one of the most one sided competitions ever"
    ash happy "Baja Blast, is {w=0.9}BY FAR"
    ash "ONE OF THE SINGLE BEST THINGS TO BE CRAFTED BY MAN"
    ash worried "Now don't get me wrong, there is honestly better drinks out there, but they COOKED with this one"
    ash happy "easily triple platinum, give that an A but we also gonna give it top of A because its that good"
    ash "alright, next up we got the rootbeers, and honestly these all fucking slap"
    ash "A&W is probably one of the better ones to go for, nice and bubbly, relatively easy to down..."
    ash "Its honestly super good and by far one of the better root beers you can get"
    ash neutral "Mug and Barq's are also VERY good alternatives, and honestly hit any time of the year"
    ash happy "These two honestly taste very similar to each other in my opinion, but that's alright"
    ash "Honestly we giving these all As, we always hitting the streets with these in hands"
    ash neutral "now I know some of y'all might be confused as to why Canada Dry is on this list, don't worry i got my reasons."
    ash happy "Ginger ale is just the best of sodas not gonna cap"
    ash "Easily downable, great for stomaie aches, goes amazing with crackers for real"
    ash shocked "what CAN'T this drink do?"
    ash happy "A tier, easily."
    ash neutral "now we finally get to S tier, and i'm gonna be honest there was only one drink deserving of this spot"
    ash shocked "the OFFICIAL..."
    ash happy "ELIXIR OF THE GODS..."
    ash pepper "DR. PEPPER!"
    ash happy "This drink is God's blessing to us mere mortals here on (redacted)..."
    ash pepper "This drink's flavor hits kinda like a rootbeer, but it's a bit on the sweeter side and not nearly as soft."
    ash happy "It gives you a bit of bite with its Barq!"
    ash shocked "BUT DONT GET IT TWISTED,"
    ash happy "It does it in a way that add to the enjoyment of drinking it, ESPECIALLY ON THAT FIRST SIP"
    ash "OOOOOUUUUGH!"
    ash "THAT FIRST SIP <3"
    ash "LET ME TELL YOU CHAT, you will never see me rep a drink THIS HARD"
    ash worried "It's alright if it aint your favorite"
    ash happy "BUT THAT JUST MEANS YOU'RE MISSING OUT!"
    ash pepper "Dr. Pepper! EASIEST S TIER OF MY GOD,"
    ash shocked "DAMN"
    ash happy "LIFE"
    ash annoyed "...but then we got our cheap imitation..."
    ash "Pibb... Xtra..."
    ash "dear lord... this drink is just.."
    ash disgusted "..."
    ash shocked "WHO SAID IT'S GOOD!?" 
    ash annoyed "MODS, BAN THAT GUY OFF EVERY SINGLE PLATFORM."
    ash "I DONT WANT TO SEE THIS GUY IN MY STREAM, ON MY YOUTUBE, ON MY TWITTER PAGE"
    ash "ON MY TUMBLER LIVE (rest in peace), ON MY KICK (I don't even have a kick), NOT EVEN ON MY TIKTOK 'For you' PAGE, KILL THIS MAN"
    ash shocked "You like the taste of one of the phoniest, most pathetic drinks my lips ever had the displeasure of resting upon EVER!!"
    ash annoyed "YOU CAN PRACTICALLY TASTE THE CHEMICALS"
    ash "you like the hell spawn of all soft drink i cant stand for that"
    ash neutral "actually..."
    ash annoyed "yeah that's what tier this drink gets, hellspawn, get this out of my site" 
    #she just yaps here
    
    show ash:
        move_to_center
    
    hide tierlist 

    ash happy "And that's pretty much it."
    ash "So what do you think? what's YOUR favorite soda?"
    #the date branches to give you a different ending based on whether or not you like PiBB Xtra
    menu yoursoda:
        ash "What's your favorite kind of soda?"
        "Dr Pepper":
            $ fav_soda = "pepper"
            ash "Oh, great! Glad you agree."
            jump ashend
        "PiBB Xtra":
            $ fav_soda = "pibb"
            jump why_pibb
            
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
    mc "Wait,where are you going?"
    ash neutral "I gotta get home. It's late"
    mc "Wait!"
    mc "Let's make plans for another date."
    ash worried "Huh?"
    ash annoyed "Hell nah lmfao you broke asf taking me to this janky ass McDonald's 😂"
    ash happy "Thanks for the meal tho"
    "And after all I DID for her? Women are so ungrateful... grrrrr"
    #fade to black
    jump qdate
    
    return

label why_pibb:

    ash shocked "What the..."
    ash disgusted "Why would you drink a PiBB Xtra when Dr Pepper is right there...?"
    mc "it's a cherry coola that was meant to compete with but not taste exactly like dr pepper"
    mc "You see the coca cola company (coke for short) understood, after the faliure of new coke, {nw=0.3}"
    mc "that in competeing with pepsico, they should not attempt to directly imitate their products 
        in order to avoid alienating their core audience in Atlanta. {nw=0.3}"
    ash worried "Um- {nw=0.3}"
    mc "that was actually one of many such run-ins with attempting to mimic pepsico. in fact the wretched pepsico {nw=0.3}"
    mc "had forced the coke company to change the original name already. anyway. {nw=0.3}"
    mc "PiBB Xtra is a refreshing spiced cherry cola for when you need a delicious pick-me-up from any Coke product-carrying retailer. {nw=0.3}"
    ash annoyed "TONY."
    ash disgusted "If I wanted to drink a cherry cola from the Coca-Cola company, I would just drink a Cherry Coke!"
    mc "It's NOT a cherry cola it is a SPICED cherry cola, there's a whole WORLD of difference!"
    mc "But that may be a bit too nuanced for your female brain..."
    ash shocked "Oh, misogyny. I'm out"
    hide ash with dissolve
    "No way she left!"
    "That wasn't misogyny it was just a keen observation from my large brain! grrr....."
    "I'm so angry I could..."
    "couldd..."
    "..."
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    #fade to black
    jump qdate
    
    return
#endregion Just Ash...




label qdate:
    #black screen. he fell asleep.
    "???" "..hello..."
    "???" "Hello?"
    "huh?"
    "who goes there!?"
    #when he wakes up the mcdonald's looks a little strange.
    #Q stands in front of him, and it's a date?
    qt "you seem chill. lets hang out"
    mc "Are you my *yaaaaawn* date?"
    qt "uhhhh sure."
    qt "Ok. First question:"
    qt "What are your pronouns?"
    "gabes really resting my pasticence with all ofthe curveballs hes throwing me."
    "first a man. now a LIBERAL"
    "I HAVE TO STAND MY GROUND."
    mc "I don't {i}do{/i} pronouns."
    qt "No pronouns?"
    mc "No."
    qt "Only your name?"
    mc "Yeah."
    mc "wait,"
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
    qt "So I took em. {w}Don't need those anymore!"
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
    #q fades away and the mcdonald's turns back to normal

    #normal points check
    if normal_points > 3:
        call afterq
    else:
        pass
    jump onyx


    return


label onyx:

    #some of this is hidden if he meets gabriel after q
    mc jawdrop "Huh.. wait _ still can't talk about __self!"
    mc "fuck..."

    mc_thought rage "guess __ stuck like this for a while."
    mc_thought sensitive "_ still got another date, hopefully the next frew girls 
    dont mind not being able to say anything about __ pronouns"
    "Feels like Gabriel did this just to watch __ suffer more than he knows _ already have."
    mc_thought rage "Yeah... definitely set up by... THEM huh.."
    mc_thought rage "_ swear... ___ definitly get __ revenge after this is all ov-"
    
    show onyx 
    ox neutral "um... __ wouldn't happen to be Tony correct??"
    mc conservative "oh uh yeah"
    mc "that's... __"
    ox worried "how are ___ doing that with ___ mouth?"
    #onxy looks concerned never | experienced anything like this

    mc sensitive "she took __ pronouns."
    ox worried "Who's pronouns?"
    mc "__ pronouns"
    ox "Pronouns?"
    mc "__ Pronouns"
    ox "But.. who took who's pronouns?"
    mc "she took __ pronouns"
    ox "she took pronouns?"
    mc "yes"
    ox confused "So.. ___ pronouns are she/her"
    mc rage "no, __ pronouns are not she/her"
    ox "then what are pronouns then?"
    mc smug "__ pronouns are ___/__"
    ox worried "...well?"
    mc "__/___"
    ox "so pronouns are.. nothing?"
    ox "___ dont know what pronouns are?"
    mc rage "_ KNOW WHAT PRONOUNS ARE"
    ox angry "Then which pronouns do ___ use?!"
    mc genius "oooooh... _ see what the problem is."
    ox shocked "What is the problem?"
    mc "YOU cant understand __!"
    ox worried "...what am i not getting then???"
    mc rage "__ pronouns!"
    ox sad "i think ___ are the one who doesn't get pronouns Tony..."
    "god help __"
    mc "no you misunderstand!"
    ox "i don't think i do..."
    mc "NO, ITS __ PRONOUNS... THEY'RE GONE!"
    ox worried "I'm pretty sure we still use pronouns everyday."
    mc "_ REALIZE THAT NOW"
    ox neutral "umm... i did??? 🤔"
    mc "No... _... uhg.."
    ox angry "...well since ___ clearly don't understand"
    ox neutral "Im just gonna say that MY pronouns are he/him"
    mc jawdrop "{w=0.9}w h a t"
    ox "My pronouns are He/Him"
    mc "Your pronouns are he/him?! _ can't believe this!"
    ox happy "OH! GOOD! I UNDERSTOOD THAT ONE!"

    jump night_three

    return




label dragon:
    "It's the last date."
    "So dar that ASS-istant Niecy has been setting me up to FAIL."
    "Sending me a beautiful woman and there's alwasy somme trick..."
    "I'm hoping the next one is a REAL catch this time."
    "Oh, that must be her."
    
    show aizeer

    dg neutral "Hello!"
    mc smug "Hello beautiful woman."
    dg happy "How are __?"
    dg shocked "*gasp* __ pronouns!"
    mc sensitive "What about them?"
    dg "They're gone!"
    dg "Hold on, I'll fix this:"
    #thunderclap with white flash
    $ renpy.notify("Pronouns restored.")
    dg happy "That should do it."
    dg "It's such a beautiful evening! Why are we cramped indoors?"
    mc smug "Eh, I don't like the outdoors."
    dg neutral "Oh uhh.. Any specific reason why?"
    mc genius "well.. Why would anyone spend time outside?"
    mc "it's so gross and mucky out there you know? Not really ideal for a gamer like me."
    dg happy "ahh, so you play games professionally then?"
    mc conservative "what.. No.."
    "I mean I definitely COULD, i'm god's gift to gaming after all."
    "I just don't want to hurt all those people trying so desperately to get into high ranks haha."
    dg "oh, so just a hobby then? Maybe you like more story based games?"
    mc smug "Nah, I mostly play FPSs since those are what TRUE gamers play."
    dg "I personally play mostly platformers, they're not as stressful you know."
    mc "fitting for someone of your stature probably. You should work your way up to some REAL games"
    dg "Heh, probably could try some more difficult stuff yeah, you could probably walk circles around me!"
    mc_thought jawdrop "Wait what.. She didn't even deny it!"
    dg "maybe we can play some fighting or party games sometime! That could be fun!" 
    mc smug "against a non-gamer? That would be quick work."
    dg "that's okay, it's about fun right?" 
    mc jawdrop "umm.. No? Gaming isn't about fun.."
    dg shocked "huh?"
    mc genius "Gaming is about being better than your opponent."
    mc "crushing them, making them salty at your superiority" 
    dg worried "..oh"
    mc smug "listen it's fine, i wouldn't expect a girl to understand at the end of the day"
    dg neutral "..well maybe you can explain it to me sometime"
    dg "sounds like an interesting discussion"
    mc jawdrop "...wait really?"
    mc smug "i mean uh.. of course! I'd gladly explain the complex world of gaming to you"
    dg "we can also watch a movie or something, do you have any favorites?"
    mc sensitive "oh uhh.."
    mc_thought jawdrop "Damn I can only think of anime movies!"
    mc_thought rage "Come on tony, you got this, you're doing good so far.. I think.."
    mc_thought rage "Just.. say the first thing on your mind!"
    mc smug "My Hero Academia: World Heroes' Mission"
    mc_thought jawdrop "{w=0.8}G O D!"
    mc_thought rage "{w=0.8}D A M N I T!"
    dg "oh is that like, an anime thing?"
    mc sensitive "uh.. yeah.."
    dg "never really was into anime but that sounds cool."
    mc "we could maybe go back to my place to watch it?"
    dg happy "you know, I think I'd like that!"
    "Wait.. something isn't right.."
    mc conservative "*sigh*"
    mc "all right"
    mc "what's the catch."
    dg neutral "Oh, no catch!"
    dg worried "But I am technically a dragon."
    mc_thought jawdrop "..."   

    jump night_four


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
    gb "So have you decided on who you'd like to continue pursuing?"
    mc "Nah, you gotta set up some more dates. They all left and I can't figure out why :/"
    gb "You're telling me you fumbled all of them?"
    gb "All of them, in a row?"
    gb "Every single one?"
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
    gb "Tony."
    gb ""
    call killing_chant
    mc "What?"
    gb "You're going to hell."
    gb "Goodbye."

    if normal_points >6:
        show screen expression game_over_scene pass (True, False)
    else:
        show screen expression game_over_scene pass (False, False)
    #you died :(
    
    return

label failsafeending:
    gb "That's weird..."
    mc "Is something wrong?"
    gb "um..."
    jump regularending
    #ending continues as normal. should be unreachable by the player
    return

label earlyend:
    nc worried "Nooooooo!!"
    mc neutral "Can you stop SCREAAMING and let me finish?"
    mc "Jeez woman."
    mc smug "So like I said, I was already kinda put off by her being old and fat."
    mc "But when she transformed into a wing monster, I just couldn't deal."
    mc "So I told her,"
    mc_polite "*slurs*"
    mc "I don't know WHAT she was thinking goin out in public like that."
    gb happy "Wow! I'm so impressed!"
    mc genius "Are you!"
    gb "Yeah!"
    gb annoyed "You really showed my mother who's boss!"
    mc jawdrop "that was your mom?" #tiny
    nc sad "You're really in it now..."
    call screen expression game_over_scene pass (False, False)
    #you died
    return

label sodaending:

    gb "ok who the FUCK drinks mr pibb"
    mc "it is no longer called MISTRE PIBB it's called PiBB Xtra and it's a spiced cherry cola thats"
    gb "I'm killing you. {w=0.4} I'm killing you"
    show screen expression game_over_scene pass (False, False)
    #you died :(
    return
#endregion
