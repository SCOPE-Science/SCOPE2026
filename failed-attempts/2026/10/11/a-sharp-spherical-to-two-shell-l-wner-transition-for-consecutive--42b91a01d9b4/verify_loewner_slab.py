"""Reproducible finite algebra/geometry checks for cardinality-slab ellipsoids.
Run: python verify_loewner_slab.py   (Python standard library only).
The proof in RESULT.md applies to all integer parameters; these checks do not prove it.
"""
from math import comb, sqrt, isclose

def prediction(n,a,b):
    D=(n/2-a)*(b-n/2)
    if 4*D>=n:
        return n/2,n/4,n*(n-1)/4,list(range(a,b+1)),True
    h=b-a; A0=a*(n-a); Delta=b*(n-b)-A0
    if Delta==0: p=.5
    else:
        B=n*Delta-2*A0
        p=(B+sqrt(B*B+4*(n+1)*Delta*A0))/(2*(n+1)*Delta)
    return a+p*h,p*(1-p)*h*h,A0+p*Delta,[a,b],False

count=0
for n in range(2,55):
    for a in range(n):
        for b in range(a+1,n+1):
            mu,V,R,contacts,sphere=prediction(n,a,b)
            assert V>0 and R>0,(n,a,b,mu,V,R)
            s=[(k-mu)**2/V+(n-1)*k*(n-k)/R for k in range(a,b+1)]
            assert max(s)<=n+1e-7,(n,a,b,s)
            assert abs(s[0]-n)<1e-7 and abs(s[-1]-n)<1e-7,(n,a,b,s)
            if sphere:
                assert max(abs(x-n) for x in s)<1e-7,(n,a,b,s)
                assert abs(mu-n/2)<1e-7
            elif b-a>1:
                assert max(s[1:-1])<n-1e-7,(n,a,b,s)
            count+=1
# Representative exactly rational semiaxis checks at balanced slabs.
from fractions import Fraction
for n in range(2,55):
    for a in range((n+1)//2):
        b=n-a
        D=Fraction((n-2*a)**2,4)
        if D<Fraction(n,4):
            V=D; R=Fraction(n*n,4)-D
            assert R-(n-1)*V==n*(Fraction(n,4)-D)
print('PASS',count,'integer parameter triples (n=2..54), boundary/contact/semiaxis checks')
