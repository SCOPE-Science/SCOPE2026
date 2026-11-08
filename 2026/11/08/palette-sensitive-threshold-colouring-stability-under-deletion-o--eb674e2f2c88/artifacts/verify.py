from itertools import product, combinations
from math import factorial

def threshold(g, subset):
 for v in combinations(subset,4):
  ed=sum((min(a,b),max(a,b)) in g for a,b in combinations(v,2))
  ds=[sum((min(a,b),max(a,b)) in g for b in v if b!=a) for a in v]
  if (ed,tuple(sorted(ds))) in [(2,(1,1,1,1)),(3,(1,1,2,2)),(4,(2,2,2,2))]: return False
 return True

def brute(m,n,d,q):
 g={(i,m+j) for i in range(m) for j in range(n) if i!=0 or j>=d}
 return sum(all(threshold(g,[i for i in range(m+n) if col[i]==j]) for j in range(q)) for col in product(range(q),repeat=m+n))

def predicted(m,n,d,q):
 import math
 from collections import defaultdict
 F={(a,b,c):1/math.factorial(a)/math.factorial(b)/math.factorial(c) for a in range(m) for b in range(d+1) for c in range(n-d+1) if min(a,b+c)<=1}
 H={(a,b,c):1/math.factorial(a)/math.factorial(b)/math.factorial(c) for a in range(m) for b in range(d+1) for c in range(n-d+1) if a==0 or b+c<=1 or (a==1 and c==0)}
 D={(0,0,0):1.0}
 for _ in range(q-1):
  DD=defaultdict(float)
  for (a,b,c),u in D.items():
   for (aa,bb,cc),v in F.items():
    if a+aa<m and b+bb<=d and c+cc<=n-d: DD[(a+aa,b+bb,c+cc)]+=u*v
  D=DD
 t=sum(u*H.get((m-1-a,d-b,n-d-c),0) for (a,b,c),u in D.items())
 return round(q*math.factorial(m-1)*math.factorial(d)*math.factorial(n-d)*t)
for m in range(2,5):
 for n in range(2,5):
  for d in range(0,n+1):
   for q in (1,2,3):
    if q**(m+n)>20000:continue
    b=brute(m,n,d,q);p=predicted(m,n,d,q)
    assert b==p,(m,n,d,q,b,p)
print('VERIFY_OK')
