import re
ham1= []
spam2 =[]
count = 0;
with open('file1.py','r') as t:
    for a in t:
    if a[0]=='h':
        ham1.append(a)
    elif a[0]=='s':
        spam2.append(a)


words=list()
s =0
for j in ham1:
    #print(j)
    tester=j
        s+=1
            if s==1:
                cbreak
tester=tester[3:]
print(tester)
cleanString=re.sub('\W+', ' ',tester)
print(cleanString.lower()) #this remove all commas, periods, #,/ and make words in lower case


"""
for t in spam2:
    print(t)
print('ay')
"""



"""
Git Lessons:
To get to Spam Folder:
cd Documents
cd "___" //drage the folter


cd /Users/Alma/Downloads/pam-Filter-Master
Spam-Filter-master Alma$ git status

cd /Users/Alma/Downloads/Spam---something master
git status
cd ..
git clone https://github.com/thesubway/Spam-Filter.git   /*prob dragged*/
cd Spam-Filter
git status
git add .

git commit -m "test"
git push




"""