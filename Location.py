#:
#?
#!

from os import listdir
from os.path import isfile, join

class Location:
	FILES =  {} 

	@classmethod
	def loadStatic(cls):
		onlyfiles = [f for f in listdir('./locations') if isfile(join('./locations', f))]
		for fn in onlyfiles:
			if fn.startswith("."):
				continue;
			with open("./locations/" + fn, 'r', encoding='utf-8') as file:
				a = file.read()
				cls.FILES[fn] = a.splitlines()

Location.loadStatic()

