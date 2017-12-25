import math
import itertools

def get_hash_value(row):
	min_val = math.inf
	max_val = -math.inf
	for val in row:
		max_val = max(val, max_val)
		min_val = min(val, min_val)
	return max_val - min_val

def get_hash_value_2(row):
	combs = itertools.combinations(row, 2)
	return int(sum([max(comb)/min(comb) for comb in combs if (comb[0] % comb[1] is 0 or comb[1] % comb[0] is 0)]))

def get_row(filename):
	with open(filename) as f:
		parsed_lines = [list(map(int, line.rstrip().split("\t"))) for line in f]
	f.close()
	return sum([get_hash_value(line) for line in parsed_lines])

print(get_row("input.txt"))