define d = Character("Inspector", who_color="#952304", image="devil")
define o = Character("Officer")

image bg soft_white = Solid("#F5F5F5")
image bg black = Solid("#000")

image side devil = im.FactorScale(im.Flip(im.Crop("dem-neu.png", (45, 65, 510, 735)), horizontal=True), 0.5)
image side devil relaxed = im.FactorScale(im.Flip(im.Crop("dem-inq.png", (45, 65, 510, 735)), horizontal=True), 0.5)

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
    $ show_encyclopedia = True

    nvl_narrator """
    {a=notes:outis:name}Some guy{/a}, not formally identified yet (only {a=def:anonymous_id}anonymous id{/a} on him), died from ingesting a coffee spiced with a {a=notes:outis:poison}high quantity of common medical drugs{/a}.

    \"Poor man's poison\" as the coroner called it: Anything you can usually found in a medicine cupboard mixed together at once.
    """

    $ quick_death = True

    nvl_narrator """
    Death after consumption was pretty quick due to the victim already being alcoholized at that time and {a=notes:outis:quick_death}drugs and alcohol reacting{/a} violently to each other.
    """

    $ alcoholic = True

    nvl_narrator """
    Analysis of the liver seems to indicate the victim was a {a=notes:outis:alcoholic}alcoholic{/a}. {a=def:no_probing}Probable{/a} use of a {a=notes:outis:mod}heavy hepatic-support program{/a}, and therefore of {a=def:mod_limit}few or none other programs{/a}.

    {clear}

    Suicide is a valid hypothesis, but so is murder.
    """

    $ anna_suspect = True

    nvl_narrator """
    In the latter case, the barista, registered as {a=notes:anna}Anna{/a}, is the most likely suspect. She had every opportunity to pour the deadly cocktail into the cup.
    """

    $ zelda_suspect = True

    nvl_narrator """
    However, the victim didn't go to the counter himself to fetch the drink. Instead, it was the woman he was sharing a table with (identifier: {a=notes:zelda}Zelda{/a}) who got it, and brought it back alongside her own order.

    She could have slip the drug on her way, or even back at the table, while the man was looking elsewhere.

    {clear}

    According to several different witnesses (two other employees and a bored regular waiting for someone late), another man also went to the victim's table shortly after the deadly coffee was delivered.

    They had a short but lively conversation, then this person left the restaurant. A short window of opportunity, but a clearly existing one.

    Those three are supposedly the only ones who got close enough of the cup between the time it was prepared and its consumption, so my dear colleagues have decided to focus all of their attention on them.

    And, indeed, since no trace of poison was found anywhere else in the restaurant, except for a small, anonymous plastic bag lying on the floor that anyone could have thrown there during the confusion following the death, the logical razor would have that one of them is the culprit.

    At least, they're the most likely to give me any useful information on what happened.

    {clear}

    Anna and Zelda have already been interrogated one time, through superficially, alongside every other present at the shop when the cops came in. They were then escorted here for a more thorough investigation.
    """

    $ mephisto_suspect = True

    nvl_narrator """
    The mysterious man, {a=def:name}known{/a} as {a=notes:mephisto}Mephisto{/a}, is a faithful customer, and someone in the staff had his number. He has answered positively to the gentle but firm request to come at the station for questioning.
    """

    nvl hide dissolve
    scene bg black with dissolve

    "So, three suspects, or at least witnesses, currently kept alone with their thoughts in individual rooms, waiting for someone, anyone, to talk to them."

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
default heard_mephisto_excuse = False
default mephisto_false_request = False
default know_mephisto_heard_zelda = False
default hint_about_outis_target = False
default not_a_doors = False
default vulpem = False
default mephisto_confession = False
default anna_confession = False

label choose_your_suspect:
    scene bg black

    menu:
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

menu deductions:
    "Mephisto behavior + Mephisto testimony" if know_mephisto_waited and heard_mephisto_request and not mephisto_false_request:
        $ mephisto_false_request = True
        jump mephisto_false_request
    "Nothing for now":
        jump choose_your_suspect

label identity_tracker_reveal:
    scene bg black with fade

    """
    So…

    Asking in-depth questions about deep nanoreshaping…

    Commissioning artistic visions of what someone could look like after very specific series of transformations…

    Seems like the victim was trying to determine the current appearance of someone having undergone an integral transformation.
    """

    $ know_outis_job = True

    """
    In other words, {a=notes:outis:job}he{/a} was an {a=def:identity_tracker:0.5}identity tracker{/a}.

    What's the saying again?

    {i}Among the muckrakers, no one is hated as much as the identity tracker{/i}?

    {i}In the renaissance age of privacy, the identity tracker is a sin of the past sniffing out past sins{/i}?

    Nevertheless, the answer I'm trying to unearth is probably related to the victim's occupation.

    And maybe to who he was was he trying to found. And why.

    He could have been an independent tracker, searching for some lucrative scandal. In that case, the girl in the photo should be famous, rich, or from a famous or rich family.

    But he could as well be working under contract. Finding track of somebody someone else has lost sight of against a great deal of money.

    And in my line of duty, the sponsor of such searches is more often than not a mafioso seeking for a bad payer or a traitor to the family.

    Not someone the tracked went to meet. At any cost.
    """

    if know_photo_girl:
        jump photo_inconsistency
    elif know_mephisto_waited and not mephisto_false_request:
        jump mephisto_false_request
    else:
        jump choose_your_suspect

label photo_inconsistency:
    scene bg black with fade

    "You can never be 100\% sure, but looks like the girl in the photo is indeed Phoenix Door."

    $ go_rainbow = True
    $ photo_inconsistency = True

    "A girl who never {a=def:rainbow:0.5}went rainbow{/a} at all. So {a=notes:outis:phoenix}why{/a} would an identity tracker focus his efforts on her?"

    if hint_about_outis_target and not not_a_doors:
        jump not_a_doors
    elif know_mephisto_waited and not mephisto_false_request:
        jump mephisto_false_request
    else:
        jump choose_your_suspect

label mephisto_false_request:
    scene bg black with fade

    $ mephisto_false_request = True

    """
    There's obviously something more to Mephisto's little scene.

    He claims he just wanted to ask for his money, yet he waited patiently in his own corner while his debtor was alone at his table, before suddenly jumping to his throat just after he got his coffee.
    """

    jump choose_your_suspect

label not_a_doors:
    scene bg black with fade
    $ not_a_doors = True

    """
    No, you couldn't find anyone in the Doors family matching the description from Outis.
    """

    if not anna_puzzle:
        """
        Maybe you should ask Anna about this. She seems surprisingly resourceful at identifying persons from the upper class with very little information.
        """

    if know_mephisto_waited and not mephisto_false_request:
        jump mephisto_false_request
    else:
        jump choose_your_suspect

