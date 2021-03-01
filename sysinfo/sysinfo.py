from erk import *

import psutil
import math
import platform

def convert_size(size_bytes):
	if size_bytes == 0: return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

class Sysinfo(Plugin):

	def __init__(self):
		self.name = "Sysinfo"
		self.description = "Display system info with \"/sysinfo\""
		self.version = "2.2"
		self.author = "Dan Hetrick"
		self.website = "https://github.com/nutjob-laboratories/erk"

	def load(self):
		self.autocomplete("/sysinfo","/sysinfo")

	def input(self,client,name,text):

		if name=="Server": return False

		tokens = text.split()
		if len(tokens)>0:
			if tokens[0].lower()!="/sysinfo":
				return False

		output = []

		output.append("\x02Client:\x0F "+self.info())

		output.append("\x02OS:\x0F "+platform.platform(terse=0))
		
		cpucount = psutil.cpu_count()
		cpu_usage = psutil.cpu_percent()
		cpu_type = platform.processor()
		cpu_freq = psutil.cpu_freq()
		cpu_freq = str(cpu_freq.max/1000)+" gHz"

		output.append("\x02CPU:\x0F "+cpu_type+" ("+cpu_freq+", "      +str(cpu_usage)+"% used, "+str(cpucount)+" cores)")

		ri = psutil.virtual_memory()

		total_ram = convert_size(ri.total)
		used_ram = convert_size(ri.used)
		available_ram = convert_size(ri.available)
		percent_ram = ri.percent

		output.append("\x02RAM:\x0F "+total_ram+" total ("+used_ram+" free)")

		client.msg(name,' Ã¢ÂÂ¢ '.join(output))

		return True
