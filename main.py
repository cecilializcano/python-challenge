import csv
#Read csv file
with open ('Resources/election_data.csv') as file:
    data = csv.reader(file,delimiter=',')
    ballot_id=[]
    county=[]
    candidate=[]
    i=0
    #Read text file row by row
    for row in data:
        if i!=0:
            ballot_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        i=i+1
    
total_votes=str(len(ballot_id))

#Ensure that the candidates names are sorted and add a blank cell
candidate2=sorted(candidate)
candidate2.append('')
#Find different candidates and their quantity of votes
persons=[]
votes=[]
vote=0
i=0
u=0
for person in candidate2:
    if i==0:
        persons.append(person)
        i=1
    if persons[u]!=person:
        persons.append(person)
        u=u+1
        votes.insert(u-1,vote)
        vote=0
    else:
        vote=vote+1
persons.pop()
votes_percent=[]

#Transform votes into %
for i in votes:
    votes_percent.append(round(i*100/len(ballot_id),3))

#Find index that has higher votes_percent
winner_index=0
winner=votes_percent[0]
i=0
for x in votes_percent:
    if x>winner:
        winner=x
        winner_index=i
    i=i+1

#print on terminal
u=0
print('Election Results' +'\n'+'\n')
print('-------------------------' +'\n'+'\n')
print('Total Votes: '+ total_votes + '\n'+'\n')
print('-------------------------' +'\n'+'\n')
for person in persons:
    print(persons[u]+': '+ str(votes_percent[u])+'% '+'('+str(votes[u])+')'+'\n'+'\n')
    u=u+1
print('-------------------------' +'\n'+'\n')
print('Winner: '+persons[winner_index]+'\n'+'\n')
print('-------------------------' +'\n'+'\n')

#Write results on text file
u=0
with open ('Analysis/Result.txt','w') as result:
    result.write('Election Results' +'\n'+'\n')
    result.write('-------------------------' +'\n'+'\n')
    result.write('Total Votes: '+ total_votes + '\n'+'\n')
    result.write('-------------------------' +'\n'+'\n')
    for person in persons:
        result.write(persons[u]+': '+ str(votes_percent[u])+'% '+'('+str(votes[u])+')'+'\n'+'\n')
        u=u+1
    result.write('-------------------------' +'\n'+'\n')
    result.write('Winner: '+persons[winner_index]+'\n'+'\n')
    result.write('-------------------------' +'\n'+'\n')