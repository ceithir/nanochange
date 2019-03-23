define z = Character("Zelda", who_color="#ffde4b")

image zelda = im.Crop("zelda.png", (55, 75, 480, 700))

default zelda_testimony = False
default zelda_drawings = False
default zelda_identity_tracking = False
default zelda_anna = False
default zelda_mephisto = False
default zelda_truer_conversation = False
default zelda_latin = False

label zelda_introduction:
    "To do after character design is done"
    jump zelda_questions

label zelda_questions:
    show zelda at center

    menu:
        "Tell me what happened." if not zelda_testimony:
            $ zelda_testimony = True
            $ know_zelda_job = True
            $ know_outis_name = True
            jump zelda_testimony
        "Did you notice anything unusual with the staff?" if zelda_testimony and not zelda_anna:
            $ zelda_anna = True
            jump zelda_anna
        "Let's focus on the person who disturbs your conversation." if zelda_testimony and not zelda_mephisto:
            $ zelda_mephisto = True
            $ heard_mephisto_betrayal = True
            jump zelda_mephisto
        "Tell me more about Outis job proposal." if zelda_testimony and not zelda_drawings:
            $ zelda_drawings = True
            $ seen_drawings = True
            jump zelda_drawings
        "Ever wondered about Outis' motives?" if know_outis_job and not zelda_identity_tracking:
            $ zelda_identity_tracking = True
            jump zelda_identity_tracking
        "Seems like your discussion with Outis was heated." if know_mephisto_heard_zelda and not zelda_truer_conversation:
            $ zelda_truer_conversation = True
            $ hint_about_outis_target = True
            jump zelda_truer_conversation
        "{i}Vulpem pilum mutat, non mores.{/i}" if vulpem and not zelda_latin:
            $ zelda_latin = True
            jump zelda_latin
        "No more questions.":
            jump choose_your_suspect

label zelda_testimony:
    z """
    I think it all started last Tuesday.

    I was working on my personal projects when I received a message about a potential commission, from a person using the alias Outis*.

    He wanted a realistic portrait. Not necessarily my forte, but I wasn't going to refuse a paid gig.

    As his requirements were complex, and we were living in the same city, I agreed, perhaps foolishly, to meet him face to face to discuss the matter further.

    Fast forward to this morning. I'm early, he's not, I'm getting some paperwork done while enjoying a cup of coffee.

    Finally, he comes in, salutes me, orders a coffee, and we get to talk about his project.

    Soon, his coffee is ready, I go fetch it, and a new one for myself while I'm at it.

    I'm barely back that another customer walks straight to us, and starts arguing crassly with Outis. He answers similarly, and the man runs away in rage.

    I'll never know what this was all about, as Outis then drank his coffee, and Hell's gates opened.

    I guess you already saw men dying in your line of duty. Me never before this day. That was even more horrible than anything I could have imagined.

    He looked sick, then in pain, then he felt from his seat. People tried to help him, but life just slowly exited his body a bit more with each passing instant.

    I cannot describe it with words. I haven't known this man for more than a few minutes, so I didn't really feel grief.

    But the swiftness with which death took him away… That's some terrifying shit for sure.
    """

    jump zelda_questions

label zelda_drawings:
    z """
    He provided me with a set of photos of some person, and asked me to imagine, and draw, what they would look like with a few more years, different hair and eye color, alternative skin tone, subtle changes in bone structure etc.

    It was all very strict. He had made several lists, each with a precise combination of transformations that he wanted to see applied.
    """

    d "And what did the results looked like?"

    z "Nothing like anyone I know, and nothing like anyone that was in the café today, if that's what you want to know. I have some of the sketches with me if you want to see them."

    d "Please do. Any hint can be relevant."

    # Transition

    """
    The half-dozen of rough drawings show unknown, but surprisingly diverse, visages.

    Facial features are heavily different from one image to the next, a full gradient from smoothness to hardness, light to dark.

    There's also a photo, from what looks like a posh long-haired highschooler.
    """

    d "Are they all supposed to be slight variations of the same girl?"

    z "Yeah. All the changes were minor, but the lists were very long."

    jump zelda_questions

