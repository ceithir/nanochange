define z = Character("Zelda", who_color="#ffde4b")

image zelda neutral = im.Crop("Ar-neu.png", (55, 75, 480, 700))
image zelda nervous = im.Crop("Ar-nerv.png", (55, 75, 480, 700))
image zelda disturbed = im.Crop("Ar-relie.png", (55, 75, 480, 700))

default zelda_testimony = False
default zelda_drawings = False
default zelda_identity_tracking = False
default zelda_anna = False
default zelda_mephisto = False
default zelda_truer_conversation = False
default zelda_latin = False

label zelda_introduction:
    show zelda neutral at center with fade

    "Zelda."

    "The wild card of this story. Nobody admits to knowing her and she was quite close to the victim when he died."

    jump zelda_questions

label zelda_questions:
    show zelda neutral at center

    menu:
        "Tell me what happened." if not zelda_testimony:
            $ zelda_testimony = True
            jump zelda_testimony
        "Did you notice anything unusual with the staff?" if zelda_testimony and not zelda_anna:
            $ zelda_anna = True
            jump zelda_anna
        "Let's focus on the man who disturbed your conversation." if zelda_testimony and not zelda_mephisto:
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
        "…" if mephisto_confession and not anna_confession:
            jump zelda_almost
        "You're some first-grade manipulative bitch, aren't you Seraphina?" if mephisto_confession and anna_confession:
                jump grand_finale
        "No more questions." if not mephisto_confession or not anna_confession:
            jump choose_your_suspect

label zelda_testimony:
    z """
    I think it all started last Tuesday.
    """

    $ know_outis_name = True

    z """
    I was working on my personal projects when I received a message about a potential commission, from a person using the alias {a=notes:outis:name}Outis{/a}.
    """

    $ know_zelda_job = True

    z """
    He {a=notes:zelda:portrait}wanted a realistic portrait{/a}. Not necessarily my forte, but I wasn't going to refuse a paid gig.

    His requirements were complex, and since we lived in the same city, I agreed I agreed, perhaps foolishly, to meet him face to face to discuss the matter further.

    Fast forward to this morning. I'm early, he's not, I'm getting some paperwork done while enjoying a cup of coffee.

    Finally, he comes in, greets me, orders a coffee, and we get to talk about his project.

    Soon, his coffee is ready, I go fetch it, and a new one for myself while I'm at it.

    I've only just returned to our table when another customer walks straight toward us and starts arguing crassly with Outis. He answers similarly, and the man runs away in rage.
    """

    show zelda disturbed with dissolve

    z """
    I'll never know what this was all about, as Outis then drank his coffee, and Hell's gates opened.

    I guess you've already seen men dying, in your line of duty. But I never had before today. That was even more horrible than anything I could have imagined.

    He looked sick, then in pain then he fell from his seat. People tried to help him, but life just wouldn't stop leaving his body, a bit more with each passing moment.

    I cannot describe it with words. I hadn't known that man for more than a few minutes, so I didn't really feel grief.

    But the swiftness with which death took him away… That's some terrifying shit for sure.
    """

    jump zelda_questions

label zelda_drawings:
    z """
    He provided me with a set of photos of some person, and asked me to imagine, and draw, what they would look like with a few more years, different hair and eye color, alternative skin tone, subtle changes in bone structure etc.
    """

    $ mephisto_job_details = True

    z """
    {a=notes:zelda:portrait}It was all very strict.{/a} He had made several lists, each with a precise combination of transformations that he wanted to see applied.
    """

    d "And what did the results looked like?"

    z "Nothing like anyone I know, and nothing like anyone that was in the café today, if that's what you want to know. I have some of the sketches with me if you want to see them."

    d "Please do. Any hint can be relevant."

    show zelda neutral with fade

    """
    The half-dozen of rough drawings show unknown, but surprisingly diverse, visages.

    Facial features are heavily different from one image to the next, a full gradient from smoothness to hardness, lightness to darkness.

    There's also a photo, from what looks like a posh long-haired highschooler.
    """

    d "Are they all supposed to be slight variations of the same girl?"

    z "Yeah. All the changes were minor, but the lists were very long."

    if know_outis_query:
        jump identity_tracker_reveal
    else:
        jump zelda_questions

