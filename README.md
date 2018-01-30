# VN-master

# Continuous Integration

As such, as of now I am planning on creating a simple CI for this project, which will include extra helpful features like a node graph for each pull.

# Tentative Style and Conventions Guide

In order to keep the code base from becoming spaghetti (very easy in renpy), please follow these rules or I will not accept your pull request.

*Note:* These are not final, if something doesn't really work out or could be better, just start a conversation on discord

* Route names for programmming purposes will be the last name of the corresponding character
* All .rpy files relating to a specific route *must* be under a subfolder under game
  
  * That subfolder should have the name of the route
  
* *ALL* global labels must be formatted as such: `routename_x`, where x can be anything you want.

  * For example, dwinelle_lunch is a possible global label.
  
  * This is to prevent label collision. Unfortunately, having all labels inside a specific route be sublabels is not terribly feasible, so this pseudo namespace is the compromise
  
* Avoid if at all possible *define* statements inside files inside your route folder; keep them in the global .rpy files in root

* Keep all character definitions in character.rpy; create the character definition with the full name, then create a shorter one below

* Do modify gui.rpy

* Try to override styles in override_styles.rpy instead of modifying screens.rpy (it's just easier to see changes)
  
* Python code is expected to follow [PEP8](https://www.python.org/dev/peps/pep-0008/), essentially follow the style part of [CS61a](https://cs61a.org/articles/composition.html)

  * This is a looser rule, just skim through and try.
