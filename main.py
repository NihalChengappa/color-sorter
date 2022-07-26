from PIL import Image
from numpy import append
import crop_and_arrange
import hsv_func
img = Image.open('/home/nihalchengappa/Documents/color sorter/final_image.png')
pix = img.load()
res=[]
file1 = open("myfile.txt","w")
sn=0
count=0
for i in range(img.size[1]):
    row=[]
        
    for j in range(img.size[0]):
        # print("i={},j={}".format(i,j))
        r,g,b=pix[j,i]
        h,s,v=hsv_func.rgb_to_hsv(r,g,b)
        if h>200 and h<225 and v>30 :
            count+=1
            # file1.write(str(count)+",i="+str(i)+",j="+str(j)+"\n")
            row.append("1")
            pix[j,i]=(0,0,0)
            # print(h,s,v)
        else:
            row.append("0")
        if (i+1)%crop_and_arrange.offset[0]==0 and (j+1)%crop_and_arrange.offset[1]==0:
            if count>=50:
                file1.write("{}.Valid image no : {}\n".format(sn,(i+1)/10))
                sn+=1
                count=0
            else:
                # print("Invalid")
                count=0
    res.append(row)
file1.close()
img.show()


   