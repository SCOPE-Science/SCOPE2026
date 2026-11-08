from itertools import permutations, combinations, product
from math import comb, factorial
from fractions import Fraction
from random import Random

def params(f):
 n=len(f)
 ds=[0]*n
 for v in f:ds[v]+=1
 z=sum(comb(d,3) for d in ds if d>=3)
 m=sum(comb(d,2)*(n-d) for d in ds if d>=2)
 c1=sum(f[i]==i for i in range(n))
 c3=0
 for i in range(n):
  if len({i,f[i],f[f[i]]})==3 and f[f[f[i]]]==i:c3+=1
 c3//=3
 plus=minus=0
 for ss in combinations(range(n),3):
  im=[f[v] for v in ss]
  if len(set(im))!=2:continue
  common=next(v for v in set(im) if im.count(v)==2)
  unique=next(v for v in set(im) if im.count(v)==1)
  if unique in ss and common not in ss: plus+=1
  if common in ss and unique not in ss: minus+=1
 return z,m,c1,c3,plus,minus

def formula(f,i):
 n=len(f);z,m,c1,c3,plus,minus=params(f);t=comb(n,3)
 a=Fraction(1,3)-Fraction(2*z+m+2*comb(c1,3) if c1>=3 else 2*z+m,6*t)+Fraction(c3,6*t)
 return a+Fraction((plus-minus)*(2*i-(n+1)),6*t*(n-3))

def counts(f):
 n=len(f);ans=[0]*(n-2)
 for o in permutations(range(n)):
  lab=[0]*n
  for i,x in enumerate(o):lab[x]=i
  p=[lab[f[x]] for x in o]
  for i in range(1,n-1):ans[i-1]+=(p[i-1]<p[i]>p[i+1])
 return ans

def run():
 tests=0
 rng=Random(731)
 for n in range(4,6):
  for f in product(range(n),repeat=n):
   c=counts(f)
   for i,v in enumerate(c,2):
    got=formula(f,i)
    assert got*factorial(n)==v,(n,f,i,got,v)
    tests+=1
 for n,nsamples in [(6,140),(7,24),(8,6)]:
  for _ in range(nsamples):
   f=tuple(rng.randrange(n) for _ in range(n));c=counts(f)
   for i,v in enumerate(c,2):
    got=formula(f,i)
    assert got*factorial(n)==v,(n,f,i,got,v)
    tests+=1
 print('VERIFY_OK',tests,'exact assertions')

if __name__=='__main__':run()
