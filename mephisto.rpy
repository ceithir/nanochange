
label mephisto_introduction:
    "To do after character design is done"
    jump mephisto_questions

default mephisto_testimony = False
default mephisto_job = False

menu mephisto_questions:
    "Tell me what happened." if not mephisto_testimony:
        $ mephisto_testimony = True
        jump mephisto_testimony
    "Let's talk about your daily activities." if mephisto_testimony and know_mephisto_job and not mephisto_job:
        $ mephisto_job = True
        $ know_outis_query = True
        jump mephisto_job
    "No more questions.":
        jump choose_your_suspect

label mephisto_testimony:
    m """
    I talked to a guy, that guy died shortly after, and now I'm obviously a suspect.

    Let me tell you this is all bad luck on my side.

    This guy was owing me money and has been avoiding me as of late.

    Since he was there for once, I took the opportunity to ask for my cash. When he tried to play dumb, I just ragequitted.
    """

    d "How much was he owing you?"

    "Not much. That was more for the principle of the thing."

    jump mephisto_questions

label mephisto_job:
    m "I work in computers for a living."

    d """
    That's certainly technically true, like everything you've told me so far.

    But I don't want prudent half-lies Mister Mephisto. I want you to help me with my investigation.

    As a senior police officer operating on a criminal affair, I'm entitled to give you a free pass on any minor breach of law you may have committed.

    And of course, your testimony will be anonymized.

    So stop playing around, and tell me what Outis really wanted of a popular biohacker.
    """

    m "I don't…"

    d "Please."

    "The nanospecialist shuts his mouth and remains silent for what feels an eternity."

    m "I want an official, written agreement that anything I could tell you won't bite me back in the ass."

    d "Sure, I'll fetch you that."

    # Transition

    "After reading the paper shield twice, he finally agrees to my terms."

    m """
    I've worked for Outis several times in the past. It was more or less an intriguing side-job of mine.

    You see, my usual work is more boring that it sounds.

    It's like 50\% repeated meetings with the customers to understand what they really want, 25\% tedious follow-up and attuning, 20\% recycling past code, and 5\% unexplored territories.

    Outis didn't want custom mods for himself. I'm sure he was using some, related to his alcohol problems, but I'm not the one who made them. Fixing livers is too complex for me.

    I'm frankly impressed by the gals who manage to build such programs. The bots weren't made for that°, you need some serious skills to have them perform that way.

    But I don't think you want to hear about my idols. Outis then.

    Guy was some sort of theoretician of nanomachines. He always had a billion questions, about what they could do and not do.

    When his interrogations were simple enough, I'ld humor him by answering him against a coffee. When they needed further research and experimenting on my side, I'ld have him pay me a small fee.

    As of late, he had been interested in total nanoreshaping°, with some pretty complex questions. Heavy stuff, needed quite a bit of time to find his answers, so I upped my fees.

    He had accepted my rates, but he must have overestimated the size of his wallet, cause I never got the money. Said he would pay me after some big event. I think he was trying to close a deal for a book or something like that.

    So today, since he couldn't escape without dumping his girl, I nicely asked for an update, he played dumb, I said some bad words, and decided to go elsewhere to cool down my head.
    """

    jump mephisto_questions
