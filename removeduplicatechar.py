s="aabbddcceeddRR44EEttDF"
temp=[]
for c in s:
    if c not in temp:
        temp.append(c)
print(temp)