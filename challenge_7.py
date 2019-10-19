from PIL import Image
import re
im = Image.open('oxygen.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_values = set(pixel_values)

# lista = []
stg = ''
for x in pixel_values:
	# lista.append(x[0])
	stg += ''.join(chr(x[0]))

# stg = re.sub("\d", "", str(stg))
# stg = re.sub("\W", "", str(stg))

print(stg)
