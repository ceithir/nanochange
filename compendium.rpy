default show_notes = False

default quick_death = False
default alcoholic = False
default anna_suspect = False
default mephisto_suspect = False
default zelda_suspect = False
default zelda_wait = False
default outis_mephisto_acquaintance = False
default outis_sober = False
default outis_perfume = False
default pulcinella = False
default mephisto_aggressive = False
default bobson = False
default mephisto_outis_money = False
default mephisto_job_details = False
default anna_fitting = False
default outis_journalism = False
default fairies = False
default go_rainbow = False
default heightened_senses = False
default nanolimits = False

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
                if anna_suspect:
                    frame:
                        if who == "Anna":
                            text "The Employee" at truecenter
                        else:
                            textbutton "The Employee" action Show("notes", who="Anna") at truecenter
                if mephisto_suspect:
                    frame:
                        if who == "Mephisto":
                            text "The Regular" at truecenter
                        else:
                            textbutton "The Regular" action Show("notes", who="Mephisto") at truecenter
                if zelda_suspect:
                    frame:
                        if who == "Zelda":
                            text "The Customer" at truecenter
                        else:
                            textbutton "The Customer" action Show("notes", who="Zelda") at truecenter

            fixed:
                style_prefix "notes"
                vbox:
                    if who == "Outis":
                        if know_outis_name:
                            text "Name: Outis":
                              if what == "name":
                                style "notes_highlight"
                        else:
                            text "Name: Unknown":
                                if what == "name":
                                    style "notes_highlight"
                        if know_outis_job:
                            if outis_journalism:
                                text "Occupation: {s}Journalist{/s} Identity tracker":
                                    if what == "job":
                                        style "notes_highlight"
                            else:
                                text "Occupation: Identity tracker":
                                    if what == "job":
                                        style "notes_highlight"
                        elif outis_journalism:
                            text "Occupation: Journalist?":
                                if what == "job":
                                    style "notes_highlight"
                        text "Cause of death: Poisoned with basic meds":
                            if what == "poison":
                                style "notes_highlight"
                        if alcoholic:
                            text "Mods: Reinforced liver":
                                if what == "mod":
                                    style "notes_highlight"
                        if quick_death:
                            text "Poison acted quicker than it should have due to high alcohol consumption.":
                                if what == "quick_death":
                                    style "notes_highlight"
                        if alcoholic:
                            if outis_sober:
                                text "Alcoholic. Tried to hide it. People were not fooled.":
                                    if what == "alcoholic":
                                        style "notes_highlight"
                            else:
                                text "Alcoholic.":
                                    if what == "alcoholic":
                                        style "notes_highlight"
                            if outis_perfume:
                                text "Extra effort to dissimulate his alcohol problem today.":
                                    if what == "perfume":
                                        style "notes_highlight"
                        if know_photo_girl:
                            if photo_inconsistency:
                                text "Was investigating… Phoenix Doors? → Makes no sense?":
                                    if what == "phoenix":
                                        style "notes_highlight"
                            else:
                                text "Was investigating… Phoenix Doors?":
                                    if what == "phoenix":
                                        style "notes_highlight"
                        if know_outis_query and not know_outis_job:
                            text "Was investigating… sloughing?"

                    if who == "Anna":
                        text "Name: Anna"
                        text "Occupation: Coffee shop employee"
                        text "Prepared the cup that was ultimately poisoned."
                        if anna_fitting:
                            text "Extra efforts to blend in with the crowd.":
                                if what == "fitting":
                                    style "notes_highlight"
                        if know_anna_talked_to_outis:
                            text "Was pestered by Outis.":
                                if what == "outis_attention":
                                    style "notes_highlight"

                    if mephisto_suspect:
                        if who == "Mephisto":
                            text "Name: Mephisto"
                            if know_mephisto_job:
                                text "Occupation: Biohacker."
                            if heightened_senses:
                                text "Enhanced senses.":
                                    if what == "heightened":
                                        style "notes_highlight"
                            text "Had an altercation with the victim very shortly before his death."
                            if outis_mephisto_acquaintance:
                                text "Was an acquaintance of the victim.":
                                    if what == "acquaintance":
                                        style "notes_highlight"
                            if mephisto_outis_money:
                                text "The victim was owing him money.":
                                    if what == "outis_debt":
                                        style "notes_highlight"
                            if mephisto_aggressive:
                                text "Unusually aggressive today.":
                                    if what == "aggressive":
                                        style "notes_highlight"

                    if zelda_suspect:
                        if who == "Zelda":
                            text "Name: Zelda"
                            if know_zelda_job:
                                text "Occupation: Artist"
                                if mephisto_job_details:
                                    text "Was working on an artist's impression of what a person could look like now.":
                                        if what == "portrait":
                                            style "notes_highlight"
                                else:
                                    text "Was working on a portrait for Outis.":
                                        if what == "portrait":
                                            style "notes_highlight"
                            text "Brought the deadly cup to the victim."
                            if zelda_wait:
                                text "Was within reach of the cup during its preparation.":
                                    if what == "counter":
                                        style "notes_highlight"
                            if know_mephisto_heard_zelda:
                                text "Deeper in Outis' schemes that she likes to pretend.":
                                    if what == "poker":
                                        style "notes_highlight"

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

style notes_highlight is notes_text:
    italic True

default show_encyclopedia = False

