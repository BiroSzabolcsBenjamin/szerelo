file=open("szerelo.txt","r",encoding="UTF-8")
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

#3.
for i in range(len(file_data)):
    if(file_data[i][2]>="2000"):
        print(file_data[i][1],file_data[i][2],"ben ált munkába")

#4.

#5.