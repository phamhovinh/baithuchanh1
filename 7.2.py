#chương trình đọc 1 file tính số kí tự, số từ và dòng của file
k=onpen('D:/a.text','r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc,lc+=wc+1,lc+1
print("The no.of chá is %d\n the no.of words is %d\n the no.of lines is %d"%(char,wc,lc))
