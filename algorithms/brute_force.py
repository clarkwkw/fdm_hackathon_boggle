from . import utils

def solve(board, dictionary, size = 4):
	words = frozenset()
	for i in range(size):
		for j in range(size):
			visited = utils.boolean_2d_map(size, False)
			new_words = __find_words(board, dictionary, i, j, size, visited, "")
			words = words.union(new_words)

	return words

def __find_words(board, dictionary, i, j, size, visited, traversed):
	all_words = frozenset()
	visited[i][j] = True

	for di in range(-1, 1 + 1):
		for dj in range(-1, 1 + 1):
			new_i, new_j = i + di, j + dj
			if utils.valid_index(new_i, new_j, size) and not visited[new_i][new_j]:
				words = __find_words(board, dictionary, i + di, j + dj, size, visited, traversed + board[i][j])

				all_words = all_words.union(words)

	visited[i][j] = False

	if len(all_words) == 0 and dictionary.exists(traversed):
		return frozenset([traversed])

	return all_words
