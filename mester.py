file=open("szerelo.txt","r",encoding="UTF-8")
file2=open("abc.txt","w",encoding="UTF-8")
file3=open("ujszerelo.txt","w",encoding="UTF-8")
file_data=[]

for i in file:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:
        file_data.append(i.split('\t'))

del file_data[0]

#1.
print("Szerelők létszáma: ",len(file_data))

#2.
for i in range(len(file_data)):
    if(file_data[0][2]>file_data[i][2]):
        print(file_data[i][1],"a legnagyobb munka tapasztalattal rendelkező szerelő.")

#3.
for i in range(len(file_data)):
    if(file_data[i][2]>="2000"):
        print(file_data[i][1],file_data[i][2],"ben ált munkába")

#4.
for i in range(len(file_data)):
    file2.write(file_data[i][1]+"\n")

#5.
for i in range(len(file_data)):
    del file_data[i][0]
    file3.write(file_data[i][0]+"\t"+file_data[i][1]+"\n")

