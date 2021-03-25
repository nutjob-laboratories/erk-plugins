from erk import *
import random

_ERK_PLUGIN_ = "Nick Grabber"

class NickGrabber(Plugin):
	"""
		This is a basic "blank" Ərk plugin with all the
		event methods available. Just change the name of
		the class, change the "NAME", "VERSION", and
		"DESCRIPTION" class attributes, and you're half-
		way to writing an Ərk plugin!
	"""

	NAME = "Nickname Grabber"
	VERSION = "1.0"
	DESCRIPTION = "Grabs an in-use nickname"

	def __init__(self):
		self.nickname_to_grab = None
		self.wait = 0


	def input(self,window,text):
		
		tokens = text.split()

		if len(tokens)==1 and tokens[0].lower()=="/grab":
			self.print("Usage: /grab NICKNAME")
			return True

		if len(tokens)==2 and tokens[0].lower()=="/grab":
			tokens.pop(0)
			self.nickname_to_grab = tokens.pop(0)

			ut = self.uptime()
			if ut: self.wait = ut + random.randint(1,20)
			self.print("Grabbing "+self.nickname_to_grab+"...")
			return True


	def tick(self,uptime):
		
		if self.nickname_to_grab!=None:
			if self.nickname_to_grab == self.irc.nickname:
				self.nickname_to_grab = None
				self.wait = 0
			else:
				if self.wait < uptime:
					self.irc.setNick(self.nickname_to_grab)
					self.wait = uptime + random.randint(1,20)