screen encyclopedia(what=None, scroll=0.0):
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
            viewport:
                draggable True
                mousewheel True
                arrowkeys True
                yinitial scroll
                style_prefix "encyclopedia"

                vbox:
                    if mephisto_suspect:
                        text "{b}About names{/b} The distinction between legal name, usage name and {i}nom de plume{/i} does not exist anymore. A person's name is whatever they choose to respond when asked about it, and people may answer to many different names depending on context.":
                            if what == "name":
                                style "encyclopedia_highlight"
                    text "{b}Anonymous ID{/b} A smart card in which are stored only information relevant to the rights of its owner (for example, if they are allowed to drive), but not their name, address, physical description or any other personal data. The method used to guarantee the authenticity of authorizations and ownership may vary, but is generally based upon advanced cryptography.":
                        if what == "anonymous_id":
                            style "encyclopedia_highlight"
                    if know_mephisto_job:
                        text "{b}Biohacker{/b} A programmer specialized in finding ways to circumvent the original limitations of standard nanomachines to have them perform tasks far beyond their original purpose. Their services can range from minor customization of programs written by other hackers to creating from scratch routines able to entirely replace complex surgical operations.":
                            if what == "biohacker":
                                style "encyclopedia_highlight"
                    if bobson:
                        text "{b}Bobson & Bobson{/b} Parent company of Biofresh™ and century-old pharmaceutical giant. Nowadays, the company is mainly known for its intensive lobbying, its abusive lawsuits and its numerous barely legal intimidation maneuvers, all meant to have the nanomachines' users pay them good money and conform to what they edict is proper use of their technology. Though they lost most of their edge after Pulcinella's Law was enacted, they still can ruin a given person's life if determined enough.":
                            if what == "bobson":
                                style "encyclopedia_highlight"
                    if fairies:
                        text "{b}Fairies{/b} Nickname of the common nanobots. A reference to how they were called in the ads for the Enchanted Beauty Mask™, the product for which they were originally created. Following the scandal of the Great Spread, and the reappropriation of the bots by their new hosts for diverse and unprecedented usages, the appellation has become somewhat ironic.":
                            if what == "fairies":
                                style "encyclopedia_highlight"
                    if go_rainbow:
                        text "{b}Go rainbow{/b} To willingly change one's identity. The idiom conveys the idea that the person both cut all ties with her previous live, and used all means available to craft a new one from a blank page.":
                            if what == "rainbow":
                                style "encyclopedia_highlight"
                    if know_outis_job:
                        text "{b}Identity tracker{/b} A private investigator specialized in tracking persons through names', locations' and appearances' changes, often breaching every single privacy law in the process.":
                            if what == "identity_tracker":
                                style "encyclopedia_highlight"
                    if alcoholic:
                        text "{b}Modular limit{/b} Hard limit to the number of operations nanomachines can operate simultaneously on a single body. This number is directly correlated to the number of bots into one's body, itself a function of numerous factors (nanomachines stop self-replicating as soon as they detect they're putting a strain on their host's metabolism). High-priority life-support mods are often configured to aim for this limit, disabling every other mod when enabled.":
                            if what == "mod_limit":
                                style "encyclopedia_highlight"
                    if alcoholic:
                        text "{b}My body, my business{/b} It is highly illegal (and barely technologically possible) for anyone, police included, to read the memory of other, dead or alive, people's nanomachines to try to determine which program they are or were running. Therefore, even in the context of a criminal investigation, experts can at best hazard prudent educated guesses. See also: Pulcinella Law.":
                            if what == "no_probing":
                                style "encyclopedia_highlight"
                    if nanolimits:
                        text "{b}Nanolaws of robotics{/b} Nickname of a set of instructions engraved deeply into the original \"Fairy\" model of nanobots, designed to be impossible to override and to protect their host against malicious usage. Since more than 99.99% of nanobots in use nowadays are a copy of that original model, due to them having self-replicating endlessly (the \"Great Spread\"), they still pretty much rule the entire biohacking community. They're often symbolically reduce to three commandments: 1. Bots cannot change one's body without the host's consent. 2. Only reversible changes are allowed. 3. The brain and the nervous system cannot be altered directly.":
                            if what == "nanolimits":
                                style "encyclopedia_highlight"
                    if pulcinella:
                        text "{b}Pulcinella's Law{/b} Also known as {i}Freedom through hypocrisy{/i} laws. A body of laws allowing anyone to use the nanomachines inside their own body as they see fit without technically breaking the patents of the Bodyfresh™ company. The trick is that having them run a unlicensed program is still illicit on paper, but the law enforces a strict ban on checking the bots' internal memory, making it impossible to prove the misdemeanor, and therefore for trials on those charges to end up with a guilty sentence. The world has been runninng on that absurd compromise for ten years now. See also: My body, my business.":
                            if what == "pulcinella":
                                style "encyclopedia_highlight"
                    if know_outis_query:
                        text "{b}Sloughing{/b} The act of discarding one's skin (as reptiles do). Also slang for a long series of nanomodifications designed to reshape entirely one's face and/or body, due to the metaphor of the person leaving behind their old appearance in the same way the snake gets rid of its used scales. Sloughing is the main reason any kind of appearance-based authentication has been obsoleted, even though a full sloughing can take years to complete.":
                            if what == "sloughing":
                                style "encyclopedia_highlight"

            textbutton "Close" action Hide("encyclopedia") at right

style encyclopedia_text:
    color "#000"
    justify True

style encyclopedia_viewport:
    xpos 15

style encyclopedia_vbox:
    spacing 10
    xsize 920

style encyclopedia_highlight is encyclopedia_text:
    italic True

init python:
    def new_hyperlink_styler(target):
        return hyperlink_styler(target)

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
            options = target.split(':')
            what = options[1]
            scroll = 0.0
            if len(options) > 2:
                scroll = float(options[2])
            renpy.show_screen("encyclopedia", what, scroll)
            renpy.restart_interaction()
        else:
            return hyperlink_function(target)

    style.default.hyperlink_functions = (new_hyperlink_styler, new_hyperlink_clicked, None)

