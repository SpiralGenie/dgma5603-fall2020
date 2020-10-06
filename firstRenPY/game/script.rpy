define e = Character("Reena")

default dire = False

label start:

    scene bg black with Dissolve(.25)

    e "Oh darn it all..."

    e "These bills just keep piling up and I can't seem to make ends meet."

    play music "audio/mushrooms.mp3"

    scene bg cafe evening with Dissolve(.5)

    show reena sad 2 with Dissolve(.25):
        zoom 0.5
        xalign 0.5
        yalign 1.0

    e "What am I supposed to do? The landlord is coming to collect this month's rent tomorrow..."

    if dire:
        jump burnitdown
    else:
        menu:

            "Burn the place down":
                jump burnitdown


            "Fret over it some more":
                jump fret

label fret:
    $ dire = True

    "Reena continued fretting over her monetary issues."

    e "Well shoot, worrying did nothing."

label burnitdown:
    show reena annoyed 1

    e "hmm..."

    hide reena annoyed 1 with Dissolve(.25)

    scene bg black with Dissolve(.5)

    stop music fadeout 1.0

    e "Oh... I know..."

    play music "audio/campfire.mp3"

    scene bg cafe fire with Dissolve(.75)

    show reena happy 1:
        zoom 0.5
        xalign 0.5
        yalign 1.0


    e "I'm burning my cafe down for the insurance money."

    e "lmao"

    show reena happy 1 with move:
        zoom 0.5
        xalign 0.75
        yalign 1.0

    show reena neutral 2
    e "now get out."

    hide reena neutral 2 with moveoutright
    stop music fadeout 1.0
    scene bg black with Dissolve(1.0)

    return
