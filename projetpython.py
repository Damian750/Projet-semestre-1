import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\22bla\\Documents\\Damien Ecole\\Info')
df=pd.read_csv("EIVP_KM2.csv")
# for idx,column in enumerate(df.columns):
#     print(idx,column)

ID,NOISE,TEMP,HUMIDITY,LUM,CO2,SENT_AT=[],[],[],[],[],[],[]

for k in df['id']:
    ID.append(k)
for k in df['noise']:
    NOISE.append(k)
for k in df['temp']:
    TEMP.append(k)
for k in df['humidity']:
    HUMIDITY.append(k)
for k in df['lum']:
    LUM.append(k)
for k in df['co2']:
    CO2.append(k)
for k in df['sent_at']:
    SENT_AT.append(k)
    


    


