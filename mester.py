file=open("szerelo.txt","r")
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
