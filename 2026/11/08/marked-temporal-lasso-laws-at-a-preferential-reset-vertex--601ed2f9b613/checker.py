"""Finite exact checks for biased functional-frame orbit law.
Only finite identities are computationally checked; asymptotics require proof.
Run: python checker.py
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log1p, isclose

def falling(z,k):
    if k<0: raise ValueError
    r=1
    for j in range(k):r*=max(0,z-j)
    return r

def cells(n,p):
    a=p+(1-p)/n
    b=(1-p)/n
    out={}
    for t in range(1,n+1):
        base=falling(n-2,t-1)*b**t
        for j in range(t):
            if j==0:
                v=base+(t-1)*a*falling(n-2,t-2)*b**(t-1) if t>1 else base
            else:
                v=base+a*falling(n-2,t-2)*b**(t-2)*(a+(t-2)*b)
            out[(t,j)]=v
    return out

def orbit(f):
    seen={};cur=1;t=0
    while cur not in seen:
        seen[cur]=t;t+=1;cur=f[cur]
    return t,seen[cur],list(seen)

checks=0
for n in range(2,6):
    for p in (F(0),F(1,4),F(2,3)):
        w=[(p+(1-p)/n) if x==0 else (1-p)/n for x in range(n)]
        observed={k:F(0) for k in cells(n,p)}
        for f in product(range(n),repeat=n):
            prob=F(1)
            for v in f:prob*=w[v]
            t,j,_=orbit(f);observed[(t,j)]+=prob
        expected=cells(n,p)
        assert sum(observed.values())==1
        assert observed==expected,(n,p,observed,expected)
        checks+=len(observed)

# A separate enumeration of both transitions and valuations checks the
# bivariate probability generating formula for transient/cycle mark counts.
n=4;p=F(1,3);q=F(1,5);s=F(2,3);z=F(3,4)
weights=[p+(1-p)/n if i==0 else (1-p)/n for i in range(n)]
actual=F(0)
for f in product(range(n),repeat=n):
    w=F(1)
    for dest in f:w*=weights[dest]
    t,j,seq=orbit(f)
    for lab in product((0,1), repeat=n):
        v=F(1)
        for x in lab:v*=q if x else (1-q)
        aa=sum(lab[x] for x in seq[:j]);bb=sum(lab[x] for x in seq[j:])
        actual+=w*v*s**aa*z**bb
formula=sum(v*(1-q+q*s)**j*(1-q+q*z)**(t-j) for (t,j),v in cells(n,p).items())
assert actual==formula,(actual,formula)

# Numerically examine exact survival derived by no-hub/one-hub decomposition.
def surv(n,p,k):
    if k==0:return 1.
    if k>=n:return 0.
    b=(1-p)/n; a=p+b
    # avoid underflow for moderately large n
    v=1.
    for i in range(k): v*=(n-2-i)*b
    u=1.
    for i in range(k-1): u*=(n-2-i)*b
    return v+k*a*u

for n,a in [(2000,0),(2000,1),(5000,2)]:
    p=a/n**.5
    for r in (.5,1,2):
        k=round(r*n**.5)
        target=exp(-r*r/2-a*r)*(1+a*r)
        assert abs(surv(n,p,k)-target)<.04,(n,a,r,surv(n,p,k),target)

# Supercritical scale: p ->0 and p sqrt(n) ->infinity.
for n,p in [(10**8,.003),(10**9,.001)]:
    for r in (.5,1,2):
        k=round(r/p)
        target=exp(-r)*(1+r)
        assert abs(surv(n,p,k)-target)<.005,(n,p,r,surv(n,p,k),target)

print('BIASED_FUNCTIONAL_FRAME_ORBIT_CHECKS_OK exact_cells=',checks,
      'maps_and_valuations_checked=4096', 'critical_and_supercritical_survivals=verified')
