from collections import deque
from math import factorial, comb

def stirling(n,k):
 a=[[0]*(k+1) for _ in range(n+1)];a[0][0]=1
 for i in range(1,n+1):
  for j in range(1,min(i,k)+1):a[i][j]=j*a[i-1][j]+a[i-1][j-1]
 return a[n][k]

def expected(m,n,k):
 if k<m-1:return 0
 if m==n:
  return 2*m**m-m*m*factorial(m-1) if k==m-1 else 1
 if k==m-1:return m*n**(m-1)
 if k==n-1:return 1+n*sum(comb(m,r)*factorial(r)*stirling(n-1,r) for r in range(1,m-1))
 return 1

def test(m,n):
 N=m*n;full=(1<<N)-1
 neighbors=[]
 for i in range(m):
  for j in range(n):
   neighbors.append(sum(1<<(x*n+y) for x in range(m) for y in range(n) if (x==i or y==j) and (x!=i or y!=j)))
 P=[]; pop=[]; checked=0
 for mask in range(1,1<<N):
  rs=sum(any(mask>>(i*n+j)&1 for j in range(n)) for i in range(m))
  cs=sum(any(mask>>(i*n+j)&1 for i in range(m)) for j in range(n))
  classification=rs>=m-1 or cs>=n-1
  observed=mask
  for u in range(N):
   if mask>>u&1:observed|=neighbors[u]
  while True:
   new=observed
   for u in range(N):
    if observed>>u&1:
     unobs=neighbors[u]&~observed
     if unobs and not(unobs&(unobs-1)):new|=unobs
   if new==observed:break
   observed=new
  direct=observed==full
  assert classification==direct,(m,n,mask,rs,cs)
  checked+=1
  if classification:P.append(mask);pop.append(mask.bit_count())
 index=set(P)
 cs=[]
 for k in range(m-1,n+1):
  nodes={v for v in P if v.bit_count()<=k}
  num=0
  while nodes:
   num+=1
   seed=nodes.pop();q=[seed]
   while q:
    v=q.pop()
    for t in range(N):
     u=v^(1<<t)
     if u in nodes:
      nodes.remove(u);q.append(u)
  cs.append((k,num,expected(m,n,k)))
  assert num==expected(m,n,k),(m,n,cs)
 print('PASS',m,n,'subsets',checked,'PDS',len(P),'components',cs)

for m,n in [(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4)]:test(m,n)
