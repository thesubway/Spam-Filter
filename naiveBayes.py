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

for j in ham1:  #
    print(j)

for t in spam2:
    print(t)