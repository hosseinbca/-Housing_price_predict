"""
 This script gets URLs that Belongs to shabesh.com and save each URL in the text file.
 (web scraping)
"""

from informationAndvariables import *
import os
import requests

urls = URLS
path = PAGE_FOLDER_ADDRESS

print("\n================================\nWeb scraping started")

for i in range(len(urls)) :
        for j in range(int(urls[i][1])) :
                r = requests.get(urls[i][0]+str(j+1))
                file_name = urls[i][2]+str(j+1)+".txt"
                file_name = os.path.join(path,file_name)
                print(str(i)+"   "+file_name)
                f= open(file_name,"w+", encoding = 'utf-8')
                f.write(r.text)
                f.close()
                print("saved")

print("\n================================\nWeb scraping finished")