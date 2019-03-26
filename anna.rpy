define a = Character("Anna", who_color="#dcad94", image="anna")

image anna neutral = im.Crop("rest-neu.png", (145, 60, 345, 700))
image anna nervous = im.Crop("rest-nerv.png", (145, 60, 345, 700))
image anna happy = im.Crop("rest-reliev.png", (145, 60, 345, 700))

default anna_testimony = False
default anna_outis = False
default anna_zelda = False
default anna_mephisto = False
default anna_outis_2 = False
default anna_photo = False
default anna_scenery = False
default anna_puzzle = False
default anna_damnatio = False

label anna_introduction:
    show anna neutral at center with fade

    "Anna."

    "Your archetypal employee of a small brand café. Part-barista, waitress, cook, cleaner, she does her part of all the day-to-day work needed to keep the place running."

    jump anna_questions

label anna_questions:
    show anna neutral at center

    menu:
        "Tell me what happened." if not anna_testimony:
            $ anna_testimony = True
            jump anna_testimony
        "What can you tell me about Outis?" if anna_testimony and not anna_outis:
            $ anna_outis = True
            jump anna_outis
        "What can you tell me about Zelda?" if anna_testimony and not anna_zelda:
            $ anna_zelda = True
            jump anna_zelda
        "What can you tell me about Mephisto?" if anna_testimony and not anna_mephisto:
            $ anna_mephisto = True
            $ know_mephisto_job = True
            jump anna_mephisto
        "Did you have a fight with Outis?" if anna_outis and not anna_outis_2 and know_anna_talked_to_outis:
            $ anna_outis_2 = True
            $ anna_name = True
            jump anna_outis_2
        "Show photo" if anna_testimony and seen_drawings and not anna_photo:
            $ anna_photo = True
            $ know_photo_girl = True
            jump anna_photo
        "Let's focus on the last minutes." if anna_testimony and not anna_scenery:
            $ anna_scenery = True
            $ know_mephisto_waited = True
            jump anna_scenery
        "I have a peculiar request for you." if know_photo_girl and hint_about_outis_target and not anna_puzzle:
            $ anna_puzzle = True
            $ vulpem = True
            jump anna_puzzle
        "Damnatio memoriae." if mephisto_confession and not anna_damnatio:
            $ anna_damnatio = True
            $ anna_confession = True
            $ anna_disabled = True
            jump anna_damnatio
        "No more questions.":
            jump choose_your_suspect

label anna_testimony:
    show anna happy with dissolve

    a """
    It was a slow day at work. Far less people than usual.

    You see, our usual customers are mainly people working nearby. But, with the snowstorm, they couldn't make it to work today. No work, no coffee before work.

    So, for most of the morning, they were more employees than customers in the shop, and everything was quiet.
    """

    show anna neutral with dissolve
    $ know_outis_name = True

    a """
    At some point, that guy came in. A semi-regular. Not here everyday, but comes frequently enough that I remember his face. Uses the alias {a=notes:outis:name}Outis{/a}.

    He asked for the flavor of the week, a Dark Latte Americano.

    The right machine hadn't been booted yet, so it took me a bit of time to prepare his order.
    """

    show anna nervous with dissolve

    a """
    Like five, maybe ten minutes?
    """

    show anna neutral with dissolve

    a """
    Didn't really check. As I said, the atmosphere was distressed. People took their time, nobody wanted to return into the cold fast.
    """

    $ zelda_wait = True

    a"""
    So, the girl he was with came to take his drink. A new face, never seen her before. She also ordered an extra espresso for herself, and {a=notes:zelda:counter}waited at the counter{/a} while I made both.

    She went back to their table with both cups, I went back to dozing off.

    Soon after, Mephisto joined them, and they had a verbal fight.

    They weren't exactly shouting through the whole room, so I didn't understand what they said, but it didn't sound nice.

    It was shortly over though. Mephisto bade out before things escalated too far.
    """

    show anna nervous

    a """
    And then…

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

    She waved at him, and he went to join her. They discussed for some time without ordering anything, then Outis came to the counter to ask for a coffee, and returned quickly to his seat.

    She came herself soon after, asked for a refill, did some small talk about the weather while she waited, and went back to their table with both cups.

    Overall, they looked more like they were negotiating than flirting.
    """

    jump anna_questions

label anna_mephisto:
    a """
    Mephisto is not there everyday, but it's as if.

    I think the café is more or less his public office. Some people come just to speak to him.
    """

    d "Which kind of people?"

    a """
    Of all kinds actually. He's got quite the varied following. People of all ages, genders, colors.

    Though, thinking about it, I never saw anyone which looked like they had difficult ends of months discuss with him for long.
    """

    d "And for which reason was he that popular with the {i}bourgeoisie{/i}?"

    show anna nervous

    "I can see the cogs in her brain turn as she's trying to formulate a non-suspicious answer. May as well cut short her circumlocutions."

    d "Is he a dealer?"

    show anna neutral with dissolve

    "She's taken aback for a second, then answers calmly."

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

