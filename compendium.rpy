default show_notes = False
default new_notes = False

screen notes(who="Outis"):
    tag notes
    zorder 1
    modal True

    frame:
        xsize 960
        ysize 600
        xalign 0.5
        yalign 0.5
        background Solid("#f2eecb")

        vbox:
            hbox:
                style_prefix "notes_header"
                frame:
                    if who == "Outis":
                        text "The Victim" at truecenter
                    else:
                        textbutton "The Victim" action Show("notes", who="Outis") at truecenter
                frame:
                    if who == "Anna":
                        text "The Employee" at truecenter
                    else:
                        textbutton "The Employee" action Show("notes", who="Anna") at truecenter
                frame:
                    if who == "Mephisto":
                        text "The Regular" at truecenter
                    else:
                        textbutton "The Regular" action Show("notes", who="Mephisto") at truecenter
                frame:
                    if who == "Zelda":
                        text "The Customer" at truecenter
                    else:
                        textbutton "The Customer" action Show("notes", who="Anna") at truecenter

            fixed:
                style_prefix "notes"
                vbox:
                    if who == "Outis":
                        if know_outis_name:
                            text "Name: Outis"
                        else:
                            text "Name: {i}Unknown{/i}"
                        text "Cause of death: Poisoned with basic meds"

                    if who == "Anna":
                        text "Name: Anna"

                    if who == "Mephisto":
                        text "Name: Mephisto"

                    if who == "Zelda":
                        text "Name: Zelda"

            textbutton "Close" action Hide("notes") at right

style notes_text:
    color "#000"

style notes_vbox:
    spacing 10
    xpos 10
    ypos 10

style notes_header_text:
    color "#8b0000"

style notes_header_frame:
    xsize 240
    ysize 50
    background None

style notes_header_button_text:
    color "#000"
    hover_color "#551a8b"

init python:
    def new_hyperlink_styler(target):
        return hyperlink_styler(target)

    def new_hyperlink_hovered(target):
        return None

    def new_hyperlink_clicked(target):
        if target == 'notes':
            globals()["new_"+target] = False
            renpy.show_screen(target)
            renpy.restart_interaction()
        else:
            return hyperlink_clicked(target)

    style.default.hyperlink_functions = (new_hyperlink_styler, new_hyperlink_clicked, new_hyperlink_hovered)

