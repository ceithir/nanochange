define d = Character("The Devil")
define o = Character("Officer")
define a = Character("Anna")
define m = Character("Mephisto")
define z = Character("Zelda")

label start:
    d "Late, sorry. Traffic was a nightmare. Snow everywhere, the highway closed…"
    o "Yeah, yeah, we know, same for everyone. You're the only senior officer who happens to be there today actually."
    d "That means I'm going to get all the worst cases, ain't I?"
    o "Indeed. First-degree murder. Here's the file. The suspects are already waiting for you in the interrogation room."
    d "Have pity of me and make them wait 10 more minutes, time to read that and get a coffee."

    "The officer agrees, but I'm sadly forced to discard the second part of the plan. The old-school percolator is empty and I don't have time enough to prepare a new batch of hot liquid energy."
    "To add insult to my withdrawal symptoms, today's affair is coffee related. As in, someone got killed in a coffee shop."

    nvl_narrator """
    Some guy°, not formally identified yet (only anonymous id* on him), died from ingesting a coffee spiced with a high quantity of common medical drugs°.

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

    Anna and Zelda have already been interrogated one time, through superficially, alongside every other present at the shop when the cops came in. They were then escorted here for a more thorough investigation.

    The mysterious man, named* Mephisto°, is a faithful customer, and someone in the staff had his number. He has answered positively to the gentle but firm request to come at the station for questioning.
    """

    "So, three suspects, or at least witnesses, currently kept alone with their thoughts in individual room, waiting for someone, anyone, to talk to them."

    "Which one do I want to relieve first?"

    jump choose_your_suspect

default anna_introduction = False
default mephisto_introduction = False
default zelda_introduction = False

default know_outis_name = False
default know_mephisto_job = False
default know_outis_query = False
default know_zelda_job = False
default seen_drawings = False
default know_outis_job = False

menu choose_your_suspect:
    "Anna the employee":
        if not anna_introduction:
            $ anna_introduction = True
            jump anna_introduction
        else:
            jump anna_questions
    "Mephisto the regular":
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
    "EXIT (debug)":
        jump debug_exit

menu deductions:
    "Reshaping + Drawings" if know_outis_query and seen_drawings and not know_outis_job:
        $ know_outis_job = True
        jump identity_tracker_reveal
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

    jump choose_your_suspect

label debug_exit:
    return
