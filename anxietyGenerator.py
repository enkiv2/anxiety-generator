#!/usr/bin/env python

from random import Random
random = Random()
import sys, string

def interrogatories():
	return random.choice([
		"a lot of people have done this already.",
		"a lot of the people who succeed here are pretty awful people, so it's better that you don't even try.",
		"can you handle the rejection if you do this?",
		"do you think anyone will ever take you seriously if you try this?",
		"don't over-index on success here. Because it might not happen.",
		"have you ever finished anything?",
		"have you ever made progress on something like that?",
		"have you ever made something like this work?",
		"I don't know. Can you do any part of this? Even a small part?",
		"I don't meant to second-guess you.",
		"I don't want to doubt you, but...",
		"I doubt it can ever work.",
		"I doubt you can think of a place to get started, can you?",
		"I doubt you'll make progress here.",
		"I have no idea what success would look like here, well, except that this is obviously not success.",
		"I mean shouldn't it be done by now?",
		"I'd love to see you prove me wrong here.",
		"I'm guessing this all feels beyond you, which is normal for people who are risking everything without any real strategy.",
		"Is there anything you can do to keep this from being a total disaster?",
		"we all acknowledge it's a long shot for you even to attempt this.",
		"let's be honest, your track record is pretty weak.",
		"maybe it's better to just put all of this behind you?",
		"there's no chance you can pull this off, is there?",
		"let's just hope that past results don't equal future success.",
		"well, where's probably too much attention in life paid to actually doing things, don't you think?",
		"this problem is a barrier to success, but you can't have it all.",
		"where would you put your chances for success? Zero percent? Greater?",
		"you might just want to give yourself credit for good intentions.",
		"you probably are used to being at the front of the class, and this is a wake-up call that you're not even in the middle.",
		"you'll probably just screw it up, right?",
		"you're probably putting too much pressure on yourself to do something good.",
		"you're ready to buckle down, maybe. so that's good. If you do it.",
		"you should at least try."
	])

def offers():
	return random.choice([
		"In saying",
		"Telling people about how you're going to",
		"Offering that you're going to",
		"Insisting you can",
		"Demanding people believe you when you say that you will",
		"Being so sure you can",
		"Telling yourself that soon you are going to",
		"Being the guy who always says you will"
	])

def contemplatives():
	return random.choice(["I was thinking about your attempts to",
		"Let's talk about where you are at with your desire to",
		"A moment to talk about how you want to",
		"Just checking in talk about your thing where you",
		"Wondering about the status with your project to",
		"I don't know if you were serious when you said you wanted to",
		"I want to think about your plan to",
		"I heard you when you talked about how you wanted to",
		"So you want to",
		"You're finally ready to",
		"After what seems like forever you want to",
		"You wake up today and you're expecting to",
		"People are expecting you to",
		"So everyone is really curious to see if you can",
		"We were all talking about how you want to",
		"I understand that it is your goal to"])

def returns():
	return random.choice(["Anyway,",
               "So basically,",
               "what it comes down to is,",
               "what I want to know is,",
               "essentially,",
               "okay so",
               "the upshot is",
               "the thing that matters is:",
               "the fact to not here is,",
               "can you tell me: ",
               "are you ready to answer: ",
               "look at it like this:",
               "consider--",
               "reflect:",
               "tell me,",
               "drop a line,",
               "keep me in the loop,",
               "I'm curious,",
               "I'd be interested in hearing your take,",
               "I'm all ears--",
               "let me know: ",
               "inform me: "])

def call_to_action():
	return random.choice([
                     "what do you think?",
                     "what is your take?",
                     "can you do any of this?",
                     "are you ready?",
                     "will you even try?",
                     "is this another one of your \"things\"?",
                     "will you be able to change everyone's minds?"])

