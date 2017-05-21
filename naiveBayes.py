print ('Hello')
ham1 = []
spam2 = []
count = 0;
with open('file1.py', 'r') as t:
    for a in t:
        if a[0] == 'h':
            ham1.append(a)
        elif a[0] == 's':
            spam2.append(a)


track =0;
for j in ham1:  # to isolate each words in j
    for s in j:
        print(s)
    track+=1
    if track==1:
        break

"""
for t in spam2:
    print(t)
print('ay')
"""



"""
Git Lessons:
cd /Users/Alma/Downloads/pam-Filter-Master
Spam-Filter-master Alma$ git status

cd /Users/Alma/Downloads/Spam---something master
git status
cd ..
git clone https://github.com/thesubway/Spam-Filter.git   /*prob dragged*/
cd Spam-Filter
git status
git add .
git commit
git commit -m "test"
git push




"""