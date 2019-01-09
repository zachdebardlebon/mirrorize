from PIL import Image
import random
import sys

filename = sys.argv[1]
image = Image.open(filename)

width, height = image.size

new = Image.new('RGB', (width, height))

new_side_length = width
for i in range(5):
	if i == 0:
		new.paste(image, (0, 0))
		image = image.resize((width//2, height//2))
	else:	
		new_side_length = new_side_length//2
		offset = (width - new_side_length)//2
		new.paste(image, (offset, offset))
		image = image.resize((new_side_length//2, new_side_length//2))

new.save(filename.split('.')[0] + "_mirrored.png")
