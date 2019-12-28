from erk import *

class HelloWorld(Plugin):
	def __init__(self):
		self.name = "Hello World plugin"
		self.description = "Example plugin for documentation"

	def input(self,client,name,text):

		# Since we can't write to console windows,
		# we won't try to, and exit if the plugin
		# was triggered by console input
		if name=="Server": return False

		# Look for our new command
		if text=="/hello":

			# Found it! Now lets display our message
			self.write(name,"Hello, world!")

			# Now, we return "True" to make sure that
			# "/hello" isn't sent to the IRC server as
			# a chat messages
			return True

class Notes(Plugin):
	def __init__(self):
		self.name = "Note taking plugin"
		self.description = "Example plugin for documentation"
		self.notes = []

	def input(self,client,name,text):

		# Since we can't write to console windows,
		# we won't try to, and exit if the plugin
		# was triggered by console input
		if name=="Server": return False

		# Tokenize the input
		tokens = text.split()

		# Handle the "/clear" command
		# This will delete any stored notes
		if len(tokens)>0 and tokens[0].lower()=="/clear":
			self.notes = []
			return True

		# Handle the "/note" command
		# This adds a new note to the stored notes
		if len(tokens)>0 and tokens[0].lower()=="/note":
			tokens.pop(0)
			n = ' '.join(tokens)
			self.notes.append(n)
			return True

		# Handle the "/notes" command
		# This will display any stored notes
		if len(tokens)>0 and tokens[0].lower()=="/notes":

			# If there are no stored notes, let the
			# user know and return
			if len(self.notes)==0:
				self.write(name,"No notes found")
				return True

			# Format the note list using HTML
			t = "<ul>"
			for n in self.notes:
				t = t + "<li>"+n+"</li>"
			t = t + "</ul>"

			# Display the stored notes to the user
			self.write(name,t)
			return True