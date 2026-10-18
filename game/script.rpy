define mc = Character("[mc_name]", what_color="#ADD8E6")
define mari = Character("Mari", what_color="#C8A2C8")
define mom = Character("Mom", what_color="#8B0000")
default mc_name = ""

define config.default_text_cps = 25

image bg_bedroom = im.Scale("images/bg_bedroom.png", 1920, 1080)

transform mari_kid:
    zoom 0.75
    xalign 0.5
    yalign 1.0

label start:

    $ _preferences.text_cps = 40

    pause 0.5

    $ mc_name = renpy.input("What's your name?")
    $ mc_name = mc_name.strip()

    if mc_name == "":
        $ mc_name = "Miku"

    while mc_name.lower() in [
        "medi",
        "9a7ba",
        "kawtar",
        "arwa",
        "zamla tabona",
        "bitch",
        "mari",
        "ghlida",
        "9a7bini zabinini"
    ]:

        if mc_name.lower() == "medi":
            "..."
            "Nope. You can't use THAT name. Try another one!"

        elif mc_name.lower() == "9a7ba":
            "AWILIII, bad bad bad!! Pick another name!"

        elif mc_name.lower() == "kawtar":
            "That's my name, hmph. Choose another one!"

        elif mc_name.lower() == "arwa":
            "Meow, Arwa, I love u wlkn no fuck u, don't use ur name hereee!"

        elif mc_name.lower() == "zamla tabona":
            "Yo, Medi, stop using bad names!"

        elif mc_name.lower() == "bitch":
            "STOP!!! Pick a different name!"

        elif mc_name.lower() == "mari":
            mari "That's my name, sweetie :3 But you can't use it!"

        elif mc_name.lower() == "ghlida":
            "7choma! Choose another name!"

        elif mc_name.lower() == "9a7binini zabinini":
            "STOOOOOP! Pick another name!"

        $ mc_name = renpy.input("Choose another name.")
        $ mc_name = mc_name.strip()

        if mc_name == "":
            $ mc_name = "MEOWMEOWMEOW"

    "Alright, [mc_name]..."

    #its just a joke between my friends lol pls dont mind the names hehe ok im sorry pls dont kill me guyes :( 

    scene black

    with fade 

   

    "I'm just a kid."

    "A completely normal kid living an ordinary life."

    "I go to school."

    "I do my homework."

    "I complain about waking up early."

    "Nothing special at all."

    pause 1

    "But lately... things haven't felt quite the same."

    "My parents have been coming home late almost every night."

    "I know they're working hard, but the house feels emptier every day."

    "Sometimes, I wish someone would sit beside me and ask how my day went."

    "It's a silly thing to wish for, isn't it?"

    "I turn onto my side and stare at the clock."

    "It's getting late."

    "Hm..."

    pause 1

    "..."

    "Ugh!"

    with hpunch

    "I've been staring at the ceiling for hours, and I still can't fall asleep"

    scene bg_bedroom

    with fade

    "I pull the covers up and look around my dark room."

    "Outside, the wind rustles through the branches, casting shadows that sway across the walls."

    "I close my eyes and try to ignore the strange noises coming from outside."

    "THUMP!"

    "oh shit-"

    with hpunch

    mc "..."

    mc "Sister...? Is that you?"

    "I wait for an answer."

    "Nothing."

    mc "Seriously? If you’re trying to scare me, it’s not funny!"

    "The room goes quiet again."

    "Only the faint moonlight reaches through the window."

    "Then I hear another little sound near the bookshelf."

    mc "I know I heard something..."

    "Maybe I should check."

    #meow im so fucking tired ughhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

    menu:

        "Check who fell.":

            mc "Sister...? Did you fall over your books again—"

            mc "HUH—?!"

            show mari surprised at mari_kid

            with dissolve

            "A small girl with twin tails is sitting on the floor, rubbing her knee. A glowing halo floats above her head."

            show mari nervous at mari_kid

            with dissolve

            mari "Ouch, ouch, ouch... That really hurt..."

            mari "E-Ehh?! Wait... You can actually see me?!"

            mc "Who are you?! What are you doing in my room?!"

            show mari nervous at mari_kid

            with dissolve

            mari "Please don’t panic! I’m not an intruder or a burglar or anything!"

            mc "THEN WHY ARE YOU IN MY ROOM?!"

            show mari happy at mari_kid

            with dissolve

            mari "I’m Mari, your official guardian angel!"

            mc "..."

            mc "My what?"

            show mari happy at mari_kid

            with dissolve

            mari "Your guardian angel!"

            mc "I know what a guardian angel is! I just didn't expect one to fall off my bookshelf!"

            show mari confuse at mari_kid

            with dissolve

            mari "In my defense, that bookshelf is surprisingly slippery."

            mc "How does a bookshelf get slippery?!"

            mari "That's a very good question."

            "I stare at her, waiting for a better explanation."

            "She stares back."

            mc "Am I dreaming?"

            show mari happy at mari_kid

            with dissolve

            mari "Nope!"

            mc "Did I hit my head?"

            mari "Not that I know of!"

            mc "You're not helping."

            show mari nervous at mari_kid

            with dissolve

            mari "S-Sorry..."

            "She looks down, fiddling nervously with her hands."

            "For someone who just appeared in my bedroom, she seems almost as nervous as I am."

            mc "Okay... let's start over."

            mc "What's your name?"

            show mari happy at mari_kid

            with dissolve

            mari "Mari! It's nice to meet you!"

            mc "And you're really an angel?"

            mari "A guardian angel, yes!"

            mc "are those are your wings?"

            show mari confuse at mari_kid

            with dissolve

            mari "yup they might look small now but they grow bigger when i need them"

            mc "And the halo?"

            show mari happy at mari_kid

            with dissolve

            mari "That's part of the uniform!"

            mc "You have a uniform?"

            show mari nervous at mari_kid

            with dissolve

            mari "yeah...you can say that"

            mc "This is going to be a very long night."

            mari "hey! hopefully not You're supposed to be sleeping!"

            mc "YOU'RE the one who made a loud noise!"

            show mari nervous at mari_kid

            with dissolve

            mari "I said I was sorry!"

            "Despite myself, I almost laugh."

            "She's strange. Extremely strange."

            "But somehow, she doesn't feel dangerous."

            mc "Fine. I'll hear you out."

            show mari surprised at mari_kid

            with dissolve

            mari "Realllly?!"

            mc "Don't make me regret it."

            show mari happy at mari_kid

            with dissolve

            mari "I promise!"

            mari "I've been assigned to watch over you for a while now."

            mc "Huh? Why me?!"

            show mari normal at mari_kid

            with dissolve

            mari "I can’t tell you everything just yet."

            mc "That's suspicious."

            show mari nervous at mari_kid

            with dissolve

            mari "It's angel stuff!"

            mc "That explains absolutely nothing!!"

            mari "Ehehe... sorry."

            "She glances around my room."

            show mari normal at mari_kid

            with dissolve

            mari "You've been having trouble sleeping lately, haven't you?"

            mc "How would you know that?"

            mari "I’ve been keeping an eye on you."

            mc "That's a little creepy."

            show mari nervous at mari_kid

            with dissolve

            mari "I mean... in a guardian angel kind of way!"

            mc "Still creepy."

            "She looks a little embarrassed."

            mari "I’m sorry. I didn’t mean to make you uncomfortable...sorry"

            "I look away."

            mc "It's just been lonely lately."

            mc "My parents are always busy, and the house is so quiet when I'm home."

            mc "I know it’s not their fault. I just wish I had someone to talk to sometimes."

            "Mari listens without interrupting."

            show mari shy at mari_kid

            with dissolve

            mari "Then I'm glad I came here."

            "I'm sure she knows already about my life and my family..."

            mc "Even if you fell off a bookshelf?"

            show mari happy at mari_kid

            with dissolve

            mari "Especially if I fell off a bookshelf!"

            "she looks so proud of herself how...adorable :3"

            "A small laugh escapes me."

            mc "You're ridiculous."

            mari "And you're smiling!"

            "she points at me and i didnt help but giggle"

            mc "Am not!"

            mari "Are too!"

            "For the first time tonight, my room doesn't feel quite so quiet."

            mc "So what do guardian angels actually do all day?"

            show mari normal at mari_kid

            with dissolve

            mari "We help people, watch over them, and keep them company when they need it."

            mc "Do you have other people to look after?"

            mari "Of course! But right now, you're my responsibility."

            mc "Lucky me."

            show mari happy at mari_kid

            with dissolve

            mari "Hey! I'm a very good guardian angel!"

            mc "You fell off my bookshelf."

            show mari nervous at mari_kid

            with dissolve

            mari "reallly? we're never going to forget that, are we?"

            mc "Absolutely not."

            "She pouts, and I find myself smiling again."

            show mari happy at mari_kid

            with dissolve

            mari "Well, I think we're going to get along just fine!"

            mc "You haven't even known me for an hour."

            mari "And yet, I already know you complain a lot."

            mc "EXCUSE ME?"

            mari "Ehehe!"

            "I shake my head, trying not to laugh."

            mc "You're lucky you're an angel."

            mari "Does that mean you forgive me?"

            mc "I'll think about it."

            show mari happy at mari_kid

            with dissolve

            mari "I'll take that as a yes!"

            "Mari glances at the clock."

            show mari normal at mari_kid

            with dissolve

            mari "It's getting really late, [mc_name]. You should get some sleep."

            mc "Easy for you to say. I've been trying for hours."

            show mari happy at mari_kid

            with dissolve

            mari "Hmm... maybe I can help."

            mc "How?"

            mari "A little angel magic!"

            mc "Wait. Is that safe?"

            show mari nervous at mari_kid

            with dissolve

            mari "Of course!"

            mc "Why did you hesitate?"

            mari "I DIDN’T!"

            "She raises one hand, and a faint, warm light gathers around her fingertips"

            mc "Mari... what are you doing?"

            show mari shy at mari_kid

            with dissolve

            mari "Just close your eyes for me okie?"

            mc "I have a bad feeling about this"

            mari "Trust me, [mc_name]. Just this once"

            "I'm exhausted, and her voice sounds strangely comforting"

            "For once, someone is here with me-"

            "but hey how she knows my name ugh...I feel sleepy anyway"

            "My eyelids begin to feel heavy"

            mc "Mari...?"

            show mari happy at mari_kid

            with dissolve

            mari "Goodnight, [mc_name]"

            mari "please sleep well and have sweet dreams"

            "Her voice grows distant."

            "The warm light slowly spreads across the room."

            "Did she really use her magic to make me fall asleep...?"

            pause 1.5

            scene black

            with Dissolve(3.0)

            "Everything went dark..."

            mari "mwah goodnight"

            pause 2.0

            "Somewhere in the darkness, I hear a quiet voice."

            mari "..."
            mari "too bad you won't remember all of this in the morning"
            mari "sorry [mc_name]!!!"

        "Call for Mom and tell her to leave.":

            mc "Sis, I told you not to come into my room—"

            pause 1.5

            mc "..."

            show mari surprised at mari_kid

            with dissolve

            mc "MOOOOOOOOOM! THERE'S A WEIRD FLOATING GIRL IN MY ROOM!"

            mari "Waah! Wait, wait, wait! Don't scream! I'm harmless!"

            mc "GET OUT!"

            show mari nervous at mari_kid

            with dissolve

            mari "I'm your guardian angel!"

            mc "THAT'S NOT AN EXPLANATION- huh!?"

            mari "It is where I come from!"

            mc "i-I DON'T CARE!"

            "I scramble out of bed and reach for the door."

            show mari nervous at mari_kid

            with dissolve

            mari "Okay, okay! I'm sorry! I'm vanishing now!"

            hide mari

            with dissolve

            "A tiny flash of light fills the room."

            "When I look back, she's gone."

            mc "..."

            mc "What the heck was that?"

            "Footsteps echo from down the hall as Mom opens the door."

            mom "What’s wrong? Why are you shouting?"

            mc "THERE WAS A GIRL IN MY ROOM!"

            mom "A girl?"

            mc "SHE HAD A HALO! AND SHE FELL OFF MY BOOKSHELF!"

            "Mom looks at the bookshelf, then back at me."

            mom "Sweetheart, you’ve been awake too long. Try to get some sleep"

            mc "BUT I SAW HER!"

            mom "We’ll talk in the morning, okay?"

            "She closes the door gently behind her."

            "I sit on the edge of my bed, staring at the empty bookshelf."

            mc "I know what I saw..."

            scene black

            with fade

            "But no matter how hard I try, I can't explain it."

        "Ignore it.":

            mc "..."

            "Maybe my sister is just playing a prank on me."

            "Or maybe I’m dreaming."

            "I pull the blanket over my head."

            "Whatever made that noise can wait until morning."

            "I'm far too tired to care anymore."

            "Tomorrow will probably be another ordinary day."

            "At least, that’s what I tell myself."

            scene black

            with Dissolve(3.0)

            "Eventually, I fall fast asleep"
            "mhm i wonder if my sis still here?"

            pause 2.0
            "I dont think i care..."

    return
