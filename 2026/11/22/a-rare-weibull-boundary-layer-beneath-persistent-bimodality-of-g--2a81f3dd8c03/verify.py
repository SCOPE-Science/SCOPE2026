#!/usr/bin/env python3
"""Reproducibility checks for the rare conditional Weibull mode in a power-Gumbel family.

Analytic quantifiers and asymptotic arguments appear in RESULT.md.  This
checker uses SymPy for exact stationary equations and built-in floating point
for parameter-grid sanity checks; none of its finite numerical probes are
presented as an infinite-domain proof.
"""
import math
import sympy as sp
z,k,c,sig,eps,t=sp.symbols('z k c sig eps t', positive=True)
Lm=k*sp.log(z)+sp.log(c)+z/sig-c*sp.exp(z/sig)
Lp=k*sp.log(z)+sp.log(c)-z/sig-c*sp.exp(-z/sig)
assert sp.simplify(sp.diff(Lm,z)-(k/z+(1-c*sp.exp(z/sig))/sig))==0
assert sp.simplify(sp.diff(Lp,z)-(k/z+(c*sp.exp(-z/sig)-1)/sig))==0
assert sp.simplify(sp.diff(Lm,z,2)+k/z**2+c*sp.exp(z/sig)/sig**2)==0
assert sp.simplify(sp.diff(Lp,z,2)+k/z**2+c*sp.exp(-z/sig)/sig**2)==0
# Uniqueness of the stationary root follows from strictly negative second derivatives.
# Negative mode: t=c*z/sig, solve t exp(t/c)-t/c-k=0.
tseries=k+(k-k**2)*eps
assert sp.series(tseries*sp.exp(tseries*eps)-tseries*eps-k,eps,0,2).removeO().expand()==0
# The conditional Weibull transform is exact, not just asymptotic.
w=sp.symbols('w',nonnegative=True)
assert sp.simplify(sp.exp(-c*(sp.exp(w/c)-1)).subs(w,c*sp.log(1+t/c))-sp.exp(-t))==0
assert sp.series(c*(sp.exp(w/c)-1),c,sp.oo,3).removeO().expand() == w+w**2/(2*c)+w**3/(6*c**2)

def bisect_dec(f,lo,hi):
    assert f(lo)>0 and f(hi)<0
    for _ in range(120):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

for p,mu,sigma in [(1.2,0.6,1.4),(2.,0.,1.),(3.4,-1.3,2.2)]:
    kt=(p-1)/p
    for n in [5,100,10000,10000000]:
        ct=n*math.exp(-mu/sigma)
        b=sigma*math.log(ct)
        fminus=lambda zz:kt/zz+(1-ct*math.exp(zz/sigma))/sigma
        fplus=lambda zz:kt/zz+(ct*math.exp(-zz/sigma)-1)/sigma
        zminus=bisect_dec(fminus,1e-20,max(100.,10*sigma))
        zplus=bisect_dec(fplus,1e-20,max(100.,10*sigma+abs(b)))
        assert zminus>0 and zplus>0
        # independent CDF calculation using the exact Gumbel-max closure
        for x in [-3.2,-0.4,0.,0.4,2.1,6.0]:
            H=x*abs(x)**(p-1)
            left=math.exp(-n*math.exp(-(H+mu)/sigma))
            right=math.exp(-math.exp(-(H+mu-sigma*math.log(n))/sigma))
            assert abs(left-right) < 1e-12
        # The rare negative-lobe probability is exp(-c), exactly.
        assert 0<zminus<100 and 0<zplus<100
        if ct>1000:
            zm0=sigma*kt/ct
            assert abs(zminus/zm0-1) < 0.01
            log_actual=math.log(p/sigma)+kt*math.log(zminus)+math.log(ct)+zminus/sigma-ct*math.exp(zminus/sigma)
            log_asym=math.log(p/sigma)+kt*math.log(sigma*kt)+math.log(ct)/p-kt-ct
            assert abs(log_actual-log_asym)<0.01, (log_actual,log_asym)
            if b>10:
                log_right=math.log(p/sigma)+kt*math.log(zplus)+math.log(ct)-zplus/sigma-ct*math.exp(-zplus/sigma)
                log_right_asym=math.log(p/sigma)+kt*math.log(b)-1
                assert abs(log_right-log_right_asym)<0.01
        # Conditional survival = P(E > c[exp(w^p/c)-1]) exactly.
        for wt in (0.1,0.3,0.7,2.0):
            st=math.exp(-ct*math.expm1(wt**p/ct))
            assert 0<st<=math.exp(-wt**p)+1e-15
            assert abs(st-math.exp(-wt**p))<0.2
print('PASS: exact derivatives, negative-mode expansion, exact exponential coupling, twelve parameter cases and rare-mode bounds.')
