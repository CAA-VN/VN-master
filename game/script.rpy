# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
init python:
    s = Shake((0, 0, 0, 0), 0.2, dist=15)

image dwinelle = "images/dwinelle/default.png"
image sather = im.Scale("images/scene/sather_gate.jpg", 1645, 720)

label start:
    $ inbox = Inbox("Rosa")

    $ phone = Phone()
    
    jump dwinelle_demo

label dwinelle_demo:

    scene black

    show screen phone_calling

    $ phone.receive_message("Hey, are you there?")

    "" 
    
    "Excuse me! Is this... GBO Group Six?" with s

    show dwinelle

    "A tall woman with puffy blonde hair stops just short of where I\'m standing, catching her breath from under the large, green gate. As she catches her breath,"

    "she\'s clutching a stack of wrinkled papers in one hand, while keeping herself steady by holding her knee with her other hand."

    p "Are you the Group Six orientation leader?"

    d "That would be me. My name's Rosa." with s

    "Despite the shaky introduction, Rosa looks well-dressed and a lot older than the other students I've seen, even compared to the other orientation leaders. Is she... a graduate student?"

    "Her face is well sculped and has lost the baby fat in her cheeks. And even at this distance, I can tell that she's wearing a strong perfume. Roses."

    scene sather
    show dwinelle

    "She's finally standing up after having gulped some air. She straightens out her shirt and takes a moment to compose herself."

    d "I'm pretty late, huh."

    "She's double checking her papers as she smooths them out. I can tell they're freshly printed since none of the corners are warped."

    return
    
    
