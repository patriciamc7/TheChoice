image calle = "calle.jpg"
image pressRoom = "Assets/Intro/PressRoom/intro.png"
image servicio = "Assets/Intro/EscenaPolicias/Intro3.png"
image manifestacion = "Mani.png"
image tertulia = "tertulia.png"
image sala1 = "bar_prueba2.png"
image Collins Saludando = "Assets/Collins/sala1/Poses/BocaCerradaSaludo.png"
image Collins Casual = "Assets/Collins/sala1/Poses/BocaCerradaCasual.png"
image Collins Casual2 = "collins_sala2.png"
image casa = "sala2.png"
image noticias = Movie(play="noticias.webm", size=(1920,1080),)
define click = "audio/click.mp3"
define d = Character("Collins")

label start:#
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

    scene calle
    "Es el año 2632. Los androides son una parte esencial de la sociedad."
    "Forman parte de tareas como construcción, transporte, tareas del hogar. Pero solo son vistos como herramientas sin ningún prospecto de que eso cambie. "

    scene pressRoom
    "Hace tres días que se ha descubierto que la presidenta no era humana sino una androide."
    "Las ramificaciones de este acontecimiento aún no están definidas."

    scene servicio
    "Se han iniciado pequeñas manifestaciones en la ciudad debido a este descubrimiento"
    " ¿cómo ha llegado el androide a presidente?"
    scene manifestacion
    " ¿quién lo puso ahí?"
    " ¿ha sido capaz de engañarnos a todos y que nadie se diera cuenta? o lo que es peor, ¿hay más como él?"

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
    $ player_name = renpy.input("Enter name")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Alan Quim González"
label sala1:

    scene sala1
    play music "audio/Bar.mp3" fadein 2 fadeout 2
    show Collins Saludando
    d "Buenas, soy el detective Collins, ¿es usted ..."
    menu:
        "Emm… [player_name].": #humano
            play sound click
            $ humano_sospechoso +=1
            hide   Collins Saludando
            show Collins Casual
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "[player_name], ¿qué quiere?": #androide
            play sound click
            $ androide_confiado +=1
            hide   Collins Saludando
            show Collins Casual
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

        "Afirmativo":
            play sound click
            $ androide_sospechoso +=1
            hide   Collins Saludando
            show Collins Casual
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"


        "Soy [player_name], ¿Nos conocemos?":
            play sound click
            $ humano_confiado +=1
            hide   Collins Saludando
            show Collins Casual
            d "Todavía no, como habrá oído, estamos investigando el caso del presidente, hemos hecho un descanso en la investigación y he venido a por un café. Y usted, ¿qué hace aquí?"

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
    $ time = 10                                    ### set variable time to 3
    $ timer_range = 10                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_call = 'respuestaRapida'               ### set where you want to jump once the timer runs out
    show screen countdown                          ### call and start the timer
    play music "audio/tic_tac.mp3" fadein 2
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
        "(Sonríe rápidamente y de forma brusca) ¡Como desee!":
            play sound click
            $ androide_sospechoso +=1
        "(Sonriendo normal) ¡No me ha molestado para nada! Que tenga un buen dia":
            play sound click
            $ humano_confiado +=1
    stop music


