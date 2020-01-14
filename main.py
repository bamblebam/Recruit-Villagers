right,left=0,0
n=int(input("number of houses "))
m,c=list(map(int,input().split()))
for i in range(n):
  x,y,p=list(map(int,input().split()))
  if(y-m*x-c>0):
    right+=p
  else:
    left+=p

print(max(right,left))
