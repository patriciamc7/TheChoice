image intro = "final.png"
image sala1 = "bar.png"
define d = Character("Federico")
image fedec1 = "FedeSala1Cerrados.png"
image fedeb1 = "FedeSala1Bajados.png"


label start:
    $ androide_confiado = 0
    $ humano_sospechoso = 0
    $ androide_sospechoso = 0
    $ humano_confiado = 0
    $ personaje = True
    scene intro
    #foto servicio secreto alarmados:

    "Hace tres días que se ha descubierto que el presidente no era humano sino un androide."
    "Las ramificaciones de este acontecimiento aún no están definidas."

    #foto
    "Se han iniciado pequeñas manifestaciones en la ciudad debido a este descubrimiento"
    " ¿cómo ha llegado el androide a presidente?"
    " ¿quién lo puso ahí?"
    " ¿ha sido capaz de engañarnos a todos y que nadie se diera cuenta? o lo que es peor, ¿hay más como él?"

    #foto
    "A causa de esto están surgiendo distintas corrientes de pensamiento sobre cómo juzgar lo ocurrido."
    "Hay quienes quieren respuestas y justicia, otros sienten miedo ante lo que aún podría quedar por descubrir y algunos argumentan que el hecho de que sea un androide no debería ser motivo de preocupación."


    "Elige tu personaje"
    menu:
        "Humano":
            $ personaje = True
        "Androide":
            $ personaje = False
    #return

label sala1:

    scene sala1
    show fedec1 with dissolve
    d "Buenas, soy el detective Federico, ¿es usted X?"
    menu:
        "Emm… sí.": #humano
            $ humano_sospechoso +=1
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Sí, ¿qué quiere?": #androide
            $ androide_confiado +=1
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Afirmativo":
            $ androide_sospechoso +=1
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Soy X, ¿Nos conocemos?":
            $ humano_confiado +=1
            d "Todavía no, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"
    #responder
    menu:
        "He quedado con alguien y como he llegado pronto estoy haciendo tiempo.":
            $ humano_confiado +=1
        "Me apetecía un café y he venido, ¿a qué viene tanta pregunta?":
            $ humano_sospechoso +=1
        "He venido a buscar refrigerante para mi aparato digestivo y a la vez estimularme.":
            $ androide_sospechoso +=1
        "Estaba paseando y he decidido tomar un café en el sitio más cercano.":
            $ androide_confiado +=1

    d "Perdona, ¿te estoy incomodando?, no puedo dejar la profesión ni para tomar un café jaja"
    menu:
        "No tranquilo… ja ja…":
            $ humano_sospechoso +=1
        "No no, perdón por la sequedad, un mal día.":
            $ androide_confiado +=1
            d "¡Qué me dices!, ¿qué ha pasado?"
            menu:
                "Eeeeh… Nada nada, he dormido mal, en el trabajo me he llevado bronca… En fin… ":
                    $ humano_sospechoso +=1
                "Nada importante, pequeñas tonterías acumuladas…":
                    $ androide_confiado +=1
        " Tranquilo, a todos nos ocurre lo mismo hoy en día con lo que está ocurriendo":
            $ humano_confiado +=1

    d "Bueno, dejo de molestarle más, adiós, y alegre esa cara!"
    menu:
        "(Con una sonrisa torcida) ¡Adiós!":
            $ humano_sospechoso +=1
        "(Cara seria) Adiós.":
            $ androide_confiado +=1
        "(sonríe rápidamente y de forma brusca) ¡Como desee!":
            $ androide_sospechoso +=1
        "(sonriendo normal) ¡No me ha molestado para nada! Que tenga un buen dia":
            $ humano_confiado +=1

    return
