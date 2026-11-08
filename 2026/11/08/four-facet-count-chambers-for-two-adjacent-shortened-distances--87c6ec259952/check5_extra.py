from itertools import combinations
from fractions import Fraction as F
from time import monotonic

def solve(mat,b):
 n=len(b); a=[[F(x) for x in row]+[bi] for row,bi in zip(mat,b)]
 for k in range(n):
  i=next((i for i in range(k,n) if a[i][k]),None)
  if i is None:return None
  a[i],a[k]=a[k],a[i]
  t=a[k][k]
  for j in range(k,n+1):a[k][j]/=t
  for i in range(k+1,n):
   p=a[i][k]
   if p:
    for j in range(k,n+1):a[i][j]-=p*a[k][j]
 for k in range(n-1,-1,-1):
  for i in range(k): a[i][n]-=a[i][k]*a[k][n]
 return tuple(a[i][n] for i in range(n))

def direct5(r,s):
 rows=[]
 for i,j in combinations(range(5),2):
  d=r if (i,j)==(0,1) else s if (i,j)==(1,2) else F(1)
  for sign in (1,-1):
   v=[0]*4
   if i<4:v[i]+=sign
   if j<4:v[j]-=sign
   rows.append((tuple(v),d))
 vertices=set()
 for comb in combinations(rows,4):
  solution=solve([v for v,d in comb],[d for v,d in comb])
  if solution is not None and all(sum(v[k]*solution[k] for k in range(4))<=d for v,d in rows): vertices.add(solution)
 return len(vertices)

if __name__=='__main__':
 start=monotonic()
 for r,s in [(F(3,4),F(3,5)),(F(2,3),F(2,3)),(F(3,4),F(1,4)),(F(1,2),F(1,2))]:
  n=direct5(r,s);print(r,s,n,'elapsed',round(monotonic()-start,1))
