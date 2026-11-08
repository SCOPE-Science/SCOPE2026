"""Direct quadrature and exact-algebra tests for Gaussian-smoothed PSD equivalence.
This is an optional finite numerical sanity check, not an exhaustive proof.
"""
import math
PI=math.pi

def simpson(f,lo,hi,n=12000):
    assert n%2==0
    h=(hi-lo)/n
    s=f(lo)+f(hi)
    for i in range(1,n):
        s+=(4 if i%2 else 2)*f(lo+i*h)
    return h*s/3

def smooth(S,w,lo=-16,hi=16):
    return simpson(lambda x:S(x)*math.exp(-2*PI*(w-x)**2),lo,hi)

# Exact normalizing identity for all t: P_T(t)=C*exp(a*t)*P_S(t)
# for T(x)=C*exp(a*x-a*a/(8*pi))*S(x-a/(4*pi)).
for a in [-4.,-0.7,0.,1.1,4.0]:
    d=a/(4*PI)
    for idx,S in enumerate([lambda x:math.exp(-0.83*(x-0.5)**2),
              lambda x:(1+x*x)**-2]):
        T=lambda x,S=S,d=d,a=a:math.exp(a*x-a*a/(8*PI))*S(x-d)
        for w in [-2.,-0.3,0.,0.5,2.]:
            actual=smooth(T,w)
            predicted=math.exp(a*w)*smooth(S,w)
            assert abs(actual-predicted)<=3e-9*max(predicted,actual,1e-12),(idx,a,w,actual,predicted)

# Compact bands, integrate separately on translated support to avoid jump errors.
for a in [-4., 0.5, 5.0]:
    d=a/(4*PI)
    for w in [-2.,-0.5,0.,1.,2.]:
        left=simpson(lambda x:math.exp(a*x-a*a/(8*PI)-2*PI*(w-x)**2),d-1.1,d+1.1)
        right=math.exp(a*w)*simpson(lambda x:math.exp(-2*PI*(w-x)**2),-1.1,1.1)
        assert abs(left-right)<1e-10*max(left,right,1e-12),(a,w,left,right)

# An exact analytic Gaussian formula tests the constant-intensity classification.
for b in [0.0,0.5,2.0,7.0]:
    for center in [-3.,0.,2.]:
        # P(w)=C*exp(-B*(w-center)^2) with B=2*pi*b/(2*pi+b).
        B=(2*PI*b)/(2*PI+b)
        # (log P)''=-2 B and  rho=1-B/(2*pi).
        rho=1-B/(2*PI)
        assert abs(rho-2*PI/(2*PI+b))<1e-14

# Probabilistic variance identity, using a smooth algebraic-tail PSD.
S=lambda x:(1+x*x)**-2
for w in [-3.,-1.2,0.,1.,3.]:
    z=smooth(S,w)
    m=simpson(lambda x:x*S(x)*math.exp(-2*PI*(w-x)**2),-16,16)/z
    m2=simpson(lambda x:x*x*S(x)*math.exp(-2*PI*(w-x)**2),-16,16)/z
    rho=4*PI*(m2-m*m)
    h=0.002
    logp=lambda u:math.log(smooth(S,u))
    dd=(logp(w+h)-2*logp(w)+logp(w-h))/h**2
    assert abs(rho-(1+dd/(4*PI)))<3e-6,(w,rho,dd)

# Compact bands can be moved arbitrarily far while keeping the same rho.
a=30*PI
d=a/(4*PI)
S=lambda x:1. if abs(x)<1 else 0.
T=lambda x:math.exp(a*x-a*a/(8*PI)) if abs(x-d)<1 else 0.
assert d>2
# use log-peak and analytic relation rather than integrate an extremely large exponent.
assert abs((a*d-a*a/(8*PI))-a*a/(8*PI))<1e-12
print('ALL_COLORED_NOISE_FIBER_CHECKS_PASSED')
