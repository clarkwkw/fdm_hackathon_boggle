def boolean_2d_map(size, default):
	return [[default for _ in range(size)] for _ in range(size)]

def valid_index(r, c, size):
	return r >= 0 and c >= 0 and r < size and c < size