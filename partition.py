#!/usr/bin/python3

import sys

def process(strings, expression, replacestring, separator):
	return expression.replace(replacestring, separator.join(strings))

if __name__ == "__main__":
	if len(sys.argv) < 5:
		print(sys.argv[0] + " LIMIT REPLASESTRING SEPARATORSTRING EXPRESSION")
		print("  e.g.: " + sys.argv[0] + " 10 _replace_ , '{\"names\": [_replace_]}'")

	limit = int(sys.argv[1])
	replacestring = sys.argv[2]
	separator = sys.argv[3]
	expression = sys.argv[4]

	buffer = []

	for rawline in sys.stdin:
		line = rawline.strip()
		if len(line) == 0: continue
		buffer.append(line)
		if len(buffer) >= limit:
			print(process(buffer, expression, replacestring, separator))
			buffer.clear()

	if len(buffer) > 0:
		print(process(buffer, expression, replacestring, separator))
