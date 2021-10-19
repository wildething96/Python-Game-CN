import os
from useful_functions import typeWriter, typeWriter2, isInt


# dictionaries of each guest
worth = {
    "Who are you?": "I am Mr Worth's wife",
    "How can you describe your relationship with your husband?": " We loved and supported each other. He had his work and I had my love for board games. I travel through the country to attend tournaments so I would only see him on the weekends.",
    "Anything happened recently that will push someone to kill him?": "No, we had a very beautiful life. In fact, we were celebrating tonight his promotion at work with friends.",
    "Did you notice anything suspicious tonight?": "No, everyone seems happy to be here and enjoying the night. Only a small hiccup tonight with our former gardener who was not very happy about being let go",
    "Where were you at the time of the accident?" : "I was in the kitchen, making sure that everything was ready for tonight",
    "Any idea why there was a knife under your bed Mrs Worth?" : "Is not what you think Detective, well it was but I could go through with it. I found out that my Husband has" +
    "been cheating on me with that repulsive Mrs Miller, they were even going to run away together and leave me with nothing!" +
    "I lost my head for second for a moment but despite it all I couldn't do it",
    "Do you know about your husbands will?" : "Yes... sort of. I mean I do but I do not know its contain"
}  


bouchet = {
    "Who are you?": "I am Mr Garcon Bouchet, as to yesterday the gardener of Mr & Mrs Worth.",
    "Why were you invited to the dinner party?": "As a parting gift from Mrs Worth.",
    "Why were you fired?": "Supposedly, they could not afford my service anymore but I doubt it is the real reason",
    "How long have you been working for the Worth?": "I worked on this manor for 17 long years. The Worth have been occupying the property for the 7 last years.",
    "You must have seen and heard quite a lot. Do you know anyone that might have a reason to kill the victim:": "I have no idea. though something has been going on with him and Mrs Miller.",
    "Is there anything you know from working on the estate that might be of interest" : "I know that Mrs Worth has been betting on chess matches and has racked up quite the debt, though she hasn't told Mr Worthh",
    "Why were you arguing with Mr. Worth earlier in the evening bouchet?" : "I was convincing him to let me keep my job. As I have a very ill wife and her medical bills are not cheap.",
    "Did you notice anything suspicious tonight?": "Nothing, I have a lot on my mind. This evening was a complete blur.",
    "Where were you at the time of the murder?" : "I was in the dinner room" 
}
miller = {
    "Who are you?": "Hello detective, I am Mrs Claudia Miller, the wife of Mr. Worth's bestfriend Mr Miller",
    "Are you here with your husband?": "I am but he's not here right now, he went for one of his walks after eating. though he should be back by now",
    "How did your husband and Mr. Worth get to know each other?": "They were university buddies. They did everything together..... ",
    "Do you know if Mr. Worth had a will or his contain?" : "Yes, my husband told me that in case of his death, his wife will inherit everything",
    "How would you describe the relationship between Mr and Mrs Worth?": "From the outside, they were the perfect couple. Although Mr Worth was always complaining at lot about his wife's endless chess tournaments. He felt neglected by his wife and alone.",
    "Did you see or hear anything suspicious?": "At one point, I was feeling dizzy. So I left the dinner party for 10 minutes to find refuge in one of the bedroom. I saw Mr Worth and the Garderner arguing loudly",
    "Where were you at the time of the accident of Mr. Worth?": "I was in the dinning room with the others guest.",
    "Was there anything going on between you and Mr Worth?" : "Why would you ask that? has somebody said something?",
}

ricardo_simpson = {
    "Who are you?" : "I am Mr Worth's colleague.",
    "What was your relationship with the deceased?" : "We were working together at Berkshire Group.",
    "How long have you been working side to side with him?" : "He has been in the group for 3 years before I joined him 7 years ago",
    "Were you and Mr. Worth on good terms?" : "Not really. Mr. Worth was not afraid to cut corners or used anything he can so he can get ahead. This promotion should have been mine!!!",
    "Why were you invited to the dinner party" : "The dinner party was to bury the hatchet and have a fresh start in our professional relationship",
    "When did you see Mr. Worth last ricardo?" : "I saw him right before he left for his errand.",
    "Have you seen or heard anything strange?" : "On several occasions, I have seen Mrs Miller and Mr Worth have lunches together. The way.... ",
    "Where were you at the time of the accident?" : "I was in the bathroom.",
}

