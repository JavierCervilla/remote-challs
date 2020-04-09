#!/usr/bin/env python3

import sys

def error():
	print('usage: ' + sys.argv[0] + ' <1-9 squared_rows...>')
	exit(1)

def snail(mtx):
	row_start = 0
	row_end = len(mtx) - 1
	col_start = 0
	col_end = len(mtx[0]) - 1
	while (row_start <= row_end and col_start <= col_end):
		if row_end == row_start or col_end == col_start: ending = ""
		else: ending = ", "
		print(", ".join(mtx[row_start][i] for i in range(col_start, col_end + 1)), end = ending)
		row_start += 1
		print(", ".join(mtx[i][col_end] for i in range(row_start, row_end + 1)), end = ending)
		col_end -= 1
		if row_end >= row_start: print(", ".join(mtx[row_end][i] for i in range(col_end, col_start - 1, -1)), end = ending)
		row_end -= 1
		if col_end >= col_start: print(", ".join(mtx[i][col_start] for i in range(row_end, row_start - 1, -1)), end = ending)
		col_start += 1

def main():
	args = len(sys.argv)
	matrix = []
	if args < 2  > 21: error()
	else:
		for fila in range(1,args):
			if len(sys.argv[fila]) != args - 1 or sys.argv[fila].isnumeric() == False: error()
			else:
				matrix.append([])
				for col in range(len(sys.argv[fila])):
					if sys.argv[fila][col] != '0': matrix[fila - 1].append(sys.argv[fila][col])
					else: error()
	snail(matrix)

if __name__ == "__main__":
	main()
