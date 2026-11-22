from fractions import Fraction as Q
from math import factorial

def atan_bounds(x,n):
    s=sum(((-1)**k * x**(2*k+1))/Q(2*k+1) for k in range(n))
    term=((-1)**n*x**(2*n+1))/Q(2*n+1)
    return min(s,s+term),max(s,s+term)

a,b=atan_bounds(Q(1,5),18)
c,d=atan_bounds(Q(1,239),6)
PIL=16*a-4*d; PIU=16*b-4*c
SPL=Q(177245385,100000000); SPU=Q(177245386,100000000)
S2L=Q(141421356,100000000); S2U=Q(141421357,100000000)
assert SPL*SPL<PIL<PIU<SPU*SPU
assert S2L*S2L<2<S2U*S2U

def bounds_series(x, half=False):
    # alternating power series bounds, pair k=17 negative, k=18 positive
    def s(n): return sum(Q((-1)**k)*x**(2*k+1)/Q(2**k if half else 1)/Q(factorial(k)*(2*k+1)) for k in range(n+1))
    return s(17),s(18)

def erf_bounds(x,half=False):
    lo,hi=bounds_series(x,half)
    faclo=(S2L if half else 2)/SPU
    fachi=(S2U if half else 2)/SPL
    return faclo*lo,fachi*hi

def deriv_bounds(x):
    E0,E1=erf_bounds(x)
    H0,H1=erf_bounds(x,True)
    return 1-2*E1+H0,1-2*E0+H1

def exp_bounds(z):
    def s(n):return sum(((-z)**k)/Q(factorial(k)) for k in range(n+1))
    return s(19),s(20)

def leaf1_bounds():
    dl,du=deriv_bounds(Q(1))
    el,eu=exp_bounds(Q(1))
    hl,hu=exp_bounds(Q(1,2))
    # L(1)=deriv(1) + (2/sqrt pi)(1-exp(-1)) - (sqrt2/sqrt pi)(1-exp(-1/2))
    return dl+Q(2)/SPU*(1-eu)-S2U/SPL*(1-hl), du+Q(2)/SPL*(1-el)-S2L/SPU*(1-hu)

l99,u99=deriv_bounds(Q(99,100));l1,u1=deriv_bounds(Q(1));v0,v1=leaf1_bounds()
CLOW=(2-S2U)/SPU; CHIGH=(2-S2L)/SPL
print('deriv.99 bounds',float(l99),float(u99));print('deriv1 bounds',float(l1),float(u1));print('leaf1 bounds',float(v0),float(v1));print('Linf bounds',float(CLOW),float(CHIGH))
assert l99>0 and u1<0 and v1<Q(2,5) and CLOW>Q(33,100)
print('PASS RATIONAL INTERVALS')

# Independent scalar eigenbasis expansion tests (finite sums are numerical, not proofs).
import math

def norm_nn(s,t,K):
    return sum(2/(math.pi*math.pi)*math.sin(math.pi*n*s)**2/n**2*(1-math.exp(-math.pi*math.pi*n*n*t))**2 for n in range(1,K+1))

def norm_dn(s,t,K):
    return sum(2/(math.pi*math.pi)*math.cos(math.pi*(n+.5)*s)**2/(n+.5)**2*(1-math.exp(-math.pi*math.pi*(n+.5)**2*t))**2 for n in range(K))

K=4000
for t in (0.001,0.01,0.08,0.3):
    n0=norm_nn(0,t,K)
    assert abs(n0)<1.e-20
    for m in (3,4,8):
        hub=(1-1/m)*norm_dn(0,t,K)
        for s in (0.0,0.005,0.025,0.1,0.3,0.5,0.8,0.95,1.0):
            v=norm_nn(s,t,K)/m+(1-1/m)*norm_dn(s,t,K)
            assert v <= hub+1.e-10, (m,s,t,v,hub)
    # Exact reflection normalization of source Dirichlet eigenfunction coefficients at t=infinity.
assert abs(2/math.pi**2*sum((n+.5)**-2 for n in range(25000))-1)<1.e-5
# Leading profile verified numerically with Gaussian formula (not a rate certificate).
Linf=(2-math.sqrt(2))/math.sqrt(math.pi)
for m in (3,4,10):
    assert (2*(1-1/m)*Linf)>(.44-1.e-13)
print('PASS spectral tests and branching profile checks')
# Verify the mixed-boundary image identity against the separated eigenbasis.
for t in (.01,.1,.3):
    def g(v): return math.exp(-v*v/(4*t))/math.sqrt(4*math.pi*t)
    for x,y in ((.2,.8),(.9,.9),(.2,.3)):
        image=sum((-1)**k*(g(x-y+2*k)-g(x+y+2*k)) for k in range(-12,13))
        eigen=sum(2*math.sin((n+.5)*math.pi*x)*math.sin((n+.5)*math.pi*y)*math.exp(-math.pi**2*(n+.5)**2*t) for n in range(200))
        assert abs(image-eigen)<2.e-12
print('PASS mixed-boundary image/kernel identity tests')
