import numpy as np
N=int(input())
arr=[]
for i in range(N):
    A=list(map(float,input().split()))
    arr.append(A)
print(round(np.linalg.det(arr),2))

