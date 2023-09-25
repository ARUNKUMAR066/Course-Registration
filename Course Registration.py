t=int(input())
for i in range(t):
    k,m,n=map(int,input().split())
    if k+n<=m:
        print("Yes")
    else:
        print("No")
