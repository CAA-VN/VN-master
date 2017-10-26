
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

        def __init__(self, other = ""):
            self.inbox = []
            self.msg_queue = []
            self.other = other
            self.loading_image = None

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

    inbox = Inbox("")

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
            text(inbox.other) xalign 0.5 color "#000"
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
            add inbox.loading_image
            
init -2 python:


    phone_frame = Frame("gui/frame.png", 15, 15)
    style.phone = Style(style.default)
    #style.phone_frame.background = None
    #style.phone_frame.xalign = 0.46
    #style.phone_frame.yalign = 0.5    
    style.phone_window.background = phone_frame
    