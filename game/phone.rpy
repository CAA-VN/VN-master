
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

        caller_dictionary = {
            'Rosa': 'gui/rosa_head.png',
            'Mom': 'gui/unknown-female.png'
        }

        def __init__(self):
            self.message = ""
            self.audio_image = "audio_wave_quiet"
            self.caller_image = "gui/unknown-female.png"
            self.caller = ""

        def call(self, caller):
            renpy.show_screen("phone_calling")
            self.caller_image = self.caller_dictionary.get(caller, "gui/unknown-female.png")
            self.caller = caller

        def hangup(self):
            renpy.hide_screen("phone_calling")
            self.caller_image = "gui/unknown-female.png"
            self.caller = ""


        def receive_message(self, message, continuous = False, delay=-1.0):
            self.message = message
            self.audio_image = "audio_wave"

            if delay < 0:
                avg_sec_per_letter = 0.085
                delay = len(message.replace(" ", "")) * avg_sec_per_letter

            renpy.restart_interaction()
            renpy.pause(delay)
            self.audio_image = "audio_wave_quiet"
            renpy.restart_interaction()

            if not continuous:
                renpy.pause()

        


    inbox = Inbox("")
    phone = Phone()

image audio_wave:
    "gui/audio_wave/1.png" #the image is 110x32
    0.06
    "gui/audio_wave/2.png"
    0.06
    "gui/audio_wave/3.png"
    0.06
    "gui/audio_wave/4.png"
    0.06
    "gui/audio_wave/5.png"
    0.06
    "gui/audio_wave/6.png"
    0.06
    "gui/audio_wave/7.png"
    0.06
    "gui/audio_wave/8.png"
    0.06
    "gui/audio_wave/9.png"
    0.06
    "gui/audio_wave/10.png"
    0.06
    "gui/audio_wave/11.png"
    0.06
    "gui/audio_wave/12.png"
    0.06
    "gui/audio_wave/13.png"
    0.06
    "gui/audio_wave/14.png"
    0.06
    "gui/audio_wave/15.png"
    0.06
    "gui/audio_wave/16.png"
    0.06
    "gui/audio_wave/17.png"
    0.06
    "gui/audio_wave/18.png"
    0.06
    "gui/audio_wave/19.png"
    0.06
    "gui/audio_wave/20.png"
    0.06
    "gui/audio_wave/21.png"
    0.06
    "gui/audio_wave/22.png"
    0.06
    "gui/audio_wave/23.png"
    0.06
    "gui/audio_wave/24.png"
    0.06
    "gui/audio_wave/25.png"
    0.06
    "gui/audio_wave/26.png"
    0.06
    "gui/audio_wave/27.png"
    0.06
    "gui/audio_wave/28.png"
    repeat

image audio_wave_quiet:
    "gui/audio_wave/quiet_1.png"
    0.06
    "gui/audio_wave/quiet_2.png"
    0.06
    "gui/audio_wave/quiet_3.png"
    0.06
    "gui/audio_wave/quiet_4.png"
    0.06
    "gui/audio_wave/quiet_5.png"
    0.06
    "gui/audio_wave/quiet_6.png"
    0.06
    "gui/audio_wave/quiet_7.png"
    0.06
    "gui/audio_wave/quiet_8.png"
    0.06
    "gui/audio_wave/quiet_9.png"
    0.06
    "gui/audio_wave/quiet_10.png"
    0.06
    "gui/audio_wave/quiet_11.png"
    0.06
    "gui/audio_wave/quiet_12.png"
    0.06
    "gui/audio_wave/quiet_13.png"
    0.06
    "gui/audio_wave/quiet_14.png"
    0.06
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

screen phone_calling:
    modal False
    frame:
        xalign 0.46 yalign 0.5
        add "gui/phone_call_base.png"
        background None
        style_group "phone_call"
        frame:
            background None
            yalign -1
            xfill False
            add (phone.caller_image) xalign 0.49 ypos 100
            text (phone.caller) xalign 0.49 ypos 220

            add (phone.audio_image) xalign 0.49 ypos 400
            text (phone.message) size 14 xalign 0.49 ypos 430 xmaximum 240
            
            
init -2 python:
    user_frame = Frame("gui/user_text.png", 6, 6)
    other_frame = Frame("gui/other_text.png", 6, 6)
    style.phone = Style(style.default)
    #style.phone_frame.background = None
    #style.phone_frame.xalign = 0.46
    #style.phone_frame.yalign = 0.5    
    