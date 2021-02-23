image calle = "calle.jpg"
image servicio = "servicio_secreto.jpg"
image mani1 = "mani1.jpg"
image mani2 = "mani2.jpg"
image tertulia = "tertulia.jpg"
image sala1 = "bar.png"
image federico saludando = "FedeSala1Cerrados.png"
image federico hablando = "FedeSala1Bajados.png"
image tertulia = "tertulia.jpg"
define click = "audio/click.mp3"
define d = Character("Federico")

label start:
    $ androide_confiado = 0
    $ humano_sospechoso = 0
    $ androide_sospechoso = 0
    $ humano_confiado = 0
    $ personaje = True
    stop music

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        # This is to fade the bar in and out, and is only required once in your script

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Call(timer_call)])

        if time > 1:
            bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 left_bar "#000000" right_bar "#807e7e" at alpha_dissolve # This is the timer bar.
            text str(time) xalign 0.5 yalign 0.9 color "#ffffff" at alpha_dissolve

        elif time>0.1:
            bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 left_bar "#000000" right_bar "#6e1818" at alpha_dissolve # This is the timer bar.
            text str(time) xalign 0.5 yalign 0.9 color "#ff1100" at alpha_dissolve

    init:# time = the time the timer takes to count down to 0.
        $ timer_range = 0 # timer_range = a number matching time (bar only)
        $ timer_call = 0 # timer_call = the label to call to when time runs out

    #Foto calle transitada
    scene calle
    "Es el año 2632. Los androides son una parte esencial de la sociedad."
    #Foto professions
    "Forman parte de tareas como construcción, transporte, tareas del hogar. Pero sólo son vistos como herramientas sin ningún prospecto de que eso cambie."

    #foto servicio secreto alarmados:
    scene servicio
    "Hace tres días que se ha descubierto que el presidente no era humano sino un androide."
    "Las ramificaciones de este acontecimiento aún no están definidas."

    scene mani1
    "Se han iniciado pequeñas manifestaciones en la ciudad debido a este descubrimiento"
    " ¿cómo ha llegado el androide a presidente?"
    scene mani3
    " ¿quién lo puso ahí?"
    " ¿ha sido capaz de engañarnos a todos y que nadie se diera cuenta? o lo que es peor, ¿hay más como él?"

    #foto tertulia
    scene tertulia
    "A causa de esto están surgiendo distintas corrientes de pensamiento sobre cómo juzgar lo ocurrido."
    "Hay quienes quieren respuestas y justicia, otros sienten miedo ante lo que aún podría quedar por descubrir y algunos argumentan que el hecho de que sea un androide no debería ser motivo de preocupación."
    scene black
    "Elige tu personaje"
    menu:
        "Humano":
            play sound click
            $ personaje = True
        "Androide":
            play sound click
            $ personaje = False
    #return

label sala1:

    scene sala1
    play music "audio/Bar.mp3" fadein 2 fadeout 2
    show federico saludando with dissolve
    d "Buenas, soy el detective Federico, ¿es usted X?"
    menu:
        "Emm… sí.": #humano
            play sound click
            $ humano_sospechoso +=1
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Sí, ¿qué quiere?": #androide
            play sound click
            $ androide_confiado +=1
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Afirmativo":
            play sound click
            $ androide_sospechoso +=1
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Soy X, ¿Nos conocemos?":
            play sound click
            $ humano_confiado +=1
            d "Todavía no, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"
    #responder
    hide federico saludando
    show federico hablando
    menu:
        "He quedado con alguien y como he llegado pronto estoy haciendo tiempo.":
            play sound click
            $ humano_confiado +=1
        "Me apetecía un café y he venido, ¿a qué viene tanta pregunta?":
            play sound click
            $ humano_sospechoso +=1
        "He venido a buscar refrigerante para mi aparato digestivo y a la vez estimularme.":
            play sound click
            $ androide_sospechoso +=1
        "Estaba paseando y he decidido tomar un café en el sitio más cercano.":
            play sound click
            $ androide_confiado +=1

    d "Perdona, ¿te estoy incomodando?, no puedo dejar la profesión ni para tomar un café jaja"
    $ time = 3                                     ### set variable time to 3
    $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_call = 'respuestaRapida'               ### set where you want to jump once the timer runs out
    show screen countdown                          ### call and start the timer
    #show screen countdownNumber
    play music "audio/tic_tac.flac" fadein 2
    menu:
        "No tranquilo… ja ja…":
            play sound click
            stop music
            hide screen countdown                  ### stop the timer
            $ humano_sospechoso +=1
        "No no, perdón por la sequedad, un mal día.":
            play sound click
            stop music
            hide screen countdown                  ### stop the timer
            $ androide_confiado +=1
            d "¡Qué me dices!, ¿qué ha pasado?"
            menu:
                "Eeeeh… Nada nada, he dormido mal, en el trabajo me he llevado bronca… En fin… ":
                    play sound click
                    $ humano_sospechoso +=1
                "Nada importante, pequeñas tonterías acumuladas…":
                    play sound click
                    $ androide_confiado +=1
        " Tranquilo, a todos nos ocurre lo mismo hoy en día con lo que está ocurriendo":
            play sound click
            stop music
            hide screen countdown                  ### stop the timer
            $ humano_confiado +=1

    d "Bueno, dejo de molestarle más, adiós, y alegre esa cara!"

    menu:
        "(Con una sonrisa torcida) ¡Adiós!":
            play sound click
            $ humano_sospechoso +=1
        "(Cara seria) Adiós.":
            play sound click
            $ androide_confiado +=1
        "(sonríe rápidamente y de forma brusca) ¡Como desee!":
            play sound click
            $ androide_sospechoso +=1
        "(sonriendo normal) ¡No me ha molestado para nada! Que tenga un buen dia":
            play sound click
            $ humano_confiado +=1
    stop music
    return

    label respuestaRapida:
        stop music
        #hide screen countdownNumber
        play sound "audio/ring.mp3"
        d "Vaya estas tardando mucho en constestar no?"
