# Echo.py

# Uses the message_public event method to echo all channel
# chat back to the channel.
from erk import Plugin,Shared

class EchoExample(Plugin):

  def __init__(self):
    self.name = "Echo"
    self.version = "1.0"
    self.description = "Echoes all public chat."
    
  def message_public(self,serverID,channel,user,message):
    self.msg(channel,message)
