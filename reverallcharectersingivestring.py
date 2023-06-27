s="Sahasra and keerthana are sisters"
temp=s.split()
print(temp)
result=[]
i=0
while i < len(temp):
    result.append(temp[i][::-1])
    i = i+1
print(result)
outputresult= "  ".join(result)
print(outputresult)