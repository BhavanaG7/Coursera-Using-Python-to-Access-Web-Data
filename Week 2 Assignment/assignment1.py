fhandle=open("Actual.txt")
val=[]
for i in fhandle:
    import re
    y=re.findall("[0-9]+",i)
    if y!=[]:
        val.extend(y)

val=list(map(int,val))
print(sum(val))