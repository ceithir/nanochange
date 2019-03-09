label zelda_introduction:
    "To do after character design is done"
    jump zelda_questions

default zelda_testimony = False

menu zelda_questions:
    "Tell me what happened." if not zelda_testimony:
        $ zelda_testimony = True
        $ know_zelda_job = True
        $ know_outis_name = True
        jump zelda_testimony
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

