import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
import pandas as pd



inputPath="/Users/Omneya/Desktop/HW3/tesseract/image/"
for imageName in os.listdir(inputPath):
              
        imagePath = os.path.join(inputPath, imageName)
        
  
        # applying ocr using pytesseract for python
        extract = pytesseract.image_to_string(Image.open(imagePath))
        extract=''.join(extract)
        extract=extract.split('\n')
        lst=list()
        for i in extract:
          if i!='' and i!=' ':lst.append(i)

        imageName=imageName.replace('.png','.csv')
        outputPath=inputPath
        
      
    
        df = pd.DataFrame(lst) 
        df.to_csv(imageName) 

       