label zelda_identity_tracking:
    z "Oh, I think he was a facade for a rich girl wanting to know beforehand what she would like after a full makeover."

    d "Do you believe that?"

    z "Not strongly. But as long as I have at least one innocent explanation available, I can accept that kind of job without my conscience ringing too strongly."

    d "And what are your less innocent theories?"

    z "When someone asks for what is basically a facial composite, I tend to get the idea they are trying to catch someone."

    d "And what's your opinion on identity trackers then?"

    z "Everyone got to make a living. Blame capitalism, not me."

    jump zelda_questions

label zelda_anna:
    z "Not really. Average employees of an average shop."

    d "Did you interact with any of them?"

    z "Just the girl that made my coffee. We had a short yet deep philosophical discussion about how cold and how snowy it is."

    d "Did she say or do anything special?"

    z """
    From what I could see, she did not put anything strange into Outis' coffee, nor did she do anything outstanding.

    Frankly, I even remember finding her a bit bland.
    """

    jump zelda_questions

label zelda_mephisto:
    z """
    I don't know if there is really anything I can add about that man.

    He was there when I arrived, behind his computer, focused on his work.

    I wondered if he could be Outis, but he did not match the description my client had sent me.

    After that I forgot about his existence until the incident.
    """

    d "What did he say exactly?"

    z "Bad words mainly. The lexical field was of lies, lack of honor, and breach of confidence."

    d "He accused Outis of having betrayed his trust?"

    z "Maybe. Was really hard to understand without context."

    d "And what did Outis answer?"

    z "He did not. He just asked impolitely of his accusatory to go somewhere else do something else."

    d "And then?"

    z "The man gave up and departed angrily."

    jump zelda_questions

label zelda_truer_conversation:
    z "You never worked as a freelancer, did you? Client always complains about everything, comparing your work not what he asked, but what he imagined."

    d """
    That may be true, but other people's testimonies that particular conversation went far beyond that.

    You talked about plausible deniability before, but it is becoming obvious you were far too involved for that.
    """

    "For just one second, she stands silent, weighting her options."

    z "Fine. Maybe Outis was suggesting he had some big catch at the end of his line, and it would be in my best financial interest to keep working for him."

    d "Details, please."

    z """
    Some girl. Rich, prestigious, family. Public image thoroughly controlled. Lots of skeletons in the closet.

    He was tracking a minor flaw in the storytelling of a rich, prestigious, family. You know, the kind with a thoroughly controlled public image, and a whole cemetery in the closet.

    One of their owns had been slowly fading away from their official propaganda through time. At first, she was quite prominent in the glossy pictures, then her appearances became scarce and into the background, until she entirely vanished.

    And, according to Outis' expertise, she was showing signs of using some heavy reshaping mod in her last pictures. The changes in her bone structure were quite clear in that regard he said.

    And he was trying to convince me that, from this tenuous lead, he had almost discovered everything that happened, and that, with just a little extra push, he could get a lot of money either from the girl or her family.

    He did not drop any name, so, for all I know, he could be lying out of his buttocks.
    """

    d "And what would have been your role in his scheme?"

    z """
    Unclear. I think he was trying to get an idea of what the chimera he was chasing looked like at different stages of her life, so he could determine the details of what had happened.

    Honestly, I brand him as a completely delusional, mostly harmless, man. I do not think he would have succeeded at discovering anything money-worthy.

    But I was still trying to get paid for the work already done, so I needed to keep the conversation going by playing his game, on the surface at least.
    """

    jump zelda_questions

label zelda_latin:
    # Change in expression

    z "What?"

    d "Just testing a theory."

    jump zelda_questions

