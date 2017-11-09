
init python:
    import renpy.store as store

    class TextMessage(store.object):

        def __init__(self, message, is_self = True):
            self.message = message
            self.is_self = is_self
            self.sending_message = False
            self.align = 1.0 if is_self else 0.0
            self.message_frame = user_frame if is_self else other_frame
            self.color = "#fff" if is_self else "#000"

    class Inbox(store.object):

        def __init__(self, other = ""):
            self.inbox = []
            self.msg_queue = []
            self.other = other
            self.loading_image = None

        def change_recipient(self, name):
            self.other = name

        def add_message(self, message, delay = 1.0):
            if message.is_self:
                self.stop_animation()
            else:
                self.start_animation()
            renpy.pause(delay)
            self.inbox.append(message)
            self.stop_animation()
            renpy.restart_interaction()

        def start_animation(self):
            self.loading_image = "phone_loading"
            renpy.restart_interaction()

        def stop_animation(self):
            self.loading_image = None
            renpy.restart_interaction()
       
        def process_message(self):
            if self.msg_queue:
                self.inbox.append(self.msg_queue.pop(0))
            
            renpy.restart_interaction()
        
        def __iter__(self):
            for mail in self.inbox:
                yield mail
    
    class Phone(store.object):

        def __init__(self):
            self.message = ""

        def call(self, caller):
            pass

        def hangup(self):
            pass

        def receive_message(self, message):
            self.incoming_message = message
            renpy.restart_interaction()
            renpy.pause()
        


    inbox = Inbox("")
    phone = Phone()

image phone_loading:
    LiveCrop((0, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((50, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((100, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((150, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((200, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((250, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((300, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    LiveCrop((350, 0, 50, 7), "gui/phone_loading.png") 
    0.1
    repeat


screen phone_text:
    modal False
    frame:
        xalign 0.46 yalign 0.5
        add "gui/phone_overlay.png"
        background None
        style_group "phone_text"
        vbox:
            xalign 0.49
            yalign 0.4
            xfill False
            text(inbox.other) xalign 0.5 color "#000"
            side "t r":
                area (0, 20, 265, 400)
                viewport id "message_list":
                    vbox:
                        for message in inbox:
                            frame: 
                                background None
                                xminimum 260
                                frame at :
                                    ypadding 8
                                    xpadding 8
                                    xalign (message.align)
                                    background message.message_frame
                                    text (message.message) color message.color size 14
                vbar value YScrollValue("message_list")
            #add inbox.loading_image yalign 1.0

screen phone_calling:
    modal False
    frame:
        xalign 0.46 yalign 0.5
        add "gui/phone_call_base.png"
        background None
        style_group "phone_call"
        vbox:
            xalign 0.49
            yalign 0.4
            xfill False
            add "gui/rosa_head.png" xalign 0.5 ypos -90
            text ("Rosa") xalign 0.5 ypos -80

            side "b r":
                area(0, 20, 265, 70)
                text ('"You still there?"') size 14 xalign 0.5 ypos 80
            
            
init -2 python:
    user_frame = Frame("gui/user_text.png", 6, 6)
    other_frame = Frame("gui/other_text.png", 6, 6)
    style.phone = Style(style.default)
    #style.phone_frame.background = None
    #style.phone_frame.xalign = 0.46
    #style.phone_frame.yalign = 0.5    
    