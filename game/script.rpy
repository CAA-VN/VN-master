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
    
    jump common_scene1
