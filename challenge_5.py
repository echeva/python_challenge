#http://www.pythonchallenge.com/pc/def/peak.html
#http://www.pythonchallenge.com/pc/def/pickle.html

import pickle
import re
import ast 

objetc = []
file = pickle.load(open('banner.p', "rb"))
for l in file:
	stg = ''
	for a,b in l:
		stg += ''.join([a for x in range(b)])
	print(stg)	
#variable = ast.literal_eval(file)

#result http://www.pythonchallenge.com/pc/def/channel.html
