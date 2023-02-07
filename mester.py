file=open("szerelo.txt","r")
<<<<<<< HEAD
file_data=[]


#1 feladat
for i in file:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:    
        file_data.append(i.split('\t'))

del file_data[0]

print(file_data)

#2 feladat



for i in range(len(file_data)):
    if(file_data[i][1]<=max):
        file.write(file_data[i][0]+"\t"+file_data[i][2]+"\n")
max=float(input("Neki van a legnagyobb rutinja:",file))
=======
file2=open("abc.txt","w")
file3=open("ujszerelo.txt","w")
file_data=[]
file_data2=[]
file_data3=[]

for i in file:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:
        file_data.append(i.split('\t'))

del file_data[0]
>>>>>>> a4e47b6a4085ceb6e1d5f8bfcfb03390866562c7
