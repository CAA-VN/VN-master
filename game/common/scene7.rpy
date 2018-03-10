label common_scene7:
    
    scene bg sather_gate
    
    "Wrapping the last half of my sub, I turn toward the direction of my dorm."
    "Before I can go any further, I feel a vibration. I hear a faint, familiar ringtone play as I pull my phone from my pocket, seeing 'Trav Stratton' displayed on the screen along with a picture of a young boy, middle school aged."
    "Though the song is drowned out by the street noise and bustle from the plaza, I can recall the lyrics to it by heart. He speaks cheerfully first before I can get a single word in."
    $ phone.call('Trav')
    $ phone.receive_message("‘Allo, allo! Did you forget about the little people already? You’re so cold!")
    p "You’re the one who chose not to go to school, Trav."
    $ phone.receive_message("And yet here I am, stress-free and working... Where are you again?")
    "Travis Stratton. I’ve been friends with him since elementary school. He’s always been a quick-witted, happy guy, and we’ve stayed close friends." 
    "His own academic success is near nonexistent, choosing to enjoy his youth instead of worrying about homework, or even classwork." 
    "When I told him that I was entering Bell University, he feigned heartbreak after hearing how far away I would be going."
    "He stopped pursuing any more education. He’s still working at his family business in our hometown, saying that life was exciting where he settled."
    "I decide to poke at him."
    p "Better than where you are."
    $ phone.receive_message("Ouch, and here I was, trying to check in on you. Let’s talk though! Is now a bad time?")
    p "It’s fine, I just finished lunch on campus. I’m still trying to find a spot to eat during the semester."
    $ phone.receive_message("Isn’t there a cafeteria or something?")
    p "If there is, I haven’t found it yet. Other than the dining hall near my dorm."
    $ phone.receive_message("Look harder then. You got any plans afterwards?")
    p "Just going to head home."
    $ phone.receive_message("Great! Then tell me about Bell. Is it everything you ever wanted? Were all of your fantasies realized? Is it truly magical?")
    "It’s only been a few days since I moved into the dorms, yet so many things have already happened."
    p "The university is huge, and beautiful like the pamphlets we looked at together; there are people walking everywhere, at all times." 
    p "I was surprised to see so many different people around, but I think that it’ll keep things interesting around here. Everyone has a direction they want to go, and they’re pretty passionate about what they want to do."
    p "Just like what a top university is supposed to be like."
    "I hear a whistle from the receiver."
    $ phone.receive_message("Wow, a real utopia.")
    "Suddenly, a flash of memories remind me of some less savory things. From the crime reports of the area to the litter I saw under the bridge, there were things that were hidden under the surface of the seemingly pristine university." 
    "I think back to the amount of homeless people that I saw—that pass me right now, as I’m walking back to my dorm. Though I haven’t heard a 'Heck Yeah' today, I knew that I would encounter the man again. My worries cloud my mind like a puff of smoke."
    p "Close enough."
    $ phone.receive_message("Why only close?")
    p "Well."
    "I trail off for a moment, wondering how much I should tell him. Even though I hadn’t experienced anything personally, there is a fear that I would soon."
    p "I think everyone here is afraid of their grades falling. They aren’t worried about the homeless here, but they do avoid stepping on ground ornaments because of superstitions."
    $ phone.receive_message("Like, what kind of superstitions? Help me out here, it’s not like I go there.")
    p "Stuff like stepping on a seal would doom your 4.0 GPA, but then rolling down a small hill on campus would restore your luck."
    p "And then entering the main library, but going out of a different entrance to keep the knowledge of everything you just studied."
    "A burst of laughter on the other side of the line stops me from continuing."
    $ phone.receive_message("Sounds like bullshit to me.")
    "I let him finish, a little glad that someone finds it as ridiculous as I originally thought. But Bell must be bothering more than I know, because I choose to linger on the topic."
    p "Everyone else treats it pretty seriously though."
    $ phone.receive_message("It’s just old wives’ tales meant to scare off new kids. I bet they’re all in on the same prank.")
    p "I guess."
    $ phone.receive_message("You haven’t even picked out your classes yet. Don’t be so worried about your GPA.")
    "I sigh away from the phone. Was it still worth it to try and finish my thought?"
    p "The environment is still pretty new. I don’t know why there are so many superstitions oriented around grades. And everything is… different."
    $ phone.receive_message("Different can be fun! You’re just getting the new school jitters like when we entered high school. It’ll be fine.")
    $ phone.receive_message("Listen, if you were top of the class all your life, there’s no way you’ll do bad at Bell.")
    
    p "I guess you have a point."
    $ phone.receive_message("The pointiest! Just chill out and go with it. A university is like a whole new universe waiting to be explored!")
    "Though unconvinced, I divert Trav’s attention to a new topic."
    p "The people around here are much different than back at home, too."
    $ phone.receive_message("Oh, ho? Who have you met?")
    p "Not too many at the moment, but I met a couple of people right before you called. Marie and William. I had lunch with one, and met the other while she was advertising for her club."
    
    p "They knew each other beforehand, but they’re both on bad terms."
    "I hear laughter."
    $ phone.receive_message("Oh man, there’s some drama already? Geez what a cruel world.")
    p "I’m not sure what it’s about yet. Seems messy, though."
    $ phone.receive_message("You think you’ll get the chance to?")
    p "Maybe, or maybe not. I’m not sure yet. They were both older than me, so I don’t think I’ll have many chances unless I take classes with them."
    p "Marie had a… strong personality. And it doesn’t seem like William wants to bother her more than he already has."
    $ phone.receive_message("Who else didja meet?")
    "I hesitate."
    p "A senior named Rosa."
    $ phone.receive_message("How’d you meet?")
    p "She was my orientation leader, who was substituting for my real orientation leader. A lot of it is kind of complicated."
    p "Long story short, she opened my eyes to a lot of things that I didn’t realize before, and I don’t know if I liked what I saw—"
    $ phone.receive_message("Not this again. Don’t worry, kid, you’ll be fine! Don’t let one person scare you off.")
    p "I… I won’t, Trav."
    $ phone.receive_message("Great! Hopefully you’ll meet some people our age soon. The older people sound kind of weird.")
    p "Actually, I did on my second day. Both of them live in my building and they helped me around campus."
    p "Well, one of them did. Her name is Vi. The other girl, Cora, wasn’t very talkative until we started talking about CS."
    $ phone.receive_message("Which is?")
    p "CS. It stands for Computer Science. Cora was planning to be an Electrical Engineering and Computer Science major, so she’s taking 'fill'."
    $ phone.receive_message("That sounds like some complicated stuff. Dang, I could never do any of that.")
    p "Vi already figured out her major too. She’s an intended 'fill' major, on track to enter the medical field. I think that she’s taking BIO 1B as a prerequisite."
    $ phone.receive_message("A go-getter. I like that. What about the other people? Are they doing stuff like rocket science already?")
    p "Marie was set on doing Pre-Haas, which is the business major. She’s taking 'fill' while William didn’t look like he really cared about his major. He said he was taking fun classes like 'fill'. As for Rosa..."
    "I rattle my head for her major. While only a few days had passed, it felt like weeks had already gone by."
    p "I think it was English. She was doing 'fill'. She doesn’t care about doing well at all, though."
    "Trav let out a small snort. I can imagine his playful signature smirk on his face."
    $ phone.receive_message("No offense, but I think that it’s funny how the first years have the STEM majors while the older kids are more into the social sciences and stuff.")
    $ phone.receive_message("What about you? I don’t think you told me your major before you left for Bell.")
    p "I don’t have one yet. I’m supposed to be choosing my classes at the end of orientation, which basically picks my major."
    p "When it’s time to pick, I have to make my schedule based on what I want to do and what I want my future to look like."
    $ phone.receive_message("Woah, that’s loads different than in high school! I forgot that you build your own schedule in college.")
    p "It’s also a lot of pressure."
    $ phone.receive_message("You got that right, but there’s no way that you aren’t leaning toward one already. So spill it!")
    p "Come on, Trav. I still have time to think about it."
    $ phone.receive_message("Not that much though. I don’t know, kid. You gotta pick whatever you think is best, you know?")
    $ phone.receive_message("Something that you can manage with people that you might like. It’s gotta be something you know you can do.")
    p "Yeah, I get you. But what is best?"
    $ phone.receive_message("Obviously something that’s safe and secure. Why else do you think I’m taking on the shop with my parents?")
    "My silence prompts him to say more."
    $ phone.receive_message("Listen, it sounds like you need some time to think about it by yourself. Don’t worry too much about it though, friend.")
    $ phone.receive_message("It’s just a decision that will affect you for the rest of your life. No take backs!")
    "He laughs a little, pleased with his own advice."
    $ phone.receive_message("I’ll let you go for now; think long and hard, ok?")
    p "Yeah, I will. Thanks for calling, Trav."
    $ phone.hangup()
    "After I hang up, I toss myself into bed and sigh. I’m reminded of how draining Trav can be, and also how well natured he is."
    "He has a pace that I have trouble keeping up with, but I know that I can rely on his friendship to push me forward."
    "Talking with him put my long days into perspective. A lot did happen in a short period of time, and I’m glad that I got a moment to sort it all out. Was college always going to be so eventful?"
    "I ignore another news update on my phone, rolling off to the side to face the wall."
    "A major… is a major decision. One that I don’t think I’m prepared enough to make. The time to choose is approaching more quickly than I realized."
    
    jump common_scene8
