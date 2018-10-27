import algorithms
import dictionary


DICTS = [
	"resources/real/Dictionary1.txt",
	"resources/real/Dictionary2.txt",
	"resources/real/Dictionary3.txt",
	"resources/real/Dictionary4.txt"
]

BOARD = [
	["S", "S", "L", "E"],
	["A", "T", "M", "Z"], 
	["L", "S", "R", "A"],
	["T", "P", "L", "E"]
]

SIZE = 4

'''
DICTS = [
	"resources/mock/Dictionary.txt"
]


BOARD = [
	["G", "I", "Z"],
	["U", "E", "K"],
	["Q", "S", "E"]
]

SIZE = 3
'''

def main(solve):
	d = dictionary.Dictionary(DICTS)
	for word in solve(BOARD, d, SIZE):
		print(word)


if __name__ == "__main__":
	main(algorithms.brute_force.solve)