s= " take up one idea and make thi happen idea but where idea is good idea"
subs = "idea"
found= False
pos = -1
leng= len(s)
while True:
    pos=s.find(subs,pos+1,leng)
    if pos == -1:
        break
    print("found the sub string at position ", pos)
    found=True

if found == False:
    print("sub string not found")