import cv2
import math
import glob
import csv
import os
import sys


#program to make images smaller in order to fit tesseract requirements 
def crop_image(PATH, image_file, save_path):
    os.chdir(PATH)
    img = cv2.imread(image_file)
    h,w,c=(img.shape) # save image dimensions
    height=h
    h=math.ceil(h/32767)
    crop=1
    x_start=0
    x_end=32500
    constant=32500
    

    name=image_file.split("/")
    name=name[2]
    name=name.split(".")
    name=name[0]
    
    os.chdir(save_path)
    while crop<=h:
        if crop==h:
            cropped_image = img[x_start+1:height, 0:1000]
            cv2.imwrite(str(name)+"-00"+str(crop)+'.png', cropped_image)
        else:
            cropped_image = img[x_start:x_end, 0:1000]
            cv2.imwrite(str(name)+"-00"+str(crop)+'.png', cropped_image)
            x_start+=(constant)
            x_end+=(constant)
            if crop==1:
                x_start+=1
        crop+=1

#take the given images and create a csv file with the names in order to run crop_image program on them
def create_img_csv(path):
    images = glob.glob(path+'*.png')
    Image_Name_lst=[]
    for i in images:
        name=i.split("/")
        Image_Name_lst.append(name[2])
    Image_Name_lst= sorted(Image_Name_lst)
    
    folder=path.split("/")
    folder=folder[1]
    path=folder
    if not os.path.isdir(path+'_cropped'):
        os.makedirs(path+'_cropped')
    fake_csv=open(folder+'_Images.csv', "w")
    writer = csv.writer(fake_csv)
    for name in Image_Name_lst:
        writer.writerow([name])



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please include path where assignment folder is saved  Ex:'/Users/melissaperkins/Desktop/TEAM_SEIZE_THE_DATA_DSCI550_HW_BIGDATA/Step1/' ")
    else:
    	try:
            PATH=sys.argv[1]
            #Create CSVs
            os.chdir(PATH)
            create_img_csv('data/aljazeera/')
            create_img_csv('data/cnn/')
            create_img_csv('data/fox/')
            print('CSV files created')


            #aljazeera images
            os.chdir(PATH)
            fake_csv=open('aljazeera_Images.csv', encoding='utf-8-sig')
            read_csv= csv.reader(fake_csv)
            for row in read_csv:
                crop_image(PATH, 'data/aljazeera/'+row[0], 'aljazeera_cropped')
            print('Aljazeera images cropped')


            #cnn images
            os.chdir(PATH)
            fake_csv=open('cnn_Images.csv', encoding='utf-8-sig')
            read_csv= csv.reader(fake_csv)
            for row in read_csv:
                crop_image(PATH, 'data/cnn/'+row[0], 'cnn_cropped')
            print('CNN images cropped')

            #fox images
            os.chdir(PATH)
            fake_csv=open('fox_Images.csv', encoding='utf-8-sig')
            read_csv= csv.reader(fake_csv)
            for row in read_csv:
                #print(row[0])
                crop_image(PATH, 'data/fox/'+row[0], 'fox_cropped')
            print('FOX images cropped')

    	except:
    		print("Please try path again")
