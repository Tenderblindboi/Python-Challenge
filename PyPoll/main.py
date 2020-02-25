import os
import csv
import statistics 
from statistics import mode

#Intitializing the file path and the necessary variables
csvpath = os.path.join("Resources", "election_data.csv")
votes=[]
total=0



#Opens the file and moves on to the next line so the header isn't included in the data 
with open(csvpath, newline="") as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")

	next(csvreader)

	#A list is appended with all of the VOTES
	for row in csvreader:

		total =total +1
		votes.append(row[2])


#Here are all the calculations for each candidates vote count and percentage
Khan=votes.count("Khan")
Khanm=round((Khan/total)*100,3)

Correy=votes.count("Correy")
Correym=round((Correy/total)*100,3)

Li=votes.count("Li")
Lim=round((Li/total)*100,3)

OTooley=votes.count("O'Tooley")
OTooleym=round((OTooley/total)*100.3)
Winner=mode(votes)


#Here is the print and write statements for the necesary files 
#I imported statistics so that I can use the mode function and save some time 
file = open("stuff.txt","w") 
str=f'Election Results\n--------------------\nTotal Votes: {total}\n--------------------\nKhan: {Khanm}% ({Khan})\nCorrey: {Correym}% ({Correy})\nLi: {Lim}% ({Li})\nO"Tooley: {OTooleym}% ({OTooley})\n--------------------\nWinner:{Winner}\n--------------------'
print(str)
file.write(str)
file.close()
