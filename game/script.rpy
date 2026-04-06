

label splashscreen:


    scene black with fade

    "This game contains content for ages 18 and over."

    menu:
        "Are you 18 years old or older?"
        "Yes, I am 18 or older":
            jump splashscreen2_en
        "No, I am under 18":
            jump menor_en

label menor_en:
    "Sorry, this game is not recommended for players under 18."
    return

default player_name = "Ethan"
default persistent.unlocked_scene1 = False
default persistent.unlocked_scene2 = False
default persistent.unlocked_scene3 = False
default persistent.unlocked_scene4 = False
default persistent.unlocked_scene5 = False
default persistent.unlocked_scene6 = False
default persistent.unlocked_scene7 = False
default persistent.unlocked_scene8 = False
default persistent.unlocked_scene9 = False
default persistent.unlocked_scene10 = False
default persistent.unlocked_scene11 = False

label splashscreen2_en:
    scene black with fade
    show logo_studio at truecenter
    with fade
    pause 2.0
    hide logo_studio with fade

    show main_menu at truecenter
    with fade
    pause 2.0
    hide main_menu with fade

    return



# =====================
# Definição de personagens
# =====================

# Camila: nome e fala em rosa
define c = Character(
    "Camila",
    color="#FFB6C1",        # nome rosa claro
    what_color="#FFE4EB"    # fala ainda mais clara, quase pastel
)

define s = Character(
    "Stranger",
    color="#000000",        # nome preto
    what_color="#e7e7e7"    # fala ainda mais clara, quase pastel
)

# Mary: nome e fala em vermelho
define m = Character(
    "Mary",
    color="#FF7F7F",        # nome vermelho claro
    what_color="#FFCFCF"    # fala bem clara
)

# Walter: nome e fala em azul
define w = Character(
    "Walter",
    color="#87CEFA",        # nome azul claro
    what_color="#D0F0FF"    # fala bem clara
)

# Jogador (verde)
define p = Character(
    "[player_name]",
    color="#98FB98",        # nome verde claro
    what_color="#E0FFE0"    # fala bem clara
)

# Adrian (roxo mais claro)
define a = Character(
    "Adrian",
    color="#A45CFF",       # roxo médio-claro para o nome
    what_color="#E0C7FF"   # fala em tom bem claro de roxo
)






# Personagens com cores escuras para as falas específicas
define c_dark = Character("Camila", color="#8B008B")  # Rosa escuro
define m_dark = Character("Mary", color="#8B0000")    # Vermelho escuro
define w_dark = Character("Walter", color="#00008B")  # Azul escuro


# Definindo cores para os nomes
define camila_name = "{color=#FF69B4}Camila{/color}"  # rosa
define steve_name  = "{color=#32CD32}Steve{/color}"   # verde

# Definição de cores para os personagens
define walter_name = "{color=#00008B}Walter{/color}"    # azul escuro
define camila_name = "{color=#8B008B}Camila{/color}"    # rosa escuro
define mary_name   = "{color=#8B0000}Mary{/color}"      # vermelho escuro



# Declaração das imagens
image fundo_casa = "images/fundo_casa.png"
image camila_olhos_fechados = "images/camila_olhos_fechados.png"
image camila_normal = "images/camila_normal.png"
image camila_sedutivo = "images/camila_sedutivo.png"
image camila_triste = "images/camila_triste.png"
image camila_olhando_lado = "images/camila_olhando_lado.png"
image Pegando = "Pegando.png"
image an = Movie (play="images/animations/1animation.webm", loop=True)
# =========================

image black2 = Solid("#000000")



# Massagens
image costas1 = "images/hospital/costas1.png"
image costas2 = "images/hospital/costas2.png"
image white = Solid("#FFFFFF")

# Declaração da animação
image anim_quarto = Animation(
    "images/frame1.png", 0.05,
    "images/frame2.png", 0.05,
    "images/frame3.png", 0.05,
    "images/frame4.png", 0.05,
    "images/frame5.png", 0.05,
    "images/frame6.png", 0.05,
    "images/frame7.png", 0.05,
    "images/frame8.png", 0.05,
    "images/frame9.png", 0.05,
    "images/frame10.png", 0.05,
    "images/frame11.png", 0.05,
    "images/frame12.png", 0.05,
    "images/frame13.png", 0.05,
    "images/frame14.png", 0.05,
    "images/frame15.png", 0.05,
    "images/frame16.png", 0.05,
    "images/frame17.png", 0.05,
    "images/frame16.png", 0.05,
    "images/frame15.png", 0.05,
    "images/frame14.png", 0.05,
    "images/frame13.png", 0.05,
    "images/frame12.png", 0.05,
    "images/frame11.png", 0.05,
    "images/frame10.png", 0.05,
    "images/frame9.png", 0.05,
    "images/frame8.png", 0.05,
    "images/frame7.png", 0.05,
    "images/frame6.png", 0.05,
    "images/frame5.png", 0.05,
    "images/frame4.png", 0.05,
    "images/frame3.png", 0.05,
    "images/frame2.png", 0.05,
    loop=True
)

# Declaração da animação
image massagemani = Animation(
    "images/amassagem1.png", 1.05,
    "images/amassagem2.png", 1.05,
    loop=True
)


# Massagens (1 a 16)
image massagem1 = "images/hospital/massagem1.png"
image massagem2 = "images/hospital/massagem2.png"
image massagem3 = "images/hospital/massagem3.png"
image massagem4 = "images/hospital/massagem4.png"
image massagem5 = "images/hospital/massagem5.png"
image massagem6 = "images/hospital/massagem6.png"
image massagem7 = "images/hospital/massagem7.png"
image massagem8 = "images/hospital/massagem8.png"
image massagem9 = "images/hospital/massagem9.png"
image massagem10 = "images/hospital/massagem10.png"
image massagem11 = "images/hospital/massagem11.png"
image massagem12 = "images/hospital/massagem12.png"
image massagem13 = "images/hospital/massagem13.png"
image massagem14 = "images/hospital/massagem14.png"
image massagem15 = "images/hospital/massagem15.png"
image massagem16 = "images/hospital/massagem16.png"

# Hospital fundos (h1 até h4)
image h1 = im.Scale("images/hospital/h1.png", 1216, 832)


# Bundah (h1 até h3)
image bundah1 = "images/hospital/bundah1.png"
image bundah2 = "images/hospital/bundah2.png"
image bundah3 = "images/hospital/bundah3.png"

transform top_center:
    xalign 0.5   # meio na horizontal
    yalign 0.0   # topo na vertical

transform zoom176:
    zoom 1.24
    xalign 0.5
    yalign 0.0

transform zzoom176:
    zoom 0.85
    xalign 0.5
    yalign 0.0

transform zzoom1762:
    zoom 0.80
    xalign 0.5
    yalign 0.0

transform zoom1762:
    zoom 1.24
    xpos 0
    ypos 0

transform zoom1763:
    zoom 1.2
    xalign 0.5
    yalign 0.0

transform zoom1764:
    zoom 0.91
    xalign 0.5
    yalign 0.0

transform zoom1:
    zoom 0.3
    xalign 0.0
    yalign 0.0

transform zoom12:
    zoom 0.5
    xalign 0.0
    yalign 0.0

transform topleft:
    xalign 0.0
    yalign 0.0

transform cortar_topo:
    zoom 1.24                  # aumenta 24%
    xalign 0.5                 # centraliza horizontalmente
    yalign 0.0                # centraliza verticalmente
    crop (0, 0, 1216, 273)     # só a parte de cima  

transform top_top:
    yalign 0.0   # topo na vertical
    xalign 0.782


image mvhosp2 = Movie(play="images/animations/ani_pingpong.webm", loop=True)
image mvhosp1 = Movie(play="images/animations/ani2.webm", loop=True)
image mvhosp3 = Movie(play="images/animations/ani3.webm", loop=True)
image mvmassagem1 = Movie(play="images/animations/massagem2.webm", loop=True)
image mvmassagem2 = Movie(play="images/animations/massagem3.webm", loop=True)
image mvchupando1 = Movie(play="images/chupando1.webm", loop=True)
image mvchupando2 = Movie(play="images/chupando2.webm", loop=True)
image janitorvideo = Movie(play="images/janitorvideo1.webm", loop=True)
image tablevideo1 = Movie(play="images/table_video1.webm", loop=True)
image tablevideo2 = Movie(play="images/table_video2.webm", loop=True)
image af_video1 = Movie(play="images/afvideo1.webm", loop=True)
image af_video2 = Movie(play="images/afvideo2.webm", loop=True)
image janelavideo1 = Movie(play="images/camilajanelavideo1.webm", loop=True)
image janelavideo2 = Movie(play="images/camilajanelavideo2.webm", loop=True)
image titvideo1 = Movie(play="images/titvideo1.webm", loop=True)
# Transform para Camila: maior, direita, um pouco pra baixo
transform camila_maior_direita_baixo:
    xpos 0.7
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8
transform mary_maior_direita_baixo:
    xpos 0.7
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8

transform walter_maior_direita_baixo:
    xpos 0.8
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8

transform camila_maior_esquerda_baixo2:
    xpos 0.6
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8


transform camila_maior_esquerda_baixo3:
    xpos 0.3
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8

transform camila_maior_esquerda_baixo4:
    xpos 0.8
    ypos 0.6
    xanchor 0.5
    yanchor 0.5 
    zoom 0.8    

transform camila_maior_esquerda_baixo5:
    xpos 0.3
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.9

transform camila_maior_esquerda_baixo6:
    xpos 0.3
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8

transform esquerda_topo_menor:
    xpos 1450    # posição em pixels a partir da esquerda
    ypos 0       # posição em pixels a partir do topo
    zoom 0.5     # reduz a imagem


transform scale_down:
    xalign 0.5
    yalign 0.5
    zoom 0.9  # reduz a imagem/vídeo para 90% do tamanho original


transform zoomout:
    xalign 0.5
    yalign 0.5
    zoom 2.0
    linear 5.0 zoom 1.0

transform zoomout176:
    xalign 0.5
    yalign 0.5
    zoom 2.0
    linear 5.0 zoom 1.24

transform zoomout1762:
    xalign 1.0
    yalign 0.5
    zoom 2.0
    linear 5.0 zoom 1.24

transform rosto_canto_inferior_direito:
    # Primeiro recorta o sprite
    crop (0, 0, 1.0, 0.33)   # x, y, largura, altura (0.33 = terço superior)
    zoom 0.6
    # Depois posiciona no canto inferior direito
    xalign 0.0
    yalign 1.05

    # Ajusta para ficar acima da caixa de fala (opcional)
    xoffset -150
    yoffset -20


transform camila_maior_esquerda_baixo9:
    xpos 0.1
    ypos 0.6
    xanchor 0.5
    yanchor 0.5
    zoom 0.8


label main_menu:

    # Toca música antes do menu aparecer, se ainda não estiver tocando
    if not renpy.music.get_playing("music"):
        play music "audio/casual_music.mp3" loop fadein 0.7

    # Mostra o menu principal
    call screen main_menu
    return

label start:

    scene black

    # ask for the player's name
    $ player_name = renpy.input("What's your name? (Default name will be Ethan)")
    $ player_name = player_name.strip()  # remove extra spaces

    # if nothing is entered, use a default
    if player_name == "":
        $ player_name = "Ethan"

    scene fundo_casa

    play music "audio/casual_music.mp3" loop fadein 1.0 volume 0.7

    "After a long day at work, you arrive home exhausted."
    "You look for Camila, your wife, calling her name with a tired voice."

    # Hide previous images of Camila
    hide camila_olhos_fechados
    hide camila_normal
    hide camila_sedutivo
    hide camila_triste
    hide camila_olhando_lado

    show camila_olhos_fechados at camila_maior_direita_baixo
    c "Welcome home, darling..."


    p "Hi, Camila..."
    p "I'm exhausted today..."

    hide camila_olhos_fechados
    show camila_normal at camila_maior_direita_baixo
    c "How was your day at work? Any big problems?"

    p "It was tough, as always. I can’t wait to rest."

    hide camila_normal
    show camila_brava at camila_maior_direita_baixo
    c "I had a rough day too... There's a patient at the hospital who’s driving me crazy."
    c "Walter... a difficult, arrogant, unbearable man."

    p "That sounds complicated. But I know you can handle him."

    hide camila_brava
    show camila_normal at camila_maior_direita_baixo
    c "Thank you, love. Your support helps me a lot."

    hide camila_normal
    show camila_olhando_lado at camila_maior_direita_baixo
    c "Even so, sometimes I wonder what awaits me when I get home..."

    p "What do you mean?"

    hide camila_olhando_lado
    show camila_sedutivo at camila_maior_direita_baixo
    c "Will we have some time just for us tonight? I’ve been missing something... more intimate."

    p "Camila, I really want to... but I’m exhausted today. I can’t."

    hide camila_sedutivo
    show camila_triste at camila_maior_direita_baixo
    c "I understand... I just feel sad when you don’t want to."
    c "It feels like you’re drifting away from me."

    p "That’s not it, love. I’m just really tired."

    c "Am I not enough for you anymore?"

    hide camila_triste
    show camila_olhando_lado at camila_maior_direita_baixo
    c "I’m going to rest for a while... I came home early just to be with you."
    c "But it’s okay, I understand."

    "You feel an emptiness in your chest as Camila walks away, the tension in the air almost tangible."
    "Maybe not everything is as it seemed..."

label dia_seguinte:

    scene black
    with fade
    "The next day..."

    scene fundo_casa
    with fade

    "You call out for Camila, but she doesn’t answer."
    p "Camila?"

    "You realize she has already left for work."
    "You notice she forgot the lunch she always takes every day."
    p "She must have been in a big hurry."

    "You decide to take her lunch to the hospital."

    stop music fadeout 1.0
    scene recepcao_hospital
    with fade

    "You arrive at the hospital reception and look for Camila, but you can’t find her."

    show mary_normal at mary_maior_direita_baixo
    m "Welcome! Are you lost? How can I help you?"

    p "Hello! I’m looking for Camila. She forgot her lunch at home, so I brought it for her."

    hide mary_normal
    show mary_chocada at mary_maior_direita_baixo
    m "You’re Camila’s husband? I didn’t even know she was married!"

    p "What do you mean? She never mentioned it? That’s strange..."

    hide mary_chocada
    show mary_normal at mary_maior_direita_baixo
    m "Anyway, she must be with a patient right now. Follow me."

    scene corredor_hospital
    with fade

    show mary_normal at mary_maior_direita_baixo
    m "She’s indeed with a patient. Do you prefer to wait here or go to her now?"

menu:
    "Go to Camila":
        jump ir_ate_camila
    "Wait":
        jump retorno_casa_esperar


