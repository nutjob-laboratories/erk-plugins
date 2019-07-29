import shlex
from erk import Plugin,Shared

# DuckDuckGo code from: https://github.com/JeremyEudy/DuckDuckPy3/blob/master/duckduckpy3.py
import json
import requests
from urllib.parse import urlencode
import sys
import xml.etree.ElementTree as ET

def search(query, safeSearch=True, html=False, meanings=True):

  #Catch optional var changes
  safeSearch = '1' if safeSearch else '0'
  html = '0' if html else '1'

  #Define url params for API searches
  urlParams = {
    'q' : query, 
    'o': 'json', 
    'kp': safeSearch, 
    'no_redirect': '1', 
    'no_html' : html, 
    'd' : meanings
  }
  #Encode params into url format
  encoded = urlencode(urlParams)

  url = "https://api.duckduckgo.com/?"+encoded

  #get search response
  r = requests.get(url)

  #jsonify response
  if(urlParams['o'] == 'json'):
    j = json.loads(r.text)
    return j
  #or return xml
  elif(urlParams['o'] == 'x'):
    x = ET.fromstring(r.text)
    return x

class DuckDuckSummarize(Plugin):

  def __init__(self):
    self.name = "DuckDuckGo Summarize"
    self.version = "1.0"
    self.description = "Users can get information on a topic from DuckDuckGo"
    

    self.command = "!quack"

  # Executed when a public message is received
  # Arguments:    serverID (str) - The ID of the server
  #               user (str) - The user who sent the message
  #               message (str) - The message
  def message_public(self,serverID,channel,user,message):
    tokens = shlex.split(message)
    if len(tokens)>0 and tokens[0].lower()==self.command.lower():
      tokens.pop(0)

      # tokens = a list of arguments passed to the command

      r = search(' '.join(tokens))
      self.msg(channel,r["AbstractURL"])
