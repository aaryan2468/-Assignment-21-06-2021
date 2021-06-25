lst = []
for i in range(2,50):
    c = 0
    for j in range(2,i):
        if (i%j) == 0:
            c=c+1
            break

    if(c==0 and i!=1):
            lst.append(i)

r = 4
copy = lst

m=(2*r)-2

count = 0

for i in range(0,r+1):
    for j in range(0,m):
        print(end=" ")
    m = m-1
    
    for j in range(0,i+1):
        count = count+1
        if(j!=0):
            print(lst[count-1], end =" ")
        else:
            print(lst[count-1], end =" ")
    print("\n")
