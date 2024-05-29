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
define mc_thought = Character(image="tony")
define mc_polite = Character()
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

#gabriel
image gabriel neutral = "images/portraits/gabriel_neutral.png"
image gabriel happy = "images/portraits/gabriel_happy.png"
image gabriel sad = "images/portraits/gabriel_sad.png"
image gabriel shocked = "images/portraits/gabriel_shocked.png"
image gabriel annoyed = "images/portraits/gabriel_annoyed.png"
image gabriel thinking = "images/portraits/gabriel_thinking.png"
image gabriel tired = "images/portraits/gabriel_tired.png"
image gabriel annoyed closed = "images/portraits/gabriel_annoyed_closed.png"
image gabriel threaten = "images/portraits/gabriel_threaten.png"
image gabriel nervous = "images/portraits/gabriel_nervous.png"

#jules
image jules neutral = "images/portraits/jules_neutral.png"
image jules happy = "images/portraits/jules_happy.png"
image jules sad = "images/portraits/jules_sad.png"
image jules angry = "images/portraits/jules_angry.png"
image jules sideeye = "images/portraits/jules_sideeye.png"

#mama
image mama happy = "images/portraits/mama_happy.png"
image mama neutral = "images/portraits/mama_neutral.png"
image mama confused = "images/portraits/mama_confused.png"
image mama sad = "images/portraits/mama_sad.png"
image mama happy monster = "images/portraits/wing_mama.png"
image mama smitten = "images/portraits/wing_mama_smitten.png"
image mama sad monster = "images/portraits/wing_mama_sad.png"
image mama worried = "images/portraits/wing_mama_worried"

#ladybird
image ladybird happy = "images/portraits/ladybird_happy.png"
image ladybird sad = "images/portraits/ladybird_sad.png"
image ladybird neutral = "images/portraits/ladybird_neutral.png"
image ladybird thinking = "images/portraits/ladybird_thinking.png"
image ladybird sideeye  = "images/portraits/ladybird_sideeye.png"

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

#q
image q neutral = "images/portraits/q_neutral.png"
image q smitten = "images/portraits/q_smitten.png"
image q yap = "images/portraits/q_yap.png"
image q smug = "images/portraits/q_smug.png"
image q shocked = "images/portraits/q_shocked.png"
image q angry = "images/portraits/q_angry.png"

#backgrounds
image bg gabriel room = "images/backgrounds/gabriel_room.png"
image bg home = "images/backgrounds/home.png"
image bg drive thru = "images/backgrounds/drivethrough.png"
image bg mcdonalds = "images/backgrounds/mcdonalds_interior.png"
image bg mcdonalds hazy = "images/backgrounds/hazy_mcdonalds_interior.png"
image bg black = Solid("000")
image bg white = Solid("fff")

#cgs

#endregion

#region Pre-defined screen transformations
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


# The game starts here.

label start:



    #show a menu that toggles the flash at the end of the story (the lightning)


    python:
        name = renpy.input("Name the protagonist! (We recommend not giving him the name of someone or something you like.)")
        name = name.strip() or "Kevin"
        

    "sys" "Looks like your name issssssssssss"
    "sys" "[mc]"
    "sys" "aren't you glad we saved you the trouble?"

    scene bg room


    e "TIME JUMP!! w"
    jump gabeintro

    # These display lines of dialogue.


    # This ends the game.

    return