label zelda_identity_tracking:
    z "Oh, I would hazard he was a facade for a rich girl wanting to know beforehand what she would like after a full makeover."

    d "Do you believe that?"

    z "Not really. But as long as I have at least one innocent explanation available, I can accept that kind of job without my conscience ringing too strongly."

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

    He was there when I arrived, behind his computer, focused on his screen.

    I wondered if he could be Outis, but he did not match the description my client had sent me.

    After that I forgot about his existence until the incident.
    """

    d "What did he say exactly?"

    z "An incoherent litany of bad words. I'm not sure even he understood what he was trying to say."

    d "And how did Outis react?"

    z "Similarly. Not the finest hour of either of them."

    d "And then?"

    z "The man gave up and departed angrily."

    jump zelda_questions

label zelda_truer_conversation:
    z "You never worked as a freelancer, did you? Client always complains about everything, comparing your work not to what they asked, but what they imagined."

    d """
    That may be true, but we have several testimonies suggesting that particular conversation went far beyond that.

    You talked about plausible deniability before. But as of now it's obvious you were far too involved for that.
    """

    "For just one second, she stands silent, weighting her options."

    z "Fine. Maybe Outis was suggesting he had some big catch at the end of his line, and it would be in my best financial interest to keep working for him."

    d "Details, please."

    z """
    Some girl. Rich, prestigious, family. Public image thoroughly controlled. Lots of skeletons in the closet.

    He was tracking a minor flaw in the storytelling of a rich, prestigious, family. You know, the kind with a thoroughly controlled public image, and a whole cemetery in the closet.

    One of their owns had been slowly fading away from their official propaganda through time. At first, she was quite prominent in the glossy pictures, then her appearances became scarce and into the background, until she entirely vanished.

    And, according to Outis' expertise, she was showing signs of using some heavy reshaping mods in her last pictures. The changes in her bone structure were quite clear in that regard he said.

    And he was trying to convince me that, from this tenuous lead, he had almost discovered everything that happened, and that, with just a little extra push, he could get a lot of money either from the girl or her family.

    He did not drop any name, so, for all I know, he could be lying out of his buttocks.
    """

    d "And what would have been your role in his scheme?"

    z """
    Unclear. I think he was trying to get an idea of what the chimera he was chasing looked like at different stages of her life, so he could determine the details of what had happened.

    Honestly, I branded him as a completely delusional, mostly harmless, man. I do not think he would have succeeded at discovering anything money-worthy.

    But I was still trying to get paid for the work already done, so I needed to keep the conversation going by playing his game. On the surface at least.
    """

    if know_photo_girl:
        jump not_a_doors
    else:
        jump zelda_questions

label zelda_latin:
    z "What?"

    d "Just testing a theory."

    jump zelda_questions

label zelda_almost:
    "The lady is not going anywhere, let's hear everyone true testimony before confronting her."

    hide zelda
    show anna neutral at center with fade

    jump anna_questions

label grand_finale:
    z "I don't think the law give you the authority to insult me inspector."

    d """
    Take it as a compliment. It's not everyday I meet someone so good at playing her fellows.

    You had what? About half an hour in a paddy wagon with those two?

    And still you managed to persuade them, with a few touches so subtle the officers didn't even put them in their report, that obstructing the instruction was their better chance to escape this mess in one piece.

    Admittedly, both were already terrified, each for their own reason. But still. Quite impressive.
    """

    z "I have no idea what…"

    d """
    Then let's start me with the beginning.

    Several weeks ago, Outis tried to blackmail you.

    He had discovered that your long lost sister, who had disappeared shortly before your father's death, was still alive under a fully reinvented identity.

    He didn't know all the details of your familial affairs, but he did guess rightfully that was something you would rather keep secret.

    His error was to think the only measures you would take would be of monetary nature.

    You managed to have him send you some of his proofs, including the transformation sketches.

    That's when you started to show just how devious you could be.

    You identified the artist, commissioned some sketches of your own, then stole her online identity.

    The last part we can prove. It took some work, but we manage to contact her, and confirm she lost access to her art account several weeks ago.
    """

    z """
    Identity theft is a serious crime, one who should not accuse someone of carelessly, especially when your so-called proofs are so weak.

    What if I say I have no idea what you're talking about, but that Outis specifically asked me to imitate the style of the artist he was previously working with?
    """

    d "I am not sure a jury will be convinced by such a far-fetched explanation."

    z "I don't need them to be convinced of my innocence, just to doubt my culpability enough."

    d """
    I know you're actually a lawyer, and you enjoy far too much those technicalities, but let's me finish my story before jumping to the trial.

    So, you put on your most colorful wig, and pretending to be the original artist, you contacted Outis and asked for a meeting in the flesh before continuing your collaboration.

    He accepted, and you dutifully prepared the poison.

    You're a prudent woman, with higher than average knowledge of lethal doses due to your past and profession, so I suppose you carefully plan your little mix to kill not too quickly.

    Acting on that hypothesis, we asked every cab companies and assimilated, and finally found that someone had requested a ride for a couple, including a sick man, near the café position, about ten minutes before the time of death.

    The car never came, slowed down by the weather, then blocked by the commotion due to the death, but it's hard to believe it could be for anyone but the murderer and their dying victim.

    You probably planned to have the cab leave you both near a place you could have discretely finished the job and get rid of the body.

    In that plan had worked, at best, we will have discovered Outis was taken out by some mysterious person impersonating an artist. A far too miserable lead to ever catch you.

    Here's come the first straw of bad luck in your perfect plan. Outis was an alcoholic. A well-known fact for every employee and regular of the café but not for you.

    And thus your perfect little plan crumbled when the combination of alcohol and drugs killed him almost instantly.

    You couldn't escape, and you ended up here, under meticulous scrutiny.
    """

    z """
    You sure spin a good tale. Now please lay down your proofs.

    I will even help you: I confess to be a con artist.

    When that stupid guy asked for someone able to draw \"in the style of\", I simply commissioned the original artist, then pretended to be the author.

    However, I just wanted to strip him bare of his money. I have no correlation whatsoever with his death.
    """

    d """
    That's an interesting defense, but with some basic flaws.

    First, when I asked you to show me the drawings and the original photo, you purposefully put aside the images resembling a bit too much your sister's current look.

    Same thing for the photo. You didn't give me the one Outis sent you, but a random one from your own archives.

    Sadly for you, you picked a easily recognizable student of your elite high school, rendering your lie quite transparent.

    The true artist provided us with the original photo and the missing sketches. They leave no doubt about the fact that Anna was the true target of Outis.
    """

    z """
    OK, I panicked. I thought these images were damning evidences of that barista girl's culpability, but I didn't want to be the one who would send her to jail.

    After all, maybe she had good reasons for her actions. Who am I to judge? And Outis sure did not strike me at a nice man.

    But that doesn't prove anything. The most innocents of people do the most stupid things under pressure. And you're quite a pressuring person.
    """

    d """
    Indeed. Afraid to lose it all if the truth was revealed, everyone lied in this whole affair. With an impressive consistency actually.

    You did help them quite a lot by coating each of your own speeches, before and after the fact, under a ton of seemingly innocent words, building up a complex illusion upon which they could easily base their own lies.

    But you made some basic mistakes.

    First, you didn't do enough research on the location of your meeting. And you learned the hard way Outis found it very funny to have business talks under his target's nose.

    Of course, in spite of your vivid disguise, Anna recognized you on the spot. {i}Vulpem pilum mutat, non mores.{/i} And you chose badly by not instantly bailing out.

    Instead, you couldn't help but taunt and threaten her, and were so cocky you even showed off the poison to her.
    """

    z """
    The word of the most likely culprit against mine? I somehow don't feel like I'm in any danger.
    """

    d """
    We also have a direct witness of your crime.
    """

    z """
    That's not possible.
    """

    d """
    Unless someone did catch a subtle movement of your arm behind the huge back of your chair thanks to its reflection in your nice glasses.
    """

    z """
    That's not humanly possible. And you cannot enhance vision beyond a certain threshold even with the latest nanomods.
    """

    d """
    That's incorrect. You cannot enhance vision {i}only{/i} with mods. But it's technically feasible. They're even scientific literature on that subject.

    And we did medically confirm the witness had a good enough vision for that impressive feat.
    """

    z """
    Is your super witness of good morality?
    """

    d """
    Are you miss I-probably-killed-my-father?
    """

    show zelda nervous with dissolve
    show zelda neutral with dissolve

    z """
    Your tale is becoming quite intricate inspector.
    """

    d """
    Yeah, that part isn't relevant to the current affair, though don't doubt we will be looking into it before long in light of the new pieces we gathered.
    """

    d """
    With two testimonies, a good idea of how you could have pulled it and a motive, I have far enough to put you behind bars for now. The judiciary system will decide of your ultimate fate.

    I just need one small piece to close the case.

    Should I arrest you under the identity of Zelda, mysterious con artist?

    Or would you rather be known as Seraphina Wagon, prestigious lawyer?
    """

    window hide
    scene bg black with fade
    show text "{size=+10}[config.name]{/size}{vspace=30}[gui.about]"

    $ renpy.pause()

    return



