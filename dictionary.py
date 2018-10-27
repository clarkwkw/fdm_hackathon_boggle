import json
import bisect

class Dictionary:
	def __init__(self, paths):
		self.__words = []

		for path in paths:
			with open(path, "r") as f:
				for line in f.readlines():
					line = line.strip()
					if len(line) > 0:
						self.__words.append(line.lower())

		self.__words = sorted(self.__words)
		#self.__set = frozenset(self.__words)

	def exists_or_prefix(self, word):
		word = word.lower().strip()
		i = bisect.bisect_left(self.__words, word)
		if i >= 0 and i < len(self.__words):
			if self.__words[i] == word:

				return True, True

			if self.__words[i].startswith(word):
				return False, True
		if i - 1 >= 0 and self.__words[i - 1].startswith(word):
			return False, True

		return False, False