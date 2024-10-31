# N,M=(int(x) for x in input().split())
# sums=[[0  for j in range(M)] for i in range(N)]
# if N==3 and M==2:
#     sums[-1][-1]=1
# elif N==2 and M==3:
#     sums[-1][-1]=1
# elif N>3 and M>3:
#  for i in range(N):
#      for j in range(M):
#          if i==2 and j==1:
#              sums[i][j]=1
#          elif i==1 and j==2:
#           sums[i][j]=1
#          else:
#              if i - 2 > 0 and j - 1 > 0:
#                  sums[i][j] += sums[i - 2][j - 1]
#              if i - 1 >0 and j - 2 > 0:
#                  sums[i][j] += sums[i - 1][j - 2]
#
# # else: sums[-1][-1]=0
# N=int(input())
# A=[float('inf') for i in range(N+1)]
# A[1]=0
# for i in range(N):
#     if i+1<=N:
#      A[i+1]=min(A[i]+1,A[i+1])
#     if i*2<=N:
#         A[i*2]=min(A[i]+1,A[i*2])
#     if i*3<=N:
#         A[i*3]=min(A[i]+1,A[i*3])
# print(A[-1])

N=int(input())
A=[int(x) for x in input().split()]
a,b,c=0,0,0
C=sum(A)
if C%3!=0:
    print(0)
for i in A:
    for j in A:
        if a==C//3:
            a+=j


print(A)
print(C)






def Levenshtein(s,g):
    n = len(s) + 1
    m = len(g) + 1
    weights = [[0 for j in range(m)] for i in range(n)]
    for i in range(1, n):
        weights[i][0] = i
    for j in range(1, m):
        weights[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            if s[i - 1] == g[j - 1]:
                weights[i][j] = weights[i-1][j-1]
            else:
                weights[i][j] = min(weights[i-1][j], weights[i][j-1], weights[i-1][j-1]) + 1
    return weights[-1][-1]

def Levenshtein(s,g):
    n = len(s) +1
    m = len(g)+1
    weights =  [[0 for j in range(m)] for i in range(n)]
    for i in range(1,n):
        weights[i][0] = i
    for j in range(1,m):
        weights[0][j] = j
    for i in range(1,n):
        for j in range(1,m):
            if s[i-1] == g[j-1]:
             weights[i][j] = weights[i-1][j-1]
            else:
             weights[i][j] = min(weights[i-1][j], weights[i][j-1], weights[i-1][j-1]) + 1
    return weights[-1][-1]






