# SCENE 17: Pick a gift for Lauren
# Locations: Department Store
# Characters: STORE CLERK (Outfit: 1), MC (Outfit: 5)
# Time: Evening
# Render Count: 

label v15s17:
    scene v15s17_1 # TPP. MC enters the department store, slight smile, mouth closed
    with dissolve

    pause 0.5

    scene v15s17_2 # TPP. MC walks through the aisles, looking at random items as he passes through. Not 100% sure what he's looking for, confused expresion, mouth closed
    with dissolve

    pause 0.5

    scene v15s17_3 # TPP. A store clerk, a smiling Asian man, mouth open, suddenly appears in front of him, Mc happy expression mouth closed, show a cash register in the distance
    with dissolve

    clerk "Hello, sir! Is there something I can help you with today?"

    scene v15s17_4 # FPP. Store Clerk (SC,) slight smile, mouth closed, happy expression, looking at MC
    with dissolve

    u "Um, hi there."

    if laurenrs:
        scene v15s17_4
        with dissolve

        u "I'm buying a birthday gift for my girlfriend, Lauren. Can you help me with that?"

        scene v15s17_4a # FPP. same as v15s17_4 SC's mouth is open
        with dissolve

        clerk "Oh, certainly! I don't know her, obviously, but girlfriends are girlfriends."

        scene v15s17_4
        with dissolve

        u "(I don't know what he means by that, but...) Ha, sure."

    else:
        scene v15s17_4
        with dissolve

        u "I'm buying a birthday gift for my friend, Lauren. Any ideas?"

        scene v15s17_4a
        with dissolve

        clerk "Well, I don't know her, but I'm sure I can help you find a unique gift!"

    scene v15s17_4a
    with dissolve

    clerk "So, what does this Lauren like?"

    scene v15s17_4
    with dissolve

    u "Well... I was thinking about getting her something useful, you know, like a gift card. So that she can buy some books."

    scene v15s17_4b # FPP. same as v15s17_4a SC raises an eyebrow at MC, looking at the MC judgementally
    with dissolve

    clerk "A gift card is always the safe option. It doesn't sound like you know her very well, so that might be best."

    scene v15s17_4
    with dissolve

    u "Well, I know her. I mean we're pretty-"

    scene v15s17_4c # FPP. same as v15s17_4a SC no expression and raises an eyebrow, still looking at the MC judgementally
    with dissolve

    clerk "So, a gift card? You're going to get her a gift card? For books?"

    scene v15s17_4
    with dissolve

    u "She likes books..."

    scene v15s17_4c
    with dissolve

    clerk "Hmm..."

    scene v15s17_4
    with dissolve

    u "Okay, so what do you recommend then?"

    scene v15s17_4b
    with dissolve

    clerk "Have you thought about spending more than $5?"

    scene v15s17_4
    with dissolve

    u "I wouldn't buy her a gift card for just $5."

    scene v15s17_4d # FPP. same as SC v15s17_4a SC increaeses to a half smile
    with dissolve

    clerk "Oh, I see. We currently have them for $5, $10, $20, then $50, then $100."

    clerk "Should I get you a $100 gift card?"

    scene v15s17_4e # FPP. same as v15s17_4 SC has no expression, mouth still closed
    with dissolve

    u "That's a bit... too much. Maybe the $50 one?"

    scene v15s17_4c
    with dissolve

    clerk "Are you sure?"

    scene v15s17_4
    with dissolve

    menu:
        "Get Lauren $50 gift card":
            $ Lauren_Gift_1 = True

            scene v15s17_4
            with dissolve

            u "Yeah, I'm sure. Let's go with that."

            scene v15s17_4c
            with dissolve

            clerk "A gift card... Alright, then."

            scene v15s17_4d
            with dissolve

            clerk "Excellent! This way to checkout."

            scene v15s17_3a # same as v15s17_3 MC follows the Store Clerk (SC) to the cash register, SC is wallking in front of MC rolling his eyes, expression of disbelief, holding a gift card, MC has a slight smile, mouth closed
            with dissolve

            pause 0.5

            scene v15s17_5 # SC is standing behind a cash register, DON'T show the counter and ONLY show the top of the cash register, looking at MC, slight smile, mouth open
            with dissolve

            clerk "Here you are... One $50 gift card! I hope you don't regret going for the safe option."

            scene v15s17_5a # same as v15s17_5 SC's mouth is closed, no expression
            with dissolve

            u "It's fine, haha. The party is really soon, so I didn't have a lot of time to think about it."

            scene v15s17_5b # same as v15s17_5a SC's mouth is slightly open, and looking down at the cash register, typing on the cash register
            with dissolve

            clerk "*Mumbles* It shows..."

            scene v15s17_5a
            with dissolve

            u "I'm sorry?"

            scene v15s17_5
            with dissolve

            clerk "Nothing, sir."

            clerk "I'm sure she'll be very happy with it."

        "Other gift options":
            scene v15s17_4
            with dissolve

            u "I don't know, are there any other options?"

            scene v15s17_4d
            with dissolve

            clerk "May I suggest jewelry?"

            if laurenrs and AutumnLunchBreak:
                scene v15s17_4f # FPP. same as v15s17_4d SC's mouth is closed
                with dissolve

                u "Yes! Autumn said she'd love that."

                scene v15s17_4b
                with dissolve

                clerk "Autumn?"

                scene v15s17_4
                with dissolve

                u "Yeah, Autumn. Her sister."

                scene v15s17_4d
                with dissolve

                clerk "Ah... I'm surprised Lauren's name isn't Summer! Haha!"

                scene v15s17_4
                with dissolve

                u "Ha... Good one."

            elif MadAtMsRose:
                scene v15s17_4
                with dissolve

                u "Hmm. It's true about women and jewelry..."

                scene v15s17_4d
                with dissolve

                clerk "Yes, sir it is!"

                scene v15s17_4
                with dissolve

                u "Ms. Rose looked so proud of her new necklace and really seemed to enjoy showing it off to me... among other things..."

            if V15_MsRoseSex:
                scene v15s17_15 # FPP. A Dreamlike Vision of MsRose fully nude in one of the sexual positions from Version 15 scene 15
                with dissolve

                pause 0.75

                scene v15s17_4b
                with dissolve

                clerk "You seem to be smiling a little strangely, sir. Are you okay?"

                scene v15s17_4
                with dissolve

                u "Yeah, sorry. I was just lost in my thoughts for a moment there."

            scene v15s17_4f
            with dissolve

            u "Okay, that sounds like a good idea. Let's look at your jewelry."

            scene v15s17_4d
            with dissolve

            clerk "Jewelry is this way."

            scene v15s17_6 # TPP. MC follows the Store Clerk to another aisle, both slight smiles, mouths closed, happy expressions
            with dissolve

            pause 0.5

            scene v15s17_7 # TPP. SC extends an arm palm up towards a jewlry case, looking at MC half smile, mouth open, MC is looking at the Jewlry case, slight smile mouth closed, show the Emerald bracelet on the left and the ruby choker necklace on the right in the jewlry case
            with dissolve

            pause 0.5

            scene v15s17_8 # FPP. Show SC standing behind the jewlry case, half smile, mouth open, looking at the jewlry, show the Emerald bracelet on the left and the ruby choker necklace on the right in the jewlry case
            with dissolve

            clerk "I would suggest the emerald bracelet or the ruby choker necklace."

            scene v15s17_8a # FPP. same as v15s17_8 SC is now looking at MC 
            with dissolve

            clerk "Both beautiful items, and currently on sale for only $50."

            if LaurenFriend:
                scene v15s17_8b # FPP. same as v15s17_8a SC's mouth is closed
                with dissolve

                u "Is jewelry too much if we're just friends?"

                scene v15s17_8a
                with dissolve

                clerk "Jewelry is never too much, young man. If you buy this for her, she will be your friend forever!"

            if laurenrs:
                scene v15s17_8b
                with dissolve

                u "Would you say jewelry is the perfect choice for a girlfriend?"

                scene v15s17_8a
                with dissolve

                clerk "Absolutely. You can never go wrong with jewelry, especially at these prices."

                scene v15s17_8c # FPP. same as v15s17_8a looking at the MC judgementally
                with dissolve

                clerk "You can still choose the gift card of course, but which of these two should we consider at the counter?"

                scene v15s17_8b
                with dissolve

            menu:
                "Emerald bracelet":
                    scene v15s17_8d # FPP. same as v15s17_8b MC is looking down at the jewlry case and points to the left towards the Emerald bracelet
                    with dissolve

                    u "I think this is the best one."

                "Ruby choker necklace":
                    scene v15s17_8e # FPP. same as v15s17_8b MC is looking down at the jewlry case and points to the right towards the Ruby choker necklace
                    with dissolve

                    u "I think this is the best one."

            scene v15s17_8a
            with dissolve

            clerk "She will look like a birthday princess!"

            clerk "Now, are you sure about your gift? Ready to checkout?"

            if AutumnLunchBreak:
                scene v15s17_8b
                with dissolve

                u "Let me think for a second..."

                scene v15s17_9 # TPP. Show SC still standing behind the jewlry case, annoyed expression, rolling up a sleeve to look at his watch, MC has with hand on chin, thinking pose, looking away from the SC
                with dissolve

                pause 0.5

                scene v15s17_8b
                with dissolve

                u "Autumn told me about a little toy horse... She said it would be a good gift if I could find it."

                scene v15s17_8c
                with dissolve

                clerk "Well, thank goodness you spoke to Autumn..."

                scene v15s17_8f # FPP. same as v15s17_8c SC raises an eyebrow
                with dissolve

                clerk "But a toy horse? Are you buying this for a child? We have many children's toys."

                scene v15s17_8b
                with dissolve

                u "No, it's a gift for sentimental reasons. She won't be expecting it."

                scene v15s17_8a
                with dissolve

                clerk "Ah, very good! Let's see what horses we have in stock, shall we?"

                scene v15s17_6a # TPP. same as v15s17_6 MC follows the Store Clerk to different aisle
                with dissolve

                pause 0.50

                scene v15s17_7a # TPP. same as v15s17_7 But instead of the jewlery the horses are inside the case, the Brown horse golden mane is on the left of the case, and the White horse black mane is on the right of the horse case
                with dissolve

                pause 0.50

                scene v15s17_10 # FPP. Show SC standing behind the horse case, half smile, mouth open, looking at the horses, show the Brown horse golden mane on the left and the White horse black mane on the right in the horse case
                with dissolve

                clerk "Here we are..."

                scene v15s17_10a # FPP. same as v15s17_10 SC is now looking at MC
                with dissolve

                clerk "There are only two different colors it seems... Hopefully one of these will suit your needs."

                scene v15s17_10b # FPP. same as v15s17_10a SC's mouth is closed
                with dissolve

                u "Okay, let's see here."

                scene v15s17_10a
                with dissolve

                clerk "Remember you can make your final decision checkout, so there's no pressure. Just pick the one you like most."

                scene v15s17_10b
                with dissolve

                u "(Autumn was pretty specific if I remember correctly.)"

                menu:
                    "Brown horse, golden mane":
                        scene v15s17_10c # FPP. same as v15s17_10b MC is looking down at the horse case and points to the left towards the Brown horse, golden mane
                        with dissolve

                        u "Alright, I'll go with this one."

                        scene v15s17_10a
                        with dissolve

                        clerk "Excellent! The checkout is this way."

                    "White horse, black mane":
                        scene v15s17_10d # FPP. same as v15s17_10b MC is looking down at the horse case and points to the right towards the White horse, black mane
                        with dissolve

                        u "Alright, I'll go with this one."

                        scene v15s17_10a
                        with dissolve

                        clerk "Excellent! The checkout is this way."
                    
                scene v15s17_3b # same as v15s17_3 MC follows the Store Clerk (SC) to the cash register, SC is wallking in front of MC full smile, mouth closed, happy expression, holding a basket containg the gift card, both jewlry options, and both horse options, MC has a slight smile, mouth closed
                with dissolve

                pause 0.75

            else:
                scene v15s17_8b
                with dissolve

                u "Yeah, I'm sure."

                scene v15s17_8a
                with dissolve

                clerk "As you wish, please follow me."

                scene v15s17_3c # same as v15s17_3b the basket SC is carrying DOES NOT have the horse options in it
                with dissolve

                pause 0.75

            scene v15s17_5
            with dissolve

            clerk "So, it's final decision time. What will it be?"

            if AutumnLunchBreak:
                scene v15s17_11 # FPP. MC looks down at the counter and see's the gift card, both jewlry options, and both horse options
                with dissolve

                menu:
                    "Get Lauren $50 gift card":
                        $ Lauren_Gift_1 = True

                        scene v15s17_5
                        with dissolve

                        clerk "Here you are... One $50 gift card! I hope you don't regret going for the safe option."

                        scene v15s17_5a
                        with dissolve

                        u "It's fine, haha. The party is really soon, so I didn't have a lot of time to think about it."

                        scene v15s17_5b
                        with dissolve

                        clerk "*Mumbles* It shows..."

                        scene v15s17_5a
                        with dissolve

                        u "I'm sorry?"

                        scene v15s17_5
                        with dissolve

                        clerk "Nothing, sir."

                        clerk "I'm sure she'll be very happy with it."

                    "Jewelry Gift":
                        scene v15s17_11b # FPP. same as v15s17_11 Close up shot of the Jewlry options
                        with dissolve

                        menu:
                            "Emerald bracelet":
                                $ Lauren_Gift_2a = True

                                scene v15s17_11d # FPP. same as v15s17_11b MC holds up the Emerald Bracelet
                                with dissolve

                                u "The emerald is too beautiful to turn away from."

                            "Ruby choker necklace":
                                $ Lauren_Gift_2b = True

                                scene v15s17_11e # FPP. same v15s17_11b MC holds up Ruby choker necklace
                                with dissolve

                                u "The ruby is perfect. She's going to love it."

                        scene v15s17_5c # FPP. same as v15s17_5 increase to a half smile
                        with dissolve

                        clerk "jewelry! She is going to love it, young man."

                    "Horse Gift":
                        scene v15s17_11c # FPP. same as v15s17_11 Close up shot of the horse options
                        with dissolve

                        menu:
                            "Brown horse, golden mane":
                                $ Lauren_Gift_3a = True

                                scene v15s17_11f # FPP. same as v15s17_11c MC holds up the Brown horse, golden mane
                                with dissolve

                                u "Definitely this one!"

                            "White horse, black mane":
                                $ Lauren_Gift_3b = True

                                scene v15s17_11g # FPP. same as v15s17_11c MC holds up the White horse, black mane
                                with dissolve

                                u "This one!"

                        scene v15s17_5d # FPP. same as v15s17_5 increase to a full smile
                        with dissolve

                        clerk "The sentimental horse, aww! It's perfect."

                        scene v15s17_5e # FPP. same as v15s17_5 SC's mouth is closed
                        with dissolve

                        u "Thank you for your help."

                        scene v15s17_5
                        with dissolve

                        clerk "Of course! In fact..."

                        scene v15s17_5d
                        with dissolve

                        clerk "I'll go ahead and wrap it for you, no extra charge."

            else: 
                scene v15s17_11a # FPP. same as v15s17_11 The horse options are NOT shown
                with dissolve

                menu:
                    "Get Lauren $50 gift card":
                        $ Lauren_Gift_1 = True

                        scene v15s17_5
                        with dissolve

                        clerk "Here you are... One $50 gift card! I hope you don't regret going for the safe option."

                        scene v15s17_5a
                        with dissolve

                        u "It's fine, haha. The party is really soon, so I didn't have a lot of time to think about it."

                        scene v15s17_5b
                        with dissolve

                        clerk "*Mumbles* It shows..."

                        scene v15s17_5a
                        with dissolve

                        u "I'm sorry?"

                        scene v15s17_5
                        with dissolve

                        clerk "Nothing, sir."

                        clerk "I'm sure she'll be very happy with it."

                    "Jewelry Gift":
                        scene v15s17_11b
                        with dissolve

                        menu:
                            "Emerald bracelet":
                                $ Lauren_Gift_2a = True

                                scene v15s17_11d
                                with dissolve

                                u "The emerald is too beautiful to turn away from."

                            "Ruby choker necklace":
                                $ Lauren_Gift_2b = True

                                scene v15s17_11e
                                with dissolve

                                u "The ruby is perfect. She's going to love it."

                        scene v15s17_5c
                        with dissolve

                        clerk "Jewelry! She is going to love it, young man."

    scene v15s17_5f # FPP same as v15s17_5 SC has his back turned to the MC, He is wrapping the present
    with dissolve

    pause 0.75

    scene v15s17_5g # FPP. same as v15s17_5 He presents and holds out towards MC a wrapped present
    with dissolve

    clerk "A pretty little package!"

    scene v15s17_5h # FPP. same as v15s17_5g MC takes the present from the SC, SC's mouth is closed
    with dissolve

    u "Haha, it's great."

    scene v15s17_5
    with dissolve

    clerk "Is there anything else I can help you with today?"

    scene v15s17_5i # FPP. same as v15s17_5 SC's mouth is closed
    with dissolve

    u "I don't think s- Oh, wait... There is."

    u "It's a costume party, ha."

    scene v15s17_5j # FPP. same as v15s17_5 SC has no expression, and no smile
    with dissolve

    clerk "Oh, boy. You know, we are very low on costumes. We only have one left."

    scene v15s17_5i
    with dissolve

    u "Really? Damn... Okay. I guess I'll take it."

    scene v15s17_5k # FPP. same as v15s17_5 SC has a raised eyebrow looking at the MC judgementally
    with dissolve

    clerk "You don't want to see it first?"

    scene v15s17_5
    with dissolve

    u "There's really no point if it's the only one you have. *Laughs* I don't have time to stop anywhere else."

    scene v15s17_5d
    with dissolve

    clerk "Very well, then *Stifled laugh*"

    scene v15s17_5e
    with dissolve

    u "I'm sure it'll fit."

    scene v15s17_5d
    with dissolve

    clerk "Yes, one size fits all! I'll just put it in the bag for you."

    scene v15s17_5e
    with dissolve

    u "Thank you again."

    scene v15s17_5l # FPP. same as v15s17_5 MC hands the SC his credit card
    with dissolve

    pause 0.50

    scene v15s17_5b
    with dissolve

    pause 0.50

    scene v15s17_5m # FPP. same as v15s17_5l SC hands MC his credit card and his bag of purchases, DON'T show what's in the bag
    with dissolve

    pause 0.50

    scene v15s17_5d
    with dissolve

    clerk "Have a great night! Tell Miss Lauren I said Happy Birthday!"

    scene v15s17_5e
    with dissolve

    u "You got it!"

    scene v15s17_12 # FPP. The SC is standing behind the cash register looking and waving goodbye with a big smile as MC as MC walks away carrying the shopping bag slight smile mouth closed
    with dissolve

    pause 0.50

    scene v15s17_13 # FPP. MC exits the store carrying his shopping bag, slight smile, mouth closed
    with dissolve

    pause 0.50

    scene v15s17_14 # FPP. MC is seen walking on the sidewalk still carrying his shopping bag, slight smile, mouth closed
    with fade

    pause 0.75

    jump v15s18