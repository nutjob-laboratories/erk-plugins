from erk import *
import random

_ERK_PLUGIN_ = "Nick Grabber"

class NickGrabber(Plugin):
	"""
	
		NICK GRABBER

		An Ərk plugin to automate trying to grab
		a nickname that someone else is using.
		Creates a new command, /grab:

		/grab DESIRED_NICKNAME

	"""

	NAME = "Nickname Grabber"
	VERSION = "1.0"
	DESCRIPTION = "Grabs an in-use nickname"

	def __init__(self):
		self.nickname_to_grab = None
		self.wait = 0

	def input(self,window,text):

		# Here, we're going to create our new command
		
		# First, tokenize the user input
		tokens = text.split()

		# Now, look for our command in the tokens
		# If the command is issued with no argument
		# or too many arguments, show usage text
		if len(tokens)>1 and tokens[0].lower()=="/grab":
			if len(tokens)!=2:
				self.print("Usage: /grab NICKNAME")
				return True

		# If our command is issued with *one* argument,
		# the use the argument as our desired nickname,
		# and start the "nick grab" process
		if len(tokens)==2 and tokens[0].lower()=="/grab":
			tokens.pop(0)
			self.nickname_to_grab = tokens.pop(0)

			# Let the user know that the "grabbing" process
			# has begun
			self.print("Grabbing "+self.nickname_to_grab+"...")
			return True

	def tick(self,uptime):
		
		# See if we're still trying to grab the nickname
		if self.nickname_to_grab!=None:

			# Check to see if we've grabbed the nickname
			if self.nickname_to_grab == self.irc.nickname:

				# The nickname is grabbed!
				# Stop the grabbing process
				self.nickname_to_grab = None
				self.wait = 0
			else:

				# It's time to try and grab the nickname!
				if self.wait < uptime:

					# Try to grab the nickname
					self.irc.setNick(self.nickname_to_grab)

					# If this doesn't work, we'll try again
					# in 1 to 20 seconds
					self.wait = uptime + random.randint(1,20)

	def registered(self):

		# Add our new command, /grab, to the autocompleter
		self.autocomplete("/grab","/grab ")

		# Add our new command to the /help text
		self.help("/grab NICKNAME","Grabs an in-use nickname")

