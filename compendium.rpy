default show_notes = False
default new_notes = False

screen notes(who="Outis", what=None):
    tag compendium
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
                            text "Name: Unknown":
                                if what == "name":
                                    style "notes_highlight"
                        text "Cause of death: Poisoned with basic meds":
                            if what == "poison":
                                style "notes_highlight"

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

style notes_highlight:
    color "#ff3232"
    italic True


default show_encyclopedia = False

screen encyclopedia(what=None):
    tag compendium
    zorder 1
    modal True

    frame:
        xsize 960
        ysize 600
        xalign 0.5
        yalign 0.5
        background Solid("#f2eecb")

        vbox:
            fixed:
                style_prefix "encyclopedia"
                vbox:
                    text "{b}Anonymous ID{/b}: TODO":
                        if what == "anonymous_id":
                            style "encyclopedia_highlight"

            textbutton "Close" action Hide("encyclopedia") at right

style encyclopedia_text:
    color "#000"

style encyclopedia_vbox:
    spacing 10
    xpos 10
    ypos 10

style encyclopedia_highlight:
    color "#000"
    italic True

init python:
    def new_hyperlink_styler(target):
        return hyperlink_styler(target)

    def new_hyperlink_hovered(target):
        return None

    def new_hyperlink_clicked(target):
        if target.startswith("notes"):
            globals()["new_notes"] = False
            options = target.split(':')
            if len(options) > 2:
                who = options[1].capitalize()
                what = options[2]
            elif len(options) == 2:
                who = options[1].capitalize()
                what = None
            else:
                who = "Outis"
                what = None
            renpy.show_screen("notes", who, what)
            renpy.restart_interaction()
        elif target.startswith("def"):
            [_, what] = target.split(':')
            renpy.show_screen("encyclopedia", what)
            renpy.restart_interaction()
        else:
            return hyperlink_clicked(target)

    style.default.hyperlink_functions = (new_hyperlink_styler, new_hyperlink_clicked, new_hyperlink_hovered)

