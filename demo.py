import sys, os
from src.typed_ast.typed_ast import *

def main():
	os.system('clear')
	print("Basic inference of assignments..")
	ta = TypedAST("src/tests/assignment.py")
	ta.print_src()
	raw_input()
	print("Final type environment:")
	ta.print_modules()
	raw_input()
	os.system('clear')
	print("Full typed abstract syntax tree:")
	print(ta.format_tree())
	raw_input()
	os.system('clear')
	print("Inference of built-in arithmetic..")
	ta2 = TypedAST("src/tests/arithmetic.py")
	ta2.print_src()
	raw_input()
	print("Final type environment:")
	ta2.print_modules()
	print(ta2.format_tree())
	raw_input()
	os.system('clear')
	print("Type inference of function definitions and calls..")
	ta = TypedAST("src/tests/functions.py")
	ta.print_src()
	raw_input()
	print("Final type environment:")
	ta.print_modules()
	raw_input()
	print("Full typed abstract syntax tree:")
	print(ta.format_tree())
	raw_input()
	print("Type inference of class definitions and attributes..")
	ta = TypedAST("src/tests/classes.py")
	ta.print_src()
	raw_input()
	print("Final type environment:")
	ta.print_modules()
	raw_input()

if __name__ == "__main__":
	main()