"""Numerical and exact-arithmetic checks for heteroscedastic SGD schedules.
Run: python3 check.py (Python standard library only).
"""
import math, random
from fractions import Fraction
rng = random.Random(20261105)

def huber(z,a,L):
    return L*z*z/2 if abs(z) <= a else L*(a*abs(z)-a*a/2)

def dhuber(z,a,L):
    return L*min(a,max(-a,z))

def phi(h,variances,L,D):
    N=len(h); t=[1+2*sum(h[i:]) for i in range(N)]+[1]
    return L*D*D/(2*t[0])+sum(variances[i]*h[i]*h[i]/(2*L*t[i+1]) for i in range(N))

def witness(h,variances,L,D,signs):
    N=len(h); t=[1+2*sum(h[i:]) for i in range(N)]+[1]
    a=[D/t[0]]+[math.sqrt(variances[i])*h[i]/(L*t[i+1]) for i in range(N)]
    x=[D]+[0.]*N
    for i in range(N):
        grads=[dhuber(xj,aj,L) for xj,aj in zip(x,a)]
        x=[xj-h[i]*gj/L for xj,gj in zip(x,grads)]
        x[i+1]-=h[i]*math.sqrt(variances[i])*signs[i]/L
    return sum(huber(xj,aj,L) for xj,aj in zip(x,a))

def opt(variances,L,D):
    N=len(variances)
    def build(c0):
        cs=[c0]
        for i in range(1,N):
            v=variances[i-1]/variances[i]*cs[-1]*(1+cs[-1])
            if not math.isfinite(v):return None,None
            cs.append(v)
        p=1.
        for c in cs:
            p*=1+2*c
            if not math.isfinite(p):return None,None
        return cs, variances[0]*c0*p*p
    lo,hi=0.,1.
    while True:
        cs,v=build(hi)
        if v is None or v>=L*L*D*D:break
        hi*=2
    for _ in range(150):
        mid=(lo+hi)/2
        _,v=build(mid)
        if v is None or v>L*L*D*D:hi=mid
        else:lo=mid
    cs,_=build((lo+hi)/2)
    tail=1.;h=[0.]*N
    for i in reversed(range(N)):
        h[i]=cs[i]*tail; tail*=1+2*cs[i]
    return h,cs

def checkclose(a,b,rtol=5e-11):
    assert abs(a-b)<rtol*max(1.,abs(a),abs(b)),(a,b)

checks=0
# Exact rational step-size reversal witness, without floating approximations.
c0=Fraction(1,10); c1=Fraction(11,25)
t0=(1+2*c0)*(1+2*c1)
v0=1/(c0*t0*t0); v1=v0/4
h0=c0*(1+2*c1); h1=c1
assert c1==4*c0*(1+c0)
assert (h0,h1)==(Fraction(47,250),Fraction(11,25))
assert v0==Fraction(78125,39762)
assert v1==Fraction(78125,159048)
assert h0<h1<Fraction(3,2)
checks+=7
ho,co=opt([float(v0),float(v1)],1,1)
checkclose(ho[0],float(h0)); checkclose(ho[1],float(h1));checks+=2
# Verify exact source-style adversarial objective for random choices, all sign outcomes.
for rep in range(480):
    n=rng.randrange(1,8)
    L=10**rng.uniform(-1.,1.);D=10**rng.uniform(-1.,1.)
    variance=[10**rng.uniform(-2,2) for _ in range(n)]
    h=[rng.uniform(0,1.5) for _ in range(n)]
    signs=[rng.choice([-1,1]) for _ in range(n)]
    checkclose(witness(h,variance,L,D,signs),phi(h,variance,L,D))
    checks+=1
# Verify global optimal stationarity and local convex certificate.
for rep in range(375):
    n=rng.randrange(1,8)
    L=10**rng.uniform(-1.,1.);D=10**rng.uniform(-1.,1.)
    variance=[10**rng.uniform(-.8,1.2) for _ in range(n)]
    h,c=opt(variance,L,D)
    t=[1+2*sum(h[i:]) for i in range(n)]+[1.]
    checkclose(c[0]*variance[0]*t[0]**2,L*L*D*D)
    checks+=1
    for i in range(n-1):
        checkclose(variance[i+1]*c[i+1],variance[i]*c[i]*(1+c[i]))
        diff=h[i]-h[i+1]
        rhs=variance[i+1]/variance[i]-1+c[i]+2*c[i]*c[i]
        assert diff*rhs >= -1e-11*max(1,abs(diff),abs(rhs))
        checks+=2
    for j in range(n):
        step=1e-5*max(1,h[j]);hp=h.copy();hm=h.copy()
        hp[j]+=step;hm[j]=max(0,hm[j]-step)
        v=phi(h,variance,L,D)
        assert phi(hp,variance,L,D)>=v-5e-8*max(1,abs(v))
        assert phi(hm,variance,L,D)>=v-5e-8*max(1,abs(v))
        checks+=2
# Noise dominated limit: arbitrary ordering of inverse variances.
variances=[9,1,25,4,16,2]
for scale in [10**4,10**5,10**6]:
    hs,_=opt([scale*v for v in variances],1,1)
    for j,v in enumerate(variances):
        assert abs(scale*hs[j]*v-1)<.01
        checks+=1
print('PASS',checks,'checks; exact reversal h=(47/250,11/25), variances=(78125/39762,78125/159048)')
