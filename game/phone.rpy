
image top_text = ParameterizedText(window_bg = phone_frame, ypos=-0)

init python:
    import renpy.store as store

    class Text(store.object):

        def __init__(self, message, is_self = True):
            self.message = message
            self.is_self = is_self
    
    class Inbox(store.object):
        
        def __init__(self):
            self.mail = []

screen phone:
    modal True
    frame:
        xalign 0.46 yalign 0.5
        add "gui/phone_overlay.png"
        background None
        style_group "phone"
        vbox:
            xalign 0.485
            yalign 0.4
            xfill False
            label "Inbox"
            text ("Messages: 69")
            side "t r":
                area (0, 0, 260, 400)
                viewport id "message_list":
                    vbox:
                        for i in range(5):
                            frame: 
                                background None
                                xminimum 260
                                frame at :
                                    xalign 1.0
                                    background phone_frame
                                    text ("Is that true?") color "#000" 
            
        hbox:
            null height 20

init -2 python:


    phone_frame = Frame("gui/frame.png", 15, 15)
    style.phone = Style(style.default)
    #style.phone_frame.background = None
    #style.phone_frame.xalign = 0.46
    #style.phone_frame.yalign = 0.5    
    style.phone_window.background = phone_frame
    