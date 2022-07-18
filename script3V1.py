"""
 This script calculates average of Price per Meter in the each district and save it in to an array (P_PER_M_Info)
 and replace the average replaces the average instead of the price per meter in the dataframe depending on the district
"""

from informationAndvariables import *
import pandas as pd

file_name = DATASETV1_ADDRESS #dataset address
dataset = pd.read_csv(file_name)  #dataset file
dataset = dataset.iloc[:, 1:]
dataset['PricePerMeter'] = dataset['PricePerMeter'].astype(float)

print("\n================================\n")
print(dataset)

#if price_per_meter.csv exists use this part of code
price_per_meter_df = pd.read_csv(PRICE_PER_METER_ADDRESS)
price_per_meter_df = price_per_meter_df.iloc[:, 1:]

for row in range(len(dataset)) : 
    dataset.at[row,'PricePerMeter']=dataset.loc[row][4]/1000000

#if price_per_meter.csv don't exist use this part of code
'''
price_per_meter_df = pd.DataFrame(columns=['sum','count','avarage'],data=[[0,0,0]]*23,dtype='float') 

for row in range(len(dataset)) : 
    dataset.at[row,'PricePerMeter']=dataset.loc[row][4]/1000000
    price_per_meter_df.at[int(dataset.loc[row][3]),'sum'] += dataset.loc[row][4]
    price_per_meter_df.at[int(dataset.loc[row][3]),'count'] += 1

for r in range(price_per_meter_df.shape[0]):
    if price_per_meter_df.at[r,'count'] !=0 :
        price_per_meter_df.at[r,'avarage']=price_per_meter_df.at[r,'sum']/price_per_meter_df.at[r,'count']

price_per_meter_df.to_csv(PRICE_PER_METER_ADDRESS)
print("\n================================\nCreating price_per_meter.csv finished")
'''

print("\n================================\nDivide the PricePerMeter column finished")
print(price_per_meter_df)

for row in range(len(dataset)) :
    dataset.at[row,'PricePerMeter'] = price_per_meter_df.at[int(dataset.at[row,'District']),'avarage']

dataset= dataset.reset_index()
print("\n================================\nReplacing avarage in PricePerMeter column finished")
dataset = dataset.iloc[: , 1:]
print(dataset)
dataset.to_csv(DATASETV2_ADDRESS)