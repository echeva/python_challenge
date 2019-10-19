name = '90052'
lista = []

try:
	while True:
		# print(name)
		with open('channel/' + name + ".txt", "r") as f:
			content = f.read()
			name = content.split(' ')[-1]
			lista.append(name)
except:
	print(lista, len(lista))
