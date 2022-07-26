from PIL import Image
from numpy import append
import crop_and_arrange
import hsv_func
img = Image.open('/home/nihalchengappa/Documents/color sorter/final_image.png')
pix = img.load()
res=[]
for i in range(img.size[0]):
    row=[]
    for j in range(img.size[1]):
        r,g,b=pix[i,j]
        h,s,v=hsv_func.rgb_to_hsv(r,g,b)
        if h>200 and h<225 and v>30 :
            row.append("1")
            pix[i,j]=(0,0,0)
            # print(h,s,v)
        else:
            row.append("0")
    res.append(row)
img.show()


   