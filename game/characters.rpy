
init python:
    
    def character_factory(name, narrator = False):
        prefix, suffix = '“', '”'

        if narrator:
            prefix, suffix = "", ""

        return Character(name, 
                what_prefix = prefix, 
                what_suffix = suffix,
                ctc = "ctc_blink")


#Full character definitions

define narrator = character_factory(None, True)
define nvl_narrator = Character(None, kind=nvl)

define player = character_factory(None)
define dwinelle = character_factory("Rosa")
define player_mom = character_factory("Mom")
define cora = character_factory('Cora')
define violet = character_factory('Violet')

#Shortened definitions

define p = player
define d = dwinelle
define p_m = player_mom
define nvl_n = nvl_narrator
define c = cora
define v = violet

#Character images

image dwinelle_default = "dwinelle/default.png"
