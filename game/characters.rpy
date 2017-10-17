
init python:
    
    def character_factory(name, narrator = False):
        prefix, suffix = '"', '"'

        if narrator:
            prefix, suffix = "", ""

        return Character(name, 
                what_prefix = prefix, 
                what_suffix = suffix,
                ctc = "ctc_blink")


#Full character definitions

define narrator = character_factory(None, True)

define player = character_factory(None)
define dwinelle = character_factory("Rosa")


#Shortened definitions

define p = player
define d = dwinelle
