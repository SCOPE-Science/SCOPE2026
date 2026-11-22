"""Exact-rational checks for finite-sample null coupling of two GOF tests.
Requires Python 3 standard library only. The code is supplementary, not an infinite-proof substitute.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import random, math

def poly(*coeff): return {i:F(c) for i,c in enumerate(coeff) if c}
def add(a,b):
    out=defaultdict(F,a)
    for i,c in b.items():out[i]+=c
    return {k:v for k,v in out.items() if v}
def mul(a,b):
    out=defaultdict(F)
    for i,c in a.items():
        for j,d in b.items():out[i+j]+=c*d
    return dict(out)
def scale(a,c):return {i:v*F(c) for i,v in a.items()}
def mean(a):return sum((v/F(i+1) for i,v in a.items()), F(0))
def sq(a):return mul(a,a)
def cov(a,b):return mean(mul(a,b))-mean(a)*mean(b)

def badd(a,b):
    out=defaultdict(F,a)
    for key,v in b.items():out[key]+=v
    return {k:v for k,v in out.items() if v}
def bmul(a,b):
    out=defaultdict(F)
    for (i,j),c in a.items():
        for (k,l),d in b.items():out[(i+k,j+l)]+=c*d
    return dict(out)
def bscale(a,c):return {k:v*F(c) for k,v in a.items()}
def triangular_int(a,upper=False):
    total=F(0)
    for (i,j),v in a.items():
        lo=F(1,(j+1)*(i+j+2))
        total += v*(F(1,(i+1)*(j+1))-lo if upper else lo)
    return total

assertions=0
def eq(a,b,label):
    global assertions
    assertions+=1
    assert a==b, (label,a,b)

u=poly(0,1); one=poly(1); half=F(1,2)
aT=scale(poly(1,30,-90,40,40),F(1,30))
aW=poly(F(1,3),-1,1)
aM=sq(add(u,poly(-half)))
eq(aT,poly(F(1,30),1,-3,F(4,3),F(4,3)),"aT")
eq(add(aW,scale(aM,-1)),poly(F(1,12)),"Watson constant diagonal")
eq(mean(aT),F(2,15),"T expectation")
eq(mean(aW),F(1,6),"CvM expectation")
eq(mean(aM),F(1,12),"M expectation")
eq(cov(aT,aT),F(169,8100),"T diagonal variance")
eq(cov(aW,aW),F(1,180),"CvM diagonal variance")
eq(cov(aT,aW),F(1,140),"T-CvM diagonal covariance")
eq(cov(aT,aM),F(1,140),"T-M diagonal covariance")

# C(s,t) = E[g_s(U) h_t(U)], t<=s (LOWER), t>s (UPPER).
s={(1,0):F(1)};t={(0,1):F(1)};I={(0,0):F(1)}
cLOW=badd(bmul(s,t),bscale(bmul(bmul(s,s),t),-1))
cUP=bmul(badd(I,bscale(t,-1)),badd(badd(t,bscale(s,-1)),bmul(s,s)))
offTW=triangular_int(bmul(cLOW,cLOW))+triangular_int(bmul(cUP,cUP),upper=True)
eq(offTW,F(13,1260),"T-CvM off diagonal")

# Mixed T-mean Fourier component, m(s)=E[g_s(U)(U-1/2)].
x=add(u,poly(-half))
m=add(poly(F(1,12)),scale(mul(mul(x,x),x),F(-2,3)))
eq(mean(sq(m)),F(1,126),"T-M off diagonal")
eq(offTW-mean(sq(m)),F(1,420),"T-Watson off diagonal")

# Null covariance of g_s/g_t, t <= s. Triangle integration doubled by symmetry.
# E[(2U-1)^2 1(U>=s)] - s(1-s)t(1-t)
gvar=badd(badd({(0,0):F(1,3)}, {(3,0):F(-4,3),(2,0):F(2),(1,0):F(-1)}), bscale(bmul(bmul(s,badd(I,bscale(s,-1))),bmul(t,badd(I,bscale(t,-1)))),-1))
offTT=2*triangular_int(bmul(gvar,gvar))
eq(offTT,F(109,8100),"T kernel off diagonal")
# Classical brownian bridge kernel t*(1-s), when t<=s.
kw=bmul(t,badd(I,bscale(s,-1)))
offWW=2*triangular_int(bmul(kw,kw))
eq(offWW,F(1,90),"CvM off diagonal")
# E[h_s(U)(U-1/2)] = s(1-s)/2.
hm=scale(mul(u,add(one,scale(u,-1))),F(1,2))
offWM=mean(sq(hm));offMM=F(1,12)**2
eq(offWM,F(1,120),"CvM-M off diagonal")
eq(offWW-2*offWM+offMM,F(1,720),"Watson off diagonal")

for n in range(1,1001):
    vT=cov(aT,aT)/n + 2*F(n-1,n)*offTT
    vW=cov(aW,aW)/n + 2*F(n-1,n)*offWW
    vV=2*F(n-1,n)*(offWW-2*offWM+offMM)
    cTW=cov(aT,aW)/n + 2*F(n-1,n)*offTW
    cTM=cov(aT,aM)/n + 2*F(n-1,n)*mean(sq(m))
    cTV=cTW-cTM
    eq(vT,F(218*n-49,8100*n),"Var T")
    eq(vW,F(4*n-3,180*n),"Var CvM")
    eq(vV,F(n-1,360*n),"Var Watson")
    eq(cTW,F(26*n-17,1260*n),"Cov T,CvM")
    eq(cTM,F(20*n-11,1260*n),"Cov T,M")
    eq(cTV,F(n-1,210*n),"Cov T,Watson")

# Numerically evaluate independent defining integral via exact piecewise polynomial antiderivatives.
def num_stat(arr):
    n=len(arr)
    x=sorted(arr)
    pts=[0.0]+x+[1.0]
    T=W=0.0
    for j,(lo,hi) in enumerate(zip(pts[:-1],pts[1:])):
        a=sum(2*val-1 for val in x[j:])/n
        b=(n-j)/n
        # gbar(t) = a-t+t^2, hbar(t)=b-1+t
        T+=(a*a*(hi-lo)-a*(hi**2-lo**2)+((1+2*a)/3)*(hi**3-lo**3)-.5*(hi**4-lo**4)+.2*(hi**5-lo**5))
        W+=((b-1)**2*(hi-lo)+(b-1)*(hi**2-lo**2)+(hi**3-lo**3)/3)
    M=(sum(arr)/n-.5)**2
    return n*T,n*W,n*(W-M)

def original_T(arr):
    n=len(arr)
    return (sum((2*a-1)*(2*b-1)*min(a,b) for a in arr for b in arr)/n
           -sum((2*a-1)*a*a*(3-2*a) for a in arr)/3+n/30)

def original_W(arr):
    n=len(arr)
    return 1/(12*n)+sum((v-(2*j-1)/(2*n))**2 for j,v in enumerate(sorted(arr),1))

rng=random.Random(17117)
for n in [1,2,3,4,7,11]:
    for _ in range(250):
        arr=[rng.random() for i in range(n)]
        t,w,v=num_stat(arr)
        assertions+=3
        assert abs(t-original_T(arr))<5e-13
        assert abs(w-original_W(arr))<5e-13
        assert abs(v-(w-n*(sum(arr)/n-.5)**2))<5e-13

# The two squared-correlation functions are strictly increasing on integer n>=2;
# positivity follows from the explicit derivative numerator factors in the proof.
for n in range(2,1000):
    def rc(k):
        a=F(45,49)*F((26*k-17)**2,(4*k-3)*(218*k-49))
        b=F(3240,49)*F(k-1,218*k-49)
        return a,b
    a,b=rc(n); ap,bp=rc(n+1)
    assertions+=3
    assert 0<b<a<1
    assert a<ap and b<bp
    assert F(20*n-11,26*n-17)>F(10,13)
print('PASS', assertions, 'checks', 'offTW',offTW,'offTT',offTT,'offWW',offWW)
