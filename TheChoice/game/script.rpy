image intro = "final.png"
image sala1 = "bar.png"
define d = Character("Federico")


label start:
    $ personaje = True
    scene intro
    "INTRO"
    "Elige tu personaje"

    menu:
        "Humano":
            $ personaje = True
        "Androide":
            $ personaje = False
    #return

label sala1:

    scene sala1
    show eileen happy with dissolve
    d "Buenas, soy el detective Federico, ¿es usted X?"
    menu:
        "Emm… sí.": #humano
            jump humano
        "Sí, ¿qué quiere?": #androide
            jump androide
    #responder
    return

label humano:
    d "Eres humano"
return

label androide:
    d "Eres androide"
return
