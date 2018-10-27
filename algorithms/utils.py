def new_2d_map(size, default):
	return [[default for _ in range(size)] for _ in range(size)]

def valid_index(r, c, size):
	return r >= 0 and c >= 0 and r < size and c < size

def list_to_board(l, size):
	m = new_2d_map(size, None)
	for i in range(len(l)):
		r, c = i//size, i%size
		m[r][c] = l[i]

	return m