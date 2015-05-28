#coding: utf-8
import sys
import random
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--width", type="int", dest="width")
parser.add_option("--height", type="int", dest="height")
parser.add_option("-r", "--row", type="int", dest="row")
parser.add_option("-c", "--column", type="int", dest="column")
parser.add_option("-n", "--name", type="str", dest="name")
parser.add_option("-g", "--gen", type="int", dest="gen")
parser.add_option("-s", "--student", type="int", dest="student")
parser.add_option("--top", action="store_true", dest="top", default=True)
parser.add_option("--bottom", action="store_false", dest="top")
(options, sys.args) = parser.parse_args()

try:
	os.mkdir(options.name)
except:
	pass

for i in range(1, options.gen + 1):
	f = open(options.name + "/" + options.name + " " + str(i).zfill(3) + ".html", "w")
	f.write(
"""<!doctype html>
<html>

<head>
<title>""" + os.path.splitext(os.path.basename(f.name))[0] + """</title>
<style type="text/css">
html, body
{
	width: 100%;
	height: 100%;
	margin: 0;
	margin: 0;
}

td.title
{
	text-align: center;
	font-size: 300%;
}

td.front
{
	border-radius: 8px;
	border: solid blue;
	text-align: center;
	font-size: 300%;
}

table.centering
{
	width: 100%;
	height: 100%;
}

table.seat
{
	width: 80%;
	height: 80%;
	margin-left: auto;
	margin-right: auto;
	border-radius: 8px;
	border: solid black;
}

table.seat td
{
	width: """ + str(int(100 / float(options.width))) + """%;
	text-align: center;
	font-size: 300%;
}
</style>
</head>

<body>
<table class="centering">
<tr>
<td class="title" colspan=\"""" + str(options.column) + """\">""" + os.path.splitext(os.path.basename(f.name))[0] + """</td>
</tr>
<tr>
<td class="front" colspan=\"""" + str(options.column) + """\">Front</td>
</tr>
""")
	it = list(range(1, options.student + 1))
	random.shuffle(it)
	it = iter(it)
	i = 0
	seat = [[0 for x in range(options.column * options.width)] for y in range(options.row * options.height)]
	for y in range(options.row * options.height):
		r = range(options.column * options.width)
		if (options.student - i) < (options.column * options.width):
			r = range(int(((options.column * options.width) - (options.student - i)) / 2), int(((options.column * options.width) - (options.student - i)) / 2) + (options.student - i))
		for x in r:
			seat[y][x] = next(it)
			i += 1

	for y in range(options.row * options.height):
		for x in range(options.column * options.width):
			if seat[y][x] == 0:
				seat[y][x] = "&nbsp;"

	if not(options.top):
		for y in range(int(options.row * options.height / 2)):
			for x in range(options.column * options.width):
				seat[y][x], seat[(options.row * options.height) - y - 1][(options.column * options.width) - x - 1] = seat[(options.row * options.height) - y - 1][(options.column * options.width) - x - 1], seat[y][x]

	for row in range(options.row):
		f.write("<tr>\n")
		for column in range(options.column):
			f.write("""<td>\n<table class="seat">\n""")
			for y in range(options.height):
				f.write("<tr>\n")
				for x in range(options.width):
					f.write("<td>" + str(seat[(row * options.height) + y][(column * options.width) + x]) + "</td>")
				f.write("\n</tr>\n")
			f.write("</table>\n</td>\n")
		f.write("</tr>\n")
	f.write("</table>\n</body>\n</html>")
	f.close()