label gabeintro:
    #scene: Gabriel's room
    scene bg gabriel room
    "I did agree to meet thiss gabriel guy to set up these dates."
    "so where is he?"
    "all I see is a really tall woman wlaiking toward me..."
    show gabriel
    gb neutral "Hi. I'm Gabriel."
    mc_thought jawdrop "SEPH-{nw=0.5}"
    gb "Is something wrong...?"
    mc smug "Oh osorry... it's just that.. you remind me of this guy from this video game."
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
    gb "Before you are several beautiful women. My assistant gathered them."
    "Hot damn! I'm excited!!!!!"
    gb "Your mission is to be normal around them. {w=0.3} Can you handle that?"
    mc "Course I can! I'm the normalest guy there is, {nw=0.2}" 
    mc "I'm so normal they used to call me Average Joe and I got the superlative for Most Normalest Guy in the yearbook {nw=0.2}"
    gb "SHut the fuck up"
    gb "Please."
    mc "ok."
    mc "*raises hand*"
    gb "What."
    mc "Is my mission just to be normal because to be honest I\"m really tryna fuck so{nw=0.5}"
    gb "Listen. Tony."
    gb "As a recovering misogynist myself, no one wants to hear you say that."
    gb "But to answer your question, these are actually functions of the same thing."
    mc "Man if it's theat easy I wouldev had a gf alaready... i feel like you're lying."
    gb "Because you're so normal?"
    mc "Yeah!"
    gb "Yeah we'll see about that."
    #gabriel fades away
    "oh."
    "he vanished."
    "well!"


    jump day_one

    return

label where_to:
    "I'vev got a long week ahead of me. But first I have to make an important decision!"

    menu:
        "Where should I take my date to?"
        "Fancy restaurant":
            "Yes, yes! The fanciest restaurant I can think of!"
            $ where = "fancy restaurant"
        "Coffee shop":
            "Of course! What better coffee shop than McCafe!"
            $ where = "coffee shop"
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

label interlude:
    #scene: gabriel room

    mc "Gabriel!"
    nc "Hello white man!"
    mc "Who's this?"
    gb "My assistant, Niecy."
    nc "Nice to meet you!"
    mc "Okay."
    nc "(\"Okay?\" Not \"The pleasure's all mine\" or \"Nice to meet you too?\")"
    gb "(I told you you wouldn't like him.)"
    gb "How goes it?"
    mc "Not great!"
    mc "How comes, yesterday, you had me do all that only for the lady to turn out to be a dude!?"
    nc "What? I thought men were okay!" 
    nc "You had the text in your bio that said,\"I have a soft spot for pretty men.\""
    mc "Whhaaaaaaaaaaat who put that there?"
    if bird_fail == False:
        gb "And we told you ahead of time... that Ladybird is a man."
        "...it's true. it was on my phone. they texted me"
        mc "Well he wasn't cool anyway!"
    else:
        gb "Well we all saw how you treated him."
        gb "No need to complain after the fact. You got your point across."
    nc "It usually takes a couple dates to find someone you click with."
    nc "We'll find someone for you! Don't worry too much."
    mc "Tbh, I'm trying to keep faith in your guys' choices of girl, but these ppl arenn't my thing at all!"
    nc "I'm so sorry!!"
    nc "I really tried my hardest to find as many women with unmatched beauty and attractive personalities as I could."
    nc "Just like you put in your description..."
    mc "Well you're not doing a very good job!"
    mc "I was so miffed from that first one I actually called over another girl to finish out the night."
    gb "Well look at you, coming out of your shell."
    mc "Yeah, she was happy to date m e but I got closer and she was kinda fat and old so I had to tell her no. Just my luck huh"
    nc "Fat and old!? Yo send her my way!"
    #gabriel niecy high five

    mc "Now that i think about it, she kinda looked like you Gabe!"
    mc "White hair, purple eyes, everything."
    gb "Huh? A woman who looked like me? who's chubby and old?"
    gb "You met my landscaper?"
    nc "But she doesn't look anything like you, does she? Besides the white hair and purple eyes."
    gb "Yeah lot's of people have white hair and purple eyes, Tony." 
    gb "You'll have to be more specific than that."
    mc "She had white hair and purple eyes, but curly hair instead of straight, and she was a bit tan...."
    nc "Well, Orion has curly hair, but she's not short or fat..."
    gb "She's short to me." 
    gb "But that's because I'm 6'6 :)"
    gb "I can't think of a single person who matches that description."
    nc "..."
    nc "Gabriel, doesn't that sound like... like it could be..."
    gb "..."

    gb "Tony..." 
    gb "Be honest."
    gb "What did you really say to her?" #gabriel's really close to the screen now.
    menu:
        "Answer":
            nc "Tony don't answer that!"
            menu:
                "Listen to Niecy and shut your yap":
                    pass

                "Double down":
                    nc "Gabriel stop him! Save him!!"
                    gb "From himself?"
                    gb "Hahaha..."
                    gb "Go ahead and finish."
                    menu:
                        "Tell Gabriel what you said despite the ominous laugh":
                            jump earlyend
                        "Cede the battle to Niecy and sit this one out":
                            pass

        "Do not":
            pass
    
    mc "Uh you know uh normal stuff."
    mc "I didn't say anything mean."
    mc "I was, like, super nice to her. And stuff."
    gb "You hurt her feelings."
    nc "I'm more curious as to why you passed up on the opportunity to fuck his mom."
    nc "Even if you weren't interested."
    gb "You win some, you lose some, I guess."
    mc "wait"
    mc "THat was your MOM?"
    nc "" #skull emoji
    gb "You've still got more dates lined up, so don't-"
    gb "Don't fuck it up."
    gb "I was going to say \"don't count yourself out just yet,\" but."
    gb "I have  no reason to say that."
    nc "That's not really your style, anyway."
    gb "No, no it isn't. You're right, Niecy! You always are <3"
    gb "Now GET OUT OF MY SIGHT!"
    
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
    #scene: tony's room
    "I'd better get ready for my first date."
    call where_to
    jump jules
    return

