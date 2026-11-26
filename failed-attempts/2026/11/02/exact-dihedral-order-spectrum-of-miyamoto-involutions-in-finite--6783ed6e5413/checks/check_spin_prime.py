from itertools import product
from math import gcd
from collections import Counter

def chi(a,q):
 a %=q
 if not a:return 0
 return 1 if pow(a,(q-1)//2,q)==1 else -1

def phi(n):
 return sum(gcd(a,n)==1 for a in range(1,n+1))

def pred(q,coef):
 m=len(coef);n=m-1;eps=chi((-1)**(n//2)*__import__('math').prod(coef[1:]),q)
 def N(s):
  if n%2==0:
   return q**(n-1)+((q-1) if s%q==0 else -1)*eps*q**(n//2-1)
  return q**(n-1)+(0 if s%q==0 else eps*chi(s,q)*q**((n-1)//2))
 result={1:2,q:2*(N(0)-1)}
 for d in range(2,q+2):
  if (q-1)//2 %d == 0:
   result[d]=phi(d)* (q**(n-1)-eps*q**(n//2-1) if n%2==0 else q**(n-1)+eps*chi(-1,q)*q**((n-1)//2))
  if (q+1)//2 %d == 0:
   result[d]=phi(d)* (q**(n-1)-eps*q**(n//2-1) if n%2==0 else q**(n-1)-eps*chi(-1,q)*q**((n-1)//2))
 return {d:v for d,v in result.items() if v}

def mult(a,b,q):
 n=len(a)
 return [[sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]

def matrix(u,coef,q):
 m=len(u)
 return [[(2*u[i]*coef[j]*u[j]-(i==j))%q for j in range(m)] for i in range(m)]

def order(mat,q):
 n=len(mat)
 eye=[[int(i==j) for j in range(n)] for i in range(n)]
 z=eye
 for d in range(1,2*q+5):
  z=mult(z,mat,q)
  if z==eye:return d
 raise Exception('out of bound')

def run(q,coef):
 m=len(coef);u=tuple([1]+[0]*(m-1))
 R=matrix(u,coef,q)
 counts=Counter()
 for v in product(range(q),repeat=m):
  if sum(c*x*x for c,x in zip(coef,v))%q!=1:continue
  T=mult(R,matrix(v,coef,q),q)
  counts[order(T,q)]+=1
 expected=pred(q,coef)
 print('q=',q,'coef=',coef,'actual',dict(sorted(counts.items())),'pred',expected,'PASS=',dict(counts)==expected)
 assert dict(counts)==expected

for q in (3,5,7,11):
 for co in ([1,1,1],[1,1,2],[1,1,1,1],[1,1,2,1]):
  run(q,co)
print('SPIN_FACTOR_Miyamoto_ORDER_SPECTRUM_OK')
