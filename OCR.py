#Libraries implementation
import pandas as pd
import yaml
from functools import reduce
from PIL import Image 
import pandas as pd
import cv2
import imutils
from PIL import Image
# #Read text file
# data_frame = pd.read_csv("test.txt", sep='\t', 
#                          names=['Name', 'Age', 'Profession']) 
  
#aftrer ML model genrated txt file
data = pd.read_csv(r'/media/user4/data/API/API_test/yolov5_cheque/inference/output/1.txt', delim_whitespace=True, names = ['label','x1','y1','x2','y2'])
#Convert label column into list
data_label=data['label'].to_list()

#Read class file (data.yaml)
with open(r'/media/user4/data/API/API_test/yolov5_cheque/yolov5/exp88_yolov5s_results_blank_cheque/cls.txt') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    data_list = yaml.load(file, Loader=yaml.FullLoader)
    #print(data_list)

# Get the data into list format
get_list=list(data_list.values())
# print(get_list)
#Convert data into single list
single_list = reduce(lambda x,y: x+y, get_list)
# print(single_list)
#Store data into this temporary list
list_label=[]

#Logic to match text file and class file to extract each label class
for sub_data in data_label:
    for sub_index,sub_val in enumerate(single_list):
        # print(sub_index,sub_val)
        if sub_data == sub_index:
            list_label.append(sub_val)
# print(list_label)
#create new dataframe 
df = pd.DataFrame({'new_col':list_label})
# print(df)
#Replace label with new dataframe  
data['label']=df['new_col']
# print(data)

#Create a new csv file with extracting data
csv = data.to_csv(r'/media/user4/data/API/API_test/yolov5_cheque/inference/output/1.csv', index = False)
print("OCR is working")
import printer