label night_one:
    "man..."
    "tonight was CRAZY."
    ""
    jump day_two
    return


label day_two:
    #it's the next day and tony's up bright and early because gabe 
    #said he has to show out and be gentle for the next date.
    "Another day?"
    "Another HAWT BABE! woohoo!"
    "Gabriel said for this one that I have to have to treat this next one with \"gentleness and care.\""
    "No need ot remind me, Im' the gentlest gy there is."
    "I evemm have my yearbook superlative for gentlest guy..."
    "Of cours,e I mean my middle shchool yearbook."
    jump ladybird
    return

label night_two:
    #tony's gonna plan to show up at gabriel's room angry, feeling set up.
    "Tuh. a MAN named LADYbird? riDICKulous."
    "Tomorrow morning I'm gonna show Gabriel a pizza my mind."
    jump interlude

    return

label night_three:
    #return here after onyx. last time's a charm.
    "Another resounding... failuer."
    "The girl could be cute, and I'll JUST start to overlook her flaws..."
    "And then there's always a catch!"
    "The Universe is so CRUEL to me!!"
    "guess i'll just go to bed and try to prepare for tomorrow..."
    jump dragon
    return

label night_four:
    "So many women and not a single one of them dateable."
    "Damn."
    "I guess tomorrow I'm gonna have to tell Gabriel to send some more myway."
    "And to tell his assistant to stop ffffmucking it up for me..."
    jump endingcheck
    return


#endregion Days

#region Dates

