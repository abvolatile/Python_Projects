#
# PYTHON:   version 3.6.0
#
# AUTHOR:   Annie Bowman
#
# PURPOSE:  Tech Academy Python Course Item #48
#           Sort Algorithm DRILL
#


#using Shell Sort type of algorithm (because it's cute)

def listSort(anylist):
    sublists = len(anylist)//2
    while sublists > 0:
        for start in range(sublists):
            gapInsertSort(anylist,start,sublists)
        sublists = sublists // 2

def gapInsertSort(alist,start,gap):
    for x in range(start+gap,len(anylist),gap):
        curval = anylist[x]
        pos = x
        while pos >= gap and anylist[pos-gap] > curval:
            anylist[pos] = anylist[pos-gap]
            pos = pos-gap
        anylist[pos] = curval

anylist = [67,45,2,13,1,998]
listSort(anylist)
print(anylist)

anylist = [89,23,33,45,10,12,45,45,45]
listSort(anylist)
print(anylist)

