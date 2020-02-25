import os
import csv
from csv import DictReader




#Intitializing the file path and the necessary variables
csvpath = os.path.join("Resources", "budget_data.csv")
total=0
count=0
average=0

change = []
date =[] 


#Opens the file and moves on to the next line so the header isn't included in the data 
with open(csvpath, newline="") as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")

	next(csvreader)
	#A list is appended with all of the profit/losses along with a list of all of the dates
	for row in csvreader:
		#data=row.split(',')
		#list.append(data[1])
		total += float(row[1])
		count=count+1
		change.append(row[1])
		date.append(row[0])
    	


		
#All of the final result variable 
minimum=min(change)
maximum=max(change)
MaxI=change.index(maximum)
MinI=change.index(minimum)
average=(total/count)
maxdate=date[MaxI]
mindate=date[MinI]



#File writing and printing all the necessary information 
file = open("stuff.txt","w") 

str=f'Financial Analysis\n ------------------- \nTotal Months:{count}\nTotal:${total}\nAverage change:${average}\nGreatest Increase in Proftits: {maxdate} (${maximum})\nGreatest Decrease in Profits: {mindate} (${minimum})'
print(str)
file.write(str)
file.close()



