
label mephisto_introduction:
    "To do after character design is done"
    jump mephisto_questions

default mephisto_testimony = False
default mephisto_job = False
default mephisto_identity_tracking = False
default mephisto_outis = False
default mephisto_anna = False
default mephisto_photo = False
default mephisto_truer_motives = False

menu mephisto_questions:
    "Tell me what happened." if not mephisto_testimony:
        $ mephisto_testimony = True
        jump mephisto_testimony
    "Tell me as much as you can about the victim." if mephisto_testimony and not mephisto_outis:
        $ mephisto_outis = True
        $ know_anna_talked_to_outis = True
        $ know_outis_name = True
        jump mephisto_outis
    "What can you tell me about Anna?" if mephisto_testimony and not mephisto_anna:
        $ mephisto_anna = True
        jump mephisto_anna
    "Let's talk about your daily activities." if mephisto_testimony and know_mephisto_job and not mephisto_job:
        $ mephisto_job = True
        $ know_outis_query = True
        $ heard_mephisto_excuse = True
        jump mephisto_job
    "Ever met an identity tracker?" if know_outis_job and not mephisto_identity_tracking:
        $ mephisto_identity_tracking = True
        jump mephisto_identity_tracking
    "Show photo" if mephisto_testimony and seen_drawings and not mephisto_photo:
        jump mephisto_photo
    "Why did you wait?" if mephisto_false_request and not mephisto_truer_motives:
        $ mephisto_truer_motives = True
        jump mephisto_truer_motives
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

label mephisto_anna:
    m """
    The serving girl?

    I haven't interacted much with her, but from what I've seen, she's basically average.

    I was already a regular when she got hired, about two years ago I would say. Does this job cause it pays at least part of the bills, and does it well enough, but it's no really a lifelong passion of her.

    She's also often present at the café. I guess that's her main gig.
    """

    d "Nothing unusual at all?"

    "He takes a minute to think about your question."

    m """
    Well, sometimes, I feel like she's trying a bit too hard to fit in.

    For example, I once overheard a conversation between her and several of her colleagues where she was pretending to know about some popular band from ten years ago when it was painfully obvious she had no idea who they were.

    Likewise, she used to occasionally employ some pretty uncommon Latin idioms, then turn red as if she had said something terrible when someone raised an eyebrow in surprise. She's updated her speech pattern to get ride of them entirely.
    """

    d "You're quite observant aren't you?"

    m "Need to be for my job. Identifying bad clients early is a crucial part of it."

    jump mephisto_questions

label mephisto_truer_motives:
    m "Wait?"

    d "You didn't go to Outis when he entered the café. Nor did you while he was waiting alone. You only moved when he was about to drink his coffee."

    m """
    Oh. I can see how this may make me look suspicious.

    But the truth is more bland than that. From my seat, I could overhear some parts of their conversation.

    And, well, at that moment, Outis was dodging the issue of when he would pay her for her work.

    That made my blood boil, so I jumped in to placate him as a the untrustworthy man he is.

    He didn't really let me speak though, and quickly pushed me into true anger territory, a state in which I'm only able to babble pitifully.

    So I fled, not exactly proud of myself.
    """

    d "What did he say to you?"

    m """
    He was quite aggressively pretending not to know me. The whole virtue outraged act. Threw in a few insults about my mental state.

    Not very original, but quite efficient. Didn't know how to react at all except with anger.
    """

    d "Fine. But while we're at fixing your testimony, and now we've made clear you could hear what Zelda and Outis were saying, please tell me what they did say."

    m """
    I didn't hear {i}everything{/i}.

    But, yeah, maybe I've heard some bits…

    But you're going to be disappointed. They both were talking like someone else could be listening to them, only alluding to subjects, and never being explicit about them.

    However, I think that was more than mere care about privacy. They reminded me of two poker players with a bad hand, each trying to outbluff the other.

    From what I grasped, Outis was insinuating something very strongly. The word {i}reputation{/i} came back a few times.

    Zelda kept her cards close to her chests, asking piercing questions but never revealing her intentions.

    They had some drawings and photos in-between them. Couldn't say if they were arguments or apples of discord.

    The whole affair smelled of money, but they only broad the subject after their short break to get coffee.
    """

    d "And I thought they never succeeded at coding super-hearing."

    m """
    It's not that hard to program the nanomachines to improve the mechanical part of hearing.

    But it takes a lot of tedious training to make your brain properly use your new capacities. Cannot affect the nerves directly after all°, so you have the right reflexes the old way, through repetitions of exercises.

    That's why restoring hearing is easy with the current technology, but making it far better than average never caught on. But a few persons do have it.
    """

    "I do know that, but I let him showing off. A confident suspect is a talkative suspect."

    jump mephisto_questions

