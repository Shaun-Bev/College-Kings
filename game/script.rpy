define config.enable_steam = False
define config.developer = True
define config.console = True
define config_debug = False
define config_censored = False

define config.version = get_version("14.9.0{}".format("s" if config.enable_steam else ""))

define config.steam_appid = 1463120

define config.gl2 = True
define _quit_slot = "99-1"


# The game starts here.
label start:
    # Get Animation/Transform List
    show no_hard_feelings at achievementShow
    $ achievementAtList = renpy.get_at_list("no_hard_feelings")
    hide no_hard_feelings

    python:
        v15_nora_clues.add(Clue("Keys", "images/v15/detective_board/keys.png"))
        v15_nora_clues.add(Clue("Diary", "images/v15/detective_board/diary.png"))
        v15_nora_clues.add(Clue("Earring", "images/v15/detective_board/earring.png"))
        v15_nora_clues.add(Clue("Broken Bottle", "images/v15/detective_board/broken_bottle.png"))
        v15_nora_clues.add(Clue("Message", "images/v15/detective_board/message.png"))
        v15_nora_clues.add(Clue("Phone Number", "images/v15/detective_board/phone_number.png"))
        v15_nora_clues.add(Clue("Unknown", "images/v15/detective_board/unknown.png"))
        v15_nora_clues.add(Clue("Unknown", "images/v15/detective_board/unknown.png"))
        v15_nora_clues.add(Clue("Unknown", "images/v15/detective_board/unknown.png"))
        v15_nora_clues.add(Clue("Unknown", "images/v15/detective_board/unknown.png"))

        v15_nora_locations.add(Location("Dock", "images/v15/detective_board/dock.png"))
        v15_nora_locations.add(Location("Oldest Boulangerie", "images/v15/detective_board/oldest_boulangerie.png"))
        v15_nora_locations.add(Location("Old Mansion", "images/v15/detective_board/old_mansion.png"))
        v15_nora_locations.add(Location("Sewers", "images/v15/detective_board/sewers.png"))
        v15_nora_locations.add(Location("Club", "images/v15/detective_board/club.png"))
        v15_nora_locations.add(Location("Suburb", "images/v15/detective_board/suburb.png"))
    

    #call screen detective_board
    call screen real_life_mode

label end_credits: # for compatibility
label gameEnd:
    stop music fadeout 3
    play music "music/vocal.mp3"

    call screen end_screen

label credits:
    show credits:
        ypos 50
        xalign 0.5

    call screen credits
