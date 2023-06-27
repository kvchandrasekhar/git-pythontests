s="Sahasra and keerthana are sisters"
temp=s.split()
print(temp)
finalresult=[]
i= len(temp)-1
while i >= 0:
    finalresult.append(temp[i])
    i = i-1
print(finalresult)
finaloutput=" ".join(finalresult)
print(finaloutput)