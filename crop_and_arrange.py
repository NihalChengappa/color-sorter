from itertools import count
import cv2
import math

img = cv2.imread("/home/nihalchengappa/Documents/color sorter/rice.jpg") # 512x512

img_shape = img.shape
tile_size = (20,20)
offset = (20,20)
count=0

for i in range(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
    for j in range(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
        cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]
        # Debugging the tiles
        cv2.imwrite("temp_img.png", cropped_img)
        img1 = cv2.imread("/home/nihalchengappa/Documents/color sorter/temp_img.png")
        img2 = cv2.imread("/home/nihalchengappa/Documents/color sorter/final_image.png")
        if count<1:
            cv2.imwrite("final_image.png", cropped_img)
            count+=1
        else:
            im_v = cv2.vconcat([img2,img1 ])
            cv2.imwrite('/home/nihalchengappa/Documents/color sorter/final_image.png', im_v)
            count+=1
