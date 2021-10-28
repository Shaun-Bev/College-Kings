# SCENE 35: Alternative to Penelope Date
# Locations: MC's Wolves/Apes room.
# Characters: MC
# Time: Night

label v14s35:
    if joinwolves:
        scene v14s35_1 # TPP. Show MC chilling on his phone in his wolves room, slight smile, mouth closed.
        with dissolve
    else:
        scene v14s35_2 # TPP. Show MC chilling on his phone in his apes room, slight smile, mouth closed.
        with dissolve

    play sound "sounds/vibrate.mp3"

    $ jenny.messenger.newMessage(_("Hey [name], you busy right now?"), queue =False)
    $ jenny.messenger.addReply(_("No, what's up?"))
    $ jenny.messenger.newMessage(_("Well, I've been wanting to swimming in this little lagoon I found."))
    $ jenny.messenger.addReply(_("You wanna go now?"))
    $ jenny.messenger.newMessage(_("Yeah, why not? ;) Penelope is busy, so I wanted to see if you'd be down."))
    $ jenny.messenger.addReply(_("Okay sure, where's this lagoon at?"))
    $ jenny.messenger.newImgMessage(_("Picture of the Lagoon, somehow with a location marker in the photo"))
    $ jenny.messenger.newMessage(_("See you soon!"))

    if False: ### just making sure it shows up on lint
        scene v14jenText

    label s35_PhoneContinue:
        if jenny.messenger.replies:
            call screen phone
        if jenny.messenger.replies:
            "(I should reply to Jenny.)"
            jump s35_PhoneContinue

    if joinwolves:
        scene v14s35_3 # TPP. Show MC standing naked in his wolves room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s35_3a # TPP. Same as v14s35_3, MC pulling up his swimming trunks still slightly naked, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s35_3b # TPP. Same as v14s35_3a, MC standing in the room with his swimming trunks fully on, slight smile, mouth closed
        with dissolve

    else:
        scene v14s35_4 # TPP. Show MC standing naked in his Apes room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s35_4a # TPP. Same as v14s35_4, MC pulling up his swimming trunks still slightly naked, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s35_4b # TPP. Same as v14s35_4a, MC standing in the room with his swimming trunks fully on, slight smile, mouth closed
        with dissolve

    scene v14s35_5 # TPP. Show MC walking to the Lagoon, slight smile, mouth closed.
    with fade

    jump v14s36