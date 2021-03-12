# #!/usr/bin/python
from PIL import Image
import os, sys

path = "/media/user4/data/API/API_test/yolov5_cheque/output/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            path1= '/media/user4/data/API/API_test/yolov5_cheque/output/'
            f, e = os.path.splitext(path1+item)
            #imResize = im.resize((200,200), Image.ANTIALIAS)
            im.save(f + '.jpg', 'JPEG', dpi=(300,300)) 
            #imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()


import detect 

# #!/usr/bin/python
# from PIL import Image
# import os, sys

# path = "/home/user4/Downloads/DATASET/FINAL_DATAset/indian_cheque_resized/"
# dirs = os.listdir( path )
# directory = "changed_dpi"
# path1 = os.path.join(path, directory) 
# os.mkdir(path1) 
# def resize():
#     for item in dirs:
#         if os.path.isfile(path+item):
#             im = Image.open(path+item)
#             # path1= '/home/user4/Downloads/DATASET/FINAL_DATAset/indian_cheque_resized/d'
#             f, e = os.path.splitext(path+item)
#             #imResize = im.resize((200,200), Image.ANTIALIAS)
#             im.save(f + '.jpg', 'JPEG', dpi=(300,300)) 
#             #imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

# resize()




# ############### folder procesing #####################
        
        
        
# from PIL import Image
# import os, sys
# import cv2

# path = "/home/user4/Downloads/DATASET/YOLO_Micr/val/images/"
# dirs = os.listdir( path )

# def resize():
#     for item in dirs:
#         if os.path.isfile(path+item):
#             # im = Image.open(path+item)
#             im = cv2.imread(path+item)
#             path1= '/home/user4/Downloads/DATASET/YOLO_Micr/val/images/proceesed/'
#             f, e = os.path.splitext(path1+item)
#             #imResize = im.resize((200,200), Image.ANTIALIAS)
#             gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#             # img = cv2.medianBlur(im,5)
#             thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)
#             #im.save(f + '.jpg', 'JPEG', dpi=(300,300)) 
#             warped = cv2.resize(thresh, (2400,1100))
#             # cv2.imwrite()
#             cv2.imwrite(f + '.jpg', warped)

#             # im.save(f + ' resized.jpg', 'JPEG', quality=90)

# resize()
