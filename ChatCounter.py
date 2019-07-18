# ChatCounter.py

# Counts how many times users have "spoken" in the client's
# presence. Send a private message to the client consisting
# of !count to see how many chat have been counted.

from erk import Plugin,Shared

class ChatCounterExample(Plugin):
  def __init__(self):
    self.name = "Chat Counter"
    self.version = "1.0"
    self.description = "Counts every public message Erk sees"

  def load(self):
    Shared["counter"] = 0
    self.silent = True
    self.nowindows = True
    self.suppress("!count*")

  def message_public(self,serverID,channel,user,message):
    Shared["counter"] = Shared["counter"] + 1

  def message_private(self,serverID,user,message):
    tokens = user.split("!")
    if len(tokens)==2:
        user = tokens[0]
    
    if message == "!count":
      self.msg(user,"Total public messages: " + str(Shared["counter"]))