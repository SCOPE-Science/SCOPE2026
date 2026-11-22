"""Independent exhaustive check of one-point type polynomial for cyclic co-crowns."""
from collections import Counter
from math import comb

def poly_add(a,b,sgn=1):
 c=a.copy()
 for k,v in b.items():c[k]=c.get(k,0)+sgn*v
 return Counter({k:v for k,v in c.items() if v})
def mult(a,b):
 c=Counter()
 for (i,j),v in a.items():
  for (k,l),w in b.items():c[(i+k,j+l)]+=v*w
 return c

def formula(n):
 one=Counter({(0,0):1,(1,0):1,(0,1):1})
 t0=Counter({(0,0):2});t1=one
 for _ in range(2,n+1):
  t0,t1=t1,poly_add(mult(one,t1),mult(Counter({(1,1):1}),t0),-1)
 tr=t1
 p=tr.copy()
 # x^n*((1+x)^n-1), and y analogue
 for k in range(1,n+1):
  p[(n+k,0)]+=comb(n,k);p[(0,n+k)]+=comb(n,k)
 for i in range(2):
  for e,m in [(n-1,1),(n,2),(n+1,1)]:p[((e,0) if i==0 else (0,e))]+=n*m
 return Counter(p)

def direct(n):
 N=2*n
 reqA=[sum(1<<i for i in range(n) if j not in (i,(i+1)%n)) for j in range(n)]
 reqB=[sum(1<<j for j in range(n) if j not in (i,(i+1)%n)) for i in range(n)]
 z=Counter()
 # State A: 0 incomparable; 1 below new; 2 above new. B similarly.
 for a in range(3**n):
  q=a;L=U=0
  for i in range(n):
   digit=q%3;q//=3
   if digit==1:L|=1<<i
   if digit==2:U|=1<<i
  for b in range(3**n):
   q=b;LB=UB=0
   for j in range(n):
    digit=q%3;q//=3
    if digit==1:LB|=1<<j
    if digit==2:UB|=1<<j
   if any((reqA[j]&L)!=reqA[j] for j in range(n) if LB>>j&1):continue
   if any((reqB[i]&UB)!=reqB[i] for i in range(n) if U>>i&1):continue
   if L or LB:
    if U or UB:
     if LB or U:continue
     if any((reqB[i]&UB)!=UB for i in range(n) if L>>i&1):continue
   z[(L.bit_count()+LB.bit_count(),U.bit_count()+UB.bit_count())]+=1
 return z

def lucas(m):
 a,b=2,1
 for _ in range(m):a,b=b,a+b
 return a

for n in range(3,7):
 f=formula(n);d=direct(n)
 assert f==d, (n,(f-d),(d-f))
 assert sum(f.values()) == lucas(2*n)+2**(n+1)+8*n-2
 print(f'n={n}: {sum(f.values())} types, {len(f)} bidegrees; exhaustive comparison OK',flush=True)
print('VERIFY_OK')
