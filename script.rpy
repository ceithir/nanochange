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

define d = Character("The Devil")
define o = Character("Officer")
define a = Character("Anna")
define m = Character("Mephisto")
define z = Character("Zelda")

image bg soft_white = Solid("#F5F5F5")
image bg black = Solid("#000")

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

label start:
    d "Late, sorry. Traffic was a nightmare. Snow everywhere, the highway closed…"
    o "Yeah, yeah, we know, same for everyone. You're the only senior officer who happens to be there today actually."
    d "That means I'm going to get all the worst cases, ain't I?"
    o "Indeed. First-degree murder. Here's the file. The suspects are already waiting for you in the interrogation room."
    d "Have pity of me and make them wait 10 more minutes, time to read that and get a coffee."

    "The officer agrees, but I'm sadly forced to renounce to the second part of the plan. The old-school percolator is empty and I don't have enough time to prepare a new batch of hot liquid energy."
    "To add insult to my withdrawal symptoms, today's affair is coffee related. As in, someone got killed in a coffee shop."

    window hide

    scene bg soft_white with dissolve
    nvl show dissolve

    $ show_notes = True
    $ new_notes = True

    nvl_narrator """
    {a=notes}Some guy{/a}, not formally identified yet (only anonymous id* on him), died from ingesting a coffee spiced with a {a=notes}high quantity of common medical drugs{/a}.

    \"Poor man's poison\" as the coroner called it: Anything you can usually found in a medicine cupboard mixed together at once.

    Death after consumption was pretty quick due to the victim already being alcoholized at that time and drugs and alcohol violently reacting together.

    Analysis of the liver seems to indicate the victim was a alcoholic°. Probable* use of a heavy hepatic-support program°, and therefore of few or none other programs*.

    {clear}

    Suicide is a valid hypothesis, but so is murder.

    In the latter case, the barista, registered as Anna°, is the most likely suspect. She had every opportunity to pour the deadly cocktail into the cup.

    However, the victim didn't go to the counter himself to fetch the drink. Instead, it was the woman he was sharing a table with (identifier: Zelda°) who got it, and brought it back alongside her own order.

    She could have slip the drug on her way, or even back at the table, while the man was looking elsewhere.

    {clear}

    According to several different witnesses (two other employees and a bored regular waiting for someone late), another man also went to the victim's table shortly after the deadly coffee was delivered.

    They had a short but lively conversation, then this person left the restaurant. A short window of opportunity, but an existing one.

    The same cannot be proved for any other person present at the shop that day. It's not totally impossible that someone else had such an opportunity, but there's no witness of it, so my dear colleagues have decided to focus their attention on those three.

    {clear}

    Anna and Zelda have already been interrogated one time, through superficially, alongside every other present at the shop when the cops came in. They were then escorted here for a more thorough investigation.

    The mysterious man, named* Mephisto°, is a faithful customer, and someone in the staff had his number. He has answered positively to the gentle but firm request to come at the station for questioning.
    """

    nvl hide dissolve
    scene bg black with dissolve

    "So, three suspects, or at least witnesses, currently kept alone with their thoughts in individual room, waiting for someone, anyone, to talk to them."

    "Which one do I want to relieve first?"

    jump choose_your_suspect

default anna_introduction = False
default mephisto_introduction = False
default zelda_introduction = False

default mephisto_disabled = False
default anna_disabled = False

default know_outis_name = False
default know_mephisto_job = False
default know_outis_query = False
default know_zelda_job = False
default seen_drawings = False
default know_outis_job = False
default know_anna_talked_to_outis = False
default anna_name = False
default know_photo_girl = False
default photo_inconsistency = False
default heard_mephisto_betrayal = False
default know_mephisto_waited = False
default heard_mephisto_request = False
default mephisto_false_request = False
default know_mephisto_heard_zelda = False
default hint_about_outis_target = False
default not_a_doors = False
default vulpem = False
default mephisto_confession = False
default anna_confession = False

menu choose_your_suspect:
    "Anna the employee" if not anna_disabled:
        if not anna_introduction:
            $ anna_introduction = True
            jump anna_introduction
        else:
            jump anna_questions
    "Mephisto the regular" if not mephisto_disabled:
        if not mephisto_introduction:
            $ mephisto_introduction = True
            jump mephisto_introduction
        else:
            jump mephisto_questions
    "Zelda the customer":
        if not zelda_introduction:
            $ zelda_introduction = True
            jump zelda_introduction
        else:
            jump zelda_questions
    "THINK (debug)":
        jump deductions

menu deductions:
    "Reshaping + Drawings" if know_outis_query and seen_drawings and not know_outis_job:
        $ know_outis_job = True
        jump identity_tracker_reveal
    "Identity tracker + Photo" if know_outis_job and know_photo_girl and not photo_inconsistency:
        $ photo_inconsistency = True
        jump photo_inconsistency
    "Mephisto behavior + Mephisto testimony" if know_mephisto_waited and heard_mephisto_request and not mephisto_false_request:
        $ mephisto_false_request = True
        jump mephisto_false_request
    "Photo + Zelda testimony" if know_photo_girl and hint_about_outis_target and not not_a_doors:
        $ not_a_doors = True
        jump not_a_doors
    "Nothing for now":
        jump choose_your_suspect

label identity_tracker_reveal:
    """
    So…

    Asking in-depth questions about deep nanoreshaping…

    Commissioning artistic visions of what someone could look like after very specific series of transformations…

    Seems like the victim was trying to determine the current appearance of someone having undergone an integral transformation.

    In other words, he was an identity tracker*°.

    What's the saying again?

    {i}Among the muckrakers, no one is hated as much as the identity tracker{/i}?

    {i}In the renaissance age of privacy, the identity tracker is a sin of the past sniffing out past sins{/i}?

    Nevertheless, the answer I'm trying to unearth is probably related to the victim's occupation.

    And maybe to who he was was he trying to found. And why.

    He could have been an independent tracker, searching for some lucrative scandal. In that case, the girl in the photo should be famous, rich, or from a famous or rich family.

    But he could as well be working under contract. Finding track of someone someone else has lost sight of against a great deal of money.

    And in your line of duty, the sponsor of such searches if more often than not a mafioso seeking for a bad payer or a traitor to the family.
    """

    jump deductions

label photo_inconsistency:
    "You can never be 100% sure, but looks like the girl in the photo is indeed Phoenix Door."

    "A girl who never discarded her identity° at all. So why would an identity tracker focus his efforts on her."

    jump deductions

label mephisto_false_request:
    """
    There's obviously something more to Mephisto's little scene.

    He claims he just wanted to ask for his money, yet he waited patiently in his own corner while his debtor was alone at his table, before suddenly jumping to his throat just after he got his coffee.
    """

    jump deductions

label not_a_doors:
    """
    No, you couldn't find anyone in the Doors family matching the description from Outis.
    """

    if not anna_puzzle:
        """
        Maybe you should ask Anna about this. She seems surprisingly resourceful at identifying persons from the upper class with very little information.
        """

    jump deductions

