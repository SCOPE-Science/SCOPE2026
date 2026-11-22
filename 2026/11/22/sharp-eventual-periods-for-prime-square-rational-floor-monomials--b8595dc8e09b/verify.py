from math import gcd,lcm
from fractions import Fraction
from functools import lru_cache

def factors(x):
 d=2; s=[]
 while d*d<=x:
  if x%d==0:
   s.append(d)
   while x%d==0:x//=d
  d+=1
 if x>1:s.append(x)
 return s

@lru_cache(None)
def spec(a,p,k):
 b=p*p
 t={r:(a*pow(r,k,b))%b for r in range(1,b) if r%p}
 Q=1
 for v in t.values():
  for q in factors(v): Q=lcm(Q,q)
 return t,Q,(p if k%p==0 else p*p)*Q

def f(a,p,k,n):return int(gcd(n,a*n**k//(p*p))==1)
def model(a,p,k,n):
 if n%p==0: return int(k==2 and n==p)
 t,Q,P=spec(a,p,k)
 return int(gcd(n,t[n%(p*p)])==1)

def least_period(xs):
 n=len(xs)
 return min(q for q in range(1,n+1) if n%q==0 and all(xs[i]==xs[i%q] for i in range(n)))

ct=0;small=0
for p in (2,3,5,7,11,13):
 for a in range(1,min(p*p,20)):
  if a%p==0:continue
  for k in range(2,11):
   t,Q,P=spec(a,p,k)
   for n in range(1,220):
    assert f(a,p,k,n)==model(a,p,k,n),(a,p,k,n,'model')
   for n in range(p+1,100):
    assert model(a,p,k,n)==model(a,p,k,n+P),(a,p,k,n,'period')
   if P<=1600:
    xs=[model(a,p,k,n) for n in range(p+1,p+P+1)]
    assert least_period(xs)==P,(a,p,k,least_period(xs),P)
    expected=sum(Fraction(sum(gcd(j,v)==1 for j in range(1,v+1)),v) for v in t.values())/(p*p)
    assert Fraction(sum(xs),P)==expected,(a,p,k,P,'density')
    small+=1
   if k==2:assert f(a,p,k,p)==1 and model(a,p,k,p+P)==0
   else:assert f(a,p,k,p)==0
   ct+=1
print('PRIME_SQUARE_FLOOR_COPRIMALITY_OK',ct,'FULL_PERIOD_DENSITIES',small)
