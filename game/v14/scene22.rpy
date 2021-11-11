# SCENE 22: If you help Lindsey
# Locations: Janitors Closet
# Characters: MC (Outfit: 9), LINDSEY (Outfit: 1)
# Time: Evening

label v14s22:
    scene v14s22_1 # TPP. MC is walking on campus and stumbles upon the janitor's closet, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s22_2 # TPP. mc peeks his head in and sees Lindsey
    with dissolve

    pause 0.75

    scene v14s22_3 # FPP. The entire room is decorated with her campaign material and flyers, lindsey is in the corner with her back turned to the mc
    with dissolve

    pause 0.75

    scene v14s22_3a # FPP. same as v14s22_3 Lindsey turns around to face the mc, looks at mc, half smile, mouth open
    with dissolve

    u "This is an office right here!"

    scene v14s22_4 # TPP. Lindsey walks over to MC and they hug casually
    with dissolve

    pause 0.75

    scene v14s22_5 # FPP. lindsey full smile, mouth open
    with dissolve

    li "Hey, you! Thanks for coming. You like the spot, huh?"

    scene v14s22_5a # FPP. same as v14s22_5 lindsey mouth closed
    with dissolve

    u "Hell yeah, I love this."

    u "The real question is, how did you get permission to use it?"

    scene v14s22_5
    with dissolve

    li "I did a little favor for the janitor and now..."

    li "Well, let's just say he's a big Lindsey supporter now."

    scene v14s22_5a
    with dissolve

    u "Wait... Lindsey, did you... You know...?"

    scene v14s22_5c # FPP. same as v14s22_5a Lindsey tilts her head confused
    with dissolve

    pause 0.75

    scene v14s22_5d # FPP. same as v14s22_5 Lindsey looks shocked covering her mouth and then laughs
    with dissolve

    li "God, no! *Laughs*"

    scene v14s22_5a
    with dissolve

    u "*Whispers* Thank fucking god..."

    scene v14s22_5
    with dissolve

    li "Mr. Rose and I helped the janitor get all of his kids into SVC for free."

    scene v14s22_5a
    with dissolve

    u "Oh... Wow, Lindsey."

    scene v14s22_5e # FPP. same as v14s22_5 lindsey hand gesture, hand open, palm up
    with dissolve

    li "I just helped them with their applications but Mr. Rose dealt with all the admission stuff."

    scene v14s22_5a
    with dissolve

    u "\"Just helped\"? You're an angel, Lindsey!"

    u "What did Mr. Rose get out of all of this?"

    scene v14s22_5e 
    with dissolve

    li "That man's like the devil... All he said to the janitor was \"you owe me a favor\"."

    scene v14s22_5a
    with dissolve

    u "(What a weird dude...)"

    scene v14s22_5e
    with dissolve

    li "He said it with a smile and the janitor laughed, but it really seemed like a \"deal with the devil\" type of moment..."
    li "We should be careful about making deals with him in the future."

    scene v14s22_5a
    with dissolve

    u "That's definitely noted."

    scene v14s22_6 # TPP. Lindsey walks past the mc to the door
    with dissolve

    pause 0.75

    scene v14s22_7 # TPP. from the hallways perspective Lindsey makes sure no one's around and/or coming, closes door and then back at MC
    with dissolve

    pause 0.75

    scene v14s22_5f # FPP. same as v14s22_5e lindsey slight smile, but serious look, mouth open
    with dissolve
    play sound "sounds/doorclose.mp3"

    li "Okay, so... the reason we're here."

    scene v14s22_5g # FPP. same as v14s22_5f lindsey mouth closed
    with dissolve

    u "Planning."

    scene v14s22_5f
    with dissolve

    li "Bingo!"

    li "Thankfully, I've planned out most of the campaign already. I just have a few areas where I could use your opinion."

    scene v14s22_5h # FPP. same as v14s22_5f lindsey holds up two fingers
    with dissolve

    li "I'm gonna give you some choices and I just need to know what you feel is best for us and the campaign."

    scene v14s22_5g
    with dissolve

    u "Roger that. Can do."

    scene v14s22_5f
    with dissolve

    li "Before we start, I wanna run you through some things because this isn't as easy as I originally thought."

    scene v14s22_5g
    with dissolve

    u "Of course, shoot."

    scene v14s22_5f
    with dissolve

    li "Phase one of my plan is to secure funding. We don't have hidden funds or special resources like Chloe does."

    li "So money is priority number one, aka \"secure funding\"."

    scene v14s22_5g
    with dissolve

    u "Gotcha, we have to actually put in some work."

    scene v14s22_5i # FPP. same as v14s22_5f lindsey rolls her eyes
    with dissolve

    li "Right. Unlike, well... others."

    scene v14s22_5g
    with dissolve

    u "(Chloe...)"

    scene v14s22_5e
    with dissolve

    li "Right, so with that in mind now just have a look at my board and choose what you think is best."

    li "Both plans work and I'm comfortable with either one so... Whatever you decide is what I'll go with."

    scene v14s22_5g
    with dissolve

    u "That's some heavy pressure, Linds."

    scene v14s22_5
    with dissolve

    li "I trust you with my life, [name]. Now, choose."

    scene v14s22_5a
    with dissolve

    u "*Gulps*"

    # Lindsey's planning board appears and MC makes his choices from the UI screen
