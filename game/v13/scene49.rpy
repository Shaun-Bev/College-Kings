# SCENE 49: Walking back with Aubrey
# Locations: Sidewalk, Hotel.
# Characters: AUBREY (Outfit: 4), MC (Outfit: 1) 
# Time: Evening

label v13s49:
    scene v13s49_1 # TPP. Show MC and Aubrey walking down the sidewalk, both slight smile, mouths closed.
    with dissolve

    pause 0.75

    scene v13s49_2 # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
    with dissolve

    au "Thanks for taking these pictures for me [name]. I'm gonna choose my favorite one and upload it right now."

    scene v13s49_2a # FPP. Same as v13s49_2, Aubrey looking at phone, Aubrey slight smile, mouth closed.
    with dissolve

    pause 0.75

# Haven't been taught how to do the Kiwii process.
# -Aubrey post one her pictures on Kiwii with the caption "Swimming Up The Ladder"

### ERROR: KiwiiPost("Aubrey, "Picture of Aubrey on the beach in Amsterdam", "Swimming up the ladder! #ScheveningenBeach", numberLikes=4218)
### ERROR: kiwiiPost.newComment("Imre", "Hot as fuck Aubrey!!")
### ERROR: kiwiiPost.newComment("Chloe", "This is the hottest pic I’ve ever seen of you! ="Aubrey")
### ERROR: kiwi Post.add Reply("Wow, they turned out great!")
### ERROR: kiwiiPost.addReply("Ah, beautiful. But even better in person ;)", mentions="Aubrey)
### ERROR: kiwiiPost.newComment("Aubrey", "Thank you! <3")
### ERROR: kiwiiPost.newComment("Naomi", "OMG! You look just like me! <3")

    scene v13s49_2b # FPP. Same as v13s49_2, (Aubrey's phone off camera), Aubrey slight smile, mouth closed.
    with dissolve

    u "Of course, anytime."

    scene v13s49_1a # FPP. Same as v13s49_1, Different location on the sidewalk.
    with dissolve

    pause 0.75

    scene v13s49_3 # FPP. MC and Aubrey in the hotel lobby, Aubrey slight smile, mouth open.
    with fade

    au "I'm gonna go put some clothes on."

    scene v13s49_3a # FPP. Same as v13s49_3, Aubrey slight smile, mouth closed.
    with dissolve

    u "Haha, you do that."

    scene v13s49_3b # FPP. Same as v13s49_3a, Show Aubrey walking away from MC.
    with dissolve

    if v13s48_ryan_double_date:
        scene v13s49_4 # FPP. Show Ryan walking up to MC, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v13s49_4a # FPP. Same as v13s49_4, Ryan standing in front of MC.
        with dissolve

        jump v13s50
  
    elif not v13s48_ryan_double_date and emily_europe:
        scene v13s49_5 # FPP. Show Emily walking up to MC, angry expression, mouth closed.
        with dissolve

        pause 0.75

        scene v13s49_5a # FPP. Same as v13s49_5, Emily standing in front of MC.
        with dissolve

        jump v13s51

    else:
        if chloegf:
            jump v13s52
        elif rileyrs:
            jump v13s53
        else:
            jump v13s54