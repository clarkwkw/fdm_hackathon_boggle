import algorithms
import dictionary
import json


DICTS = [
	"resources/real/Dictionary1.txt",
	"resources/real/Dictionary2.txt",
	"resources/real/Dictionary3.txt",
	"resources/real/Dictionary4.txt"
]

BOARD = ["T", "D", "O", "T", "R", "O", "F", "S", "I", "E", "S", "E", "T", "I", "S", "T"]

SIZE = 4

MIN_LENGTH = 3

ANS_FILE = "output.txt"

def main(solve, board):
	d = dictionary.Dictionary(DICTS)
	ans = []
	for word in solve(board, d, SIZE):
		if len(word) >= MIN_LENGTH:
			ans.append(word)

	return ans


if __name__ == "__main__":
	ans = main(algorithms.brute_force.solve, BOARD)
	with open(ANS_FILE, "w") as f:
		f.write("\n".join(ans))

	print("Answer outputted to %s"%ANS_FILE)