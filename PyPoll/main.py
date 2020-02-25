import os
import csv
import statistics 
from statistics import mode

csvpath = os.path.join("Resources", "election_data.csv")
votes=[]
total=0

with open(csvpath, newline="") as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")

	next(csvreader)

	for row in csvreader:

		total =total +1
		votes.append(row[2])



Khan=votes.count("Khan")
Khanm=round((Khan/total)*100,3)

Correy=votes.count("Correy")
Correym=round((Correy/total)*100,3)

Li=votes.count("Li")
Lim=round((Li/total)*100,3)

OTooley=votes.count("O'Tooley")
OTooleym=round((OTooley/total)*100.3)
Winner=mode(votes)

file = open("stuff.txt","w") 
str=f'Election Results\n--------------------\nTotal Votes: {total}\n--------------------\nKhan: {Khanm}% ({Khan})\nCorrey: {Correym}% ({Correy})\nLi: {Lim}% ({Li})\nO"Tooley: {OTooleym}% ({OTooley})\n--------------------\nWinner:{Winner}\n--------------------'
print(str)
file.write(str)
file.close()
