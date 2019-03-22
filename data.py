import pandas as pd

my_csv = pd.read_csv("hospital_directory.csv")

column=my_csv['Location_Coordinates']
column=column.str.split(',')
Hosp_Name=my_csv['Hospital_Name']

#while i<=5:
	#print(column[i][0])
	#i+=1
lat=[]
for i in range(len(column)):
	lat.append(column[i][0])

lon=[]
for j in range(len(column)):
	lon.append(column[j][1])

print(type(column[1][1]))
print(column[1][1])
print(float(column[1][1]))