label jules:
    #just a normal date from someone who can't get over her ex...
    
    jl "Hey!"
    mc "Hello."
    jl "How are ya?"
    mc "I'm pretty good."
    jl "Cool! I'm Jules."
    mc "It's tony."
    jl "Nice to meet you."
    jl "Sorry I'm late! I didn't have time to button my shirt."
    mc "Hey, I'm not complainin."
    jl "*laughs*"
    mc "So? What do you thinkof the venue huh? preddy cool isn't it?"
    jl "I don't love this place, actually."
    jl "But I mean it's all right for a casual thing, you know? With your friends."
    jl "When we first came to the city, Bo and I used to come here just to be somewhere that wasn't outside."
    mc "Who's Bowen Eye?"
    jl "Oh, Bo is... a lot to me! But, you know... we're supposed to be on break."
    jl "He's not anyone you have to worry about."
    #silence
    jl "So um, what do you for fun!"
    mc "Usually I play video games, very intellectual exercise."
    jl "It's a very expensive exercise, too. But I hear they're good for cognition and reflexes."
    mc "Are you perhasp as cultured as I am?"
    jl "Me? Oh, I don't really play. Growing up, there was really one person I knew who had one of those..."
    jl "Gaming consoles?"
    jl "Bo and I would go visit him from time to time."
    jl "But he and his mom ended up moving away..."
    jl "They look fun, though. Changed a lot, haven't they?"
    jl "What kinds of games do you play?"
    mc "I odn't simply play one Kind, of game."
    jl "I figured! That's... why I asked, \"what kind{b}s{/b}.\""
    mc "Well, everything, I guess!"
    jl "So you can help me out a bit! Cuz I started to get really into these, like..."
    jl "I think they're called adventure games?"
    mc "Oh those don't count"
    jl "wh"
    jl "Why not?"
    mc "Cuz they don't have enough gameplay. Like you're just clickin on stuff and reading it."
    jl "Are all games not just clicking on stuff?"
    mc "Well when I use my custom Ubuntu distro on my Raspberry Pi am I playing video games?"
    jl "You could be! I don't know what raspberry pies have to do with anything!"
    mc "Well I'm much more well-versed on the topic than you are!"
    jl "Okay! Enlighten me."
    mc "There's an objective definition for a game. A game must meet multiple criteria..."
    mc "There must be a win condiiton and a loss condition,"
    mc "There must be explicit rules,"
    mc "AND it must require significant skill or physical activity to complete."
    jl "Huh, okay."
    jl "So Candyland isn't a game."
    mc "It-"
    jl "Is it?"
    "WHO Does she think she is!?"
    jl "I'm not trying to catch you in a bind or anything, I promise!"
    jl "I just wanna understand you."
    mc "It is a game,"
    jl "Even htough it's effectively predetermined?" 
    jl "It doesn't require any skill at all. To pick a card from a deck."
    jl "I used to play the damn thing with Bo all the time."
    jl "He'd say I was cheating cuz he rarely ever won. But he always let me go first, so..."
    mc "You talk about this Bo guy a LOT."
    jl "*sigh* Is it that obvious?"
    jl "We grew up together, so everything reminds me of him."
    mc "I see. I see you."
    mc "You can't imagine a world without him because your small mind doesn't allow your schemas to develop."
    jl "What!?"
    mc "It's the nature of a woman, from a small town especially, to have that experience, Julia."
    mc "But because I'm {i}very{/i} open-minded,..."
    mc "Even though you can't carry a conversation on MY turf..."
    mc "I can DEFINITELY carry one on yours."
    mc "I read a book for the first time."
    jl "Oh, I totally get you. I've been so distracted with everything going on, I barely have time to read either."
    jl "I haven't finished a good book in so long."
    jl "..."
    jl "I'm sorry, did you say you read a book for the first time?"
    mc "Yeah"
    jl "Like ever?"
    mc "Yeah, it was tough but I got through it."
    jl "You've never read a book before?"
    mc "No, is that weird?"
    jl "It's a little weird, yeah."
    jl "I don't wanna judge or anything, though."
    jl "What book was it?"
    mc "Cat in the Hat"
    jl "{w=0.7}Dr. Seuss?"
    mc "Yeah"
    jl "How did you find the {w=0.6}you know, {w=0.4}the experience?"
    mc "was alright. I liekd the pictures"
    jl "he's, yanno. he's a good artist"
    jl "um"
    jl "rhymes are good too"
    mc "there's rhymes?"
    jl "..."
    jl "If you liked that story, might I suggest Green Eggs and Ham next?"
    mc "Woah there... I appreciate an intellectual, especially a woman who's an intellectual-"
    mc "though not as intellectual as me-"
    mc "but there's no need to be a show off."
    jl "It's... y'know, it's whatever."
    jl "I think I should go now."
    mc "What? But... you agreed to meet! I still have approximately three hours of quality time with you left!"
    jl "{cps=*0.2}Nyeahhhhhhhhhhhhh{/cps} I changed my mind."
    mc "But what did I doooooooo actually what did I do!"
    jl "Okay, well, uh, you got my name wrong, after I told it to you."
    jl "You called me small-minded? Over, essentially, nothing."
    jl "I'm just getting the overall vibe that you wouldn't really respect or appreciate me."
    mc "I thought we were having a respectful, intellectual exchange!" 
    jl "*sigh* Okay, well,"
    jl "Even if we hit it out of the park, I just don't know. About us. I don't know"
    jl "It's my fault, partly. I really, REALLY miss my ex."
    jl "But the, um. Elitism? Chauvinism? There's a word for it..."
    jl "It's not helping."
    mc "Well jeez!"
    mc "I had no idea you were so sensitive!"
    jl "(I knew this was a bad idea...)"
    jl "Tony? Is it Tony?"
    mc "Yees..."
    jl "It was uh, nice meeting you."
    mc "Fine!! Be that way!!"
    mc "I hope I never see you again!!"
    jl "(Yeah I'm getting outta here.)"
    #jules leaves.

    jump mamad
    
    return

