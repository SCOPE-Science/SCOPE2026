"""Independent finite checks of formulas for a fixed-origin wrapped count law.

Run with Python 3.9 or later: python3 verify_wpl_modes.py.
All rational checks use Fraction, not floating-point predicates.
Finite checks supplement rather than replace the all-parameter analytic proof.
"""
from fractions import Fraction as F
from math import comb, expm1, log1p, sqrt, isclose

checks = 0

def ck(condition, message):
    global checks
    checks += 1
    assert condition, message


def mass(m, t, r):
    # Closed wrapped mass derived by summing the linear-geometric parent.
    q = 1+t
    A = q**m-1
    return t*t*q**m*((r+t+2)*A + m)/(q**(r+3)*A*A)


def original(k,t):
    return t*t*(k+t+2)/(1+t)**(k+3)


def H(m,t):
    q=1+t
    return 1/t-t-2-F(m,1)/(q**m-1)


def P(m,r,t):
    # Sign of p_(r+1)-p_r equals sign of this polynomial numerator.
    return ((1-t*(r+2)-t*t)*((1+t)**m-1)-m*t)


for m in range(2,20):
    for t in (F(1,100),F(1,7),F(1,2),F(3,2),F(10,1)):
        v=[mass(m,t,r) for r in range(m)]
        ck(sum(v)==1,('normalization',m,t))
        for r in range(m-1):
            ck((v[r+1]>v[r])==(H(m,t)>r),('adjacent',m,t,r))
            ck((v[r+1]>v[r])==(P(m,r,t)>0),('polynomial',m,t,r))
            ck((v[r+1]/v[r]) == ((r+t+3)*((1+t)**m-1)+m)/((1+t)*((r+t+2)*((1+t)**m-1)+m)),('ratio',m,t,r))
        for r in range(1,m-1):
            ck(v[r]**2>v[r-1]*v[r+1],('strict interior log concavity',m,t,r))
        modes=[r for r,p in enumerate(v) if p==max(v)]
        h=H(m,t)
        predicted=max(0, min(m-1, -((-h.numerator)//h.denominator)))  # ceil exact
        # Only exact ties can make ceil rule ambiguous; tested t values avoid known ties.
        ck(modes == [predicted],('mode',m,t,modes,predicted))

for m in range(2,25):
    for j in (1,2,3,4,7,10):
        t=F(j,31)
        q=1+t
        S=sum(q**r for r in range(m))
        ck(S*S > m*m*q**(m-1),('AM-GM squared strict',m,t))
        deriv= -1/t**2-1 + F(m*m,1)*q**(m-1)/(q**m-1)**2
        ck(deriv < -1,('derivative bound',m,t))

# First non-origin mode occurs only for m>=6, and at m=6
# the polynomial boundary has an exact rational enclosure.
lo=F('0.13478761972309')
hi=F('0.13478761972311')
ck(P(6,0,lo)>0, 'critical lower bound')
ck(P(6,0,hi)<0, 'critical upper bound')
for m in range(2,6):
    for t in (F(1,1000),F(1,100),F(1,10),F(1,1)):
        ck(H(m,t)<0,('small-modulus root absence diagnostic',m,t))
for m in (6,7,8,9,10,13,20):
    R=max(0,(m-4)//2)
    ck(H(m,F(1,100000)) > R-1, ('small theta last mode',m))
    ck(H(m,F(20,1))<0,('large theta zero mode',m))

# Direct wrap sums: a computed finite partial sum should be below
# the exact probability, with a rapidly diminishing omitted tail.
for m,t in ((5,F(1,3)),(6,F(1,2)),(10,F(2,3))):
    for r in range(m):
        partial=sum((original(r+j*m,t) for j in range(200)),F(0,1))
        ck(partial<=mass(m,t,r),('partial sum must not exceed',m,t,r))
        ck(float(mass(m,t,r)-partial)<1e-24,('tail diagnostic',m,t,r))

# m grows: the 0-to-1 threshold increases to sqrt(2)-1,
# with a derived exponential first-order gap; this is a diagnostic.
limit=sqrt(2)-1
for m in (20,30,40):
    a,b=.1,limit
    for _ in range(90):
        mid=(a+b)/2
        hm=1/mid-mid-2 - m/expm1(m*log1p(mid))
        if hm>0:a=mid
        else:b=mid
    root=(a+b)/2
    ratio=(limit-root)/(m*2**(-m/2)/(4+2*sqrt(2)))
    ck(1<ratio<1.05,('asymptotic diagnostic',m,ratio))

print('CHECK_OK',checks)