label test2:
    python:
        lindsey_board.add_approach("Sell Lindsey's Car", opinion="An old car that sits around in my Grandfather's barn, he' allowing me to have it. It's not the prettiest, but it gets you where you need to go.")
        lindsey_board.add_approach("Steal from the Chick's treasury", opinion="I know this sounds crazy... Why would I want to steal from the Chick's, right? Well, Chloe holds all of our funds in her bedroom and right now she's using them towards her campaign. We have to get that money before she spends it all on herself.")
        
        lindsey_board.add_subtask(0, "Take images of Lindsey's car without Lindsey on them.",
            opinion="The buyers probably want clear, detailed photos. Use your phone to get  pictures of all angles so they know exactly what they're buying.",
            people=[mc, lindsey])
        lindsey_board.add_subtask(0, "Take images of Lindsey's car with Lindsey on them.",
            opinion="The advertisement has to be PERFECT considering what this piece of junk looks like. I'll get dressed up really nice and we'll make sure we get pictures of all angles so they know exactly what they're buying",
            people=[mc, lindsey])
        lindsey_board.add_task(0, "Customize online listing",
            opinion="Not only does our ad have to catch people's eyes, but we also need to make sure we come up with an attractive description of the car. Most importantly, we also need to decide how much we're asking for.",
            people=[mc, lindsey])
        lindsey_board.add_task(0, "Meet with potential buyers",
            opinion="Once we have a few interested buyers, we'll ask them meet up with us so they can look at the car. Who knows what kind of people we'll run into, either way we have to convince them to buy. And try to get as much money as possible.",
            people=[mc, lindsey, buyer])

        lindsey_board.add_subtask(1, "Make sure Chloe isn't home with concert tickets ",
            opinion= "If we want to get Chloe away from her room for the night, all we need are two tickets to the concert happening this Thursday. She won't be able to say no, she's been wanting to see this band for a whlle.",
            people=[mc, chloe])
        lindsey_board.add_subtask(1, "Invite her and then not show up to something",
            opinion="The budget-friendly way to keep Chloe occupied is to make sure she's waiting for you to show up at dinner. I'll get you a reservation for two at that new Italian place, all you have to do is make her go there and wait for you as long as she possibly will.",
            people=[mc, chloe])
        lindsey_board.add_task(1, "Lindsey distracts Aubrey",
            opinion="The only person left to distract will be Aubrey, and I can take care of that with a simple 'Hey Aubrey, I think I want to try anal!' line.",
            people=[lindsey, aubrey])
        lindsey_board.add_task(1, "MC steals the chick's money from Chloe's room",
            opinion="The final and most important part, you get into Chloe's room and sniff out the cash. It could be in multiple places, so check everywhere. And honestly... See what else you can find that might help us out in the future.",
            people=[mc])

    call screen planning_board(lindsey_board)

    # Once concluded the screen disappears

