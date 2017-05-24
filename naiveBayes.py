import re
ham1= []
spam2 =[]
count = 0;
with open('SMSSpamCollection','r') as t:
    for a in t:
        if a[0]=='h':
            ham1.append(a)
        elif a[0]=='s':
            spam2.append(a)


def clean(strArr):
    words = list()
    s = 0
    for j in strArr:
        # print(j)
        tester = j
        s += 1
        if s == 1:
            break
    tester = tester[3:]
    print(tester)
    cleanString = re.sub('\W+', ' ', tester)
    print(cleanString.lower())  # this remove all commas, periods, #,/ and make words in lower case

clean(ham1)

"""
for t in spam2:
    print(t)
print('ay')
"""


def stopWords():
    words = {}
    words["a"] = 1
    words["about"] = 1
    words["above"] = 1
    words["after"] = 1
    words["again"] = 1
    words["against"] = 1
    words["all"] = 1
    words["am"] = 1
    words["an"] = 1
    words["and"] = 1
    words["any"] = 1
    words["are"] = 1
    words["arent"] = 1
    words["as"] = 1
    words["at"] = 1
    words["be"] = 1
    words["because"] = 1
    words["been"] = 1
    words["before"] = 1
    words["being"] = 1
    words["below"] = 1
    words["between"] = 1
    words["both"] = 1
    words["but"] = 1
    words["by"] = 1
    words["cant"] = 1
    words["cannot"] = 1
    words["could"] = 1
    words["couldnt"] = 1
    words["did"] = 1
    words["didnt"] = 1
    # words["do"] = 1
    words["does"] = 1
    words["doesnt"] = 1
    words["doing"] = 1
    words["dont"] = 1
    words["down"] = 1
    words["during"] = 1
    words["each"] = 1
    words["few"] = 1
    words["for"] = 1
    words["from"] = 1
    words["further"] = 1
    words["had"] = 1
    words["hadnt"] = 1
    words["has"] = 1
    words["hasnt"] = 1
    words["have"] = 1
    words["havent"] = 1
    words["having"] = 1
    words["he"] = 1
    words["hed"] = 1
    words["hes"] = 1
    words["her"] = 1
    words["here"] = 1
    words["heres"] = 1
    words["hers"] = 1
    words["herself"] = 1
    words["him"] = 1
    words["himself"] = 1
    words["his"] = 1
    words["how"] = 1
    words["hows"] = 1
    words["i"] = 1
    words["id"] = 1
    words["im"] = 1
    words["ive"] = 1
    # words["if"] = 1
    words["in"] = 1
    words["into"] = 1
    words["is"] = 1
    words["isnt"] = 1
    words["it"] = 1
    words["its"] = 1
    words["itself"] = 1
    words["lets"] = 1
    words["me"] = 1
    words["more"] = 1
    words["most"] = 1
    words["mustnt"] = 1
    words["my"] = 1
    words["myself"] = 1
    words["no"] = 1
    words["nor"] = 1
    words["not"] = 1
    words["of"] = 1
    words["off"] = 1
    words["on"] = 1
    words["once"] = 1
    words["only"] = 1
    words["or"] = 1
    words["other"] = 1
    words["ought"] = 1
    words["our"] = 1
    words["ours	ourselves"] = 1
    words["out"] = 1
    words["over"] = 1
    words["own"] = 1
    words["same"] = 1
    words["shant"] = 1
    words["she"] = 1
    words["shed"] = 1
    words["shes"] = 1
    words["should"] = 1
    words["shouldnt"] = 1
    words["so"] = 1
    words["some"] = 1
    words["such"] = 1
    words["than"] = 1
    words["that"] = 1
    words["thats"] = 1
    words["the"] = 1
    words["their"] = 1
    words["theirs"] = 1
    words["them"] = 1
    words["themselves"] = 1
    words["then"] = 1
    words["there"] = 1
    words["theres"] = 1
    words["these"] = 1
    words["they"] = 1
    words["theyd"] = 1
    words["theyll"] = 1
    words["theyre"] = 1
    words["theyve"] = 1
    # words["this"] = 1
    words["those"] = 1
    words["through"] = 1
    words["to"] = 1
    words["too"] = 1
    words["under"] = 1
    words["until"] = 1
    words["up"] = 1
    words["very"] = 1
    words["was"] = 1
    words["wasnt"] = 1
    words["we"] = 1
    words["wed"] = 1
    words["well"] = 1
    words["were"] = 1
    words["weve"] = 1
    words["were"] = 1
    words["werent"] = 1
    # words["what"] = 1
    words["whats"] = 1
    words["when"] = 1
    words["whens"] = 1
    words["where"] = 1
    words["wheres"] = 1
    words["which"] = 1
    words["while"] = 1
    words["who"] = 1
    words["whos"] = 1
    words["whom"] = 1
    words["why"] = 1
    words["whys"] = 1
    words["with"] = 1
    words["wont"] = 1
    words["would"] = 1
    words["wouldnt"] = 1
    # words["you"] = 1
    words["youd"] = 1
    words["youll"] = 1
    words["youre"] = 1
    words["youve"] = 1
    words["your"] = 1
    words["yours"] = 1
    words["yourself"] = 1
    words["yourselves"] = 1
    return words
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