"""
 This script read all the txt files , that contain webpage datas 
 and extracts our important and necessary numbers like area, age, number of rooms and prices.
 Then save datas of one house in a row of df (our DataFrame),
 and at the end save df in a CSV format file.
"""

from informationAndvariables import *
import os
import re
import pandas as pd
from bs4 import BeautifulSoup

dataframe = pd.DataFrame(columns=['Area','Age','Rooms','District','PricePerMeter','Price']) 
urls = URLS

#loop in txt files
len1 = len(urls)
for row in range(len1):
    len2 = int(urls[row][1])
    for counts in range(len2):
        file_name = urls[row][2]+str(counts+1)+".txt"
        file_name = os.path.join(PAGE_FOLDER_ADDRESS,file_name)
        f = open(file_name, "r",encoding='utf-8')
        FullPageCode=f.read()
        soup = BeautifulSoup(FullPageCode,'html.parser')
        f.close()
        all_houses = soup.find_all('div', class_='list_infoBox__2sBvI')
        #loop in houses
        for i in range(len(all_houses)):
            house_div = BeautifulSoup(str(all_houses[i]),'html.parser')
            cost = house_div.find('span' , class_='list_infoPrice__mWQlx')
            atr = house_div.find_all('span' , class_='px-1')
            if re.sub(r'\D' , '' , cost.text) =='' :
                continue
            if len(atr) < 3 :
                continue
            temp_one_house=pd.array([None]*6) #0=Area,1=Age,2=Rooms,3=District,4=PricePerMeter,5=Price
            temp_one_house[3] = urls[row][3]
            temp_one_house[0] = int(re.sub(r'\D' , '' , atr[0].text))
            temp_one_house[1] = 1400 - int(re.sub(r'\D' , '' ,atr[2].text ) )
            temp_one_house[2] = int(re.sub(r'\D' , '' ,atr[1].text )) 
            temp_one_house[5] = int(re.sub(r'\D' , '' , cost.text))
            temp_one_house[4] = int(temp_one_house[5]/temp_one_house[0])
            dataframe.loc[dataframe.shape[0]] = temp_one_house
        print(row,"from ",len1,"  &  ",counts,"from ",len2)

dataframe.to_csv(DATASETV1_ADDRESS)
print("\n================================\nCreating datasetV1.csv finished")