from erk import *
import random

_ERK_PLUGIN_ = "Nick Grabber"

class NickGrabber(Plugin):
	"""
		Nick Grabber plugin for the Ərk IRC client

		Creates a new command, /grab
		Usage: /grab DESIRED_NICKNAME

		It attempts to change the client's nickname to the
		desired nickname at random intervals (every 1 to 20
		seconds). Once the desired nickname has been obtained,
		the plugin stops trying to grab the nick.
	"""

	NAME = "Nickname Grabber"
	VERSION = "1.0"
	DESCRIPTION = "Grabs an in-use nickname"

	def __init__(self):
		self.nickname_to_grab = None
		self.wait = 0


	def input(self,window,text):
		
		tokens = text.split()

		# If /grab is called without any arguments,
		# then display usage text and exit
		if len(tokens)==1 and tokens[0].lower()=="/grab":
			self.print("Usage: /grab NICKNAME")
			return True

		# If /grab is called with *ONE* argument, then
		# take that argument, and try to change the
		# user's nick
		if len(tokens)==2 and tokens[0].lower()=="/grab":
			tokens.pop(0)
			self.nickname_to_grab = tokens.pop(0)

			ut = self.uptime()
			if ut: self.wait = ut + random.randint(1,20)
			self.print("Grabbing "+self.nickname_to_grab+"...")
			return True

		# This isn't really required, but
		# it's nice to explicitely exit :-)
		return False


	def tick(self,uptime):
		
		if self.nickname_to_grab!=None:
			if self.nickname_to_grab == self.irc.nickname:
				self.nickname_to_grab = None
				self.wait = 0
			else:
				if self.wait < uptime:
					self.irc.setNick(self.nickname_to_grab)
					self.wait = uptime + random.randint(1,20)


