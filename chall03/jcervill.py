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
	str = ''
	while (row_start <= row_end and col_start <= col_end):
		for i in range(col_start, col_end + 1):
			if (row_start == row_end): str += mtx[row_start][i]
			else: str += mtx[row_start][i] + ", "
		row_start += 1
		for i in range(row_start, row_end + 1):
			if col_start == col_end: str += mtx[i][col_end]
			else: str += mtx[i][col_end] + ", "
		col_end -= 1
		if row_end >= row_start:
			for i in range(col_end, col_start - 1, -1):
				if row_end == row_start: str += mtx[row_end][i]
				else: str += mtx[row_end][i] + ", "
		row_end -= 1
		if col_end >= col_start:
			for i in range(row_end, row_start - 1, -1):
				if col_end == col_start: str += mtx[i][col_start]
				else: str += mtx[i][col_start] + ", "
		col_start += 1
	print(str)
def main():
	args = len(sys.argv)
	matrix = []
	if  args in range (2,22):
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
