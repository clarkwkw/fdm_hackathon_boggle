import algorithms
import dictionary


DICTS = [
	"resources/real/Dictionary1.txt",
	"resources/real/Dictionary2.txt",
	"resources/real/Dictionary3.txt",
	"resources/real/Dictionary4.txt"
]

BOARD = ["S", "N", "O", "W", "O", "S", "L", "F", "O", "R", "E", "A", "E", "E", "M", "K"]

SIZE = 4

MIN_LENGTH = 3

def main(solve, board):
	d = dictionary.Dictionary(DICTS)
	ans = []
	for word in solve(board, d, SIZE):
		if len(word) >= MIN_LENGTH:
			ans.append(word)

	return ans


if __name__ == "__main__":
	print(main(algorithms.brute_force.solve, BOARD))