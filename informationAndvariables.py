"""
 This script contains constant values and address of files ,
 and an array of urls , number of pages , districts and other necessary informations for web scraping.
"""
import numpy as np
import os

PRJ_FOLDER_ADDRESS = r"C:\Users\hossein\Desktop\prj"
PAGE_FOLDER_ADDRESS = PRJ_FOLDER_ADDRESS+r"\pages"
DATASETV1_ADDRESS = os.path.join(PRJ_FOLDER_ADDRESS,"datasetV1.csv")
DATASETV2_ADDRESS = os.path.join(PRJ_FOLDER_ADDRESS,"datasetV2.csv")
DATASETV3_20_ADDRESS = os.path.join(PRJ_FOLDER_ADDRESS,"datasetV3_20.csv")
DATASETV3_50_ADDRESS = os.path.join(PRJ_FOLDER_ADDRESS,"datasetV3_50.csv")
DATASETV3_100_ADDRESS = os.path.join(PRJ_FOLDER_ADDRESS,"datasetV3_100.csv")
PRICE_PER_METER_ADDRESS = os.path.join(PRJ_FOLDER_ADDRESS,"price_per_meter.csv")

DESCRIPTION = '''پروژه پیشبینی قیمت مسکن به کمک یادگیری ماشینی
متعلق به حسین بلوپستانی اصل
--------------------------------------------------------
این برنامه با استفاده از چهار الگوریتم مناسب
و با استفاده از دیتاست جمع آوری شده
.میتواند با دریافت اطلاعات یک مسکن قیمت آنرا تخمین بزند
دیتاست تهیه شده مربوط به مساکن شهر تهران
.آگهی شده در سایت شابش می باشد
--------------------------------------------------------
برای استفاده فیلد های خالی را تنها با عدد پرکرده
.یکی از الگو هارا انتخاب و سپس کلید محاسبه را بزنید
: مثال
120 : مساحت (متر)
1398 : سال ساخت (شمسی)
2 : تعداد اتاق (عدد صحیح)
1 : منطقه (مناطق موجود در شهر تهران)
22,18,17,16,15,14,13,11,10,9,8,7,6,5,4,3,2,1 : مناطق مجاز

: توضیح فیلد قیمت هر متر
اگر قیمت هر متر مسکن را وارد کنید برنامه از آن استفاده میکند
در غیر این صورت با خالی گذاشتن این فیلد برنامه
.از میانگین قیمت هر متر در آن منطقه استفاده خواهد کرد
'''

