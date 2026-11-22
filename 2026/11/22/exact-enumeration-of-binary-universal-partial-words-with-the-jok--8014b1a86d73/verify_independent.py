from itertools import product
from collections import Counter
from sympy import Matrix

def direct(n):
 L=2**n+n-4
 counts=Counter()
 if n==4:
  for bits in product('01',repeat=L-1):
   w=''.join(bits[:2])+'*'+''.join(bits[2:])
   sh=Counter()
   for i in range(L-n+1):
    p=w[i:i+n]
    for bit in '01' if '*' in p else ('',):
     sh[p.replace('*',bit)]+=1
   if len(sh)==2**n and all(v==1 for v in sh.values()):
    counts[w[:n+2]]+=1
 else:
  V=1<<(n-1)
  for bits in product('01',repeat=n+1):
   pre=bits[:2]+('*',)+bits[2:]
   rem=set(range(1<<n))
   for i in range(3):
    p=pre[i:i+n]
    for b in '01':
     rem.discard(int(''.join(b if c=='*' else c for c in p),2))
   if len(rem)!=(1<<n)-6: continue
   s=int(''.join(bits[2:]),2)
   od=[0]*V;ind=[0]*V;A=[[0]*V for _ in range(V)]
   for e in rem:
    u=e>>1;v=e&(V-1)
    od[u]+=1;ind[v]+=1;A[u][v]+=1
   pos=[i for i in range(V) if od[i]-ind[i]==1]
   neg=[i for i in range(V) if ind[i]-od[i]==1]
   if pos != [s] or len(neg)!=1 or any(abs(od[i]-ind[i])>1 for i in range(V)):
    continue
   t=neg[0]
   Lp=Matrix(V,V,lambda i,j:(od[i] if i==j else 0)-A[i][j])
   M=Lp.minor_submatrix(t,t)
   cnt=M.det(method='domain-ge')
   assert od[t]<=1
   counts[''.join(pre)]+=cnt
 return counts
if __name__=='__main__':
 for n in [4,5,6]:
  ans=direct(n)
  print(n,dict(ans),'SUM',sum(ans.values()),flush=True)