label mamad:
    #mama from a distance cg
    $ leave_early = False

    "There's no way I'm going home without a proper date"
    "Letting a broad walk out on me.. I woulda stopped her if she wasn't six feet tall."
    "I gotta find someone else tho! So I don't let my time go to waste."
    #sees mama
    "Hey, there's a looker!"
    "damn she's thicc!"
    mc "Hello? Hello? Hello beautiful woman?"
    "???" "Are you referring to me as a beautiful woman!?"
    mc "You wanna come over here?"
    "???" "WEll I must approach, if I am being summoned..."
    "..."
    "Now that Im up cloase n personal..."
    $ renpy.notify("She's literally stunning.")
    "Shes... not that hot. Too tubby."
    mc "How old are you mama?"
    mama "The destruction of your pplanet predates me!"
    mama "Yet, I outrank every member of your species!"
    mama "In terms of the numbers, I am ranked the highest at 6,689,243rd!"
    mc "How are you ranked that low?"
    mama "On the contrary! It's the highest in the world!"
    mc "But there aren't even that many players om WoW Classic."
    mama "I beg your pardon?"
    mc "WoW Classic."
    mama ":3?"
    mc "The video game????"
    mama "I am confused as to why you brought up video games seeing as you asked me how old I am!"
    mama "I was borne from a thought around six million years ago, eight billion years in the future!"
    mc "Damn!!"
    mama "Is that, a turned off...?"
    menu:
        "Yeah":
            #premature date end
            mc "It totally is."
            mama "Oh... I'm sorry!"
            mama "I thought... I thought... since you called out to me..."
            mc "Nah. I'm going home"
            $ leave_early = true
            jump night_one
        "Nah":
            $ normal_points = normal_points + 1

    mc "where ar eyou from?"
    mama "I am from the mass of deepspace that obstructs the corners of the universe!"
    mama "I was cursed to live on Earth! But Earth is no curse at all! Not to me!!"
    mama "I traveled the universe in search of love..."
    mama "You called me over, and it must be because you love me!"
    mama "Show me some love!! Yes, let us create love!!"
    mc "WOAH."
    mc "Back off, lady. You're a 6. at best"
    "Man. It's always the ugly girls that are so forward..."
    mama "Ahh!!"
    mama "That... wasn't very nice!"
    "..."
    "you know what?"
    "That Julia chick was wrong. I'm SO oen minded."
    mc "I guess I can give you a CHANCE."
    mama "so you will date me...?"
    mc "Yeaaaaaahhhhh I gueeeeesssssss"
    mama "Wow! I am so happy, I could... I could..."
    #wing monster mama
    mc "WOAH WHAT THE-"
    "what the HECK is that?"
    "some kind of WING MONSTER?"
    mama "Ohhhh..."
    mama "I did it again..."
    mama "this always happens when I get excited...."
    mama "I have been deigning to tell you..."
    mama "In simple terms..."
    mama " I am an alien from outerspace..."
    mama "You do not ahte me for this, do you?"
    mama "It is something I cannot change..."

    menu:
        "I don't hate you":
            $ normal_points += 1
        "I hate aliens":
            pass

    $ renpy.notify("Hunting license revoked.")
    mc "No I think you're disgusting"
    mama "w..."
    mama "WAAAAAAAAAAAAAHHHHHHHHHHHHHHHH!!"
    #mama runs away
    "another customer" "what the hell was that man?"
    mc "I know she was such a freak"
    "another customer" "nah man, YOU'RE the freak!"
    "customers" "freak! freak! freak! freak! freak!"
    #you need to leave!
    mc "NUH-UH!!! NUH-UH!! NO U!!! NUH-UH!!"
    "Oh no... my attacks! they're bouncung off!"
    "I-I gotta get outta here!"

    jump night_one

    return

