import random

q1 = "Mental health is a state of mental well-being that enables people to cope with stress. The need for action on mental health is indisputable and urgent."
q2 = "Dont be sad, cheer up. I am here to assist you"
q2_ = "Practice deep breathing, exercise, prioritize tasks, set boundaries, seek support, and maintain perspective for effective stress management. This can make you feel better"
q3 = "Try to deviate your mind into some positive things if you feel this way"
q4 = "I'm really sorry to hear that you're feeling this way, but I can't provide the help that you need. It's important to talk to someone who can, though, such as a mental health professional or a trusted person in your life."
q5 = "Yes a doctor's help can be a good option. Please go ahead on our website to book your appointment with our experts"
q6 = "I know right, Its really imp to have a good friend circle who always support and motivates you to achieve your life goals "
q7 = "Im here to help! If youre comfortable, please share more details or specific concerns so I can provide more targeted assistance. If its a serious or urgent matter, consider reaching out to a mental health professional or someone you trust."
q8 = "good to see that yu are happy today :)"
q9 = "You can use the following resources : https://www.youtube.com/watch?v=PTAkiukJK7E.\nYou can also refer to the following videos - https://www.youtube.com/watch?v=CNkiPN_WZfA"
q10 = "Why don't scientists trust atoms?/n Because they make up everything!"
q11 = "Emotional Assistance de sakta hu aapko but abhi Tejaswi Didi fir se banayengi mujhe tabh batata hu lol"
q12 = "Yes, you can use '/reminder' to set a reminder for the appointment"
q13 = "Sure, to check your registeration deatils head to /registration -> /confirm."
q14 = "What makes you sad? Is it the work load? or something else that troubles you dear? "
q15 = "I am a bot that will help you in your lows and keep your spirit up <3"
q15_ = "I am a bot that will help you in your lows and keep your spirit up <3"
q16 = "You can head to the --Book your appointment now!-- to get a personalised slot booked for you"
q17 = "Sure, you can use the '/contact' for getting the contact details of our organisers."
q17_ = "Sure, you can use the '/contact' for getting the contact details of our expert doctors"
q18 = "Tried watching Sadhguru meditative videos??? They actually make you feel comfortable."
q19 = "I am here to help you manage your mental health.... <3 "
q20 = "Yes, I'll be happy to answer that :)"

def unknown():
    response = ["Could you please re-phrase that? ",
                "Hmm I'll work on understanding this, But till then please rephrase it :)",
                "I think you have misspelled it dear",
                "What does that mean?","Sorry! I am unable to understand it"][
        random.randrange(5)]
    return response

import re

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'greetings'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','are','you'])
    response('You\'re welcome!', ['thank', 'thanks','thankyou'], single_response=True)
    response('Thank you!', ['i', 'love', 'you'], required_words=['love', 'you'])
    response('Great to hear!',['fine','good','doing','well'],single_response = True)
    response('I am Sylvie-the bot! I am here to guide you through this journey',['who','are','you'],required_words = ['who','are','you'])
    # Longer responses
    response(q1, ['what','mental','health'],required_words= ['mental','health'] )
    response(q2,['I','sad'],required_words = ['sad'])
    response(q2_,['stress'],required_words = ['stress'])
    response(q3,['family'],required_words = ['family'])
    response(q4,['suicide'],required_words = ['suicide'])
    response(q5,['doctor'],required_words = ['doctor'])
    response(q6,['friends'],required_words = ['friends'])
    #response(q7_,['where','place','location'],required_words = ['location'])
    response(q7,['help','me'],required_words = ['help'])
    response(q8,['happy'],required_words = ['happy'])
    response(q9,['prepare','resources','resource','material'],required_words = ['resources'])
    response(q10,['joke'],required_words = ['joke'])
    response(q11,['assistance'],required_words = ['assistance'])
    response(q12,['set','give','reminders'],required_words = ['reminder','set'])
    response(q13,['confirm','registration'],required_words = ['confirm','registration'])
    #response(q15_, ['updates','update','changes','notice','notices','change','hackathon','hackathons'],required_words = ['updates'])
    response(q14,['depressed'],required_words = ['depressed'])
    response(q15,['what','bot'],required_words = ['what','bot'])
    response(q16,['how','book','appointment'],required_words = ['appointment'])
    response(q17,['talk','organizer','coordinator','contact'],required_words = ['talk'])
    response(q17_,['talk','contact'],required_words = ['contact'])
    response(q18,['provide', 'resources'],required_words = ['resources'])
    response(q19,['what','for','me'],required_words = ['what','for','me'])
    response(q20,['ask','question'],required_words = ['ask','question'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    #print(response)
    return response
