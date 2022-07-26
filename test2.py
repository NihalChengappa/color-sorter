from PIL import Image
from numpy import append
img = Image.open('/home/nihalchengappa/Documents/color sorter/final_image.png')
pix = img.load()
for i in range(img.size[1]):
    for j in range(img.size[0]):
        r,g,b=pix[j,i]
        print("i={},j={}".format(i,j))