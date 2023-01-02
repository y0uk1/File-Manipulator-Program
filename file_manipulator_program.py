import sys
import os


def execute_function(args):
    if args[1] == 'reverse':
        reverse(args[2], args[3])
    elif args[1] == 'copy':
        copy(args[2], args[3])
    elif args[1] == 'duplicate-contents':
        duplicate_contents(args[2], int(args[3]))
    elif args[1] == 'replace-string':
        replace_string(args[2], args[3], args[4])

def validator(args):
    # 引数の数が適切か
    if len(args) < 4:
        raise IndexError('Arguments are too short')

    # inputpathは、どの関数にも共通の引数なので、最初に確認しておく
    if args[2].isdigit():
        raise TypeError('Argument for input file is not string')
    if not os.path.exists(args[2]):
        raise FileNotFoundError('Input file not found')

    # 各関数特有の引数の確認
    if args[1] == 'reverse' or args[1] == 'copy':
        if args[3].isdigit():
            raise TypeError('Argument for output file is not string')
    elif args[1] == 'duplicate-contents':
        if not args[3].isdigit():
            raise TypeError('Argument for n is not digit')
    elif args[1] == 'replace-string':
        if args[3].isdigit():
            raise TypeError('Argument for needle is not string')
        if args[4].isdigit():
            raise TypeError('Argument for newstring is not string')

def reverse(input_path, output_path):
    with open(input_path, 'r') as f:
        contents = f.read()
    
    reversed_contents = contents[::-1]

    with open(output_path, 'w') as f:
        f.write(reversed_contents)

def copy(input_path, output_path):
    with open(input_path, 'r') as f:
        contents = f.read()
    
    with open(output_path, 'w') as f:
        f.write(contents)

def duplicate_contents(input_path, n):
    with open(input_path, 'r') as f:
        contents = f.read()
    contents += '\n'
    manipulated_contents = contents * n

    with open(input_path, 'w') as f:
        f.write(manipulated_contents) 

def replace_string(input_path, needle, new_string):
    with open(input_path, 'r') as f:
        contents =  f.read()
    
    contents = contents.replace(needle, new_string)

    with open(input_path, 'w') as f:
        f.write(contents)


if __name__ == '__main__':
    args = sys.argv
    validator(args)
    execute_function(args)
