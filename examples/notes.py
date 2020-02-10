from erk import *

class Notes(Plugin):
    def __init__(self):
        self.name = "Note taking plugin"
        self.author = "Dan Hetrick"
        self.version = "1.0"
        self.website = "https://github.com/nutjob-laboratories/erk"
        self.source = "https://github.com/nutjob-laboratories/erk"
        self.description = "Example plugin for documentation"
        self.notes = []

    def input(self,client,name,text):

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
            self.print("No notes found")
            return True

            # Format the note list using HTML
            t = "<ul>"
            for n in self.notes:
                t = t + "<li>"+n+"</li>"
            t = t + "</ul>"

            # Display the stored notes to the user
            self.print(t)
            return True