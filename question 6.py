a=string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
d=[]
i=0
while i<len(a):
    j=a[i]
    if j not in d:
        d.append(j)
    i=i+1
print(d)        
