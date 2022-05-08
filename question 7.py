# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# c=[]
# i=0
# while i<len(list1):
#     c.append(list1) 
#     c.append(list2)
#     i=i+1
# print(c)

a=[1, 5, 10, 12, 16]
b=[1, 2, 10, 13, 16]
i=0
d=[]
while i<len(a):
    d.append(a[i])
    d.append(b[i])
    i+=1   
print(d)
i=0
while i<len(d):
    j=0
    while j<len(d):
        if d[i]<d[j]:
            c=d[i]
            d[i]=d[j]
            d[j]=c
        j=j+1   
    i=i+1
print(d)