label ladybird:

    #ladybird (sier) is expecting a proper date
    #step 1: pick him up at his house
    #scene: all black
    "*knock* *knock* *knock"

    lb "I am excited to be a passenger in one of those earthly machines... what were they called..."
    lb "Automobiles."
    mc "About that..."
    mc "I don't have a car?"

    #copy over Janay's scene
    #scene: mcdonalds

    mc "Wait. You're a man?"
    lb "I think so!"
    mc "I thought you were a girl!!"
    lb "Oh, no. I'm not educated enough to be a girl, yet."
    lb "But I'm working toward my BFA (Bachelor of Femme Arts)"
    mc "Huh!? I thought... with a name like {i}Lady{/i}bird..."
    lb "You might not believe this, but my mononym penname is not, in fact, my true name!"

    

    jump night_two

    return

label ladybird_fail:
    $ bird_fail = True
    #CG: niecy and gabriel in the bushes
    nc "Uh oh. Looks likek it's going south..."
    gb "I will intervene. Worry not."
    #scene: McDonald's
    gb "Excuse me, for a moment!"
    lb "Oh...! Tiny, your compatriot."
    gb "TONY!! WHAT are you DOING!"
    mc "Just being honest!!!"
    gb "I TOLD YOU-"
    #ladybird looks at him funny
    gb "Have you no tact? I told you, gentleness and care!"
    mc "I was being gentle! I got this I promise!"
    gb "I'll be \"gentle\" when I tear you limb from limb if you don't scurry your sorry lil white ass home you paper pale worthless pile of sawdust."
    gb "I swear to god."
    #tony skidaddles
    gb "He wasn't too mean to you, was he?"
    lb "I mean, people have been cruel to me before."
    gb "Don't worry."
    gb "I'll treat you right."
    #so if you fail ladybird he isn't going to talk to you, and it should lock you out of Gaybriel too.


    jump night_two

    return

# gabriel interrupts here to ask how it's going so far