def indicators():
	return random.choice(["all signs point to you being",
                  "You:",
                  "Your issues in a nutshell: you're",
                  "just relax and stop pretending to be anything other than",
                  "your friends accept you even though you are undeniably",
                  "it's unfair that so many people say you're",
                  "you don't really deserve to be seen as",
                  "no one wants to tell you that you are",
                  "i wish you could accept that you are",
                  "all of your friends were trying to describe you and what came up was:",
                  "people are only tired of you because you are so",
                  "all the people you meet immediately think:",
                  "a tag cloud of your personality would include things like",
                  "i wonder how can you succeed at anything given that you are so",
                  "When I look at you, I think:",
                  "no one can blame you for being born",
                  "you mom and dad would never say anything but they so want to know why you choose to be",
                  "it's clear that you don't know what to do besides be",
                  "i respect that you just live your life and don't care if people think you are",
                  "most of your friends are doing okay, which makes me wonder why are you so",
                  "the only explanation for your career is that you are essentially",
                  "when you meet successful people they think of you as",
                  "Your total lack of self-control has left you",
                  "people pretend to be nice to you but they're thinking:",
                  "when you aren't around your friends say you are",
                  "it's true that you are basically",
                  "history will forget you because history forgets people who are",
                  "unlike successful people you are totally",
                  "compared to you, people who succeed are not so",
                  "unlike you, your 'friends' are not",
                  "the reason no one notices your work is because you are",
                  "the reason you are not famous is because you are",
                  "obviously you would go further in life except for your tendency to be",
                  "you could be successful if you were not",
                  "you might succeed if you didn't seem so",
                  "your parents deserve credit for loving someone so",
                  "compared to the rest of your family you sure are",
                  "compared with everyone else you grew up with you definitely turned out",
                  "Your whole life you've just been",
                  "your friends all say you are",
                  "like most people who procrastinate, you're",
                  "i don't agree with all of the people who say that you are",
                  "your mother always worried that you would turn out",
                  "if your grandparents were here right now they'd tell you that you are",
                  "people on Facebook look at your picture and think:",
                  "the minute you got in the cab your cab driver thought: I'm",
                  "it's a shame that people have painted you as",
                  "it's too bad everyone has decided you are",
                  "it's not entirely on you because people with your background are typically",
                  "it's just totally obvious that you are",
                  "the simple reason you are not happy is that you are",
                  "no doubt in my mind that you are",
                  "people in your neighborhood think of you as",
                  "ask yourself, do you always want to be",
                  "you do have something to offer, but it's too bad you're",
                  "it's hard to be a leader when you're",
                  "relax, there are worse things to be than so",
                  "you are too hard on yourself. I can think of worse ways to be than",
                  "don't beat yourself up for being",
                  "congratulate yourself. Most people would give up if they looked in the mirror and thought:",
                  "you might as well forgive yourself for being so incredibly",
                  "of all humans who ever lived you are the most"])

def youknow():
	return random.choice(["you know,",
              "which reminds me,",
              "speaking of that,",
              "not to beat a dead horse,",
              "and to take it a little further,",
              "and on that--",
              "okay, so--",
              "relatedly,",
              "I noticed that,",
              "I saw that,",
              "I made a note that"])

def action():
	return random.choice(["you wrote",
             "you told me",
             "you emailed me",
             "you said to me",
             "you said",
             "you made a comment",
             "you impulsively wrote back"])

def datespan():
	return random.choice(["not long ago",
               "pretty recently",
               "it wasn't too long ago",
               "the other day",
               "a little while ago",
               "just a little time ago",
               "recently"])

def person():
	return random.choice(["stupid", "vile", "fake", "soulless", "a bad friend", "childish", "selfish", "a fraud", "incapable of coming up with anything new", "unoriginal", "affected", "a loser", "foolish", "lumpy", "weak", "deeply flawed",  "dishonest", "hypocritical", "slow", "unable to finish anything", "badly prepared", "a terrible communicator", "inadequate", "not funny", "not smart", "not cool", "not interesting", "boring", "impossible to like", "living in fear", "afraid", "pitiful", "terrified of everything", "perpetually scared", "full of self-hatred", "shaky", "nervous", "afflicted by nerves", "weak-kneed", "deficient", "lacking in empathy", "lacking in intelligence", "devoid of brilliance", "not even clever", "incapable", "incompetent", "unequal to the task", "barely tolerable", "deservedly alone", "so easily forgotten", "likely to die soon", "diseased-looking", "at risk of a fatal disease", "a burden on others", "awkward", "socially weird", "hard to talk with", "poison", "wasteful", "fraudulent",  "like garbage", "cheesy", "fake", "unworthy of saving", "irredeemable", "phony", "faux-intelligent", "a liar", "a cheater", "deviant", "cretinous", "evil-looking", "awful", "unsightly", "unloveable", "lazy", "stupid", "devoid of willpower", "unambitious", "third-rate", "z-list", "boring", "exhausting to know", "predictable", "whiny", "needy", "ugly", "hideous", "misshapen", "awkward", "oddly-proportioned", "weird", "strange", "repulsive", "monstrish", "disgusting", "weird-faced", "unsexy", "untouchable", "crooked", "in posession of a weird nose", "undesirable", "strangely repulsive", "unkempt", "slobby", "weird-nosed", "sneaky-looking"])

