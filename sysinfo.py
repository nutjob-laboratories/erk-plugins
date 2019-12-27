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
		self.description = "Adds a new command \"/syisinfo\" that displays system information"


	def input(self,client,name,text):

		if name=="Server": return False

		tokens = text.split()
		if len(tokens)>0:
			if tokens[0].lower()!="/sysinfo":
				return False

		output = []

		output.append("\x02Client:\x0F \x1D"+self.info()+"\x0F")

		output.append("\x02OS:\x0F \x1D"+platform.platform(terse=0)+"\x0F")
		
		cpucount = psutil.cpu_count()
		cpu_usage = psutil.cpu_percent()
		cpu_type = platform.processor()
		cpu_freq = psutil.cpu_freq()
		cpu_freq = str(cpu_freq.max/1000)+" gHz"

		output.append("\x02CPU:\x0F \x1D"+cpu_type+" ("+cpu_freq+", "      +str(cpu_usage)+"% used, "+str(cpucount)+" cores)\x0F")

		ri = psutil.virtual_memory()

		total_ram = convert_size(ri.total)
		used_ram = convert_size(ri.used)
		available_ram = convert_size(ri.available)
		percent_ram = ri.percent

		output.append("\x02RAM:\x0F \x1D"+total_ram+" total ("+used_ram+" free)\x0F")

		client.msg(name,' • '.join(output))

		return True
