
n = int(input())
c = [int(c_temp) for c_temp in input().split(' ')]
i=0
count=0
c=c+[0]
while i!=(n-1):
    if(c[i+2]==0 and i<(n-2)):
        i+=2
        count+=1
    else:
        i+=1
        count+=1
print(count)
