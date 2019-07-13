string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
letters = {'a':'c', 'b': 'd', 'c':'e', 'd':'f', 'e':'g', 'f': 'h', 'g':'i', 'h':'j', 'i':'k', 
'j':'l', 'k':'m', 'l':'n', 'm':'o', 'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t', 's':'u', 
't':'v', 'u': 'w', 'v': 'x', 'w':'y', 'x': 'z', 'y': 'a', 'z':'b' }
new_string = []

for char in string:
	if char.islower():
		new_string.append(letters.get(char))
	else:
		new_string.append(char)

string = ''
print(string.join(new_string))

string = "map" #Apply on the url
#Manera sugerida por el ejercicio
trantab = string.maketrans(letters)

print(string.translate(trantab))

a = b = 5
print(a, b)