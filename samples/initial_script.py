#!/usr/bin/python3
import sys

def GameOfThrones(x):
	if len(x) == 1:
		print("Hello Karolina. Type sth in")
	else:
		print("Hello "+sys.argv[1])
		

if __name__ == "__main__":
	GameOfThrones(sys.argv)