URLS = np.array([
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B3%D8%B9%D8%A7%D8%AF%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",216,"saadat_abad",2],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",154,"zaferanie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%BE%D9%88%D9%86%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",127,"poonak",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%88%D9%84%D9%86%D8%AC%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",117,"velenjak",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A8%D9%84%D9%88%D8%A7%D8%B1-%D9%81%D8%B1%D8%AF%D9%88%D8%B3-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",113,"bolovar_ferdous",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%86%DB%8C%D8%A7%D9%88%D8%B1%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",103,"niavaran",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%BE%D8%A7%D8%B3%D8%AF%D8%A7%D8%B1%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",65,"pasdaran",4],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%81%D8%B1%D9%85%D8%A7%D9%86%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",46,"farmanie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B3%D8%A7%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",47,"sazman_barname",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B4%D9%87%D8%B1%DA%A9-%D8%BA%D8%B1%D8%A8-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",47,"shahrak_gharb",2],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AC%D9%86%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AC%D9%86%D9%88%D8%A8%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",46,"janatabad_jonoobi",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AC%D8%B1%D8%AF%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",16,"jordan",6],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%87%D8%B1%D9%88%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",39,"heravi",4],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AF%D8%B1%D9%88%D8%B3-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",38,"daroos",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AC%D9%86%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF-%D9%85%D8%B1%DA%A9%D8%B2%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",36,"janatabad_markazi",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B4%D9%87%D8%B1-%D8%B2%DB%8C%D8%A8%D8%A7-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",34,"shahr_ziba",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DA%86%DB%8C%D8%AA%DA%AF%D8%B1-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",33,"chitgar",22],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%82%DB%8C%D8%B7%D8%B1%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",28,"gheytarie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D9%84%D9%87%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",30,"elahie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B5%D8%A7%D8%AF%D9%82%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",31,"sadeghie",2],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%81%D8%B1%D8%B4%D8%AA%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",28,"fereshte",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%85%D8%AD%D9%85%D9%88%D8%AF%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",28,"mahmoodie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B3%D8%AA%D8%A7%D8%B1%D8%AE%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",27,"satarkhan",2],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B4%D9%87%D8%B1%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",27,"shahran",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D8%B2%DA%AF%D9%84-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",24,"ozgol",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%85%DB%8C%D8%B1%D8%AF%D8%A7%D9%85%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",14,"mirdamad",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B8%D9%81%D8%B1-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",12,"zafar",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%BE%DB%8C%D8%B1%D9%88%D8%B2%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",24,"piroozi",13],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D8%AE%D8%AA%DB%8C%D8%A7%D8%B1%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",22,"ekhtiarie",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86%D9%BE%D8%A7%D8%B1%D8%B3-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",21,"tehran_pars",8],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A2%DB%8C%D8%AA-%D8%A7%D9%84%D9%84%D9%87-%DA%A9%D8%A7%D8%B4%D8%A7%D9%86%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",20,"aytl_kashani",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%85%D8%B1%D8%B2%D8%AF%D8%A7%D8%B1%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",20,"marzdaran",2],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D8%B3%D8%AA%D8%A7%D8%AF-%D9%85%D8%B9%DB%8C%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",19,"ostad_moein",9],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B3%DB%8C%D8%AF%D8%AE%D9%86%D8%AF%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",15,"seyed_khandan",7],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AC%DB%8C%D8%AD%D9%88%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",18,"jeyhoon",10],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AC%D9%86%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%B4%D9%85%D8%A7%D9%84%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",18,"janatabad_shomali",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A8%D8%A7%D8%BA-%D9%81%DB%8C%D8%B6-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",17,"bagh_feyz",5],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DA%A9%D8%A7%D9%85%D8%B1%D8%A7%D9%86%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",14,"kamranie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AF%D9%88%D9%84%D8%AA-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",13,"dolat",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B3%D9%84%D8%B3%D8%A8%DB%8C%D9%84-%D8%B4%D9%85%D8%A7%D9%84%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",13,"selsebil_shomali",10],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%86%D8%A7%D8%B1%D9%85%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"narmak",8],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%85%D8%AC%DB%8C%D8%AF%DB%8C%D9%87-%D8%AC%D9%86%D9%88%D8%A8%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",5,"majidie_jonoobi",8],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%85%D8%AC%DB%8C%D8%AF%DB%8C%D9%87-%D8%B4%D9%85%D8%A7%D9%84%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"majidie_shomali",4],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DA%AF%DB%8C%D8%B4%D8%A7-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"gisha",2],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DB%8C%D8%A7%D9%81%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"yaft_abad",18],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AF%D8%A7%D8%B1%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"darabad",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AD%DA%A9%DB%8C%D9%85%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",6,"hakimie",4],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%86%D8%A7%D8%B2%DB%8C-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"nazi_abad",16],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D9%85%DB%8C%D8%B1%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"amirie",11],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A8%D8%B1%DB%8C%D8%A7%D9%86%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",10,"beryanak",10],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B2%D9%85%D8%B2%D9%85-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",4,"zamzam",17],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D9%81%D8%B3%D8%B1%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"afsarie",15],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A2%D9%87%D9%86%DA%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"ahang",14],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B5%D8%A7%D8%AD%D8%A8%D9%82%D8%B1%D8%A7%D9%86%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"saheb_gharanie",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A2%D8%B0%D8%B1%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",7,"azari",17],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DA%86%DB%8C%D8%B0%D8%B1-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",4,"chizar",1],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%82%D9%84%D9%87%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",6,"gholhak",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%88%D9%86%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",5,"vanak",3],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A8%D9%87%D8%B4%D8%AA%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",4,"beheshti",4],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B9%D8%A8%D8%A7%D8%B3-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",4,"abas_abad",4],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%DB%8C%D9%88%D8%B3%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",6,"yoosef_abad",6],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D9%85%DB%8C%D8%B1%D8%A2%D8%A8%D8%A7%D8%AF-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"amir_abad",6],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%85%D9%86%DB%8C%D8%B1%DB%8C%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"monirie",11],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%81%D9%84%D8%A7%D8%AD-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",8,"falah",17],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AC%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",9,"jey",9],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AE%D8%B2%D8%A7%D9%86%D9%87-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",6,"khazane",16],
    ["https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B7%D8%B1%D8%B4%D8%AA-%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page=",10,"tarasht",2],])
