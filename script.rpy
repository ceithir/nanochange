# Main script file, to be split later on if need be

define d = Character("The Devil")
define o = Character("Officer")
define a = Character("Anna")

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

label choose_your_suspect:
    menu:
        "Anna the employee":
            if not anna_introduction:
                $ anna_introduction = True
                jump anna_introduction
            else:
                jump anna_questions
        "EXIT":
            jump debug_exit

label anna_introduction:
    "To do after character design is done"
    jump anna_questions

default anna_testimony = False
default anna_outis = False

label anna_questions:
    menu:
        "Tell me what happened." if not anna_testimony:
            $ anna_testimony = True
            jump anna_testimony
        "What can you tell me about Outis." if anna_testimony and not anna_outis:
            $ anna_outis = True
            jump anna_outis
        "No more questions.":
            jump choose_your_suspect

    jump choose_your_suspect

label anna_testimony:
    a """
    It was a slow day at work. Far less people than usual.

    You see, our usual customers are mainly people working nearby. But, with the snowstorm, they couldn't make it to work today. No work, no coffee before work.

    So, for most of the morning, they were more employees than customers in the shop, and everything was quiet.

    At some point, that guy came in. A semi-regular. Not here everyday, but comes frequently enough that I remember his face. Uses the alias Outis°.

    He asked for the flavor of the week, a Dark Latte Americano.

    The right machine hadn't been booted yet, so it took me a bit of time to prepare his order. Like five, maybe ten minutes?

    Didn't really check. As I said, the atmosphere was distressed. People took their time, nobody wanted to return into the cold fast.

    So, the girl he was with came to take his drink. A new face, never seen her before. She also ordered an extra espresso for herself, and waited at the counter while I made it.

    She went back to their table with both cups, I went back to dozing off.

    And then, he collapsed from his chair. Everyone rushed in. He was breathing very badly, suffocating. I tried to help him. Sam, the one in charge that day, called the emergency services, but neither I nor they could do anything.

    He just died, there, in my arms.
    """

    d "And what happened after?"

    a """
    I think the medics stormed in, then the cops. My mind's a blur. Everyone was asking me questions, and I couldn't answer any of them.

    And then, I ended up here, in this dark room, with you.
    """

    jump anna_questions

label anna_outis:
    a """
    There's not much I can tell you about this guy.

    I saw him for the first time about one month ago. Perhaps two actually. Time flies.

    After that, he came back about twice a week. Always ordering the coffee that was {i}à la mode{/i}.

    Often, he'll just drink it quickly. Sometimes, he would go for a quick chat with Mephisto°.

    Mephisto is that guy who's so often there we start worrying about his well-being when he doesn't show up for a few days.

    As for the elephant into the room… Yeah, the guy clearly had a problem with alcohol. He was more often than not smelling of it.

    Never actually ordered anything alcoholic in the café though. I think he was trying to hide his addiction.

    Probably was using mods to keep his mind clear, as he didn't act like a drunk man°.
    """

    jump anna_questions

label debug_exit:
    return
