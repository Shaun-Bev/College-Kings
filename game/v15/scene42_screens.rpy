screen detective_board():
    tag detective_board
    style_prefix "detective"

    default image_path = "images/v15/detective_board/"
    default clue_positions = {
        0: (263, 203),
        1: (460, 198),
        2: (657, 203),
        3: (170, 425),
        4: (370, 430),
        5: (570, 425),
        6: (770, 430),
        7: (220, 668),
        8: (420, 668),
        9: (620, 665),
    }

    add image_path + "background.png"

    for i, clue in enumerate(v15_nora_clues):
        frame:
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "clue_background.png"

            add clue.image align (0.5, 0.5)
            text clue.name xalign 0.5 ypos 195

    vpgrid:
        cols 3

        for location in v15_nora_locations:
            frame:
                xysize (203, 247)
                background image_path + "clue_background.png"

                add location.image xalign 0.5 ypos 20
                text location.name xalign 0.5 ypos 200

    button action Return()

style detective_text is text:
    font "fonts/RockSalt-Regular.ttf"
    size 20
    color "#191814"