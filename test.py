fname=raw_input("Enter file name: ")
fh=open(fname)
lst= list()
for line in fh:
    words=line.split()
    for w in words:
        if w not in lst:
            lst.append(w)
        #return lst
newlist = sorted(lst)
print newlist
print "wow, i uploaded this file to github"
print " i have added another line"

    



