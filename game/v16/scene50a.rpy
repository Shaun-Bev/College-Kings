# SCENE 50a: MC wakes up
# Locations: APE DORM/WOLF DORM
# Characters: MC (Outfit: boxers/2/5/1)
# Time: Thursday/Friday/Saturday Morning 
#

# NOTE
# This secne is called multiple times in the story timeline
# Before making the "jump v16s50a" statement
# The previous scene must set the v16s50a_dotw variable to the FOLLOWING day of the week
# Example if the scene that jumps to s50a happens on Wednesday evening
# then the v16s50a_dotw variable MUST be set to Thursday.

label v16s50a: # 50a) MC wakes up
    # -Night to morning transition-
    scene sleep_transition_fast # Ignore animation 
    with fade

    pause 2.2
            
    scene black
    with dissolve
        
    pause 1

    # -if Chloe was alone Wed night with the baby and is MC partner 
    if v16_parent_chloe and ((v16s27_mc_baby_schedule["wednesday"] == BabyDuty.PARTNER_ALONE and v16s50a_dotw == 5) or (v16s27_mc_baby_schedule["thursday"] == BabyDuty.PARTNER_ALONE and v16s50a_dotw == 6) or (v16s27_mc_baby_schedule["friday"] == BabyDuty.PARTNER_ALONE and v16s50a_dotw == 7)):
        #! v16s50akw_1 "Chloe and MC's baby doll inside of a washing machine or dryer"
        
        $ v16s50a_kiwii_post = KiwiiPost(aubrey, "v16/v16s50a_aubpost1.webp", "Umm, good morning from the Chicks?", numberLikes=817)
        $ v16s50a_kiwii_post.new_comment(autumn, "HAHAHA", numberLikes=16, force_send=True)
        $ v16s50a_kiwii_post.new_comment(lindsey, "I was wondering if there was a story behind this...", numberLikes=47, force_send=True)
        $ v16s50a_kiwii_post.new_comment(aubrey, "Chloe on baby duty, that's the story. Lol", numberLikes=75, force_send=True)
        $ v16s50a_kiwii_post.new_comment(cameron, "What the hell?", numberLikes=13, force_send=True)

    if False: # For Lint
        scene v16s50a_aubpost1
        with dissolve

    # -MC is asleep in bed, only his bottom half under the covers. He opens his eyes. (Even if baby is there, it's not in shot)-
    
    if joinwolves: # Wolf
        scene v16s50a_11 # TPP Close up MC (neutral expression, mouth closed, eyes closed) sleeping in bed [WOLF ROOM]
    else:
        scene v16s50a_1 # TPP Close up MC (neutral expression, mouth closed, eyes closed) sleeping in bed [APE ROOM]
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s50a_11a # TPP Close up MC (neutral expression, mouth closed, eyes open) sleeping in bed [WOLF ROOM]
    else:
        scene v16s50a_1a # TPP Close up MC (neutral expression, mouth closed, eyes open) sleeping in bed [APE ROOM]
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s50a_12 # TPP MC (no expression, mouth closed) siting on the edge of his bed near his nightstand (phone on the nightstand). [WOLF ROOM]
    else:
        scene v16s50a_2 # TPP MC (no expression, mouth closed) siting on the edge of his bed near his nightstand (phone on the nightstand). [APE ROOM]
    with dissolve

    pause 0.75

    # -if MC has the baby by himself

    if ((v16s27_mc_baby_schedule["wednesday"] == BabyDuty.ALONE and v16s50a_dotw == 5) or (v16s27_mc_baby_schedule["thursday"] == BabyDuty.ALONE and v16s50a_dotw == 6) or (v16s27_mc_baby_schedule["friday"] == BabyDuty.ALONE and v16s50a_dotw == 7)):
        if joinwolves:       
            scene v16s50a_12a # TPP MC (smile, mouth closed) siting on the edge of his bed near his nightstand (phone on the nightstand), raising his arms in victory [that made it through the night with a baby] [WOLF ROOM]
        else:
            scene v16s50a_2a # TPP MC (smile, mouth closed) siting on the edge of his bed near his nightstand (phone on the nightstand), raising his arms in victory [that made it through the night with a baby] [APE ROOM]
        with dissolve
            
        u "(I survived the night!)"

        if joinwolves:
            scene v16s50a_12b # TPP MC (smile, mouth closed) siting on the edge of his bed near his nightstand (phone on the nightstand) in his bed. [WOLF ROOM]
        else:
            scene v16s50a_2b # TPP MC (smile, mouth closed) siting on the edge of his bed near his nightstand (phone on the nightstand) in his bed. [APE ROOM]
        with dissolve

        u "(I can leave [v16_baby_name] here. Someone will let my partner come in to collect it.)"            

    # -Regardless of who had the baby-

    if v16s50a_dotw == 5: # -if Thursday morning [Checkpoint 1.1] Outfit 2 
        if joinwolves:
            scene v16s50a_13 # TPP MC (no expression, mouth closed) siting on the edge of his bed near his nightstand reaching for his phone on the nightstand. [WOLF ROOM]
        else:
            scene v16s50a_3 # TPP MC (no expression, mouth closed) siting on the edge of his bed near his nightstand reaching for his phone on the nightstand. [APE ROOM]
        with dissolve

        pause 0.75
            
        # -MC looks at his phone, checking the time-
        if joinwolves:
            scene v16s50a_13a # TPP MC (no expression, mouth closed) siting on the edge of his bed near his nightstand looking at his phone in his hand. [WOLF ROOM]
        else:
            scene v16s50a_3a # TPP MC (no expression, mouth closed) siting on the edge of his bed near his nightstand looking at his phone in his hand. [APE ROOM]
        with dissolve
            
        u "(Ah, good. It's still early. Plenty of time to get to the dog shelter...)"

        # -MC gets up, gets dressed and heads out-
        if joinwolves:
            scene v16s50a_14 # TPP MC (no expression, mouth closed) putting on shirt, wearing bottoms of outfit 2 [WOLF ROOM]. 
        else:
            scene v16s50a_4 # TPP MC (no expression, mouth closed) putting on shirt, wearing bottoms of outfit 2 [APE ROOM]. 
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s50a_14a # TPP MC (no expression, mouth closed) fully dressed (outfit 2) and exiting through the open door of his room [WOLF ROOM].
        else:
            scene v16s50a_4a # TPP MC (no expression, mouth closed) fully dressed (outfit 2) and exiting through the open door of his room [APE ROOM].
        with dissolve

        pause 0.75

        # -Transition to Scene 51-
        jump v16s51

    elif v16s50a_dotw == 6: # -if Friday morning [Checkpoint 1.2] Outfit 5 
        # -MC's phone vibrates. He looks at his phone to see a text from Penelope-
        
        if joinwolves:
            scene v16s50a_12
        else:
            scene v16s50a_2
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        if joinwolves:
            scene v16s50a_13
        else:
            scene v16s50a_3
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s50a_13a
        else:
            scene v16s50a_3a
        with dissolve
            
        pause 0.75
            
        $ penelope.messenger.newMessage("Morning! Come meet me at the Dean's office? I'm looking after her new dog!", force_send=True)
        $ penelope.messenger.addReply("You're looking after Oscar?")
        $ penelope.messenger.newMessage("Yeah, that's his name. Come!")
        $ penelope.messenger.addReply("Okay, be there a min")
        $ penelope.messenger.newMessage("Yay! :)")

        label v16s50a_phone_continue:
            if penelope.messenger.replies:
                call screen phone
            if penelope.messenger.replies:
                u "I should reply to Penelope."
                jump v16s50a_phone_continue

        # -MC gets dressed and exits the room-

        if joinwolves:
            scene v16s50a_14c # TPP MC (no expression, mouth closed) putting on shirt, wearing bottoms of outfit 5 [WOLF ROOM]. 
        else:
            scene v16s50a_4c # TPP MC (no expression, mouth closed) putting on shirt, wearing bottoms of outfit 5 [APE ROOM]. 
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s50a_14d # TPP MC (no expression, mouth closed) fully dressed and exiting through the open door of his room [WOLF ROOM].
        else:
            scene v16s50a_4d # TPP MC (no expression, mouth closed) fully dressed and exiting through the open door of his room [APE ROOM].
        with dissolve

        pause 0.75
            
        # -Transition to Scene 70-
        jump v16s70


    else: # -if Saturday morning [Checkpoint 1.3] Outfit 1
        # -MC looks at his phone, checking the date-
        if joinwolves:
            scene v16s50a_13
        else:
            scene v16s50a_3
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s50a_12c # TPP MC (smile, mouth closed) siting on the edge of his bed near his nightstand, raising his arms in victory with phone in the hand. [WOLF ROOM]
        else:
            scene v16s50a_2c # TPP MC (smile, mouth closed) siting on the edge of his bed near his nightstand, raising his arms in victory with phone in the hand. [APE ROOM]
        with dissolve

        u "(That was the last baby night, nice. No more crying I'm free!)"
                
        # -MC gets up, gets dressed and heads out-

        if joinwolves:
            scene v16s50a_14e # TPP MC (no expression, mouth closed) putting on shirt, wearing bottoms of outfit 1 [WOLF ROOM].
        else:
            scene v16s50a_4e # TPP MC (no expression, mouth closed) putting on shirt, wearing bottoms of outfit 1 [APE ROOM].
        with dissolve

        pause 0.75

        if joinwolves:
            scene v16s50a_14f # TPP MC (no expression, mouth closed) fully dressed (outfit 1) and exiting through the open door of his room [WOLF ROOM].
        else:
            scene v16s50a_4f # TPP MC (no expression, mouth closed) fully dressed (outfit 1) and exiting through the open door of his room [APE ROOM].
        with dissolve

        pause 0.75

        if joinwolves:
            jump v16s83
        else:
            jump v16s84