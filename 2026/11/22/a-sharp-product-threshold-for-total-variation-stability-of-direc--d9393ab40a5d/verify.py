"""Exact arithmetic checks for directed three-site range-weighted averages."""
from fractions import Fraction as F
from random import Random

def affinity(d):
    return F(1, 1) / (1 + d*d)

def coefficients(x,a,b):
    n=len(x)
    xx=[x[0],*x,x[-1]]
    left=[];right=[]
    for i in range(n):
        wl=a*affinity(xx[i+1]-xx[i]);wr=b*affinity(xx[i+2]-xx[i+1])
        den=1+wl+wr
        left.append(wl/den);right.append(wr/den)
    return left,right

def filt(x,a,b):
    l,r=coefficients(x,a,b)
    d=[x[i+1]-x[i] for i in range(len(x)-1)]
    return [x[i]-(l[i]*d[i-1] if i else 0)+(r[i]*d[i] if i<len(d) else 0) for i in range(len(x))]

def tv(x):return sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))

def deficit(x,a,b):
    l,r=coefficients(x,a,b); d=[x[i+1]-x[i] for i in range(len(x)-1)]; n=len(x)
    assert all(1-r[i]-l[i+1]>=0 for i in range(n-1))
    P=[];N=[]
    for i in range(n-1):
        terms=[]
        if i:terms.append(l[i]*d[i-1])
        terms.append((1-r[i]-l[i+1])*d[i])
        if i+1<len(d):terms.append(r[i+1]*d[i+1])
        P.append(sum(max(t,0) for t in terms))
        N.append(sum(max(-t,0) for t in terms))
    return r[0]*abs(d[0])+l[-1]*abs(d[-1])+2*sum(min(p,m) for p,m in zip(P,N))

rng=Random(92001)
for a,b in [(F(1),F(1)),(F(3),F(1,4)),(F(1,10),F(10)),(F(2,3),F(3,2)),(F(1,5),F(3))]:
    for n in range(2,17):
        for _ in range(80):
            x=[F(rng.randrange(-30,31),rng.randrange(1,13)) for i in range(n)]
            output=filt(x,a,b)
            assert tv(output)<=tv(x)
            assert tv(x)-tv(output)==deficit(x,a,b)
print('EXACT_RATIONAL_VARIATION_CONTRACTION_AND_DISSIPATION_PASS 6000')
for a,b in [(F(2),F(1)),(F(3),F(1)),(F(3),F(1,2)),(F(11,10),F(1)),(F(1,10),F(20))]:
    assert a*b>1
    q=F(1,20)
    for L in [10000,100000]:
        x=[-F(L),-F(L),F(0),q,F(L)+q,F(L)+q]
        f=filt(x,a,b)
        if f[3]<f[2]:break
    else: raise AssertionError((a,b))
    assert tv(f)>tv(x)
print('EXACT_RATIONAL_SHARP_PRODUCT_COUNTEREXAMPLES_PASS')
for a,b in [(F(1),F(1)),(F(1,10),F(10)),(F(3),F(1,4))]:
    for n in range(4,15):
        x=[F(0),F(0)]+[F(1)]*(n-2)
        assert tv(filt(x,a,b))==tv(x)==1
print('EXACT_SHARP_UNIT_VARIATION_GAIN_PASS')
print('ALL_DIRECTED_BILATERAL_BV_CHECKS_PASS')
