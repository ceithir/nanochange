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
default anna_zelda = False
default anna_mephisto = False

default know_outis_name = False

label anna_questions:
    menu:
        "Tell me what happened." if not anna_testimony:
            $ anna_testimony = True
            $ know_outis_name = True
            jump anna_testimony
        "What can you tell me about Outis?" if know_outis_name and not anna_outis:
            $ anna_outis = True
            jump anna_outis
        "What can you tell me about Zelda?" if know_outis_name and not anna_zelda:
            $ anna_zelda = True
            jump anna_zelda
        "What can you tell me about Mephisto?" if know_outis_name and not anna_mephisto:
            $ anna_mephisto = True
            jump anna_mephisto
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

    d "Was he acting any different today from any other day?"

    a """
    Well, he had a girl with him. That's unusual enough. Though they didn't seem very close.

    I think he was wearing some extra perfume too. Maybe to turn on the charm, maybe to hide his usual wine smell.

    And I think that's all. Until the accident, everything else seemed as usual.
    """

    jump anna_questions

label anna_zelda:
    a "Who?"

    d "The girl that was with Outis."

    a "Today was the first time I've seen her."

    d "Well, then tell me what you've learned about her today."

    a """
    Well, she looks like an artist I guess? We're not the most hipster of cafés, but we do get some from time to time.

    She arrived early in the morning, ordered a simple coffee, then used her computer, alone at her table, for like half an hour before Outis arrived.

    She waved at him, and he went to join her. They discussed for some time without ordering anything more, then Outis came to the counter to ask for a coffee, and returned quickly to his seat.

    She came herself soon after, asked for a refill, did some small talk about the weather while she waited, and went back to their table with both cups.

    Overall, they looked more like they were negotiating than flirting.
    """

    jump anna_questions

label anna_mephisto:
    a """
    Mephisto is not there everyday, but it's as if.

    I think the café is his more or less his public office. Some people come just to speak to him.
    """

    d "Which kind of people?"

    a """
    Of all kinds actually. He's got quite the varied following. People of all ages, genders, colors.

    Though, thinking about it, I never saw anyone which looked like they had difficult ends of months discuss with him for long.
    """

    d "And for which reason was he that popular with the {i}bourgeoisie{/i}?"

    "I can see the cogs in her brain turn as she's trying to formulate a non-suspicious answer. May as well cut short her circumlocutions."

    d "Is he a dealer?"

    "She's taken aback for a second, then answers bluntly."

    a "No. But he is a biohacker*°."

    """
    I nod in understanding.

    Biohackers are in the gray zone of the law. What they do is technically illegal, but they're tolerated as long as they keep a plausible cover.

    It's all a consequence of that good old Pulcinella Law°.
    """

    d "Did he have an agreement with the shop?"

    a """
    More or less. We didn't ask questions, and he left generous tips.

    Had he brought disputable clients, maybe things would have been different. But his customer base was clean enough.
    """

    d "Do you know what services he offers exactly?"

    a "No. Curiosity killed the cat."

    d "And how was he acting today?"

    a """
    At the beginning, as usual, working on his computer on his usual seat.

    I remember finding very strange that he went to talk to Outis. Normally, he let people come to him, and never meddle with the other tables.

    And I found even stranger that he left immediately after. Usually, he stays in most of the day.
    """

    d "You're suspecting him, ain't you?"

    a """
    Wouldn't anyone? Though we thought he was harmless, he is an outlaw after all.
    """

    jump anna_questions

label debug_exit:
    return
