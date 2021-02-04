
image room = "room.png"
image livingroom = "final.png"
define e = Character("Eileen", color="#ff003c")

label start:

    scene room
    #show eileen happy
    "Good morning."
    "This is not a kitchen."

    show screen gotoLivingrRoomArrow

    $ renpy.pause(hard=True)


label LivingRoom: #another location
    scene livingroom
