import json


class Dictionary:
	def __init__(self, paths):
		self.__words = []

		for path in paths:
			with open(path, "r") as f:
				for line in f.readlines():
					line = line.strip()
					if len(line) > 0:
						self.__words.append(line.lower())

		self.__words = frozenset(self.__words)

	def exists(self, word):
		return word.lower() in self.__words