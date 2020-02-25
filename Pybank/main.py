import os
import csv
from csv import DictReader

csvpath = os.path.join("Resources", "budget_data.csv")
total=0
count=0
average=0

change = []
date =[] 



with open(csvpath, newline="") as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")

	next(csvreader)

	for row in csvreader:
		#data=row.split(',')
		#list.append(data[1])
		total += float(row[1])
		count=count+1
		change.append(row[1])
		date.append(row[0])
    	


		

minimum=min(change)
maximum=max(change)
MaxI=change.index(maximum)
MinI=change.index(minimum)
average=(total/count)
maxdate=date[MaxI]
mindate=date[MinI]

file = open("stuff.txt","w") 

str=f'Financial Analysis\n ------------------- \nTotal Months:{count}\nTotal:${total}\nAverage change:${average}\nGreatest Increase in Proftits: {maxdate} (${maximum})\nGreatest Decrease in Profits: {mindate} (${minimum})'
print(str)
file.write(str)
file.close()



