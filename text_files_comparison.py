"""
Read a list of files, and compare the files line by line.
"""

import glob
import sys


def compare_files_by_line(filenames):
    """
    Read a list of files, and compare the files line by line.

    Print a list of the lines, the number of unique versions of that line in the files and a sample of the start
    of each line.
    """
    lines_by_file = []
    longest_file_length = 0
    for filename in filenames:
        lines_by_file.append(filtered_lines_from_file(filename))
        longest_file_length = max(len(lines_by_file[-1]), longest_file_length)

    for line_number in range(longest_file_length):
        nth_lines = get_nth_lines(lines_by_file, line_number)
        unique_strings = count_unique_strings(nth_lines)

        samples_of_each_line = []
        for line in set(nth_lines):
            samples_of_each_line.append(f"{line[:6]:<6}")

        print(f"{line_number + 1:>4} {unique_strings:>3}", ' '.join(samples_of_each_line))


def filtered_lines_from_file(filename):
    """
    Return the lines in the file, with newlines removed from each line.
    """
    file_lines = []
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            file_lines.append(line.strip())

    return file_lines


def count_unique_strings(strings):
    """
    Take a list of strings and return the number of unique versions

    >>> count_unique_strings(['a', 'b'])
    2

    >>> count_unique_strings(['cat', 'cat', 'dog'])
    2

    >>> count_unique_strings(['', 'cat'])
    2

    >>> count_unique_strings(['cat'])
    1

    >>> count_unique_strings([])
    0
    """
    return len(set(strings))


def get_nth_lines(lines_by_file, line_number):
    """
    Take a list of lists (lines by file), and return a list of lines that are at line_number

    >>> get_nth_lines([['file 1 line 1', 'file 1 line 2'], ['file 2 line 1', 'file 2 line 2']], 1)
    ['file 1 line 1', 'file 2 line 1']

    >>> get_nth_lines([['file 1 line 1', 'file 1 line 2'], ['file 2 line 1', 'file 2 line 2']], 2)
    ['file 1 line 2', 'file 2 line 2']
    """
    nth_lines = []

    for lines in lines_by_file:
        if line_number < len(lines):
            nth_lines.append(lines[line_number])
    return nth_lines


# .get() method on list

if __name__ == "__main__":
    compare_files_by_line(glob.glob(sys.argv[1]))