jane_simpson = {
    "Who are you?" : " I am Mr Simpson's wife.",
    "How will describe Mr. Worth?" : "He was a cheater, a liar and asshole.",
    "You did not like him very much. Why is that?" : "He rips that promotion from my husband again. Despise Ricardo's hard work and honesty, he has sunk behind Mr. Worth. We should have the house, the money and the promotion, not him!" ,
    "Why did you come to the party?": "I wouldn't be here if it was not for my husband. I hated Mr Worth!!",
    "When did you see the deceased last?": "I was on my way back from the bathroom, when I saw Mrs Miller and Mr. Worth kissing in one of the bedroom. Poor Mrs. Worth if she knew",
    "Have you seen or heard anything strange?" : "Put a clue here",
    "Where were you at the time of the murder jane?" : "I was out looking for my Husband",
}

daryl = {
     "Who are you?": "I am Mrs. Gwendal Daryl, a friend of the Worth and their next door neighbor.",
    "How long have you know the Worth?" : "Since they moved in but I got closer with Mr. Worth 4 years ago.",
    "Were you in good terms with Mr. Worth? " : "Yes, we were. He was charming, playful and very helpful. Once a week, he would pay me a visit to play cards with me, chat and keep me company.",
    "Do you know anything about Mr. Worth's will?" : "He told me once that everything will be given to his wife in case of his death",
    "Do you know anyone that might have a reason to kill him daryl?" : "I know Mrs simpsons hated him but hope she wouldn't do something like this",
    "Have you seen and heard anything suspicious?" : "Now you mention it, I saw a big pair of sharp metal scissor in Mrs. Simpson's bag earlier when she dropped it. ",
    "Where were you at the time of the murder?" : "I was having a conversation with Mrs Miller in the dinning room",
}

#List of the guests
guests = {
    "Bella worth" : worth,
    "Garcon bouchet" : bouchet,
    "Claudia Miller": miller,
    "Ricardo simpson": ricardo_simpson,
    "Jane simpson" : jane_simpson,
    "Gwendal daryl": daryl
}

guest_names = []
guest_questions = []
guest_selection = 0
last_guest = 0
only_once = 0

def guestMenu(mainMenu):
    global guest_selection, last_guest, only_once, last_question
    os.system("cls||clear")
    typeWriter("Guest Menu".center(160) + "\n\n\n")
    guest_questions.clear()
    last_question = 0
    
    for num, guest in enumerate (guests, start = 1):
            typeWriter2((str(num) + ". " + str(guest)).center(160) + "\n\n")
            last_guest = num
            if only_once == 0:
                guest_names.append(guest)
           
    only_once = 1
    typeWriter((str(last_guest + 1) + ". Go back to Main Menu").center(160) + "\n\n")

    guest_selection = isInt(last_guest + 2, 0)
    if last_guest + 1 == guest_selection: mainMenu()
    
    os.system("cls||clear")
    questionMenu(mainMenu)

last_question = 0 # stores last_question in a guest's questions

def questionMenu(mainMenu):
    global guest_selection, last_question, worth_extra

    typeWriter(f"Ask {guest_names[guest_selection - 1]} a question".center(160) + "\n\n\n")


    for num , question in enumerate (guests[guest_names[guest_selection - 1]].keys(), start = 1 ):
        typeWriter2((str(num) + ". " + question).center(160) + "\n\n")
        guest_questions.append(question)
        last_question = num
  

    typeWriter2((str(last_question + 1) + ". Goodbye " + guest_names[guest_selection - 1] ).center(160) + "\n\n") # prints another final question at the bottom of list e.g. 4. Go back 
    question_selection = isInt(last_question + 2, 0)
    os.system("cls||clear")

    if last_question + 1 == question_selection: guestMenu(mainMenu) # compares last question to selection, if True takes user back to Guest Menu
    try:
        typeWriter(guests[guest_names[guest_selection - 1]].get(guest_questions[question_selection - 1]).center(160) + "\n\n")
    except IndexError:
        typeWriter
    input("Continue?".center(160) + "\n".center(160))
    os.system("cls||clear")

    guests[guest_names[guest_selection - 1]].pop(guest_questions[question_selection - 1])
    guest_questions.pop(question_selection - 1)
    questionMenu(mainMenu)