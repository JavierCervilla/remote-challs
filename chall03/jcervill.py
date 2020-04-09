#!/usr/bin/env python3

import sys

def error():
	print('usage: ' + sys.argv[0] + ' <1-9 squared_rows...>')
	exit(1)

def ending_function(rw_end,rw_st,c_end,c_st):
	if rw_end <= rw_st  and c_end <= c_st: return ""
	else: return ", "

def snail(mtx):
	row_start = 0
	row_end = len(mtx) - 1
	col_start = 0
	col_end = len(mtx[0]) - 1
	while (row_start <= row_end and col_start <= col_end):
		ending = ending_function(row_end, row_start, col_end, col_start)
		print(", ".join(mtx[row_start][i] for i in range(col_start, col_end + 1)), end = ending)
		row_start += 1
		ending = ending_function(row_end, row_start, col_end, col_start)
		print(", ".join(mtx[i][col_end] for i in range(row_start, row_end + 1)), end = ending)
		col_end -= 1
		if row_end >= row_start:
			ending = ending_function(row_end, row_start, col_end, col_start)
			print(", ".join(mtx[row_end][i] for i in range(col_end, col_start - 1, -1)), end = ending)
		row_end -= 1
		if col_end >= col_start:
			ending = ending_function(row_end, row_start, col_end, col_start)
			print(", ".join(mtx[i][col_start] for i in range(row_end, row_start - 1, -1)), end = ending)
		col_start += 1

def main():
	args = len(sys.argv)
	matrix = []
	if args in range(2, 22):
		for fila in range(1,args):
			if len(sys.argv[fila]) != args - 1 or sys.argv[fila].isnumeric() == False: error()
			else:
				matrix.append([])
				for col in range(len(sys.argv[fila])):
					if sys.argv[fila][col] != '0': matrix[fila - 1].append(sys.argv[fila][col])
					else: error()
	else: error()
	snail(matrix)

if __name__ == "__main__":
	main()
