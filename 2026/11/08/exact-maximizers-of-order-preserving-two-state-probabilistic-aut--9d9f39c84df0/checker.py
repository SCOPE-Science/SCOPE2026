from fractions import Fraction as Q
from itertools import product
from math import factorial,comb

def build(runs):
 n=sum(runs)
 k=len(runs)
 kap=Q(1,4*n); base_slope=1-kap;c=kap/2;eps=Q(1,10000*n**4)
 B=[(1-base_slope**j)/2 for j in range(n+1)]
 q=0; thresholds=[]
 for h in runs[:-1]:
  q+=h
  thresholds.append((B[q-1]+B[q])/2)
 maps=[]; bsum=0
 for i in range(k):
  maps.append((base_slope+eps*i, c-eps*bsum))
  if i<k-1: bsum+=thresholds[i]
 return maps,B,thresholds

def check(runs, brute=True):
 maps,B,T=build(runs); n=sum(runs); w=tuple(i for i,r in enumerate(runs) for _ in range(r));x=Q(0)
 assert all(0<=b<=1 and 0<=a+b<=1 and a>0 for a,b in maps)
 for j,i in enumerate(w):
  vals=[a*x+b for a,b in maps]
  assert vals[i]>max([v for h,v in enumerate(vals) if h!=i],default=-1), (runs,j,x, vals)
  x=vals[i]
  assert abs(x-B[j+1])<Q(1,5000*n*n)+Q(1,10**12)
 if brute and len(runs)>1:
  def score(word):
   y=Q(0)
   for i in word:
    a,b=maps[i];y=a*y+b
   return y
  assert all(score(z)<x for z in product(range(len(runs)),repeat=n) if z!=w)
 return x

if __name__=='__main__':
 tested=0
 for n in range(1,9):
  for q in range(1,min(4,n)+1):
   for cuts in product((0,1),repeat=n-1):
    if sum(cuts)!=q-1: continue
    r=[];k=1
    for c in cuts:
     if c:r.append(k);k=1
     else:k+=1
    r.append(k)
    check(r,brute=(n<=6))
    tested+=1
 print('Passed',tested,'explicit rational run-profile witnesses, plus full word comparisons through length six')
 for r in ([1,1,1],[1,2,1],[3,1,4],[1,1,1,1],[1,4,1,2]):
  print(r, float(check(r,brute=False)))

# Independent grid audit: enumerate representative order-preserving affine PFAs.
def grid_audit():
 from itertools import product
 from fractions import Fraction as Q
 import random
 rng=random.Random(37)
 rational_grid=[Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]
 options=[(p-q,q) for p in rational_grid for q in rational_grid if p>=q]
 tested=0;unique=0
 for _ in range(350):
  maps=[rng.choice(options) for __ in range(3)]
  x0=rng.choice(rational_grid)
  acc=rng.choice((1,-1))
  for n in range(1,6):
   vals=[]
   for word in product(range(3),repeat=n):
    x=x0
    for a in word:
     slope,intercept=maps[a]
     x=slope*x+intercept
    vals.append((acc*x,word))
   top=max(t for t,w in vals)
   matches=[w for t,w in vals if t==top]
   if len(matches)==1:
    unique+=1
    seen=set();last=None
    for a in matches[0]:
     if a!=last:
      assert a not in seen
      seen.add(a);last=a
   tested+=1
 return tested,unique

if __name__=='__main__':
 print('Order-preserving PFA grid audit:',grid_audit())

def count_audit():
 from itertools import product
 from math import factorial,comb
 checked=0
 for q in range(2,6):
  for n in range(1,8):
   value=sum(factorial(q)//factorial(q-m)*comb(n-1,m-1) for m in range(1,min(q,n)+1))
   actual=0
   for w in product(range(q),repeat=n):
    runs=[]
    for a in w:
     if not runs or a!=runs[-1]:runs.append(a)
    if len(set(runs))==len(runs):actual+=1
   assert actual==value,(q,n,actual,value)
   checked+=1
 return checked

if __name__=='__main__':
 print('Alphabet count cases:',count_audit())
