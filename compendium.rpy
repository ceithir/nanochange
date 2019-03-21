default show_notes = False
default new_notes = False

screen notes():
    tag notes
    zorder 1
    modal True

    frame:
        style_prefix "notes"
        xsize 960
        ysize 600
        xalign 0.5
        yalign 0.5
        background Solid("#f2eecb")

        vbox:
            hbox:
                yfill True
                vbox:
                    xsize 240
                    text "The Victim" style "notes_title"
                    if know_outis_name:
                        text "Name: Outis"
                    else:
                        text "Name: {i}Unknown{/i}"
                    text "Cause of death: Poisoned with basic meds"

                vbox:
                    xsize 240
                    text "The Employee" style "notes_title"
                    text "Name: Anna"

                vbox:
                    xsize 240
                    text "The Regular" style "notes_title"
                    text "Name: Mephisto"

                vbox:
                    xsize 240
                    text "The Customer" style "notes_title"
                    text "Name: Zelda"

            textbutton "Close" action Hide("notes") at right

style notes_text:
    color "#000"

style notes_vbox:
    spacing 10

style notes_title:
    color "#8b0000"
    xalign 0.5

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

