from math import comb, factorial
from collections import Counter

def ffac(n,k):
 if k<0 or n<k:return 0
 return factorial(n)//factorial(n-k)
def matching(m,n):
 return {k:comb(m,k)*comb(n,k)*factorial(k) for k in range(min(m,n)+1)}
def calc(m,n):
 ans=Counter()
 for a,b in [(m,n),(n,m)]:
  for p in range(a+1):
   for q in range(a-p+1):
    if 2*p+q<=b:
     ans[2*p+q]+=ffac(a,p+q)*ffac(b,2*p+q)//(factorial(p)*factorial(q)*2**p)
 for k,v in matching(m,n).items():ans[k]-=v
 for k,v in matching(m-2,n-2).items():
  ans[k+3]+=4*comb(m,2)*comb(n,2)*v
  ans[k+4]+=comb(m,2)*comb(n,2)*v
 for k,v in matching(m-3,n-2).items():
  ans[k+4]+=m*comb(n,2)*ffac(m-1,2)*v
 for k,v in matching(m-2,n-3).items():
  ans[k+4]+=n*comb(m,2)*ffac(n-1,2)*v
 ans[3]+=m*comb(n,3)+n*comb(m,3)
 return +ans

def brute(m,n):
 ret=Counter(); total=m*n
 neigh=[]
 for r in range(m):
  for c in range(n):
   v=sum(1<<(i*n+j) for i in range(m) for j in range(n) if i==r or j==c)
   neigh.append(v)
 for s in range(1<<total):
  if all((s & v).bit_count()<=3 for v in neigh): ret[s.bit_count()]+=1
 return ret

if __name__=='__main__':
 for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5)]:
  a=calc(m,n); b=brute(m,n); print(m,n,'OK' if a==b else 'FAIL',sum(b.values()),'max',max(b),'formula',dict(sorted(a.items())))
  if a!=b:print('brute',dict(sorted(b.items())))