label ir_ate_camila:

    show mary_neutra at mary_maior_direita_baixo
    m "I'll check who she's with now..."

    show mary_nervosa at mary_maior_direita_baixo
    m "Walter... That man is horrible. Poor Camila..."


    p "What do you mean?"

    m "Listen carefully. You, as her husband, need to do something!"
    m "That man, as old and sick as he is, needs to know his limits!"
    m "I'll take you to their room..."
    m "See if you can make him stop being so disrespectful!"

    p "Okay..."

    play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7

    scene fundo_hospital
    with fade

    "You enter and call out for Camila..."

    show camila_uniforme_surpresa at camila_maior_direita_baixo
    c "Honey??? W-what are you doing here???"

    p "I came to bring you your lunch, you forgot it at home today, honey."

    show camila_uniforme_sorrindo at camila_maior_direita_baixo
    c "You're always so thoughtful, thank you so much, sweetheart!"

    p "No problem! And who would this be by your side?"

    show walter_neutro at Position(xpos=0.90, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    show camila_uniforme_brava at camila_maior_direita_baixo zorder 10
    c "This is Walter! A patient here at the hospital, the one I told you about."

    "You notice that they are very close to each other."

    w "Hello! Camila has told me a lot about you, you know!"

    p "Oh, great! What exactly did she say?"

    w "She said that you love her very much too. How could anyone not love such a beauty, right young man?"

    show camila_uniforme_desgosto at camila_maior_direita_baixo zorder 10
    p "She really is enchanting! There's no way not to love her!"

    show walter_safado at Position(xpos=0.90, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "I completely understand you! Hehehe."


    stop music
    scene black
    play sound "audio/gemido.mp3" volume 5.0
    show Pegando at truecenter
    with fade
    pause 1.5

    play music "audio/romantic_music.mp3" loop fadein 1.0 volume 0.7
    scene fundo_hospital
    show camila_uniforme_assustada at camila_maior_direita_baixo zorder 10

    show walter_safado at Position(xpos=0.90, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)

    "You hear a moan from Camila at that instant."

    c "{i}I can't believe he's grabbing my butt in front of my husband! Honey! Do something!{/i}"

    menu:
        "What do you do?"
        "Where are you putting your hand, Walter!?":
            jump mano_walter
        "What happened, honey?! ({color=#C71585}NTR{/color})":
            jump pergunta_camila

    label mano_walter:

    show camila_uniforme_envergonhada at camila_maior_direita_baixo zorder 10

    show walter_dor at Position(xpos=0.90, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "I have spasms in my hand, I’m terribly sorry!"
    w "I’m old and, because of my illness, I can’t control parts of my body..."


    show camila_uniforme_nojo at camila_maior_direita_baixo zorder 10
    c "{i}As if my husband would believe something like that!{/i}"

    p "I understand, Walter! I know very well how it is! Old age comes for all of us, right?"

    c "{i}I can't believe this!{/i}"

    show walter_neutro at Position(xpos=0.90, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "Certainly, young man! You’re lucky to have a beautiful lady to keep you company!"

    jump corredor_hospital


label pergunta_camila:

    show camila_uniforme_assustada_falando at camila_maior_direita_baixo zorder 10
    c "L-l-love, s-so..."


    p "Are you not feeling well?"

    c "N-n-no, that’s not it..."

    show walter_neutro at Position(xpos=0.90, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "She’s just very tired, she always works hard to take care of me..."

    w "I’m very grateful to her!"

    p "I see, it seems you two are getting along well, my love! I’m very happy about that!"

    show camila_uniforme_desgosto at camila_maior_direita_baixo zorder 10
    c "Yeah, we’re getting along just fine! Pff!"


label corredor_hospital:

    stop music fadeout 1.5

    scene corredor_hospital
    with fade

    p "I don’t know why Camila doesn’t like him..."
    p "He seems to be such a good person..."

    show mary_normal at mary_maior_direita_baixo
    m "Hi! How did it go in there?"

    p "Everything went fine!"

    m "And about Walter? What about him?"

    show mary_nervosa at mary_maior_direita_baixo
    m "Did you do something? Did you tell him to stop touching the nurses???"

    p "No, why would I do that??? He’s sick..."
    p "It’s not his fault..."

    m "I can’t believe it!"
    m "You really are useless!!!"

    hide mary_normal
    hide mary_nervosa

    p "Mary leaves angrily, stomping her feet."
    p "That girl is so temperamental, like a child..."
    p "Well, now I have to go home..."

    jump retorno_casa

label retorno_casa_esperar:
    
    scene recepcao_hospital with fade
    "You wait for quite a while..."
    "..."
    p "I guess she’s not coming, I’d better take the lunchbox back home..."
    scene black with fade
    "Arriving home..."
    scene fundo_casa
    p "Unfortunately I couldn’t deliver it, I need to make sure she takes it tomorrow..."
    p "Anyway... I need to work now..."

    jump retorno_casa2

label retorno_casa:

    scene fundo_casa
    with fade

    p "I really can’t understand that red-haired nurse..."
    p "They should treat sick people better in that hospital."
    p "Camila really knows how to take good care of the patients."
    p "She’s always so attentive..."
    p "The patients in that hospital are lucky to be treated by her..."
    p "Anyway, now I have to go to work..."


label retorno_casa2:

    scene black
    with fade

    "10 hours later"

    scene fundo_casa
    with fade

    p "Aaaaah, finally home!"
    p "Honey, I’m home!"

    c "Come to the bedroom, darling! I have a surprise for you!"

    play music "audio/casual_music.mp3" loop fadein 1.0 volume 0.7

    scene fundo_quarto
    with fade

    show camila_quarto at camila_maior_direita_baixo
    c "Welcome!"

    p "Wow, what are you wearing?"

    c "Just something to please you! Do you like it?"

    p "But of course! You look beautiful!"

    c "Tonight I’m all yours! The whole night! Will you use me a lot tonight?"


    menu:
        "Absolutely!":
            $ resposta = "sim"
        "Not today... ({color=#C71585}NTR{/color})":
            $ resposta = "não"

    if resposta == "sim":

        show camila_quarto_sorrindo at camila_maior_direita_baixo

        c "Perfect, love! I love you so much! I really want to satisfy you tonight! The whole night!"

        c "Please, sit down, leave the rest to me!"


        scene black
        with fade
        show quarto
        with fade

        c "Darling... it's been so long since we did anything..."
        p "Sorry, darling, I've been very busy with work..."
        c "It's okay! But know that I’m always here to please you, okay?!"
        p "O-o-ok..."
        p "Wow, she’s so sexy."

        scene black
        with fade
        show quarto1
        with fade

        c "Where should we start? Hehehe. I really want to see what you have saved for me..."

        scene black
        with fade
        show quarto2
        with fade

        c "I’ll help you... This zipper is so tricky..."

        scene black
        with fade
        show quarto3
        with fade

        c "Well, well, well... Isn’t this my darling... Maybe it would be better if..."

        scene black
        with fade
        show quarto4
        with fade

        c "I touch it like this? Do you like it?"
        p "O-of course..."

        scene black
        with fade
        show quarto5
        with fade

        c "Do you like me touching it?"
        p "V-v-very much... It feels so good..."
        p "It’s so hard to hold back with her touching like this... Looking at me this way..."

        jump scene_loop

    else:
        show camila_quarto_triste at camila_maior_direita_baixo
        c "Ah, it’s okay, love. Maybe another time then..."
        jump hospital2


    transform centralizado_cima:
        anchor (0.5, 0.5)
        align (0.5, 1.0)

label scene_loop:

    show anim_quarto at centralizado_cima

    p "My god! This feels amazing!"
    c "Are you enjoying it?"
    p "So much...."
    c "I can't wait to use it..."
    p "I think I'm about to cum...."


label cena_pos_animacao:

    scene expression Solid("#000000") with fade
    show gozandoquarto at centralizado_cima
    hide animacao_loop

    show gozandoquarto at centralizado_cima

    p "Aargh..."

    # Troca para a próxima imagem sobre o fundo preto
    scene expression Solid("#000000") with fade
    show gozadoquarto at centralizado_cima

    c "{i}I can't believe this!{/i}"
    show brava at centralizado_cima
    c "But you-"

    p "I can't take it anymore, lo-..."

    "You fall asleep..."

    c "I prepared for a whole night"

    show infeliz at centralizado_cima

    c "Looks like it won’t be tonight either..."

    c "He fell asleep, unfortunate..."

    scene fundo_quarto with fade

    "You wake up after a good night's sleep"

    "You look beside your bed, and realize your wife has already gone to work"

label hospital2:

    scene black with fade

    "The next day..."

    scene fundo_hospital with fade

    show camila_uniforme_desgosto at camila_maior_esquerda_baixo2
    show walter_neutro at Position(xpos=0.85, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    stop music fadeout 1.0

    w "Wow! Why the long face so early today?"

    c "None of your business!"

    w "What a feisty kitty!"

    show walter_safado at Position(xpos=0.85, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "Looks like someone’s missing to tame her!"

    c "Don’t come at me with your nonsense!"

    w "Let me help you..."

    "Walter tries to touch Camila, to calm her down..."

    c "G-g-get away! I’m not in the mood today!"

    c "Just let me do my work, okay!!!"

    "Camila turns around and starts filling out her clipboard..."


    scene black with fade
    show bunda at truecenter

    play music sensual_music fadein 1.0 volume 0.7

    w "Wow..."

    w "What is this..."

    w "You are definitely the best around here..."

    c "{i}This old man doesn't stop saying nonsense...{/i}"

    w "I think I know what's going on here..."

    c "{i}Hahaha! As if he knows...{/i}"
        
    w "I don't think you're getting what you deserve..."

    w "From what I saw of your husband, he probably doesn't give you what you deserve..."

    c "{i}He doesn't know anything!!!{/i}"

    w "I think what you deserve is some slaps!!!"

    scene black
    show bunda1 at truecenter
    play sound "audio/gemido2.mp3"
    pause (2.5)

    show bunda2 at truecenter

    w "Ho-ho-ho..."
    w "What moan did I just hear?"
    c "{i}Idiot...{/i}"
    w "Looks like someone liked it, huh?"
    c "As if!"
    w "So what exactly did I just hear?"

    show bunda3 at truecenter

    c "N-n-nothing! You must be imagining things!"
    w "I must be imagining things then..."
    w "Being taken care of by such a beautiful young lady like you, it can only be an illusion! Hahaha"
    c "I'm not that young..."
    w "What? Hahaha"
    w "I've never seen such a beautiful body in my life!"
    w "Your husband is one lucky guy!"
    c "{i}I've never heard him say things like that...{/i}"
    w "If I were him, I would use your body every day!"
    c "Stop saying nonsense..."
    c "Stop saying nonsense..."
    c "{i}In the end, he's just a horny old man... I guess...{/i}"
    c "I'm going to attend another patient!"
    w "Bye-bye! Hehehe"

    stop music fadeout 1.0

    scene corredor_hospital with fade
    c "{i}I must be tired...{/i}"
    c "{i}I don't know what's going on with me today...{/i}"

    scene black with fade
    "4 hours later..."

    scene fundo_hospital with fade

    show camila_uniforme_brava at camila_maior_esquerda_baixo2
    c "I'm back, Walter!"

    c "Walter?"

    show walter_dor at Position(xpos=0.85, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "Ah... Hi sweetie..."
    w "I have terrible back pain..."

    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo2
    c "{i}Poor thing...{/i}"
    c "Do you want some medicine for relief?"

    w "No... I'm tired of medicine..."

    c "Can I help you in any way?"

    show walter_triste at Position(xpos=0.85, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "Could you give me a massage?"

    c "I'm not sure if it's appropriate..."

    show walter_dor at Position(xpos=0.85, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "Ouch..."
    w "It hurts too much..."

    c "{i}I guess it's my duty to help him...{/i}"
    c "Alright..."

    show walter_safado at Position(xpos=0.85, ypos=0.6, xanchor=0.5, yanchor=0.5, zoom=0.8)
    w "Thanks, sweetie... Hehehe"

    c "Turn over..."
    c "It'll be quick, ok! My shift is over!"

    w "No problem..."

    scene black with fade
    "Meanwhile..."
    scene fundo_casa with fade
    p "I'm home, love!"
    p "Darling?"
    "That's strange..."
    "She should have been here already..."
    p "Darling???"
    "Really, no sign..."
    "Could she still be working?"
    "Maybe there's a problem with her car?"
    "I'll try calling her..."
    "Calling..."
    "..."
    "Call not answered..."
    "Better go pick her up..."

    
label perspectiva1:

    scene black with fade
    menu:
        "Choose the perspective"
        
        "[player_name]":
            jump scene_steve1

        "Camila":
            jump scene_camila12


label scene_camila12:

    scene black with fade
    play music sensual_music fadein 1.0 volume 0.7
    show costas1 at zoomout

    c "{i}Huh???{/i}"
    c "{i}What kind of muscles are those???{/i}"
    c "{i}I...{/i}"
    c "{i}I had no idea he was like this...{/i}"

    hide costas1

    show costas2 at truecenter

    w "Are you going to help me with my pain, sweetie?"
    c "O-of course!!"

    scene black

    show massagem1 at top_center

    c "{i}I feel like...{/i}"
    c "{i}I shouldn't be doing this...{/i}"

    show massagem2 at top_center

    c "{i}Wow...{/i}"
    c "{i}It's so...{/i}"        
    c "{i}Firm...{/i}"    
    c "{i}How does an old man like him have these muscles?{/i}"    
    c "{i}I can't imagine...{/i}"

    show massagem3 at top_center

    c "{i}Does he train here at the hospital?{/i}"   
    c "{i}Lift weights or something like that?{/i}"   

    show massagem4 at top_center

    c "{i}I...{/i}"   
    c "{i}I've never touched a body this rigid before...{/i}"  

    show massagem5 at top_center

    w "Could you start the massage now, please?"

    show massagem6 at top_center

    c "O-o-of course..."
    c "S-sorry..."

    show massagem7 at top_center

    w "Hmmmmm..."    

    show massagem8 at top_center

    c "{i}I hope he didn't find it weird...{/i}"  
    w "Right there..."    
    w "Hmmm...Hmmm..."  

    show massagem9 at top_center

    c "{i}Phew...{/i}"      
    c "{i}What a relief...{/i}"    

    show massagem10 at top_center

    w "I have the feeling someone liked what they saw, huh?" 

    show massagem11 at top_center

    c "{i}I can't believe it...{/i}"   
    c "{i}He noticed...{/i}"   

    show massagem12 at top_center

    c "I-it's just that..." 
    c "I was just distracted..."  
    c "That's all..."
    
    show massagem13 at top_center

    w "Distracted by what exactly?" 
    c "{i}I don't even know how to respond...{/i}"
    w "Not used to seeing men like me?"      
    w "A real man"

    show massagem14 at top_center

    c "Stop talking nonsense!"

    show massagem15 at top_center

    c "I think the massage is done for today!"

    $ persistent.unlocked_scene1 = True
    scene black with fade
    show bundah1 at top_center

    "Camila turns and starts filling in what she did on her clipboard to finish her shift"
    c "I'm leaving already, I shouldn't even be doing this at this hour..."
    w "Look at me, my little angel..."
    w "Look what you did to me..."

    show bundah2 at top_center

    c "I told you to stop saying those things!!!"

    show bundah3 at top_center

    c "{i}M-m-my god...{/i}"
    c "{i}What's that bulge in his pants???{/i}"    
    c "{i}It can't be...{/i}"
    w "Could you help me with that too?"


define slow_dissolve = Dissolve(3.0)  # 3 segundos para aparecer lentamente


label scene_camila1:

    scene black
    stop music fadeout 1.0
    play music romantic_music fadein 1.0 volume 0.7
    show h1 at zoom176 with slow_dissolve


    c "{i}My god...{/i}"
    c "{i}What is this...{/i}"
    c "{i}It looks like it's going to tear his pants...{/i}"
    w "What's wrong? Could you help me with this?"
    w "Argh..."    
    w "It hurts when it's like this, I need relief..."    

    show h2 at zoom176
    c "{i}He looks like he's in a lot of pain...{/i}"
    w "I haven't been able to relieve myself for days..."
    w "It hurts so much..."
    c "{i}Poor thing...{/i}"
    w "Curious to see?"

    show h3 at zoom176
    c "{i}He seems eager to get out...{/i}"
    c "{i}Could it be...{/i}"
    w "Let me take him out..."

    scene black at zoomout176
    show h4 at zoom176
    c "{i}!!!!!!!!!!!!!!!!!{/i}"
    c "{i}What is this!!???{/i}"    
    c "{i}I've never seen anything like this!!!{/i}"   
    w "Scared, my sweetie?"

    show h5 at zoom176
    c "I-I-I t-t-that's..."       
    c "{i}I don't even know what to say!!!{/i}"         
    w "Never seen one this big?"

    show h6 at zoom176
    c "N-n-no! Not that!"      
    c "Nothing like that!" 

    show h7 at zoom176
    w "Well, I think it is..."
    w "Be honest with yourself"
    c "{i}It looks so... rigid... firm...{/i}"
    c "{i}It doesn't even seem real...{/i}" 
    w "Curious?"
    w "Want to touch it?"

    show h8 at zoom176
    w "Go ahead! Touch it..."    
    w "Feel free..." 

    show h9 at zoom176
    w "That's it..."
    c "{i}It's so hard...{/i}" 

    show h10 at zoom176    
    c "{i}I shouldn't be doing this...{/i}" 
    c "{i}What would my husband think of me?{/i}" 
    w "Hold it tight!"
    w "Now!"

    show h11 at zoom176
    w "Good girl!"
    c "{i}I don't know what's happening to me...{/i}"
    c "{i}When he makes me do things like this...{/i}"
    c "{i}I feel strange...{/i}"
    c "{i}Hot...{/i}"  
    c "{i}I can't refuse...{/i}"

    show h12 at zoom176
    w "Why not start the massage already?"  
    c "{i}My god... I don't know if I should...{/i}" 
    c "I-I-I c-c-can't..."
    w "Start now!"

    scene black
    show mvhosp1 at zoom176
    show h12 at cortar_topo
    w "That's it... very good..."
    c "{i}What am I doing!?{/i}"
    c "{i}I know I shouldn't...{/i}"
    c "{i}But...{/i}"           
    c "{i}I don't know what's happening to me...{/i}" 
    
    show h13 at cortar_topo
    c "{i}I have to finish this quickly!{/i}"
    c "{i}I can't keep touching this thing...{/i}"
    w "That's it, sweetie..."          
    c "{i}Speed it up...{/i}"

    scene black
    show mvhosp2 at zoom176
    show h14 at cortar_topo
    c "O-ok!"
    c "{i}Let's see how long he can last!{/i}"    
    c "Ho-ho ho!"
    c "Just the way I like to see it!"    

    scene black with fade
    "..."
    "After a long time..."

    scene black with fade
    show mvhosp3 at zoom176
    show h15 at cortar_topo

    w "That's it! Faster!"
    c "{i}My arms can't take it anymore!!!{/i}"     
    c "{i}This old man will never climax!?{/i}"   
    c "{i}This old man will never climax!?{/i}"
    w "Keep going! Don't stop!"
    c "{i}Please... I just want him to finish already...{/i}"
    w "I-I-I'm almost there..."    

    scene black with fade
    pause (0.7)
    scene black
    show h14 at zoom176
    pause (0.5)
    scene black with fade
    pause (0.5)
    scene black
    show h14 at zoom176
    pause (0.3)
    scene black with fade
    pause (0.2)
    scene black
    show h16 at zoom176 
    pause (2.0)

    scene black with fade
    show h18 at zoom176
    c "{i}How much...{/i}"    
    c "{i}How is this possible...{/i}"
    w "Hmmmm... thank you, sweetie..."     
    show h19 at zoom176
    c "{i}What did I just do...{/i}" 
    c "{i}I can never do something like this again...{/i}"
    w "Now, could you clean it up?"
    show h20 at zoom176
    c "Turn around!"        
    c "You clean it yourself!"

    $ persistent.unlocked_scene2 = True

    jump scene_casa

label scene_steve1:

    scene black with fade
    "Arriving at the hospital..."
    "It's pretty empty..."
    scene corredor_hospital with fade
    p "{i}Where is that red-haired nurse...{/i}"
    p "{i}Maybe she can help me...{/i}"
    scene black with fade
    "After searching the corridors for a long time..."
    scene corredor_hospital with fade
    p "{i}Can I check the patients' rooms?{/i}"
    p "{i}I don't know...{/i}"   
    p "{i}I guess it's forbidden... Or... not?{/i}"
    
    menu:
        "What do you do?"
        
        "Look for Camila in the corridors ({color=#C71585}NTR{/color})":
            jump scene_steve_procurar

        "Go back and wait for her at home":
            jump scene_casa

label scene_steve_procurar:

    scene corredor_hospital
    p "{i}Maybe she's around here...{/i}"
    p "{i}No...{/i}"
    p "{i}Maybe over here...{/i}"
    p "{i}Nothing here either...{/i}"
    "Until you find a room with the lights still on..."
    p "{i}She must be here...{/i}"
    scene black with fade
    show stevehospital at truecenter with Fade(1.0, 0.2, 1.0)
    p "{i}Could that be Camila?{/i}"
    p "{i}I can't see clearly...{/i}"
    p "{i}In the end, she's just taking care of a patient...{/i}"              
    p "{i}So dedicated...{/i}"   
    p "{i}I really am a lucky guy...{/i}"
    p "{i}I won't disturb her, better head back home...{/i}"

label scene_casa:

    stop music
    scene fundo_casa
    "A few hours later..."
    "You were already home, waiting in the living room..."
    "Until the door opens."

    show camila_uniforme_sorrindo at camila_maior_direita_baixo with dissolve
    c "I'm home, love..."

    p "Hi love. I was waiting for you..."

    c "Sorry for the delay... today work was really tiring."

    p "I can imagine... the hallways were quite empty when I passed by."

    show camila_uniforme_assustada at camila_maior_direita_baixo
    c "...!" 
    c "{i}I can't believe it... He was there!?{/i}"  

    show camila_uniforme_assustada_falando at camila_maior_direita_baixo
    c "You... went to the hospital?"

    p "Yes, I went looking for you. But I couldn't find you anywhere."

    show camila_uniforme_vergonha2 at camila_maior_direita_baixo
    c "Ah... I must have been busy in one of the rooms with a patient..."
    c "I was taking care of some things before finishing my shift."

    p "I see... I thought it better to come back home and wait for you."
    p "You looked very dedicated from afar... I'm proud."

    c "...Thank you..." 
    c "It's just... I really try to do my best there."

    menu:
        "What do you do?"
        
        "Ask what she was doing":
            jump scene_casa_pergunta

        "Go to sleep":
            jump scene_casa_dormir

label scene_casa_pergunta:

    show camila_uniforme_vergonha2 at camila_maior_direita_baixo
    p "But tell me, what exactly were you doing in there?"

    c "Uh... well... I... was just helping an elderly patient..."
    c "He needed some extra care..."

    show camila_uniforme_assustada at camila_maior_direita_baixo
    c "{i}I need to be careful... I can't let anything slip!{/i}" 

    p "I see... you are really dedicated, Camila."

    c "Thank you, love..."

    "The night continues with a light tension in the air..."
    jump scene_casa_fim

label scene_casa_dormir:

    show camila_uniforme_vergonha2 at camila_maior_direita_baixo

    p "It's late... I think we should go to sleep."

    c "Yes... you're right. I'm really exhausted."

    "You both head to the bedroom together."
    "Camila seems relieved not having to talk more about the hospital."
    jump scene_casa_fim

label scene_casa_fim:

    scene fundo_quarto with fade
    "The night continues quietly..."
    "But inside Camila, guilt and shame still burn silently."

    scene black with fade
    "The next day..."

    scene recepcao_hospital with fade
    "..."
    show camila_uniforme at camila_maior_esquerda_baixo4

    show mary_falando at camila_maior_esquerda_baixo3
    m "So, Camila! Today I really need you at the reception, ok?"

    show mary_normal at camila_maior_esquerda_baixo3
    c "Ah, of course Mary... no problem."

    show mary_falando at camila_maior_esquerda_baixo3   
    m "You've been spending a lot of time in the rooms lately, haven't you?"

    show camila_uniforme_assustada at camila_maior_esquerda_baixo4
    c "M-me? Hm... I was just helping a few patients who needed attention..."

    show mary_falando at camila_maior_esquerda_baixo3       
    m "Yes, I know. But remember that our priority here is organization, service, and discipline."
    m "Doctors can handle certain things. You need to be here, on the front line."

    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
    c "O-of course... I'll focus on that today."

    show mary_falando at camila_maior_esquerda_baixo3   
    m "Good girl. I know you're hardworking."

    show mary_normal at camila_maior_esquerda_baixo3     
    "Mary smiles, but her gaze keeps assessing Camila, as if suspicious of something."

    show camila_uniforme_assustada at camila_maior_esquerda_baixo4
    c "{i}Did she notice something...?{/i}"
    c "{i}No... it can't be... I need to stay calm.{/i}"

    scene black with fade
    show nurse1 at zoom1762
    "Some time passes..."
    p "Hi my love!"
    show nurse2 at zoom1762
    c "Love? What are you doing here?"
    show nurse3 at zoom1762
    p "I... came to see you. I thought you might be off the counter now."
    show nurse4 at zoom1762
    c "[player_name]... you shouldn't be here... visitors don't usually stay at the reception."
    show nurse3 at zoom1762
    p "Ah, but I just wanted to see you for a bit... you know, I missed you."
    show nurse4 at zoom1762
    c "...I missed you too, but you can't stay long."
    show nurse5 at zoom1762
    p "{i}Is that the patient from last time back there?{/i}"
    p "{i}Shouldn't he be in bed?{/i}"

    scene black
    show pegandob1 at top_center with fade
    play music romantic_music fadein 1.0 volume 0.7
    w "{i}Wow...{/i}"  
    w "{i}It was worth coming here for a little visit at the reception...{/i}"
    scene black with fade  
    show pegandob1 at esquerda_topo_menor
    show nurse4 at zoom1762
    c "Anyway... thank you for coming to see me..."
    p "No problem..."
    hide pegandob1
    show pegandob2 at esquerda_topo_menor
    show nurse6 at zoom1762
    c "!!!!!!!!!!"    
    p "What is it, dear?"
    c "{i}I can't believe Walter is here...{/i}"    
    c "{i}Not now...{/i}"
    p "What happened?"
    show pegandob2 at esquerda_topo_menor
    show nurse11 at zoom1762
    c "N-nothing!"
    p "Strange, her expression changed all of a sudden..."
    c "{i}Walter... You need to leave right now...{/i}"
    w "{i}That butt... deserves a squeeze!{/i}"
    hide pegandob2
    show pegandob3 at esquerda_topo_menor
    show nurse9 at zoom1762
    c "{i}!!!!!!!!!{/i}"    
    c "{i}My husband is in front of me!!!{/i}"    
    c "{i}I can't believe he's doing this...{/i}"    
    p "Are you really okay, dear?"
    p "You don't look well..."
    show nurse10 at zoom1762
    c "I-I'm fine..."
    hide pegandob3
    show pegandob4 at esquerda_topo_menor
    show nurse12 at zoom1762
    w "{i}What a delicious butt...{/i}" 
    c "{i}He needs to stop...{/i}"  
    c "{i}My husband will notice...{/i}"
    p "Well... alright then..."
    p "It must have been just my impression..."
    show nurse13 at zoom1762
    c "Yes dear..."
    c "Nothing to worry about..."
    hide pegandob4

    w "Later I'll play with you more..."
    show pegandob5 at esquerda_topo_menor
    show nursel at zoom1762
    pause 2.0
    hide pegandob5
    hide nursel
    show nurse12 at zoom1762
    c "!!!!!!!!"     
    p "Did you say something?"
    show nurse11 at zoom1762
    c "N-n-n-no dear..."
    p "I thought I heard something..."
    p "A sound of something hitting too..."
    c "{i}I can't believe he hit my butt in front of my husband...{/i}"   
    c "I-I think it was just your imagination, dear..."   
    p "Yeah... I think so..."
    show nurse13 at zoom1762
    p "Well... I need to go..."
    p "It was great seeing you, keep doing your best here!"
    c "O-of course... bye..."

    $ persistent.unlocked_scene3 = True
    stop music



scene black with fade

"Camila watches her husband walk away, her heart pounding."

c "{i}I can't believe Walter did that... right in front of him.{/i}"
c "{i}What if he noticed? What if he starts asking questions...?{/i}"

"She glances toward the hallway where Walter disappeared."

c "{i}I need to talk to him. I need to make sure this doesn't happen again.{/i}"

scene locker_room with fade

"Camila changes out of her uniform slowly, her hands trembling slightly."

c "{i}This is getting out of control...{/i}"
c "{i}I didn’t ask for this. I didn’t want this.{/i}"

"She sits on the bench, staring at the floor."

c "{i}But I didn’t stop him either...{/i}"

"Camila steps outside into the cool night air."

"The parking lot is quiet. Her car waits under the dim lights."

"She opens the door, sits inside, and exhales deeply."

c "{i}Tomorrow... I’ll keep my distance.{/i}"
c "{i}I’ll stay professional. I have to.{/i}"

scene fundo_quarto with fade

"Camila enters the bedroom slowly, the house silent."

"Her husband is already asleep, facing away from her."

"She changes quietly, folding her uniform with care."

c "{i}I don’t want to think about Walter...{/i}"
c "{i}I just need to sleep. Reset. Forget.{/i}"

"She slips under the covers, staring at the ceiling."

"Her eyes remain open for a long time."

c "{i}But I can still feel his...{/i}"
c "{i}The way he touched me... the way he looked at me...{/i}"
c "{i}Why didn’t I stop him?{/i}"

"She turns to her side, closing her eyes slowly."

c "{i}I need to be stronger tomorrow...{/i}"

scene black with fade
"The night passes slowly, filled with quiet unrest."


#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#

scene black with fade

"Next day..."
"Camila wakes up early, her eyes heavy from a restless night."

scene locker_room with fade

"..."

"Camila enters the locker room, still adjusting her bag on her shoulder."

"She looks around briefly, making sure no one else is there."

"With a quiet sigh, she opens her locker and begins changing into her uniform."

c "{i}Another day... I need to stay focused.{/i}"

"She ties her hair back, glancing at her reflection for a moment."

"Her phone buzzes — a notification. But it's not from her husband."

"She locks her phone, closes the locker, and heads out to start her shift."


scene corredor_hospital with fade

"..."
show adriannormal at camila_maior_esquerda_baixo5
a "Morning, Camila."
show camila_seria at camila_maior_esquerda_baixo4
c "Morning, Dr. Adrian."
a "You look... tired."
c "Just didn’t sleep well."
a "If you need a break later, let me know. I’ll cover for you."

show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
c "Thanks, but I’ll manage."
a "Still... I’m here if you need anything."

"Camila nods, keeping her eyes on the floor."
c "{i}Why does he always notice...?{/i}"

scene nurse_station with fade

"Camila reviews patient charts, her fingers trembling slightly."

"She sees Walter’s name on the list. Room 14."

c "{i}He’s still here...{/i}"
c "{i}Just do your job. Don’t react.{/i}"

"She closes the folder and walks away."

scene break_room with fade

"Camila enters the break room quietly, hoping to have a moment alone."

show camila_seria at camila_maior_esquerda_baixo4
"She pours herself some water and sits down, lost in thought."

"Footsteps echo softly behind her."

"Adrian walks in, notices her, and approaches slowly."
show adriannormal at camila_maior_esquerda_baixo5
a "You sure you’re okay?"
show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
c "I said I’m fine."
a "I know. But you don’t have to be."

"Camila looks at him, surprised by the softness in his voice."
c "It’s complicated."
a "You don’t owe me an explanation. I just want you to know... I see you."

"Camila doesn’t respond. She just nods, slowly."

c "{i}Why does that feel... comforting?{/i}"

"Adrian gives her a gentle smile, then walks away, leaving Camila alone in the break room."

"She stays seated for a moment, gathering herself."

"After a deep breath, Camila grabs her bag and heads out of the hospital."

scene black with fade
"Camila walks home under the dim evening sky, her thoughts still tangled."
c "{i}I need to keep it together...{/i}"
c "{i}Just get home, act normal...{/i}"

scene fundo_quarto with fade
show camila_seria at camila_maior_esquerda_baixo4

"Camila enters the bedroom slowly, her bag slipping from her shoulder."

"Her husband is sitting on the bed, scrolling through his phone."

p "Hey. You're late."
c "Yeah... long shift."

p "Everything okay at work?"
c "Just... a lot going on."

p "You look tired."
c "I am."

"She sits on the edge of the bed, rubbing her temples."

p "You want to talk about it?"
c "Not really. I just want to rest."

p "Alright. I won’t push."

hide camila_seria

"Camila nods, grateful for the silence, but also feeling the distance between them."

c "{i}He doesn’t ask much. He doesn’t notice much.{/i}"
c "{i}But at least he doesn’t make it worse.{/i}"

"Camila changes out of her uniform slowly, folding it with care."

"She slips under the covers, lying on her side, facing away from her husband."

"Her eyes remain open, staring into the dark."

c "{i}Adrian said he sees me...{/i}"
c "{i}Why did that feel so different?{/i}"
c "{i}Why do I keep thinking about it?{/i}"

"She closes her eyes, trying to quiet her thoughts."

scene black with fade
"The night passes slowly, filled with quiet unrest."

scene hospital_morning with fade
"Camila steps out of her car, the morning air crisp and quiet."

"She walks toward the entrance, her shoulders tense."

c "{i}Just another day. Pretend everything’s fine.{/i}"

scene corredor_hospital with fade
show camila_seria at camila_maior_esquerda_baixo4
show adriannormal at camila_maior_esquerda_baixo5

a "Morning."
c "Morning."
a "You seem... distant."
c "Just tired."
a "You said that yesterday."

"Camila hesitates."
c "I didn’t sleep well."
a "If you need to talk—"
c "I don’t."

"Adrian nods, backing off gently."
a "Okay. But I’m here."

"Camila walks past him, her steps quick."

c "{i}Why does he keep offering that?{/i}"

scene break_room with fade

"Camila sits alone, staring at her untouched coffee."


"She hears footsteps. Adrian enters, pauses, then walks to the counter."

show camila_seria at camila_maior_esquerda_baixo4
show adriannormal at camila_maior_esquerda_baixo5
a "I’ll grab mine and go. Didn’t mean to intrude."
c "You’re not intruding."

"Adrian turns, surprised."
a "You sure?"
c "I don’t know."

"Silence. Heavy, but not hostile."

c "{i}I don’t want to talk... but I don’t want to be alone either.{/i}"

scene fundo_hospital with fade

"..."
show walter_neutro at camila_maior_esquerda_baixo4
w "Morning, nurse. You look even better today."

show camila_seria at camila_maior_esquerda_baixo6
c "Please keep your hands to yourself."
w "I didn’t touch you. Not yet."

"Camila steps back, her voice firm."
c "I’m here to check your vitals. That’s all."
w "You’re tense. I could help with that..."

"Camila finishes quickly and exits the room, her heart racing."

scene corredor_hospital with fade

"..."

c "{i}I need to tell someone. But who?{/i}"

scene adrian_office with fade


show adriannormal at camila_maior_esquerda_baixo5
"..."

"Camila stands at the doorway, unsure."
a "Camila?"


show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
c "Can I sit?"

a "Of course."

"She sits down slowly, avoiding his eyes."
c "There’s a patient. He’s... making me uncomfortable."

a "Walter?"
show camila_uniforme_susto at camila_maior_esquerda_baixo4
"Camila looks up, startled."
c "How did you—"
a "I’ve seen the way he looks at you. I’ve seen your face after you leave his room."

show camila_uniforme_triste at camila_maior_esquerda_baixo4
"Camila’s eyes fill with tears, but she doesn’t cry."

c "I didn’t know who to tell."
a "You just did."

"Silence. Safe. Heavy. Real."

c "{i}Why does this feel like the first time I’ve exhaled in days...?{/i}"

"Adrian gives her a quiet nod and walks away, leaving Camila alone in the hallway."

"She stands there for a moment, gathering herself."

"Then, without a word, she grabs her bag and heads home."

scene black with fade

"Camila walks through the quiet streets, the city lights casting long shadows."

c "{i}I didn’t expect that...{/i}"
c "{i}Why did his words feel warmer than anything I’ve heard in days...?{/i}"

"She reaches her building, climbs the stairs slowly, and unlocks the door."

scene fundo_quarto with fade
show camila_seria at camila_maior_esquerda_baixo4

"Camila enters the bedroom, her steps slow and deliberate."

"Her husband is lying on the bed, shirtless."

p "Finally. I was starting to think you forgot you had a husband."
c "It was a long shift."

p "You must be exhausted. Everything okay at work?"

"Camila doesn’t respond right away. She begins changing out of her uniform."

p "You’ve been quiet lately."

c "Just tired. That’s all."

"Camila folds her uniform slowly, her hands tense."

p "Well, I’m glad you’re home. I missed you."

"Camila turns to face him briefly, then looks away."

c "Me too."

hide camila_seria

"Camila sits on the edge of the bed, her back to him."

c "{i}He doesn’t know. He doesn’t see. He only wants comfort.{/i}"
c "{i}And I’m too tired to pretend tonight.{/i}"


scene black with fade


"Camila wakes early, eyes open before the alarm."

"Her husband is still asleep beside her, one arm resting possessively across her waist."

"She gently shifts out from under it and sits at the edge of the bed."

c "{i}I told Adrian. And he listened.{/i}"
c "{i}But here... I still have to pretend.{/i}"

"She stands, grabs her robe, and walks toward the bathroom."

scene hospital_morning with fade

"Camila steps out of her car, the morning air cool against her skin."

"She walks toward the entrance, her thoughts already racing."

c "{i}Walter’s still here. Adrian’s still watching. And I’m still pretending.{/i}"

scene corredor_hospital with fade
"..."

show adriannormal at camila_maior_esquerda_baixo5
a "Morning."
show camila_seria at camila_maior_esquerda_baixo4
c "Morning."
a "You look... steadier today."
c "Trying to be."
a "That’s already something."

show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
"Camila nods, her gaze lingering for a moment longer than usual."

c "{i}Why does his presence feel like a pause in the storm?{/i}"


scene break_room with fade
show camila_seria at camila_maior_esquerda_baixo4
show adriannormal at camila_maior_esquerda_baixo5

"Camila sits alone, sipping coffee. Adrian enters, pauses, then sits across from her."

a "You sure you’re okay?"

c "I said I’m fine."
a "I know. But you don’t have to be."

"Camila looks at him, surprised by the softness in his voice."

c "It’s complicated."
a "You don’t owe me an explanation. I just want you to know... I see you."

"Silence. Heavy. Safe."

c "{i}Why does that feel... comforting?{/i}"

scene fundo_hospital with fade

show walter_neutro at camila_maior_esquerda_baixo4

w "Morning, nurse. You look even better than yesterday."
show camila_seria at camila_maior_esquerda_baixo6
c "I’m here to check your vitals. Please stay still."
w "You know, I dreamt about you last night. You were wearing less."

"Camila stiffens, but keeps her voice steady."
c "Keep your comments to yourself."
w "Why? You don’t seem to mind when I look."

"Camila finishes quickly, avoiding eye contact."
w "You’re tense. I could help with that..."
c "I’m leaving now."

"She turns to go. Walter reaches out — not enough to touch, but close."
w "I’ll be waiting for you, sweetheart."

scene corredor_hospital with fade
"..."
c "{i}He’s getting bolder. He’s testing boundaries.{/i}"
c "{i}I can’t keep ignoring this...{/i}"

show adrian_serio at camila_maior_esquerda_baixo5
a "Camila."

"She stops, startled."
a "I saw him. Through the door."

show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
c "He didn’t touch me."
a "But he wanted to. That’s enough."

"Camila looks down, ashamed."

c "I should’ve said something sooner."
a "You still can. I’ll back you up."

"She nods, slowly."

c "{i}Why does his voice make me feel like I’m not alone in this?{/i}"

scene break_room with fade

"Camila sits quietly, her coffee untouched. Adrian joins her again."

show adriannormal at camila_maior_esquerda_baixo5
a "You don’t have to carry this alone."

show camila_seria at camila_maior_esquerda_baixo4
c "I know. I just... I’m not used to being seen."
a "You deserve to be."

"Camila looks at him, something shifting behind her eyes."

c "{i}I don’t want to feel this way... but I do.{/i}"
c "{i}And I don’t know how to stop it.{/i}"

scene nurse_station with fade

"Camila hands Adrian a chart. He takes it, but his eyes linger on her."

show adriannormal at camila_maior_esquerda_baixo5
a "You know, you’re wasted here."
show camila_seria at camila_maior_esquerda_baixo4
c "What?"
a "You could be doing so much more. You’re smart. Beautiful. You just need someone to open the right doors."

"Camila frowns slightly."
c "I’m not looking for shortcuts."
a "I didn’t say shortcuts. I said opportunity."

"Camila watches him walk away, something unsettled in her chest."
c "{i}Why did that feel... transactional?{/i}"

label adrian_office1:

scene black with fade

"Later..."

scene adrian_office with fade

"Camila enters, hesitant."

show camila_seria at camila_maior_esquerda_baixo4
c "You said I could talk to you."
show adriannormal at camila_maior_esquerda_baixo5
a "Always."

"She sits. Adrian closes the door behind her — quietly, deliberately."
a "You know, I don’t do this for just anyone."
c "Do what?"
a "Listen. Care."

"Camila looks down, unsure."
show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
c "{i}Why does he keep reminding me how special I’m supposed to feel?{/i}"
a "You seem tense."
c "It’s been a long day."
a "I could help with that. Just a quick massage — nothing dramatic."

"Camila hesitates. Her eyes flick toward the door, then back to him."
c "You do that too?"
a "Only for nurses who sit in my office after hours."

"She lets out a soft breath, almost a laugh, and turns slightly in her chair."
c "Okay. Just... don’t make it weird."
a "Never."

"Adrian steps behind her, his hands hovering for a moment before resting gently on her shoulders."

label massage_scene:

scene black with fade
play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7
show amassagem1 at zoom1763

a "You're more tense than I expected."

c "It's just fatigue."

a "Fatigue doesn't only settle in your legs."

c "{i}Why am I so aware of every touch?{/i}"

a "I could help... if you let me."

c "Just... don't overdo it."

a "Never."

show amassagem2 at zoom1763

a "You deserve more care than you get."

c "You talk like you know me."

a "Maybe I know more than you think."

show massagemani at zoom1763

c "{i}He's really doing this... and I'm letting him.{/i}"

a "Just relax, Camila. Here, you don't have to pretend to be strong."

show amassagem5 at zoom1763
c "{i}I'm usually the one taking care of patients...{/i}"
c "{i}I’m not used to being the one cared for.{/i}"

label massage_extended:

show amassagem6 at zoom1763

a "I think I know what your problem is..."

show amassagem4 at zoom1763

c "I think it's just a strain or something."

show amassagem6 at zoom1763

a "Do you feel pain in your shoulders?"

show amassagem4 at zoom1763

c "Yeah... why?"

show amassagem7 at zoom1763

"Adrian moves his hands slightly lower, pressing near her upper chest — still within professional bounds, but close enough to make Camila freeze."

show amassagem8 at zoom1763

c "Where exactly do you think you're touching?"

show amassagem9 at zoom1763

a "Relax. It's purely professional."
a "I'm a doctor — I've done this a hundred times. It's normal."

show amassagem10 at zoom1763

a "There's nothing to worry about."

show amassagem11 at zoom1763

c "{i}Maybe he's right... maybe it's just clinical.{/i}"
c "{i}Still... it's embarrassing.{/i}"

scene black with fade
show amassagem10 at zoom1763

a "Is that shoulder pain something that comes back often?"

show amassagem12 at zoom1763

c "Yes..."

scene black
show amassagem10 at zoom1763

a "Hmm... it might be related to your posture. Or maybe the weight you're carrying."

show amassagem12 at zoom1763

c "(confused) What do you mean?"

scene black
show amassagem10 at zoom1763
a "(smirking) I mean physically. You're... well-endowed. That can cause tension in the upper back."

show amassagem11 at zoom1763
c "Oh..."

c "{i}Is he seriously saying that?{/i}"

show amassagem12 at zoom1763

c "So what am I supposed to do with them, then?"

scene black
show amassagem10 at zoom1763

a "I can take care of it. A massage there would help."

show amassagem12 at zoom1763

c "Just don't get carried away. Keep it professional."

scene black
show amassagem10 at zoom1763

a "Okay..."

show mvmassagem1 at zoom1764
show coberturamassagem1 at zoom1763

"Adrian's hands continue moving slowly, pressing into the tension along Camila’s upper back."

c "{i}His touch is firm... too firm to be casual.{/i}"

show coberturamassagem3 at zoom1763
c "Is this... really a massage?"

show coberturamassagem4 at zoom1763
a "(smirking) Technically, yes."

hide coberturamassagem4

show coberturamassagem3 at zoom1763
c "(frowning) Because it doesn’t feel like one."

show amassagem13 at zoom1763 with fade

c "{i}!!!!!{/i}"
c "{i}Is this... still a massage?{/i}"
c "{i}I don’t know if I should stop him or just... let it happen.{/i}"

show mvmassagem2 at zoom1764
show coberturamassagem5 at zoom1763

c "{i}His hands are so sure of themselves... like they’ve done this a thousand times.{/i}"
c "{i}It’s firm, focused... but not rough. Almost comforting.{/i}"
c "{i}Why does my body respond before my mind catches up?{/i}"
c "{i}I’m supposed to be in control. I’m the one who helps people relax — not the other way around.{/i}"
c "{i}But here I am... melting under his touch.{/i}"
c "{i}Is it wrong to want this? Or just... human?{/i}"
stop music
scene black with fade
show amassagem14 at zoom1763
play sound "audio/door_sound.mp3"
"Suddenly, a loud knock echoes through the office door."

show amassagem15 at zoom1763

a "(irritated) I think we should stop here."

a "Someone’s knocking."

a "(muttering) Always at the worst moment."

$ persistent.unlocked_scene4 = True

scene adrian_office with fade
"Adrian steps back, his jaw tight, eyes toward the door."
a "We'll continue the massage later. Until then..."
"Camila stands up quickly, adjusting her uniform, cheeks flushed."
c "(softly) Okay..."
"She walks out, avoiding eye contact, her steps quick and uneven."

scene locker_room with fade

"Inside the locker room, Camila leans against the wall, trying to catch her breath."

c "{i}What was that?{/i}"
c "{i}He knew exactly what he was doing... and I let him.{/i}"
c "{i}Was it care... or control?{/i}"
c "{i}Is he just taking advantage of me being vulnerable?{/i}"


scene black with fade

"Camila walks home, the city fading around her as her thoughts grow louder."

scene fundo_quarto with fade

"..."

p "Hey, you're late. Everything okay?"
show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4

c "(forcing a smile) Yeah... just a long shift."

p "Anything interesting happen?"

"Camila hesitates, then shrugs."
c "Just... the usual. Patients. Paperwork. A lot of tension."

p "You look tense."
c "(quietly) I know."

scene black with fade

"Camila sits on the edge of the bed, staring at her hands."

c "{i}I didn’t lie... but I didn’t tell the truth either.{/i}"
c "{i}And I don’t even know what the truth is right now.{/i}"


stop music

label camila_morning_drive:

scene black with fade

"Camila steps outside, the morning air cool against her skin. She unlocks her car, sliding into the driver’s seat."

"Her hands rest on the steering wheel for a moment before she starts the engine."

c "{i}Another day. Another performance.{/i}"

"The radio hums softly, but she barely hears it. Her eyes stay fixed on the road, the city passing in fragments — traffic lights, crosswalks, strangers rushing to their own lives."

c "{i}Everyone looks like they know where they’re going. I’m the only one pretending.{/i}"

"She grips the wheel tighter as her thoughts drift."

c "{i}Adrian’s words still echo. Walter’s eyes still linger. And at home... silence.{/i}"

c "{i}I’m tired before the day even begins.{/i}"

scene hospital_morning with fade

"She pulls into the hospital parking lot, cutting the engine. For a moment, she doesn’t move — just sits there, staring at the building."

"Finally, she straightens her uniform, forces her shoulders back, and steps out."

c "{i}Time to put the mask on again.{/i}"

label camila_shift:

    scene corredor_hospital with fade

    "Inside, the corridors are already alive with movement — nurses exchanging reports, patients calling, the steady rhythm of machines."

    c "{i}Keep moving. Don’t think. Just keep moving.{/i}"

    scene nurse_station with fade

    "Camila sorts through charts, her pen scratching across paper. The pile never seems to shrink."

    "A colleague passes by, offering a quick smile. Camila forces one back, then lowers her eyes again."

    c "{i}If I stop, even for a second, it’ll all catch up to me.{/i}"

    scene black with fade

    "She checks vitals, adjusts an IV, answers questions with practiced calm. Her body moves on instinct, her mind elsewhere."

    c "{i}Smile. Reassure. Pretend you’re not unraveling inside.{/i}"

    scene fundo_hospital with fade

    "Hours later, Camila slips into an empty hospital room. The lights are dim, the bed neatly made, untouched. She doesn’t bother turning anything on."

    label camila_exhaustion:

    "The room is silent, only the faint hum of distant machines in the corridor."

    "Camila enters slowly, her steps dragging. She doesn’t bother with coffee this time."

    "She leans forward against the side of the bed, both hands pressed flat on the mattress."

    c "{i}Just a minute... just one minute to breathe...{/i}"

    "Her head lowers until her forehead rests against her arms, her body still standing, weight slumped against the edge of the bed."
    scene black with fade
    show camila_dormindo1 at zoom1763

    label camila_interrupted:

    "Camila is asleep on her feet, leaning heavily against the bed, her forehead resting on her arms."

    "Adrian appears in the doorway, a file in his hand. He stops when he sees her."

    a "(quietly) Camila..."

    "He sets the file aside, his eyes narrowing as he studies her vulnerable posture."

    a "{i}What a perfect moment... she looks like she’s offering herself without even knowing it.{/i}"
    a "{i}Almost as if you do this on purpose, Miss Camila...{/i}"

    "He takes a slow step closer, his expression unreadable."

    "The door creaks open suddenly. Mary steps inside with a clipboard."

    m "Oh—Dr. Adrian? Camila?"

    "Adrian straightens immediately, his expression shifting back to professional calm."

    "He taps the bed firmly, waking Camila."

    a "(firmly) Camila. Wake up."

    scene fundo_hospital with fade
    show adrian_serio at camila_maior_esquerda_baixo5
    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4

    "Camila stirs, blinking, confused. She lifts her head slowly, realizing both Adrian and Mary are watching."

    c "(groggy) Dr. Adrian...? I—"

    a "(serious) You can’t sleep on duty. Not here. Not like this."

    "Mary glances between them, sensing the tension but saying nothing."

    "Camila steadies herself, still embarrassed from being caught asleep. Mary lingers nearby, watching quietly."

    a "(curt) Camila, this can’t happen again. Sleeping on duty is unacceptable."

    c "(quietly) I understand, Dr. Adrian..."

    "Adrian crosses his arms, his gaze sharp, as if weighing his next words."

    a "From now on, you’ll be stationed at the reception desk outside my office. I want you where I can keep an eye on you."

    "Camila looks up, startled. Mary shifts uncomfortably, sensing the weight behind his words."

    c "(hesitant) The reception... in front of your office?"

    a "(firm) Yes. Effective immediately. If you’re too tired to manage the floor, then you’ll work where I can supervise you directly."

    "Camila lowers her eyes, her voice barely audible."

    c "(softly) ...Yes, Doctor."

    "Mary glances at Camila, then at Adrian, but says nothing. The silence in the room feels heavy."


    scene corredor_hospital with fade

    "Minutes later, Camila walks down the corridor, her steps slow, her thoughts louder than the noise around her."

    c "{i}Reception outside his office... Was this punishment? Or something else?{/i}"
    c "{i}Why does it feel like he’s pulling me closer, piece by piece?{/i}"

    scene adrian_office with fade

    "Camila sits at the small desk outside Adrian’s office, a stack of files placed neatly in front of her."

    "Through the half-open door, she can hear his voice on the phone — calm, commanding, in control."
    c "{i}Now I’m right where he wants me... and I don’t know if I should feel safer, or more exposed.{/i}"

    scene black with fade
    show camila_recep1 at zoom1763
    show rosto1 at zoom1
    "Camila sits at the reception desk, her pen poised over the appointment book. A patient stands across from her, shifting nervously."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto2 at zoom1
    c "(smiling politely) Good morning. How can I help you today?"
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto1 at zoom1
    p "I need to schedule a follow-up with Dr. Adrian. He told me to come back within two weeks."

    "Camila nods, typing into the computer as she flips through the schedule."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto2 at zoom1
    c "Alright, let me check his availability. Could you confirm your full name and date of birth for me?"
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto1 at zoom1
    p "Of course. Daniel Costa, born March 12, 1981."

    "She types quickly, her eyes scanning the screen."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto2 at zoom1
    c "Thank you, Mr. Costa. I see your file here. The doctor has openings next Tuesday at 10 a.m. or Thursday at 3 p.m. Which works better for you?"
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto1 at zoom1
    p "Hmm... Tuesday morning might be difficult. Thursday at 3 sounds good."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto2 at zoom1
    c "Perfect. I’ll reserve that slot for you. Do you still have the same contact number ending in 4729?"
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto1 at zoom1
    p "Yes, that’s correct."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto2 at zoom1
    c "Great. I’ll send you a reminder the day before. Please arrive fifteen minutes early to update your paperwork."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto1 at zoom1
    "She prints the appointment slip and slides it across the desk with a practiced smile."
    scene black with fade
    show camila_recep1 at zoom1763
    show rosto3 at zoom1
    "As she speaks, the door behind her opens quietly. Adrian steps into the hall, his presence filling the space without a word."
    scene black with fade
    show camila_recep2 at zoom1763
    show rosto5 at zoom1
    play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7
    "Camila feels it instantly—the weight of his hand on her. Her shoulders tense, but she doesn't turn around."
    scene black with fade
    show camila_recep2 at zoom1763
    show rosto6 at zoom1
    c "(steady voice) Here you go, Mr. Costa. Thursday, 3 p.m., with Dr. Adrian."
    scene black with fade
    show camila_recep2 at zoom1763
    show rosto5 at zoom1

    "Camila keeps her eyes on the patient, her voice calm, though her pulse quickens."

    c "If you have any questions before then, please don’t hesitate to call."

    scene black with fade
    show camila_recep3 at zoom1763
    show rosto3 at zoom1
    "She feels Adrian squeezing her, increasing the intensity little by little..."

    p "(hesitant) Uh... are you sure you’re alright, miss? You seem... distracted."

    "Camila forces a small smile, her voice even."
    scene black with fade
    show camila_recep3 at zoom1763
    show rosto4 at zoom1
    c "I’m fine. Just a long shift, that’s all. Let’s confirm Thursday at 3 p.m."
    scene black with fade
    show camila_recep3 at zoom1763
    show rosto3 at zoom1
    p "(taking the paper) Okay... thank you. Take care of yourself."

    $ persistent.unlocked_scene5 = True
    "Camila nods, her smile fading as soon as the patient leaves. The silence that follows feels heavier than before."

        # After the patient leaves
    scene black with fade
    "Camila exhales slowly, her hands trembling as she gathers the last of her papers."

    "She decides to end her shift right away, unable to bear the silence any longer."

    "Camila walks out of the hospital, the night air cool against her skin."

    scene fundo_quarto with fade
    "At home, she slips quietly into bed beside her husband, his steady breathing grounding her."


    "Sleep comes quickly, though her dreams are restless."

    scene black with fade
    "Morning light filters through the curtains. Camila wakes, her chest heavy with unease."

    scene hospital_morning with fade
    "Camila arrives at the hospital entrance, her steps slow and hesitant."
    "She pauses for a moment, staring at the glass doors, her reflection looking back at her with tired eyes."
    "Her heart races, shame and fear twisting inside her chest."
    "Taking a deep breath, she forces herself to move forward."

    scene black with fade
    "Moments later, she finds herself standing outside Adrian’s office, her hand trembling as she reaches for the door."

    scene adrian_office


    "Camila steps into Adrian’s office, her voice low and hesitant."

    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
    c "Dr. Adrian... I came to apologize for yesterday."

    show adrian_serio at camila_maior_esquerda_baixo5
    a "(coldly) Apologize? You were wrong, Camila. Or do you want me to spread it across the entire hospital that you were sleeping during your shift?"

    "Her face pales, shame burning in her chest."
    c "(whispering) No... please. I understand."
    a "Good. Then you agree you must be punished in some way."

    "Camila lowers her gaze, her silence an admission of guilt."
    a "You’re going to help me with something else today..."
    a "You’ll observe me while I see patients, maybe you’ll learn something..."
    c "But will I be by your side, Dr. Adrian?"
    a "Of course not!"
    a "Patients cannot see you with me, a doctor’s consultation is confidential."
    c "But then... where do you want me to stay?"
    a "You’ll stay under my desk while I attend to them."
    c "I-I don’t think that’s appropriate, doctor..."
    a "Said the nurse who was caught sleeping on duty!"
    a "Who are you to tell me what’s appropriate or not?"
    a "Just do as I say."

label consultation_scene:

    scene black with fade
    show mesa1 at zoom1763

    "The office door opens and a patient steps inside."

    a "(calmly) Please, have a seat. Tell me what brings you here today."
    
    "Camila stands silently under the desk..."

    "Doctor, I’ve been having these headaches for the past week..."
    a "(leaning closer to the patient) I see. Let me ask you a few questions to understand better."
    "Camila lowers her gaze, her pulse quickening as she listens, unable to move or speak."
    a "Do they occur more in the morning or at night?"
    "Mostly in the evenings, after work."
    a "Alright. We’ll run some tests, but I suspect it’s stress-related."
    "I understand, doctor. Thank you for your time."
    a "You’re welcome. Please schedule the tests at the front desk before you leave."
    "The patient nods, standing up and heading toward the door."
    "The office grows quiet again as the door closes, the weight of the situation pressing down on her."
    scene black with fade
    show mesa2 at zoom1763
    c "Can I leave now?"
    scene black with fade
    show mesa1 at zoom1763
    a "Only when I say so."

    "Camila hears a sound... quite a peculiar one..."
    "Ziip..."
    "Dr. Adrian is unzipping his pants..."
    scene black with fade
    show mesa2 at zoom1763
    c "What are you doing?"
    scene black with fade
    show mesa3 at zoom1763
    "! ! ! ! ! ! ! ! ! !"
    c "{i}W-w-what???{/i}"
    c "{i}H-h-how can you...???{/i}"
    a "You already know what to do..."
    scene black with fade
    show mesa5 at zoom1763
    c "Huh????"
    c "Do you really think I'm going to do that???"
    c "In case you don’t know, I’m a married woman!"
    c "I’d never do something like this..."
    scene black with fade
    show mesa4 at zoom1763
    a "Are you really willing to risk losing your job?"
    scene black with fade
    show mesa6 at zoom1763
    a "I can see how hard you work to keep it... This will just be one more task you’ll have to do."
    a "I’m punishing you with this. I thought you had agreed to the punishment."
    scene black with fade
    show mesa7 at zoom1763
    c "F-fine..."
    scene black with fade
    show mesa6 at zoom1763
    "Moments later, the door opens."

    "Good afternoon, Doctor."
    a "Ah, Mr. Silva. Please, have a seat."
    "Her heartbeat echoes in her ears as the doctor calmly begins the consultation."

    a "So, tell me… how have you been feeling lately?"
    "The pain is still there, doctor. Especially in the mornings."
    a "I see... Have you been following the medication schedule I prescribed?"
    "Yes, sir. Every morning and before bed."
    a "Good. That’s important. Now, let’s check your reflexes and pulse."
    a "I’m punishing you with this. I thought you had agreed to the punishment."
    scene black with fade
    show mesa9 at zoom1763
    "Camila, scared, starts licking..."
    c "{i}I'll have to do this...{/i}"
    c "{i}I have to keep my job.{/i}"

    a "Your progress seems stable. Keep the routine and come back next week."
    "Thank you, Doctor."
    "Footsteps fade as the patient leaves the room."

    scene black with fade
    show mesa8 at zoom1763
    a "Don't think you'll get away with the punishment just by licking."
    a "Satisfy me, and then maybe I'll pretend I didn't see you sleeping on the job."
    c "{i}How could I have thought he was a good person! Tsk...{/i}"
    scene black with fade
    show mesa10 at zoom1763
    "Camila, start sucking him..."
    a "If you can't satisfy me by the end of the next appointment, consider yourself fired, okay?"
    scene black with fade
    show mvchupando1 at zzoom176
    play music "audio/chupandosom.mp3" loop fadein 0.2
    "Camila increases the intensity, finally giving him what he wanted."
    a "Oh... That's it..."
    a "T-that's the spirit..."
    a "Keep it up..."
    c "{i}I need to finish this soon...{/i}"
    c "{i}No one can see me in this situation...{/i}"
    a "N-next!"
    p "G-good night, Dr. Adrian..."
    p "I-I'm [player_name]."
    scene black with fade
    show mesa11 at zoom1763
    stop music
    c "{i}That's my husband!!!{/i}"
    c "{i}I have to get out of here soon! But...{/i}"
    c "{i}He can't see me in this situation...{/i}"
    c "{i}W-w-what do I do...{/i}"
    a "Your name isn't on the list."  
    p "It's just that I actually came looking for Camila..."
    p "Mary said she'd be here."
    a "Oh... You're Camila's husband? What an interesting surprise..."
    p "Why exactly?"
    scene black with fade
    show mesa13 at zoom1763
    "Adrian holds Camila's face firmly..."
    c "{i}W-what is he doing??{/i}"
    a "No, you're welcome... Hahaha"
    a "Unfortunately, I can't help you, I've assigned her another job at the moment."
    scene black with fade
    show mesa12 at zoom1763
    a "Could you wait for her to finish?"
    a "I-I don't think she'll be long..."
    scene black with fade
    show mvchupando2 at zzoom176
    play music "audio/chupandosom.mp3" loop fadein 0.2
    c "{i}! ! ! ! ! ! !...{/i}"
    c "{i}I can't breathe properly...{/i}"
    p "O-no problem... I'll be back another time..."
    a "But is there anything else I can help you with?"
    p "Oh, I don't know..."
    a "We can vent, that's what I'm working on here, don't miss the moment."
    p "So... It's about Camila..."
    a "What's wrong with her? I can tell she's always very dedicated around here."
    p "I think that's exactly the problem."
    p "She's very busy working... I feel like she's been very distant lately." 
    c "{i}N-n-that's not it...{/i}"
    a "I see..."
    a "Considering Camila... With all due respect, she's a very beautiful young woman."
    a "She must certainly be admired by many people."
    a "Don't you think she might be pleasing another man? Instead of you?"
    c "{i}I can't believe he's saying that...{/i}"
    c "{i}While I...{/i}"
    p "N-no... She would never do that..."
    c "{i}What am I doing...{/i}"
    p "As much as she has every right..."
    p "Sometimes I think I'm not enough for her."
    a "Then there's no reason to worry!"
    "Adrian increases the intensity..."
    a "She must just be tired! From working so hard."
    p "Yes, maybe..."
    p "I don't think I should really worry."
    a "Of course not!"
    scene black with fade
    show mesa13 at zoom1763
    a "She's such a young..."
    scene black with fade
    pause (0.7)
    scene black
    show mesa13 at zoom1763
    pause (0.5)
    scene black with fade
    pause (0.5)
    scene black
    show mesa13 at zoom1763
    pause (0.3)
    scene black with fade
    pause (0.2)
    scene black
    show mesa14 at zoom1763
    pause (2.0)
    stop music
    a "Arhg..."
    p "Is everything okay, Doctor?"
    scene black
    show mesa15 at zoom1763
    a "Y-yes, okay..."
    a "As I was saying, she's such a dedicated young lady."
    a "Don't worry, I'll be keeping an eye on her, I'll take care of her for you."
    p "Would you do that, Doctor?"
    a "Of course! It's the least I can do, she helps me a lot, you know..."
    p "Thank you so much, Doctor!"
    p "And... It's strange she hasn't come back yet... You gave her a really complicated job, didn't you?"
    a "Y-yes... But nothing she's not capable of."
    a "Well, if you'll excuse me..."
    p "Of course! See you later! It was great meeting you."
    p "Bye, nice meeting you."

    $ persistent.unlocked_scene6 = True

    scene black with fade
    "Camila remains kneeling beneath the desk, her body hidden from view."
    "Her forehead presses against the edge of the table, her hands trembling as she clutches the floor."
    "The silence of the room feels suffocating, broken only by her uneven breathing."

    c "(whispering) I... I can’t stay like this..."
    c "{i}Why did it have to happen in front of him...?{/i}"

    "Her cheeks burn with humiliation, her knees aching against the cold tiles."
    "She stays there for a moment longer, unable to rise, her thoughts circling around Adrian’s harsh words."

    c "(softly) He doesn’t understand... he only sees weakness."
    c "(quietly) I’ll prove him wrong... I’ll show him I’m stronger than this."

    "Finally, Camila pushes herself up from beneath the desk, brushing off her uniform."
    "Her movements are stiff, her face still flushed with shame."
    "Without looking back, she walks quickly toward the exit, her heart heavy with anger and embarrassment."


label camila_home:

    scene black with fade
    "The night feels heavier than usual as Camila finally returns home."

    scene fundo_quarto with fade
    "She steps inside quietly, her shoulders tense, her eyes fixed on the floor."
    "Her husband looks up from the living room, surprised by her silence."

    p "Camila... you’re back. How was your shift?"
    "Camila freezes, unable to meet his gaze."

    c "(softly) I... I don’t want to talk about it."
    "Her voice trembles, her face turned away, shame burning in her chest."

    p "Camila...? What’s wrong?"
    "She shakes her head quickly, refusing to answer."

    c "{i}I can’t even look at him... not after what happened...{/i}"
    c "(quietly) I’m... I’m going to sleep."

    "Camila slips into the bedroom, lying down without changing, her body heavy with exhaustion."
    "She turns her back to the door, pulling the blanket over herself."
    "Her husband lingers in the doorway, concerned, but she pretends not"

label camila_morning:

    scene black with fade
    "The morning sun filters through the hospital windows as Camila arrives for her shift."
    "She forces a smile, trying to shake off the weight of yesterday’s humiliation."
    "Hours pass quietly, until a familiar figure appears in the corridor."

    scene corredor_hospital
    show walter_safado at camila_maior_esquerda_baixo5
    w "Camila... finally. I’ve been waiting to see you."
    w "You don’t visit me anymore. I feel abandoned."
    w "Do you know how much I miss our talks?"
    

    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
    c "(uneasy) Mr. Walter... please, you shouldn’t be wandering around like this."
    c "(softly) I understand you feel lonely, but you must respect boundaries."
    w "Boundaries, boundaries... you always say that."
    w "But I know you care about me. I can see it in your eyes."
    w "Don’t pretend you don’t miss me too."

    "Walter leans closer, pressing her lightly against the wall, his tone insistent."
    c "(firm but gentle) I’m here to help you as a nurse, nothing more."
    c "(thinking) {i}He doesn’t know limits... I should be stronger, I should stop this...{/i}"

    w "You’re too serious, Camila. Just relax... let me feel close to you."
    w "Every day I wait, hoping you’ll come by. And you never do."
    w "Why are you avoiding me?"
    c "(nervous) I’m not avoiding you... I just have responsibilities."
    c "(quietly) Please, don’t make this harder for me."
    w "Harder? You make it hard by ignoring me."
    w "I want your attention, Camila. I need it."

    "Before she can respond further, a voice echoes down the corridor."
    scene corredor_hospital
    show camila_uniforme_assustada at camila_maior_esquerda_baixo4
    show walter_safado at camila_maior_esquerda_baixo5
    p "Where is Camila? Have you seen her?"
    "Camila freezes, her heart racing."
    c "(alarmed) He can’t see us like this... Walter, please!"
    w "(smirking) Afraid of being caught, aren’t you?"
    c "(urgent whisper) This isn’t a joke! He mustn’t find us here."

    "Her eyes dart around, searching for an escape."
    c "(whispering) Quick... inside the janitor’s room!"
    scene black with fade
    "In a rush, she pulls Walter toward the nearest door — the janitor’s closet."
    "The two slip inside, the cramped space pressing them close together."
    play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7
    show janitor1 at zoom1763

    c "(whispering) Stay quiet... he mustn’t find us here."
    w "(low chuckle) So now we’re hiding together... interesting."
    c "(tense) Stop it, Walter. This isn’t funny."
    "Her breath quickens, the tension of the moment overwhelming her."


label janitor_room:


    "The cramped janitor’s closet is dimly lit, the smell of cleaning supplies heavy in the air."
    "Camila presses herself against the shelves, her heart racing."


    w "Camila... you’re wonderful. I don’t understand why you keep your distance."
    w "You’re perfect to me. I can’t stop thinking about you."
    w "Why do you hide yourself away?"

    scene black
    show janitor2 at zoom1763
    c "(tense) Mr. Walter, please... this isn’t the time."
    c "(whispering) Stay quiet, someone might hear us."
    scene black
    show janitor3 at zoom1763
    w "Quiet? No... I want you to listen." 
    w "If you keep ignoring me, maybe I should call out. Maybe I should tell your husband what I see right now."
    w "I want you to please me... don't you realize how hard I am?"
    w "Shake that big ass for me, or I'll show your husband what you're really in!"
    scene black
    show janitor4 at zoom1763
    c "No! Don’t do that..."
    scene black
    show janitorvideo at zzoom176
    c "Alright... I’ll do as you ask..."
    w "Yes, just like that..."
    w "You missed me, didn’t you?"
    c "D-don’t say such foolish things!"
    w "That’s how I like to see you!"
    w "I missed this attitude of yours!"
    w "Denying me, while still giving in... you should be ashamed, my dear..."
    c "{i}H-he’s right...{/i}"
    c "{i}I shouldn’t be doing this...{/i}"

    scene black
    show janitor7 at zoom1763
    "Suddenly, a familiar voice echoes faintly from the corridor outside."

    p "Mary, where is Camila? Have you seen her?"

    "Camila freezes, her entire body stiff. The air in the closet feels suffocating."
    "She and Walter fall completely silent, the tension unbearable."

    "Her thoughts scream in panic: she’s in shock, terrified of being discovered."

    "After a long moment, the footsteps fade. The voice drifts away down the hall."

    "Camila exhales shakily, relief flooding her chest."

    c "(whispering) ...He’s gone."
    c "(softly) Thank goodness..."

    $ persistent.unlocked_scene7 = True

    stop music

    scene corredor_hospital with fade
    "Camila leaves the closet quickly, her steps hurried, putting distance between herself and Walter."
    "Her heart still pounds, but she forces herself to focus on work."

    label mesa_scene:

    scene break_room with fade
    "She enters the small rest room, closing the door behind her."
    "Her hands tremble slightly as she sits down, trying to calm herself."

    "Suddenly, her phone buzzes. She looks at the screen — it’s her husband."


    c "(softly) ...Hello?"
    p "Camila, I came to the hospital earlier, but I couldn’t find you."
    p "Where were you? I asked around, but no one seemed to know."

    "Camila bites her lip, her eyes lowering, unsure how to answer."
    c "(hesitant) I... I was busy, moving between rooms. Maybe that’s why you didn’t see me."
    p "Busy? You sound tired... are you alright?"
    c "(quietly) I’m fine, dear. Just... a long day."

    scene black with fade
    show table1 at zoom1763
    "As she speaks, Dr. Adrian appears silently in the doorway."
    "His expression is unreadable, watching her from behind as she talks on the phone."

    p "Camila, I worry when I can’t find you. Please, don’t disappear like that."
    c "(softly) I understand... I’ll be more careful."

    "Before she can continue, Adrian’s voice cuts through the room, firm and direct."

    a "Camila. What are you doing here instead of at your post?"
    "Camila stiffens, the phone still pressed to her ear, caught between her husband’s concern and Adrian’s authority."

    c "(startled) I— I was just—"
    p "(confused) Camila? Who was that? Is someone with you?"
    "Her breath catches, panic rising again as both voices demand her attention."
    scene black with fade
    "Adrian pushes Camila against the desk while she nervously talks to her husband on the phone..."
    a "Your husband should know who’s in charge of you here!"
    scene black
    show table2 at zoom1763
    play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7
    c "! ! ! ! ! ! ! ! !"
    p "Camila???"
    p "Hello???"
    c "H-hi, dear..."
    c "I-I’m here..."
    p "Is there someone there with you???"
    c "O-of course not, dear!"
    p "You’re not being honest with me, Camila!"
    c "O-of course I am, dear..."
    p "Turn on your camera, I want to see you on a video call."
    p "I want to be sure there’s no one with you."
    c "O-of course... no problem..."
    show phone1 at topleft
    "Camila turns on her camera, showing only her face..."
    p "Hmph, looks like there’s no one there..."
    p "I thought I heard voices..."
    show phone2 at topleft
    c "It must have been your imagination..."
    scene black
    show table3 at zoom1763
    show phone4 at topleft
    c "E-everything is fine..."
    scene black with fade
    show tablevideo1 at zzoom176
    show phone4 at topleft
    c "I’m in the break room... there’s no one here with me..."
    show phone3 at topleft
    p "Alright then..."
    p "I hope that’s true."
    scene black
    show table4 at zoom1763
    show phone5 at topleft
    "Camila lets out a faint sound, trying to cover her nerves..."
    p "Camila???"
    p "Did something happen???"
    show tablevideo2 at zzoom176
    show phone6 at topleft
    c "N-no, dear... don’t worry..."
    show phone8 at topleft
    c "I-I’m just feeling a little unwell..."
    show phone7 at topleft
    p "Do you need me to buy some medicine???"
    hide phone7
    show phone8 at topleft
    c "N-no, it’s not necessary, dear..."
    show phone7 at topleft
    p "Yes it is!"
    p "I’m going to buy it right now!"
    p "Don’t worry!"
    hide phone7
    show phone8 at topleft
    c "O-okay..."

    $ persistent.unlocked_scene8 = True



label version05:

scene black with fade

c "Adrian, stop! This can’t happen anymore!"
"Camila pushes Adrian away firmly."
"She quickly turns and heads toward the corridor, her heart racing."


scene corredor_hospital with fade

"Camila rushes down the corridor, her footsteps echoing in the silence."
"She avoids looking anywhere, as if the whole world were judging her."

c "{i}I can’t let them see me like this...{/i}"
c "{i}I need to regain control...{/i}"

"She stops in front of a window, the moonlight casting a pale glow across her flushed face."
"For a moment, her eyes close, fighting back the tears."

c "(whispering) I’ll prove I’m not weak..."
c "(whispering) Not to him... not to anyone."

scene black with fade

"Camila takes a deep breath, straightens her posture, and continues forward."
"Each step feels heavy, but carries a new determination."

scene adrian_office with fade
show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4

"When she enters the office, the atmosphere feels different."
"There is no room left for hesitation — only for the decision she knows she must make."

c "{i}If Adrian thinks he can break me...{/i}"
c "{i}He’ll learn I can endure.{/i}"

show adrian_serio at camila_maior_esquerda_baixo5
a "Camila...? What are you doing here?"
a "I thought you had already left."

c "No, Doctor."
c "I came back because I won’t tolerate this anymore."

a "Tolerate...? What do you mean?"
c "The way you treat me... the way you speak about me as if I’m weak."
c "I refuse to let you keep humiliating me."

a "Camila, I—"

c "No. I’ve stayed silent long enough."
c "From now on, I’ll prove my worth on my own terms."
c "And I won’t let you control me any longer."

"Her voice trembles, but her eyes burn with determination."
"Adrian stares at her, momentarily speechless, the weight of her words hanging in the air."


scene black with fade
"Adrian presses her against the desk..."
a "Stop pretending..."
show af0 at zoom1763
a "I saw how aroused you were..."
a "I felt it clearly..."
scene black
show af01 at zoom1763
c "{i}He noticed!{/i}"
c "{i}And now?!{/i}"
scene black
show af1 at zoom1763
a "Wow... Who would have thought you’d wear such daring underwear..."
a "Your body craves me... Admit it."
a "I saw how you looked, how you moved closer..."
scene black
show af3 at zoom1763
c "Y-you’re mistaken..."
c "I-I didn’t do that..."
scene black with fade
"Adrian moves Camila’s clothing aside..."
show af2 at zoom1763
a "You have to confess... That this is what you want..."
"Adrian leans closer to Camila..."
scene black with fade
show af4 at zoom1763
c "I can’t..."
scene black with fade
show af5 at zoom1763
a "Confess..."
a "Confess that you enjoy this..."
a "Did you feel how big my dick is?"
a "How much bigger is it than your husband's?"
c "Stop saying those things..."
scene black with fade
show af6 at zoom1763
c "{i}I can’t think straight...{/i}"
c "{i}It feels so tempting...{/i}"
c "{i}My body longs to be filled by that huge cock...{/i}"
scene black with fade
play sound "audio/door_sound.mp3"
"! ! ! ! ! ! ! ! ! !"
p "Camila? Are you there?"
scene black with fade
show af7 at zoom1763
c "It’s my husband!!!"
c "He’s back! Let me go!"
c "He can’t see us like this!"
scene black with fade
show af8 at zoom1763
a "Hello [player_name], yes she’s here!"
p "Oh that’s great!"
a "But I’m in the middle of a consultation with her right now..."
a "And I believe it will take a while..."
a "Can you wait outside while I finish?"
scene black with fade
show af7 at zoom1763
p "Of course!"
p "No rush! Take all the time you need..."
scene black with fade
show af8 at zoom1763
a "Thank you very much! Hahaha"
a "You heard him, right? I’ll keep you here with me before returning you to your husband..."

menu:
    "Camila feels trapped... What will she do?"
    
    "Continue...":
        scene black with fade
        show af9 at zoom1763
        c "I... I can’t resist anymore..."
        "So tell me what you want..."
        scene black with fade
        show af10 at zoom1763
        c "Put your huge cock in me, please..."
        a "That's it, good girl..."
        a "I'll give you what you want..."
        a "I hope you're qualified..."
        show af11 at zoom1763
        play sound "audio/gemido.mp3" volume 5.0
        "! ! ! ! ! ! "
        c "Ow... So thick..."
        c "So... Big..."
        c "I can't think of anything else..."
        show af_video1 at zzoom176
        a "That's it, grind on my dick..."
        a "What a naughty little slut you are..."
        c "I can’t control myself anymore..."
        c "Your dick feels so good..."
        c "It fills me completely..."
        a "That’s it, little slut..."
        play sound "audio/door_sound.mp3"
        p "Is everything okay in there, dear?"
        c "Y-y-yes!"
        c "I-I’m doing reaaallyyy gooood..."
        c "N-never felt thiiisss gooood before..."
        p "{i}This doctor really is very good at what he does...{/i}"
        a "You did very well..."
        a "You deserve a reward!"
        scene black with fade
        show af_video2 at zzoom176
        play music "audio/gemidoanime.mp3" loop
        c "{i}Ahh...{/i}"
        c "{i}So good...{/i}"
        c "{i}I’m moaning so loud... My husband will hear...{/i}"        
        c "{i}But when he takes me like this...{/i}"   
        c "{i}I can’t hold back...{/i}"
        c "{i}I’ve never felt this way before...{/i}" 
        c "{i}I can only think about serving this huge dick...{/i}"  
        a "Very good..." 
        a "You can’t focus with my dick reaching so deep inside you, can you?"
        c "N-n-no..."
        c "Y-y-your dick is the best..." 
        a "Finally you’re being honest..."
        a "I’m going to cum deep inside you..."
        a "Feel me filling you with my load!"
        scene black
        show af12 at zoom1763
        a "I’m cumming..."
        scene black
        pause (1.0)
        show af12 at zoom1763
        c "Fill me..."
        scene black
        pause (1.0)
        show af12 at zoom1763
        scene black
        pause (1.0)
        show af12 at zoom1763
        a "Argh..."
        a "You really are such a slut..."
        a "Go see your husband now!"
        c "O-o-kay..."
        $ persistent.unlocked_scene9 = True
        jump version06

    "Stop everything":
        scene black with fade
        c "No! This has to end now!"
        jump version06




label version06:
    stop music
    scene corredor_hospital
    show camila_vergonha3 at camila_maior_esquerda_baixo2

    c "H-hi... h-honey..."
    c "I... I just left the doctor's office..."
    c "Everything feels so strange... I’m a little dizzy..."
    c "I’m so sorry for making you wait..."
    

    p "Honey, are you okay? You look a bit pale..."
    p "Do you need me to call someone? Or should we sit down for a moment?"
    c "N-no, no... I’m fine, really..."
    c "I feel... muuuuch better now."
    c "I just... I just need to go home and rest."
    c "Being here with you makes me feel safe."

    p "Alright... if you’re sure. Let’s go home together."
    p "I’ll take care of everything, you just relax."

    scene black with fade

    "Camila walks slowly through the streets, the night air heavy as her mind drifts."

    scene fundo_quarto with fade

    "..."

    p "You took your time. Was the day that rough?"
    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4

    c "(softly) Sorry... I didn’t mean to worry you."

    p "I was starting to wonder if something happened."

    "Camila lowers her gaze, her shoulders tense."
    c "It was... overwhelming. Too many things at once. I just wanted to get home."

    p "You look exhausted."
    c "(with a faint smile) I am... but being here makes it easier."

    scene black with fade

    "Camila sits quietly on the edge of the bed, her fingers trembling slightly."

    c "{i}I didn’t tell him everything... but maybe I don’t even know how to put it into words.{/i}"
    c "{i}For now... I just need to breathe, and rest.{/i}"

    scene black with fade

    "The night passes quietly, and a new day begins."

    "Camila walks through the morning streets, heading toward the hospital as the city awakens."

    scene corredor_hospital with fade

    "Inside the hospital, the familiar smell of disinfectant fills the air."

    c "(thinking) Just another morning... I need to stay calm."

    "She notices the doctor at the end of the hallway."

    c "(quickly looking away) Not now... I can’t face him."

    "Camila lowers her gaze and walks faster, slipping past without a word."

    scene fundo_hospital with fade

    "She enters the room of a patient, Walter, who is resting quietly."

    "Camila approaches the bed, waiting for a response... but Walter doesn’t stir."

    c "(whispering) Walter...? Still asleep..."

    "She pauses, realizing he won’t wake up right now. A faint sigh escapes her lips."

    "Camila walks slowly toward the window, her steps heavy with thought."

    "She opens the window, letting the morning air rush in."

    scene black with fade
    show janela1 at zoom1763

    c "(quietly) I just... need a moment... to breathe."

    "The sunlight filters in, brushing against her face as she steadies herself, eyes closed, taking in the air."

    w "O-ho-ho..."
    w "What do we have here?"
    w "It feels like I’m still dreaming..."

    c "Don’t say nonsense so early, please."
    c "I don’t have the patience for this."
    c "Wait..."
    c "Is that my husband over there?"
    c "I think I forgot my lunch again today..."

    scene black with fade
    show janela2 at zoom1763

    c "Don’t say anything foolish, okay Walter!?"
    w "Of course, sweetheart, I won’t say a word..."
    c "{i}Hard to believe what he says...{/i}"

    scene black with fade
    show janela1 at zoom1763
    show janelafora1 at zoom12

    p "Good morning, dear!"
    c "Hello, darling! What are you doing here?"
    p "You forgot your food today..."
    p "I noticed you seemed distracted, so I came to bring it to you, dear!"
    c "Thank you so much... You’re always so thoughtful..."
    p "Always, my love, I’m here to please you..."

    scene black with fade
    show janela3 at zoom1763
    show janelafora4 at zoom12
    play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7

    c "An-n..."
    p "Did something happen, dear?"

    scene black with fade
    show janela3 at zoom1763
    show janelafora5 at zoom12

    c "N-no..."
    c "D-don’t worry about me, darling..."

    scene black with fade
    show janela3 at zoom1763
    show janelafora6 at zoom12

    c "{i}I knew I couldn’t trust him behind me!{/i}"
    p "I’ve noticed you’ve been acting strange lately, are you sick?"

    scene black with fade
    show janela4 at zoom1763
    show janelafora11 at zoom12

    c "{i}What is he planning to do?{/i}"
    p "Darling???"
    c "O-oh... Sorry."
    c "What were you saying?"

    c "{i}I can’t even think straight right now...{/i}"
    p "Are you feeling unwell, dear?"
    c "{i}I can’t even hear what he’s saying...{/i}"
    c "{i}Walter is trying to shove this huge thing inside me...{/i}"
    c "{i}Right in front of my husband...{/i}"

    menu:   
        "Let Walter continue":
            c "(hesitant) I... I’ll let him continue..."
            jump walter_continue

        "Stop right now":
            c "(firmly) No! This has to stop right now."
            jump version08

label walter_continue:

    scene black with fade
    show janela5 at zoom1763
    show janelafora12 at zoom12
    play sound "audio/gemido.mp3" volume 5.0
    c "{i}I-I...{/i}"
    c "{i}I-I can’t hold myself...{/i}"
    c "{i}This huge cock is driving me crazy...{/i}"
    c "{i}This thing is turning me into a slut{/i}"

    p "Darling???"
    p "What was that? Are you okay?"
    c "S-sorry..."

    scene black with fade
    show janelavideo1 at zzoom176
    show janelafora12 at zoom12

    c "{i}I can’t hold myself...{/i}"
    c "{i}Sorry, darling...{/i}"

    p "It’s alright, dear..."
    p "You don’t need to apologize, everyone feels unwell sometimes..."

    c "{i}This huge cock feels so good...{/i}"
    c "{i}I can’t stop...{/i}"

    p "I’ll leave your lunch here, okay dear?"

    hide janelafora12
    show janelafora8 at zoom12

    c "O-okay..."
    c "T-thank you so much, darling..."
    c "Y-you’re the best..."

    p "Hahaha, you’re speaking funny, dear..."
    p "Are you drunk by any chance?"

    scene black with fade
    show janelavideo2 at zzoom176
    show janelafora8 at zoom12

    c "O-of course not..."
    c "It must be the effect of the medicine..."

    p "Ah, of course!"
    p "That makes sense!"
    p "You need to be careful with the medicine you’re taking, okay?"

    c "Y-yes..."
    c "D-don’t worry, darling..."

    p "W-well... I’m leaving..."
    p "Do you want me to prepare something for dinner tonight?"

    c "Y-you decide, darling..."
    p "I’ll think of something when I get back..."

    p "And another thing..."
    p "Lately, I know I’ve been very tired with work..."
    p "And it’s been a long time since we’ve shared moments together..."
    p "Don’t you miss it? Are you feeling satisfied lately?"

    c "D-don’t worry..."
    c "I-I’m feeling very satisfied..."

    c "{i}This enormous thing satisfies me completely!{/i}"

    p "Great, dear!"

    c "{i}I feel it pulsing inside me...{/i}"
    c "{i}Ready to unleash all your cum on me...{/i}"

    p "Well, I think I’ll be going then..."

    scene black
    show janela5 at zoom1763
    show janelafora13 at zoom12

    w "Argh..."

    scene black
    pause (1.0)
    show janela5 at zoom1763
    show janelafora13 at zoom12

    c "{i}Fill me...{/i}"

    scene black
    pause (1.0)
    show janela5 at zoom1763
    show janelafora13 at zoom12

    scene black
    pause (1.0)
    show janela6 at zoom1763
    show janelafora14 at zoom12

    c "{i}I feel completely fulfilled inside...{/i}"

    p "Darling?"

    scene black
    show janela6 at zoom1763
    show janelafora15 at zoom12

    c "A-ah, o-of course... G-goodbye, darling..."
    p "Goodbye, dear!"

    $ persistent.unlocked_scene10 = True

    jump version08


label version08:

    stop music
    scene black with fade
    c "You’re driving me crazy like this..."
    c "We can’t keep going on this way..."

    c "Ah... I need to leave..."
    c "My body still feels strange..."
    c "I can’t think straight..."
    scene fundo_casa with fade
    c "After such a long day of work..."
    c "Finally... home..."
    c "I just want to rest..."

    c "But... why do I still feel this inside me?"
    c "This shame... this sensation..."
    c "I can’t stop thinking..."

    c "I can’t stop..."

    c "Maybe tomorrow will be different..."
    c "Maybe I’ll be able to forget..."
    c "But for now... I just want to sleep..."
    scene fundo_quarto with fade
    c "Darling... you’re already here..."
    p "Of course, dear. I was waiting for you."
    c "I-I’m sorry I’m late... it’s been such a long day..."
    p "I can see that. You look exhausted."
    c "Yes... I feel dizzy and embarrassed..."
    p "Come, sit with me. Tell me, are you really alright?"
    c "I don’t know... I feel strange inside..."
    p "Strange how? Is it the medicine again?"
    c "Maybe... or maybe it’s just me..."
    p "You don’t have to hide anything from me, Camila."
    c "I-I’m not hiding... I just don’t want you to worry..."
    p "I’ll always worry about you. You’re my everything."
    c "Thank you... I needed to hear that..."
    p "Rest now, dear. Tomorrow will be better."
    c "Yes... tomorrow... I hope so..."

    scene black with fade
    c "{i}I’m leaving home now... heading to the hospital again...{/i}"
    scene locker_room
    c "{i}My mind feels heavy... I can’t focus on anything else...{/i}"
    c "{i}I can't stop thinking...{/i}"
    c "{i}On Walter's huge cock... Inside me...{/i}"
    c "{i}I've never felt so fulfilled..{/i}"
    c "{i}Why does he stay with me like this? Why can’t I forget?{/i}"
    scene corredor_hospital
    c "{i}Even as I walk through the hospital doors, all I can think about right now is that enormous thing...{/i}"
    c "{i}I'm getting wet just thinking about it...{/i}"
    c "{i}I don’t know what’s happening to me...{/i}"
    scene fundo_hospital
    show camila_uniforme_vergonha2 at camila_maior_esquerda_baixo4
    c "G-good m-morning, Walter!"
    show walter_safado at camila_maior_esquerda_baixo5
    w "Good morning, sweetheart... How are you?"
    c "I-I’m fine..."
    w "Nothing you want to tell me?"
    c "N-n-no... W-why would I?"
    w "I feel like you miss my cock, don’t you?"
    c "T-that’s not it..."
    w "Be honest with yourself. You loved having me inside you, didn’t you?"
    c "Stop saying those things..."
    w "Well... I just wanted to tell you I’m very hard right now. Will you help me with that?"
    c "Walter! We can’t..."
    c "I’m married... This can’t keep happening..."
    w "And you’ll let me suffer with this pain?"
    w "I can’t keep going through this... Isn’t it your duty to help me?"
    c "I-it is..."
    w "Then?"
    c "Alright..."
    c "But not here... Follow me..."
    scene black with fade
    show tit1 at zoom1763
    play music "audio/sensual_music.mp3" loop fadein 1.0 volume 0.7
    w "Wow..."
    w "You really are very thirsty today..."
    w "Do you miss my dick?"
    scene black
    show tit2 at zoom1763
    c "I just need to help you..."
    c "Don’t get me wrong..."
    scene black
    show tit1 at zoom1763
    w "And aren’t you going to start already?"
    w "I'm waiting, bitch."
    scene black
    show tit2 at zoom1763
    c "As much as I should help you with this..."
    c "I still think it’s not appropriate..."
    scene black
    show tit1 at zoom1763
    w "Do you want me to call another nurse to help me?"
    w "I'll call another one, no problem."
    scene black
    show tit3 at zoom1763
    c "{i}What an idiot!{/i}"
    c "{i}I can’t believe he said that to me...{/i}"
    scene black
    show tit4 at zoom1763
    c "I’m the one who’s going to help you, okay?"
    c "You’re not calling any nurse!"
    scene black
    show tit5 at zoom1763
    w "Very well then..."
    scene black
    show tit6 at zoom1763
    c "{i}I can’t get used to this size...{/i}"
    c "{i}It’s too big...{/i}"
    c "{i}This isn’t normal...{/i}"
    scene black
    show tit6 at zoom1763
    w "Are you just going to stand there and watch?"
    w "Suck it already, I'm waiting!"
    w "It's much bigger than your husband's, isn't it?"
    w "That's why you miss me so much, am I right?"
    scene black
    show tit8 at zoom1763
    c "{i}What an old idiot...{/i}"
    c "{i}That huge penis doesn't even compare to my husband's, that's unfair...{/i}"
    scene black
    show tit7 at zoom1763
    c "That’s not the point..."
    c "How do you want me to help you?"
    scene black
    show tit7 at zoom1763
    w "Use those huge breasts you have, make them useful!"
    w "Squeeze my huge cock between those tits..."
    scene black
    show tit10 at zoom1763
    c "L-like this?"
    w "That’s right..."
    w "Now move those huge breasts!"
    show titvideo1 at zzoom176
    w "Y-y-yes..."
    w "Your breasts are the best..."
    c "{i}I could never do this with my husband’s small cock...{/i}"  
    c "{i}I can feel it...{/i}"  
    c "{i}This huge thing is so hard...{/i}"
    c "{i}Pulsing...{/i}"
    w "That’s it... Keep going..."
    w "Now you understand the purpose of your huge breasts?"
    w "You need to serve my cock only."
    c "{i}He’s not wrong...{/i}"
    c "{i}This huge cock fits perfectly between my breasts...{/i}"
    c "{i}I’ve never felt this way...{/i}"
    w "This feels so good..."
    w "I need you always serving me..."
    w "Don’t forget that..."
    c "{i}I feel it pulsing...{/i}"
    c "{i}I think he’s going to...{/i}"

    scene black
    show tit12 at zoom1763
    pause (1.0)
    scene black
    show tit11 at zoom1763
    pause (1.0)
    scene black
    show tit13 at zoom1763
    pause (1.0)
    c "{i}So much cum...{/i}"
    w "Swallow it all!"
    c "{i}Of course I will...{/i}"
    w "Show me your mouth!"
    show tit14 at zoom1763
    w "Good girl..."
    w "Now let me rest..."
    c "O-okay..."
    $ persistent.unlocked_scene11 = True
    stop music
    scene black
    c "{i}That was too much...{/i}"
    c "{i}Good...{/i}"

    scene black with fade
    c "{i}The day is finally ending...{/i}"
    c "{i}I’m heading home, exhausted...{/i}"

    c "{i}Almost there... I just want to rest...{/i}"

    scene black
    "Camila’s phone rings..."
    p "Hello, darling. Are you on your way home?"
    c "Y-yes... I’m almost there..."
    p "I’ve noticed you’ve been feeling a bit down lately..."
    c "I-I’m fine... just tired..."
    p "You deserve something better than just going straight to bed."
    c "What do you mean?"
    p "How about we go to a bar tonight? Just the two of us."
    c "A bar...? But it’s late..."
    p "Exactly. That’s why it will be special. You deserve it."
    c "Darling... you really think so?"
    p "Of course. You’ve been working so hard. Let’s enjoy ourselves together."
    c "Alright... just the two of us..."
    p "Yes, only us. I’ll be waiting."
    c "Thank you... I really needed this..."

    scene fundo_quarto
    c "I need to put on an outfit to surprise him..."
    c "I know..."
    scene black with fade
    show camila_vestido at center
    c "I’ll go like this..."
    c "He will love it..."

    scene fundo_bar
    "..."
    c "{i}Finally... I arrived...{/i}"
    c "{i}Where is my husband?{/i}"
    "..."
    "....."
    "........"
    c "{i}I can’t find him...{/i}"
    c "{i}I’ll order a drink in the meantime...{/i}"
    "Half an hour later..."
    c "{i}Where is he???{/i}"
    c "{i}I’ve tried calling and he doesn’t answer... How annoying...{/i}"
    scene black with fade
    show bar1 at zoom1763
    s"Hello sweetheart, how are you?"
    c "H-hello..."
    s"Are you alone, my angel?"
    c "N-n-no..."
    s"Then where is your partner?"
    c "I-I don’t know..."
    c "{i}This guy is extremely handsome and smells so good...{/i}"
    c "{i}What am I thinking???{/i}"
    s"Would you join me for just one drink?"
    c "I don’t know..."
    s"I’m alone, just one."
    s"I don’t want to feel so lonely here..."
    s"I’ll pay for you, my dear..."
    c "A-alright..."

    jump version09

label version09:
    scene black with fade

    centered "{size=48}{color=#ff3b3b}Choose Your Perspective{/color}{/size}\n\nWhose story do you want to experience?"

    menu:
        "Experience through Camila's eyes":
            jump camila_perspective

        "Experience through the Husband's eyes":
            jump husband_perspective

label camila_perspective:
    scene black with fade
    scene fundo_bar
    show camila_vestido at zoomout

    c "{i}One drink won't hurt...{/i}"
    c "{i}Where is my husband anyway...{/i}"

    scene black with fade
    show bar1 at zoom1763

    s"So... what's your name, beautiful?"
    c "C-Camila..."
    s"Camila... what a beautiful name for such a stunning woman."
    c "{i}He's so charming...{/i}"
    c "{i}And this drink is so strong...{/i}"

    s"Another round?"
    c "I... I shouldn't..."
    s"Come on, your husband left you here alone... You deserve to have fun."
    c "You're right... He should be here by now..."
    c "Another one, please..."

    "30 minutes later..."

    c "Youuu know... *hic* ...he promised he would come..."
    c "He PROMISED... *hic*"
    s"That's terrible... A woman like you shouldn't be treated like this."
    c "Exactly! *hic* You understand me..."
    c "{i}Why is everything spinning...{/i}"
    c "{i}I feel so... hot...{/i}"

    s"Are you okay, Camila?"
    c "I... I need to go to the bathroom..."
    s"Let me help you... You seem dizzy."
    c "T-thank you..."

    scene black with fade
    "He guides Camila to the men's bathroom..."

    scene bathroom_stall

    c "This... this is the men's bathroom..."
    s"It's closer... and more private."
    c "{i}Private? Why would we need privacy?{/i}"
    c "{i}Oh no... what am I doing...{/i}"

    "He leads her into a stall and locks the door..."

    s"You're so beautiful, Camila..."
    c "I... I shouldn't be here..."
    s"Your husband isn't here... but I am."

    "He moves closer, his hands on her waist..."

    c "W-wait..."

    "He kisses her neck softly..."

    c "Ahh..."
    c "{i}This feels so wrong... but...{/i}"
    c "{i}I'm so dizzy... I can barely think...{/i}"

    "She doesn't resist as he pulls her closer..."

    "Their lips meet in a heated kiss..."

    c "{i}What am I doing... what am I DOING...{/i}"

    "His hands explore her body through the dress..."

    c "Mmmm..."

    s"You want this, don't you?"
    c "I... I..."

    "She's too drunk to think clearly..."
    "Too drunk to resist..."
    "Too drunk to remember her wedding vows..."

    "He whispers in her ear..."
    s"Get on your knees for me..."

    c "{i}No... I shouldn't...{/i}"
    c "{i}But I can't think straight...{/i}"

    "Slowly, she sinks to her knees in the bathroom stall..."

    c "{i}What am I doing... oh god...{/i}"

    "Her trembling hands reach up..."

    s"That's it... good girl..."

    c "{i}I'm married... I'm MARRIED...{/i}"
    c "{i}But nothing makes sense anymore...{/i}"

    "She slowly unzips his pants..."

    c "{i}I can't believe I'm doing this...{/i}"
    c "{i}In a public bathroom... with a stranger...{/i}"

    "His cock springs free, already hard..."

    s"Look at you... such a naughty married woman..."

    c "{i}Oh god... it's so big...{/i}"

    "She wraps her fingers around his shaft..."

    s"That ring on your finger looks so good wrapped around my cock..."

    c "Mmmm..."
    c "{i}This is so wrong...{/i}"

    "She leans in, her breath hot against him..."

    s"Open your mouth for me..."

    "She parts her lips slowly..."

    c "{i}I'm really going to do this...{/i}"
    c "{i}I'm going to cheat on my husband...{/i}"

    "She takes him into her mouth..."

    s"Fuuuck... that's good..."

    "She begins to move her head back and forth..."

    play sound "audio/chupandosom.mp3"

    s"Yeah... just like that..."
    s"Your husband is a lucky man..."
    s"Or he WAS... before you became my little slut..."

    c "{i}Mmmph...{/i}"
    c "{i}Why does this feel so good...{/i}"

    "She takes him deeper..."

    s"Look at you... choking on another man's cock..."
    s"Does your husband know what a dirty girl you are?"

    "Her eyes water as she takes him deeper..."

    play sound "audio/gemido.mp3"

    s"That's it... take it all..."

    "She pulls back, gasping for air..."

    c "Ahh... ahh..."
    c "{i}I can't breathe... but I don't want to stop...{/i}"

    "She dives back down eagerly..."

    s"Fuck... you're so good at this..."
    s"Better than your husband deserves..."

    "Her head bobs faster..."

    play sound "audio/chupandosom.mp3"

    s"You love this, don't you?"
    s"You love being on your knees for me..."

    "She moans around his cock..."

    play sound "audio/gemidoanime.mp3"

    s"Such a good little whore..."
    s"Your wedding dress looks beautiful while you suck my dick..."

    c "{i}Oh god... what am I becoming...{/i}"
    c "{i}Why am I so turned on...{/i}"

    "Her hand strokes what doesn't fit in her mouth..."

    s"Faster... come on..."

    "She speeds up, desperate to please him..."

    s"Yeah... yeah... just like that..."
    s"I'm getting close..."

    "His hand grips her hair..."

    s"Don't stop... don't you fucking stop..."

    "She works harder, her jaw aching..."

    play sound "audio/gemido2.mp3"

    s"Fuck... I'm gonna..."

    "When suddenly..."

    "KNOCK KNOCK KNOCK"

    p "Excuse me? Is someone in there?"

    c "!!!"
    c "{i}That voice...{/i}"
    c "{i}OH MY GOD... THAT'S...{/i}"
    c "{i}THAT'S MY HUSBAND!!!{/i}"

    "Her eyes go wide with shock and terror..."
    "Her hands freeze..."
    "Her heart stops..."

    "KNOCK KNOCK KNOCK"

    p "Hello? This is the only stall available... Are you going to take long?"

    c "{i}He's RIGHT THERE...{/i}"
    c "{i}Just on the other side of this door...{/i}"
    c "{i}Oh god oh god oh god...{/i}"

    "The stranger smirks, looking down at Camila's horrified face..."

    s"Yeah buddy... We're going to be a WHILE."
    s"A long, LONG while."
    s"Find another bathroom."

    c "{i}NO NO NO...{/i}"
    c "{i}He's going to find out...{/i}"
    c "{i}What have I done...{/i}"

    p"But... I really need to..."

    s"NOT. MY. PROBLEM."
    s"Now get lost."

    "Footsteps walk away..."

    c "{i}He was right there...{/i}"
    c "{i}My husband was RIGHT THERE...{/i}"
    c "{i}And I'm here... on my knees...{/i}"
    c "{i}What kind of wife am I...{/i}"

    "The stranger looks down at her with a wicked grin..."

    s"That was your husband, wasn't it?"

    c "{i}...{/i}"

    s"Answer me, slut."

    c "Y-yes..."

    s"And here you are... on your knees for me..."
    s"What does that make you?"

    c "{i}I... I don't know...{/i}"

    s"Say it."

    c "..."

    s"Say. It."

    c "I'm... I'm a..."

    s"You're my little slut, aren't you?"

    c "{i}Oh god... I can't believe this is happening...{/i}"
    c "Y-yes..."

    s"Louder."

    c "Yes... I'm your slut..."

    s"Good girl... Now show me what a good slut you are..."

    # Show the CUM button
    show screen cum_button

    jump blowjob_loop

label blowjob_loop:
    scene bathroom_blowjob_1

    s"That's it... just like that..."

    scene bathroom_blowjob_2

    s"Look at you... such a dirty little wife..."

    scene bathroom_blowjob_3

    s"Your husband is out there looking for you..."

    scene bathroom_blowjob_1

    s"And you're in here... sucking my cock..."

    scene bathroom_blowjob_2

    c "{i}Mmmph...{/i}"

    s"You love this, don't you?"

    scene bathroom_blowjob_3

    s"Say yes with those pretty eyes..."

    scene bathroom_blowjob_1

    s"Fuck... you're so good at this..."

    scene bathroom_blowjob_2

    s"Does your husband know what a cock-hungry slut he married?"

    scene bathroom_blowjob_3

    c "{i}Mmm...{/i}"

    s"That's right... take it deeper..."

    scene bathroom_blowjob_1

    s"Such a good little whore..."

    scene bathroom_blowjob_2

    s"Keep going... don't stop..."

    # This creates the infinite loop - it will keep repeating
    jump blowjob_loop

label climax_scene:
    # Hide the CUM button
    hide screen cum_button

    scene bathroom_blowjob_3

    s"Oh fuck... I'm going to..."

    s"I'm cumming!"

    scene bathroom_cumshot_1

    s"Take it all, you slut!"

    c "{i}Mmmph!!!{/i}"

    scene bathroom_cumshot_2

    s"Swallow every drop..."

    c "{i}Oh god... what have I done...{/i}"

    scene bathroom_cumshot_3

    s"Such a good little whore..."
    s"Your husband has no idea what a dirty slut he married..."

    c "{i}I... I need to get out of here...{/i}"
    c "{i}I need to clean up...{/i}"
    c "{i}How am I going to face him...{/i}"

    scene black with fade

    "Camila frantically tries to clean herself up..."
    "Her hands are shaking..."
    "Her mind is racing..."
    "The guilt is overwhelming..."

    c "{i}What have I done... what have I DONE...{/i}"

    s"Open up, baby... Let me see that pretty face covered in my cum..."

    scene bathroom_aftermath

    s"Look at you... such a mess..."
    s"Take a picture of this moment... you'll never forget it."

    c "N-no... please..."

    s"Too late."

    "CLICK"

    c "!!!"
    c "{i}HE TOOK A PHOTO!!!{/i}"

    s"This will be our little secret... won't it?"

    c "Y-yes..."

    s"Good girl. Now clean yourself up..."
    s"Your husband is waiting for you."

    scene black with fade
    centered "{size=42}{color=#ff3b3b}To be continued...{/color}{/size}"
    centered "\n{size=32}The nightmare has only just begun...{/size}"

    return

label husband_perspective:
    scene black with fade

    "Earlier that evening..."

    scene street_night

    p"Damn it... the car won't start..."
    p"Of all times... RIGHT NOW?!"
    p"Camila is waiting for me..."

    "20 minutes of struggling later..."

    p"Finally!"
    p"I'm so late... She's going to kill me..."

    scene black with fade
    scene fundo_bar

    "{i}The bar is packed... so many people...{/i}"
    "{i}Where is she?{/i}"

    p"Excuse me... sorry... pardon me..."

    "{i}I can't find her anywhere...{/i}"
    "{i}Did she leave? Is she angry?{/i}"

    "I try calling her phone..."

    "..."
    "No answer..."

    "{i}Where could she be...{/i}"
    "{i}Maybe she went to the bathroom?{/i}"

    p"Also... I really need to use the restroom..."
    p"That drive was too long..."

    scene black with fade
    scene bathroom_entrance

    "The men's bathroom..."

    "{i}Let me just... take care of this first...{/i}"

    scene bathroom_interior

    "{i}Wait... only one stall?{/i}"
    "{i}And it's occupied...{/i}"
    "{i}Great...{/i}"

    "I knock on the stall door..."

    "KNOCK KNOCK KNOCK"

    p"Excuse me? Is someone in there?"

    "..."

    "{i}No response?{/i}"

    "KNOCK KNOCK KNOCK"

    p"Hello? This is the only stall available... Are you going to take long?"

    "..."

    "{i}I hear... shuffling?{/i}"
    "{i}What are they doing in there?{/i}"

    s"Yeah buddy... We're going to be a WHILE."
    s"A long, LONG while."
    s"Find another bathroom."

    "We're? There's two people in there?"
    p"But... I really need to..."

    s"NOT. MY. PROBLEM."
    s"Now get lost."

    "{i}What an asshole...{/i}"

    show screen bathroom_loop_1_buttons
    jump bathroom_loop_1_scene

label bathroom_loop_1_scene:
    scene bathroom_interior

    "{i}What are they doing in there?{/i}"
    "{i}I can hear strange sounds...{/i}"

    pause

label bathroom_closer_look_1:
    scene bathroom_closer_1

    "{i}Let me get a closer look...{/i}"
    "{i}What the hell...{/i}"

    jump bathroom_loop_1_scene

label leave_bathroom:
    hide screen bathroom_loop_1_buttons

    "{i}Whatever... I'll find another bathroom...{/i}"
    "I walk away, frustrated..."

    scene black with fade

    "{i}But... I can't stop thinking about it...{/i}"
    "{i}Should I go back?{/i}"

    show screen return_decision_buttons
    jump wait_return_decision

label wait_return_decision:
    scene black
    pause

label bathroom_loop_2_scene:
    hide screen return_decision_buttons
    show screen bathroom_loop_2_buttons

    scene bathroom_interior_2

    "{i}I'm back...{/i}"
    "{i}They're still in there...{/i}"
    "{i}What should I do?{/i}"

    pause

label bathroom_closer_look_2:
    scene bathroom_closer_2

    "{i}I can see better now...{/i}"
    "{i}This is...{/i}"

    jump bathroom_loop_2_scene

label continue_story:
    hide screen bathroom_loop_2_buttons
    hide screen return_decision_buttons
    scene black with fade

    "{i}I still need to find Camila...{/i}"
    "{i}Where could she have gone...{/i}"

    centered "{size=42}{color=#ff3b3b}To be continued...{/color}{/size}"
    centered "\n{size=32}Little does he know...{/size}"

    return



    