oblique=["Close", "(Organic) machinery", "Abandon desire", "Abandon normal instructions", "Accept advice", "Allow an easement (an easement is the abandonment of a stricture)", "Ask people to work against their better judgement", "Ask your body", "Assemble some of the elements in a group and treat the group", "Back up a few steps", "Balance the consistency principle with the inconsistency principle", "Be dirty", "Be extravagant", "Be less critical more often", "Breathe more deeply", "Call your mother and ask her what to do.", "Cascade", "Change ambiguities to specifics", "Change instrument roles", "Change nothing and continue with immaculate consistency", "Change specifics to ambiguities", "Consider different fading systems", "Consider transitions", "Consult other sources", "Convert a melodic element into a rhythmic element", "Cut a vital connection", "Decorate", "Define an area as `safe' and use it as an anchor", "Describe the landscape in which this belongs", "Destroy nothing", "Destroy the most important thing", "Discard an axiom", "Disconnect from desire", "Discover the recipes you are using and abandon them", "Discover your formulas and abandon them", "Display your talent", "Distort time", "Do nothing for as long as possible", "Do something boring", "Do something sudden, destructive and unpredictable", "Do the last thing first", "Do the washing up", "Not avoid what is easy", "Not be afraid of things because they're easy to do", "Not be frightened of cliches", "Not be frightened to display your talents", "Not break the silence", "Not stress one thing more than another", "Emphasize differences", "Emphasize repetitions", "Emphasize the flaws", "Faced with a choice, do both", "Feed the recording back out of the medium", "Feedback recordings into an acoustic situation", "Fill every beat with something", "Find a safe part and use it as an anchor", "First work alone, then work in unusual pairs.", "Get your neck massaged", "Give the game away", "Give way to your worst impulse", "Go outside", "Shut the door.", "Go slowly all the way round the outside", "Go to an extreme, move back to a more comfortable place", "Humanize something that is free of error.", "Imagine the music as a moving chain or caterpillar", "Imagine the music as a series of disconnected events", "Just carry on", "List the qualities it has, then List those you'd like.", "Listen in total darkness, or in a very large room, very quietly", "Listen to the quiet voice", "Look at a very small object, then look at its centre", "Look at the order in which you do things", "Look closely at the most embarrassing details and amplify.", "Magnify the most difficult details", "Make a blank valuable by putting it in an excquisite frame", "Make a sudden, destructive unpredictable action; incorporate", "Make an exhaustive list of everything you might do and do the last thing", "on the list", "Make it more sensual", "Make what's perfect more human", "Mechanize something idiosyncratic", "Move towards the unimportant", "Mute and continue", "Overtly resist change", "Pay attention to distractions", "Put in earplugs", "Question the heroic approach", "Remember those quiet evenings", "Remove a restriction", "Remove ambiguities and convert to specifics", "Remove specifics and convert to ambiguities", "Remove the middle, extend the edges", "Retrace your steps", "Reverse", "Short circuit", "Shut the door and listen from outside", "State the problem in words as simply as possible", "Steal a solution.", "Take a break", "Take away as much mystery as possible", "Take away the elements in order of apparent non-importance", "Take away the important parts", "Tape your mouth", "Think of the radio", "Tidy up", "Trust in the you of now", "Try faking it", "Turn it upside down", "Twist the spine", "Use \"unqualified\" people.", "Use an old idea", "Use an unacceptable color", "Use cliches", "Use fewer notes", "Use filters", "Use something nearby as a model", "Use your own ideas", "Voice your suspicions", "Work at a different speed"]

def project():
	return random.choice(["waste of time", "stupid", "meaningless", "pointless", "empty"])

def description():
	return " and ".join([person(), person(), person(), person()])

def crit():
	return " ".join([indicators(), description()])

def make_reply(reply):
	if(not reply):
		 return ""
	return ".\n\n"+(" ".join([youknow(),  datespan(), action(), ",", reply, "--and", youknow(), crit()]))

def compose(anxiety, reply):
	return ".".join(map(string.capitalize, string.split(((" ".join([contemplatives(),anxiety]))+".\n\n"+(" ".join([interrogatories(), offers()]))+" \""+anxiety+"\" -- "+(" ".join([make_reply(reply), returns(), interrogatories(), returns(), call_to_action()]))), "."))).replace(" i ", " I ").replace("\ni ", "\nI ")

if(len(sys.argv)>1):
	anxieties=sys.argv[1:]
else:
	anxieties=oblique

print(compose(random.choice(anxieties), None))
reply=raw_input("> ")
while reply!="":
	print(compose(random.choice(anxieties), reply))
	reply=raw_input("> ")