label sala2:

    show noticias:
        xpos 0 ypos 0
    "Con el paso de los días las manifestaciones han crecido y se han ido violentando, las personas quieren respuestas y el gobierno no las da."
    "Por otro lado, la presidenta ya ha sido destituida y se celebrarán elecciones en dos semanas, donde se asegurará que los candidatos sean humanos."
    hide movie
    scene black
    "Han llamado a la puerta, es el detective Collins, el del otro día, quiere hablar, entra en tu casa."
    scene casa
    show Collins Casual2
    d "Gracias por dejarme pasar, no se preocupe, es una pequeña entrevista rutinaria, se lo estamos haciendo a mucha gente."
    menu:
        "Entrevista… ¿Sobre qué?":
            play sound click
            $ humano_sospechoso +=1
            d "Supongo que está usted al día de las noticias, las manifestaciones son cada vez más multitudinarias…"
            d " ¿Ha ido usted a alguna?"

        "¿A qué se debe la invasión de mi perímetro? ":
            play sound click
            $ androide_sospechoso +=1
            d "Supongo que está usted al día de las noticias, las manifestaciones son cada vez más multitudinarias…"
            d " ¿Ha ido usted a alguna?"

        "Tranquilo, ningún problema. ¿Quiere agua, un café…?":
            play sound click
            $ humano_confiado +=1
            d "No gracias, me acabo de tomar un café en la comisaría. Supongo que está usted al día de las noticias, las manifestaciones son cada vez más multitudinarias…"
            d "¿Ha ido usted a alguna?"
    menu:
        " Sí, necesitamos explicaciones.":
            play sound click
            $ humano_confiado +=1
            d "Con que explicaciones… ¿Cómo cree usted que la presidenta nos ha podido engañar todo este tiempo?"
            menu:
                "No lo se. Y como debería saberlo yo? ¡No soy uno de esos androides!":
                    play sound click
                    $ humano_sospechoso +=1

                "¿Quién sabe? Se camuflan muy bien. Por lo que yo se usted podría ser uno.":
                    play sound click
                    $ humano_confiado +=1

                "Es muy simple imitar el aspecto de los seres humanos.":
                    play sound click
                    $ androide_sospechoso +=1

                "Es una cuestión muy compleja, siento no poder serle de más ayuda.":
                    play sound click
                    $ androide_confiado +=1

        "Emmm… No… Yo no estoy de acuerdo con estas manifestaciones. ":
            play sound click
            $ humano_sospechoso +=1
        "El acto de manifestación no es una forma lógica de conseguir resultados. ":
            play sound click
            $ androide_sospechoso +=1
        "No, pero lo he considerado.":
            play sound click
            $ androide_confiado +=1

    if personaje == False:
        d "Entiendo, veo que usted vive en un piso muy acogedor. Veo que no tiene fotografías, no es muy habitual si me lo permite."
        menu:
            "¿Usted cree? Yo he estado en muchas casas sin fotografías (mira nervioso por toda la casa al percatarse de que no tiene fotografías)":
                play sound click
                $ humano_sospechoso +=1

            "La verdad es que no me considero fotogénico.":
                play sound click
                $ humano_confiado +=1

            "No le veo la necesidad cuando puedo acceder a mi memoria para recordar los eventos.":
                play sound click
                $ androide_sospechoso +=1

            "Prefiero tenerlas en la nube y verlas en el ordenador.":
                play sound click
                $ androide_confiado +=1

label final:

    if androide_confiado > 5 & personaje == False:
        "Eres androide, te salvan porque les vas a dar información sobre los otros androides, traicionas a los tuyos para protegerte a ti mismo."

    if androide_confiado > 5 & personaje == True:
        "Eres humano, te matan aunque saben que no eres androide porque en realidad la existencia de los androides es mentira y es un complot para exterminar a gran parte de la humanidad."

    if humano_sospechoso >5 &  personaje == False:
        "Eres androide, te matan."

    if humano_sospechoso >5 &  personaje == True:
        "Eres un humano, lo haces fatal pareces un androide y te matan."

    if humano_confiado >5 &  personaje == False:
        "Eres androide, te salvas porque pareces un humano."

    if humano_confiado >5 &  personaje == True:
        "Eres un humano, te salvas."

    if androide_confiado> 5 & personaje == False:
        "Al final te descubrem pero te perdonan la vida."

    if androide_confiado> 5 & personaje == True:
        "Los androides se han alzado y estaban mirando si eres de los suyos."
return


label respuestaRapida:
    stop music
    play sound "audio/ring.mp3"
    d "Vaya estas tardando mucho en constestar no?"