#region Just Ash...
label ash:
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
    ash "Oh hey! Are you Tony?"
    mc "Wh- you're not even human!"
    ash "Get over it"
    mc "ok."
    mc "Yeah. I'm Tony."
    mc "That's my name, dont' wear it out."
    ash "Ooookay."
    ash "How are ya?"
    mc "I'm fine, thanks for asking."
    ash ""
    mc ""
    ash "(is he not gonna ask how i'm doing...?)"
    ash "So what do you do for fun?"
    "mmm, cna't flex too hard or I\"ll scare her away... gotta keep it humble..."
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
    #OR: show the tier list
    ash "So tbh imo ginger ale and rootbeer are kinda a particular flavor profile for me."
    ash "They're like spicy in all the right ways, you know?"
    #she just yaps here

    ash "And that's pretty much it."
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
    ash "I gotta get home. It's late"
    mc "Wait!"
    mc "Let's make plans for another date."
    ash "Huh?"
    ash "Hell nah lmfao you broke asf taking me to this janky ass McDonald's 😂"
    ash "Thanks for the meal tho"
    "And after all I DID for her? Women are so ungrateful... grrrrr"
    jump qdate
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
    "I'm so angry I could..."
    "couldd..."
    "..."
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    jump qdate
    # replace ending check with next date
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
    mc "Huh.. wait _ still can't talk about __self!"
    mc "fuck..."

    "guess __ stuck like this for a while."
    "_ still got another date, hopefully the next frew girls 
    dont mind not being able to say anything about __ pronouns"
    "Feels like Gabriel did this just to watch __ suffer more than he knows _ already have."
    "Yeah... definitely set up by... THEM huh.."
    "_ swear... ___ definitly get __ revenge after this is all ov-"
    
    ox "um... __ wouldn't happen to be Tony correct??"
    mc "oh uh yeah"
    mc "that's... __"
    ox "how are ___ doing that with ___ mouth?"
    #onxy looks concerned never | experienced anything like this

    mc "she took __ pronouns."
    ox "Who's pronouns?"
    mc "__ pronouns"
    ox "Pronouns?"
    mc "__ Pronouns"
    ox "But.. who took who's pronouns?"
    mc "she took __ pronouns"
    ox "she took pronouns?"
    mc "yes"
    ox "So.. ___ pronouns are she/her"
    mc "no, __ pronouns are not she/her"
    ox "then what are pronouns then?"
    mc "__ pronouns are ___/__"
    ox "...well?"
    mc "__/___"
    ox "so pronouns are.. nothing?"
    ox "___ dont know what pronouns are?"
    mc "_ KNOW WHAT PRONOUNS ARE"
    ox "Then which pronouns do ___ use?!"
    mc "oooooh... _ see what the problem is."
    ox "What is the problem?"
    mc "YOU cant understand __!"
    ox "...what am i not getting then???"
    mc "__ pronouns!"
    ox "i think ___ are the one who doesn't get pronouns Tony..."
    "god help __"
    mc "no you misunderstand!"
    ox "i don't think i do..."
    mc "NO, ITS __ PRONOUNS... THEY'RE GONE!"
    ox "I'm pretty sure we still use pronouns everyday."
    mc "_ REALIZE THAT NOW"
    ox "umm... i did??? 🤔"
    mc "No... _... uhg.."
    ox "...well since ___ clearly don't understand"
    ox "Im just gonna say that MY pronouns are he/him"
    mc "{w=0.9}w h a t"
    ox "My pronouns are He/Him"
    mc "Your pronouns are he/him?! _ can't believe this!"
    ox "OH! GOOD! I UNDERSTOOD THAT ONE!"

    jump night_three

    return




label dragon:
    "It's the last date."
    "So dar that ASS-istant Niecy has been setting me up to FAIL."
    "Sending me a beautiful woman and there's alwasy somme trick..."
    "I'm hoping the next one is a REAL catch this time."
    "Oh, that must be her."
    dg "Hello!"
    mc "Hello beautiful woman."
    dg "How are __?"
    dg "*gasp* __ pronouns!"
    mc "What about them?"
    dg "They're gone!"
    dg "Hold on, I'll fix this:"
    #thunderclap with white flash
    $ renpy.notify("Pronouns restored.")
    dg "That should do it."
    dg "It's such a beautiful evening! Why are we cramped indoors?"
    mc "Eh, I don't like the outdoors."
    dg ""


    mc "*sight*"
    mc "all right"
    mc "what's the catch."
    dg "Oh, no catch!"
    dg "But I am technically a dragon."

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
        pass
    else:
        pass
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
    nc "Nooooooo!!"
    mc "Can you stop SCREAAMING and let me finish?"
    mc "Jeez woman."
    mc "So like I said, I was already kinda put off by her being old and fat."
    mc "But when she transformed into a wing monster, I just couldn't deal."
    mc "So I told her,"
    mc_polite "*slurs*"
    mc "I don't know WHAT she was thinking goin out in public like that."
    gb "Wow! I'm so impressed!"
    mc "Are you!"
    gb "Yeah!"
    gb "You really showed my mother who's boss!"
    mc ""
    mc "that was your mom?" #tiny
    nc "You're really in it now..."
    #you died
    return

label sodaending:

    gb "ok who the FUCK drinks mr pibb"
    mc "it is no longer called MISTRE PIBB it's called PiBB Xtra and it's a spiced cherry cola thats"
    gb "I'm killing you. {w=0.4} I'm killing you"

    #you died :(
    return
#endregion
