file=open("szerelo.txt","r")
file_data=[]

for i in file:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:
        file_data.append(i.split('\t'))

del file_data[0]

#1 feladat
print("Ennyi szerelő van: ",len(file_data))

#2 feladat


