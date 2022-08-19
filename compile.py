from pygwin import *
import json
import sys

def wrong(errc, err, pos, ctn):
	r, c = 0,0 
	for x in range(pos):
		if ctn[x] == '\n':
			
		c += 1

	if errc == 0:
		print("EndNotFound: The end for {} was not found. Make sure it is terminated.".format(err))
	else:
		print("{}: {}".format(errc, err))
	print("In {} line, {} column".format(r, c))

file_to_compile = 'game.prcode'
file_info = 'game.json'

# compilation start
content = open(file_to_compile, 'r').read()
ctnt = content.strip()
diff = content.find(ctnt)
info = json.load(open(file_info, 'r'))

title = info["Title"]
size = info["Size"]

assets = {}

for x in info["Assets"]:
	if x[2] == 0:
		assets[x[0]] = pygimg.load(x[1])
	elif x[2] == 1:
		assets[x[0]] = pyg.loadsound(x[1])

# decoding the content
if ctnt.startswith('class main Main'):
	# fetch main class
	main = content.find('class end')
	if content.find('class end') == -1:
		wrong(0,"class main Main", 0+diff, ctnt)
	main = content[:main]
	mains = main.strip()
	maind = main.find(mains)