label anna_outis_2:
    a "I wouldn't call it a fight. Guy wanted to know more about me, I said I wasn't interested, he insisted, I may have spoken a little louder than I wanted too."

    d "Once?"

    a """
    Maybe twice. Or thrice.

    But you know, it's still all too usual to receive unwanted attention from customers. Usually, I'm just better at handling such interactions.
    """

    d "What did he said or tried to do that ended up blowing your fuse?"

    a "He was very inquisitive, trying to pry into my private life. And he called me by whatever name crossed his mind at the moment, instead of the one on my tag."

    jump anna_questions

label anna_photo:
    d "Do you know who this is?"

    show anna nervous with dissolve
    show anna neutral with dissolve

    "She blinks a few times at the picture."

    a "Eh, yeah. That's Phoenix Doors. One of the Doors' children. Big money. Probably works at the family company today."

    "The family name rings a bell. A quick search on your phone brings in a sharply-dressed young woman."

    d "You've recognized her instantly from such an old photo?"

    a "She hasn't changed much as you can see."

    "I must agree with her. After several years doing this job, you tend to take for granted people change skin twice a year, but that's far more true. A lot of people actually prefer to keep looking the same as long as possible."

    d "Still, you've recognized her instantly from an old photo. That's impressive."

    a "Well, we went to the same music school a long time ago."

    "The Internet does confirm that the Doors' girl did take piano lessons at a prestigious, and expensive, {i}conservatoire{/i} as part of her studies."

    jump anna_questions

label anna_scenery:
    d "Let's say from the moment you finished preparing both coffees. At that time, where exactly in the café were Outis, Mephisto, Zelda and yourself?"

    a """
    I was behind the counter.

    Zelda en route to hers and Outis' table.

    Outis and Mephisto were both seated at their usual positions, just a few steps away, each minding his own business.
    """

    d "OK. How did those position evolve from that moment?"

    a """
    Mine didn't. Zelda sat at her table. Then Mephisto rose and closed the distance to Outis.

    Not a minute later, he went out, almost in a straight line, with just a minimal detour to grab his stuff.

    Then, end of the world. No idea who did what at that moment as it was utter chaos.
    """

    d "Let's go back a little. No one else crossed path with any of you four from the moment the coffee was pulled to the tragic end?"

    a """
    No. If that was an usual day, I wouldn't have been able to say that for sure: There's always someone else waiting at the bar on in the alleys.

    But today, with so little people, each of them was really standing out, and I would have remember.
    """

    jump anna_questions

label anna_puzzle:
    d "I need to identify someone from a family like the Doors, upper upper class stuff, who vanished from public sight a few years ago."

    # Quick changes in Anna's expression

    a "Willingly or not?"

    d "In a way that the involved persons would not like to be heard about."

    a """
    That's not helping much.

    Some of those familiars are quite secretive, even for the most trivial of things. They frown at people simply suggesting they may poop.
    """

    d "Let's try it another way. From what reason would a golden child fade away?"

    a """
    Pretty much anything I would say.

    Could be someone who grew up in public relationship land, got a doctor degree, then went on to live their own live, far away from constant gossip.

    Could be the black sheep of the family, pushed away due to their terrible behavior before even mom's and dad's money cannot buy them a blank criminal record anymore.

    Could be just a change in self-marketing strategy, switching people under the spotlight to match the trends.
    """

    d "What if I say the person in question switched face entirely?"

    a """
    Don't change anything. Who did not change appearance radically at least one in their life nowadays?

    Look at you, for example. How do your own mother recognize you?
    """

    d "According to her, I could look like Mona Lisa or The Scream, she would still recognize me all the same cause I'll still be the same stubborn idiot underneath."

    a "Oh, yeah. {i}Vulpem pilum mutat, non mores.{/i}"

    "She let the Latin flow out naturally, with a Italian-sounding accent which you guess is the accurate pronunciation. Then, she almost bit her tongue when quickly switching back to English."

    a "That means {i}the fox changes his fur, not his habits{/i}. There's a similar expression with a scorpion I think."

    jump anna_questions

label anna_damnatio:
    a """
    The most terrible sentence of Roman law. To have one's existence utterly removed from history, down to their name.

    But the term is inappropriate for someone who discarded her identity of her own will. My sister just loves to show off her Latin, even I was always better at it.
    """

    d "You're not even denying it?"

    a "Unless you speak random Latin phrases to all of your suspects, I guess you know everything at this point."

    d "I'm more interested in what you saw and heard that in what you guessed."

    a """
    I didn't see her poison Outis with my own eyes, but she flashed me with the pills on the back of her sleeve when she said she was once again going to solve the problem herself while I was too busy fleeing.
    """

    d "And you didn't stop her?"

    a """
    The bitch had all power over me at the moment. One phone call to mom, and goodbye freedom.

    For good this time, as I'm pretty sure she managed to put the blame of father's death upon me. The family would just have thrown me in some hole forever, and she would have had her way without any extra interference.

    Let it be clear: She didn't kill a man to protect the new identity of her dear sister. She did it half to protect her name's reputation, half because she is prideful enough to believe she could one hundred-percent do it without being caught.
    """

    d "I can have you registered to the new identity police program if you cooperate. Will be easier than building yet another one from scratch."

    a "I have no reason not to at this point. What do you want to know?"

    d "Everything."

    jump choose_your_suspect

