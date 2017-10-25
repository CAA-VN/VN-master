
image top_text = ParameterizedText(window_bg = phone_frame, ypos=-0)

init python:
    import renpy.store as store

    class TextMessage(store.object):

        def __init__(self, message, is_self = True):
            self.message = message
            self.is_self = is_self
            self.sending_message = False
            self.align = 1.0 if is_self else 0.0

    class Inbox(store.object):

        def __init__(self):
            self.inbox = []
            self.msg_queue = []

        def add_message(self, message, delay = 1.0):
            renpy.pause(delay)
            self.inbox.append(message)
            renpy.restart_interaction()

        def show_animation(self):
            self.sending_message = True
            renpy.restart_interaction()

        def process_message(self):
            if self.msg_queue:
                self.inbox.append(self.msg_queue.pop(0))
            
            renpy.restart_interaction()
        
        def __iter__(self):
            for mail in self.inbox:
                yield mail

    inbox = Inbox()
    loading = LiveCrop((0, 0, 50, 7), "gui/phone_loading.png")

screen phone:
    modal False
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
            side "t r":
                area (0, 0, 260, 400)
                viewport id "message_list":
                    vbox:
                        for message in inbox:
                            frame: 
                                background None
                                xminimum 260
                                frame at :
                                    xalign (message.align)
                                    background phone_frame
                                    text (message.message) color "#000" 
            add loading
            
init -2 python:


    phone_frame = Frame("gui/frame.png", 15, 15)
    style.phone = Style(style.default)
    #style.phone_frame.background = None
    #style.phone_frame.xalign = 0.46
    #style.phone_frame.yalign = 0.5    
    style.phone_window.background = phone_frame
    