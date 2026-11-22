"""Independent numerical checks for sharp BV-to-L1 Cesaro iteration defect."""
from math import exp, log, lgamma, factorial
from scipy.integrate import quad
import random
import mpmath as mp


def candidate(m):
    r=exp(lgamma(m+1)/m)
    return r, exp(-r)*sum(r**k/factorial(k) for k in range(1,m+1))


def single_jump_defect(m,s,x):
    if x<=s:
        return 0.0
    u=log(x/s)
    return (s/x)*sum(u**k/factorial(k) for k in range(m))


def single_jump_norm(m,s):
    return quad(lambda x: single_jump_defect(m,s,x), s, 1,epsabs=1e-11,epsrel=1e-11)[0]

nchecks=0
for m in range(1,13):
    r,c=candidate(m)
    s=exp(-r)
    val=single_jump_norm(m,s)
    assert abs(val-c)<3e-11,(m,val,c)
    for offset in (-0.75,-0.4,-0.1,0.1,0.4,0.75):
        u=r+offset
        if u<=0:continue
        test=single_jump_norm(m,exp(-u))
        assert test<c-1e-6,(m,u,test,c)
        nchecks+=1
    nchecks+=1
print('INDEPENDENT_SINGLE_JUMP_QUADRATURE_CHECKS_PASS',nchecks)

rng=random.Random(42)
nchecks=0
for m in range(1,9):
    _,c=candidate(m)
    for _ in range(120):
        steps=sorted([rng.uniform(0.005,0.995) for _ in range(6)])
        weights=[rng.uniform(-1,1) for _ in steps]
        # Build defect by linearity, independently integrate its absolute value.
        absval=quad(lambda x:abs(sum(w*single_jump_defect(m,s,x) for w,s in zip(weights,steps))),0,1,
                    points=steps,epsabs=1e-10,epsrel=1e-10)[0]
        assert absval <= c*sum(abs(w) for w in weights)+2e-9,(m,absval,c)
        nchecks+=1
print('SIGNED_MULTIJUMP_NUMERICAL_BOUNDS_PASS',nchecks)

mp.mp.dps=80
nchecks=0
for m in (40,80,160,320,640):
    r=mp.exp(mp.loggamma(m+1)/m)
    # deficiency 1-C = exp(-r) [1+tail sum r^k/k!].
    term=mp.mpf(1)
    tail=mp.mpf(0)
    for k in range(m+1,m+250):
        term*=r/k
        tail+=term
    defect=mp.exp(-r)*(1+tail)
    leading=(mp.e/(mp.e-1))*(2*mp.pi*m)**(-1/(2*mp.e))*mp.exp(-m/mp.e)
    ratio=float(defect/leading)
    assert 0.5<ratio<1.5,(m,ratio)
    print('ASYMPTOTIC_CHECK',m,'ratio',round(ratio,6))
    nchecks+=1
print('ASYMPTOTIC_SANITY_CHECKS_PASS',nchecks)
print('ALL_CESARO_BV_L1_CHECKS_PASS')
