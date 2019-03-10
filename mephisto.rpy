
label mephisto_introduction:
    "To do after character design is done"
    jump mephisto_questions

default mephisto_testimony = False
default mephisto_job = False
default mephisto_identity_tracking = False
default mephisto_outis = False
default mephisto_photo = False

menu mephisto_questions:
    "Tell me what happened." if not mephisto_testimony:
        $ mephisto_testimony = True
        jump mephisto_testimony
    "Tell me as much as you can about the victim." if mephisto_testimony and not mephisto_outis:
        $ mephisto_outis = True
        $ know_anna_talked_to_outis = True
        $ know_outis_name = True
        jump mephisto_outis
    "Let's talk about your daily activities." if mephisto_testimony and know_mephisto_job and not mephisto_job:
        $ mephisto_job = True
        $ know_outis_query = True
        jump mephisto_job
    "Ever met an identity tracker?" if know_outis_job and not mephisto_identity_tracking:
        $ mephisto_identity_tracking = True
        jump mephisto_identity_tracking
    "Show photo" if mephisto_testimony and seen_drawings and not mephisto_photo:
        jump mephisto_photo
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

label mephisto_identity_tracking:
    "He instantly tenses up."

    m """
    Being compromised with an identity tracker is one of my worst nightmares.

    You see, what most of my clients want above all is discretion. They really don't like the idea of anyone they don't know being aware of even their most minor or obvious transformations.

    And being associated with an identity tracker is basically telling the whole world that you're a greedy secret-seller.
    """

    d "Some must have approach you through the years."

    m "Of course. It's part of my job to to make it clear I won't ever work with them."

    d "What about Outis?"

    m """
    Do you have information that I don't have?

    But, yes, I was having doubts about him. He played the scholar quite well, but as of late, I found some of his questions far too much oriented.

    Actually, he stopped paying me about the time I started being more prudent in my words around him. Dunno if that's evidence against or in favor of him.
    """

    jump mephisto_questions

label mephisto_outis:
    m """
    Outis has been an irregular customer for as of late. As far as I remember, he never came just for a coffee, but always to discuss rather professionally with someone. The café was more or less his meeting room.
    """

    d "What kind of business was he doing there?"

    m """
    Journalism or research I guess. I remember him conducting interviews more than more than once. But I didn't hear enough of these conversations to grasp their subjects, and I didn't pry.
    """

    d "Anything else you can remember? Any remarkable habit for instance?"

    m "Well, I think he tried hitting on Anna a few times. At least, I remember her rebuffing him several times."

    jump mephisto_questions

label mephisto_photo:
    d "Could not tell me who this is?"

    "He stares at the photo for a full minute before answering."

    d "Sorry, but no. Would love to have her as client though, cause she seems loaded."

    jump mephisto_questions

