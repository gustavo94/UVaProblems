from sys import stdin
import math

def ls(file_names, n_files):
	first_column_size = max([len(name) for name in file_names])
	column_size = first_column_size + 2
	n_columns = int(((60-first_column_size)/column_size)+1)
	n_rows = int(math.ceil(n_files*1.0 / n_columns))
	for row in range(n_rows):
		row_text = ''
		for column in range(n_columns):
			file_name_index = row+n_rows*column
			if file_name_index < n_files:
				row_text += file_names[file_name_index] + ' ' *(column_size-len(file_names[file_name_index]))
		print(row_text)

def main():
	lines = stdin.read().splitlines()
	n_lines = len(lines)
	current_line = 0
	while current_line < n_lines:
		n_files = int(lines[current_line])
		current_line += 1 #move to first file_name
		print('-'*60)
		ls(sorted(lines[current_line:current_line+n_files]), n_files)
		current_line += n_files #move after last file_name

	return 

main()