label v14s22_sell_car: 
    scene v14s22_5
    with dissolve

    li "Haha, good choice."

    scene v14s22_5a
    with dissolve

    u "What's so funny?"

    if chloegf:
        scene v14s22_5e
        with dissolve

        li "I just kinda figured that you wouldn't have chosen the other option. Based on your relationship with her, you know?"

        li "No worries though, we should get a good chunk of cash either way."

        scene v14s22_5a
        with dissolve

        u "Yeah, I think we'll be alright. I'm quite confident in myself."

    else:
        scene v14s22_5
        with dissolve

        li "I was wondering if that second plan was a little too much, haha. Now I have the answer. *Chuckles*"

        scene v14s22_5a
        with dissolve

        u "*Laughs* I mean, you gotta do whatcha gotta do to win, right?"

        scene v14s22_5
        with dissolve

        li "Right. But, your decision is probably the smartest of the two."

        scene v14s22_5a
        with dissolve

        u "Mmm... Probably."
    
    jump v14s22_end

label v14s22_steal:
    $ v14s22_steal_fund = True
    scene v14s22_5j # FPP. same as v14s22_5 lindsey is really excited, and throws her hands up in the air
    with dissolve

    li "Haha! This is going to be insane..."

    scene v14s22_5
    with dissolve

    u "It's a really smart plan, I just hope we can pull it off."

    if chloegf:
        scene v14s22_5k # FPP. same as v14s22_5f head tilted down, but looking directly up at mc
        with dissolve

        li "I know, me too. And..."

        li "I really do appreciate the lengths you're willing to go for me, [name]."

        scene v14s22_5f
        with dissolve

        li "I wasn't exactly sure if you'd be \"all in\" when it came to helping me, you know?"

        scene v14s22_5g 
        with dissolve

        u "I wouldn't have chosen to help you if I was too afraid to make hard decisions. My personal relationship with Chloe has nothing to do with this."

    elif lindseyrs:
        scene v14s22_5g
        with dissolve

        u "Or you. I'm here for us. Me and you."

    else:
        scene v14s22_5f
        with dissolve

        li "Me too, this amount of money could help us tremendously with the rest of the ideas I have for the campaign. Even though it's a hard pill to swallow..."

        scene v14s22_5g
        with dissolve

        u "There's nothing hard to swallow, Linds. It's the Chicks' Treasury, right? To help fund the Chicks?"

        scene v14s22_5f
        with dissolve

        li "Yeah, but..."

        scene v14s22_5g
        with dissolve

        u "You're a Chick. No buts. It all adds up to me."

    jump v14s22_end

label v14s22_end:
    if lindseyrs:
        scene v14s22_8 # TPP. Lindsey embraces and kisses MC passionately
        with dissolve

        pause 0.75

    scene v14s22_5
    with dissolve

    li "Thank you."

    scene v14s22_5a
    with dissolve

    u "Of course."

    scene v14s22_5e
    with dissolve

    li "I can't say I'm very surprised by your choices, though."

    scene v14s22_5a
    with dissolve

    u "Oh, really?"

    scene v14s22_5
    with dissolve

    li "Really."

    scene v14s22_5f
    with dissolve

    li "Guess I've gotten to know you well enough that I can pretty much guess your opinion on most things."

    scene v14s22_5g
    with dissolve

    u "Haha. Right... Either that, you spy on me, or you're a psychic."

    scene v14s22_5f
    with dissolve

    li "Guess we'll never know."

    scene v14s22_5g
    with dissolve

    li "Let's get out of here before the night crew comes in to work."

    scene v14s22_5e 
    with dissolve

    li "I may have permission to use this place, but I don't like being in their way when they're trying to get their job done, haha."

    scene v14s22_5g
    with dissolve

    u "Good idea."

    scene v14s22_9 # TPP. Mc starts to walk away from Lindsey
    with dissolve

    pause 0.75

    scene v14s22_3b # FPP. same as v14s22_3 MC glances back at Lindsey, lindsey in different location as she cleans up her supplies/walking towards door
    with dissolve

    u "(Always thinking of others, isn't she?)"

    scene v14s22_10 # TPP. MC and Lindsey exit the closet into the school hallways, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v14s22_11 # TPP. Mc and Lindsey in a different hallway, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    jump v14s22a