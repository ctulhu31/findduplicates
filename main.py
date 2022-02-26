import os
import hashlib

def addtodict(x):
    if dictoffiles.get(x[1]) != None:
        pr = dictoffiles.get(x[1])
        pr = pr + ' ' + x[0]
        dictoffiles.update({x[1]:pr})
    else:
        dictoffiles.update({x[1]: x[0]})

def findallfiles(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                md5 = hashlib.md5()
                while True:
                    data = f.read(8192)
                    if not data:
                        break
                    md5.update(data)
            x = [path, md5.hexdigest()]
            addtodict(x)
        else:
            findallfiles(path)

def recfind(path):
    print('Searching duplicates in ' + path)
    findallfiles(path)
    for i in dictoffiles.keys():
        x = dictoffiles[i]
        if x.find(path) != x.rfind(path):
            listofrepeats.append([x, i])

def writetofile(listofrepeats):
    try:
        f = open(mainpath + 'duplicates.txt','w')
        for i in listofrepeats:
            f.write('md5: ' + i[1] + ':\n')
            t = i[0]
            x = 0
            for j in t.split(mainpath):
                if x > 0:
                    f.write('     ' + mainpath + j + '\n')
                x += 1
            f.write('\n')
        f.close()
        print('All found duplicates were written to ' + mainpath + 'duplicates.txt')
        return True
    except:
        return False

def printlist(x):
    for i in x:
        print('md5:' + i[1] + ':')
        t = i[0]
        z = 0
        for j in t.split(mainpath):
            if z > 0:
                print('     ' + mainpath + j)
            z += 1

def main():
    global mainpath
    mainpath = input('Enter path to directory:')
    global dictoffiles
    dictoffiles = {}
    global listofrepeats
    listofrepeats = []
    if os.path.exists(mainpath):
        if os.path.isdir(mainpath):
            recfind(mainpath)
            if listofrepeats == []:
                print('No duplicates in directory ' + mainpath)
            else:
                if not writetofile(listofrepeats):
                    print('Can not write list of duplicates to ' + mainpath + 'duplicates.txt or can not to create duplicates.txt')
                    print('Find this duplicates:')
                    printlist(listofrepeats)
        else:
            print(mainpath + ' is not a directory')
    else:
        print(mainpath + ' does not exist')

main()