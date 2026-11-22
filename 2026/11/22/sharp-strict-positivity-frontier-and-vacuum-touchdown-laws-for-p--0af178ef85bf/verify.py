"""Independent finite diagnostics for the power-entropy advection-flux theorem.
Run: python verify.py. These checks corroborate, not replace, the analytic proof.
"""
from fractions import Fraction as Q
from math import sqrt, log, atan, pi, isclose

checks = 0

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def flux(p, a, b):
    if a == b:
        return a
    if p == 0:
        return a*b*log(b/a)/(b-a)
    if p == 1:
        return (b-a)/log(b/a)
    return ((p-1)/p)*(b**p-a**p)/(b**(p-1)-a**(p-1))

# Exact-rational quadrature means in nondegenerate power cases.
for ia in range(1, 20):
    for ib in range(ia+1, 21):
        a, b = Q(ia), Q(ib)
        for p in [-2, -1, 2, 3, 4]:
            f = Q(p-1, p)*(b**p-a**p)/(b**(p-1)-a**(p-1))
            check(a < f < b, ('mean', p, a, b))
            # Entropy-chain identity: F (U'(b)-U'(a)) = psi(b)-psi(a).
            # For p != 0,1, U'=u^(p-1)/(p-1), psi=u^p/p.
            check(f*((b**(p-1)-a**(p-1))/Q(p-1)) ==
                  (b**p-a**p)/Q(p), ('entropy', p, a, b))
            check(f == (a+b)/2 if p == 2 else True, 'arithmetic')
            check(f == 2*a*b/(a+b) if p == -1 else True, 'harmonic')

# Geometric flux, exactly conjugated to a skew-centered linear ODE.
for i in range(1, 20):
    for j in range(1, 15):
        a, b = Q(i, 7), Q(j, 5)
        check(isclose(flux(.5,float(a*a),float(b*b)),float(a*b),rel_tol=1e-12), 'geometric')

# Exact three-cell angular solution and first root.
x = [0.1, 1.0, 2.0]
m = sum(x)/3.0
omega = sqrt(3)/2.0
a = (10*sqrt(3)-sqrt(123))/59
t = 4*atan(a)/sqrt(3)
def sol(i,t):
    import math
    return m + (x[i]-m)*math.cos(omega*t) + (x[(i+1)%3]-x[(i-1)%3])/sqrt(3)*math.sin(omega*t)
check(abs(sol(0,t)) < 5e-14, 'first root')
check(0<t<.3 and sol(1,t)>0 and sol(2,t)>0, 'positive neighbors')
R = sqrt(2*sum((z-m)**2 for z in x)/3)
check(m<R, 'threshold')
for i in range(3):
    for k in range(1, 100):
        s=k*t/100
        eps=1e-7
        d=(sol(i,s+eps)-sol(i,s-eps))/(2*eps)
        rhs=(sol((i+1)%3,s)-sol((i-1)%3,s))/2
        check(abs(d-rhs)<1e-8, 'linear ODE conjugacy')

# Boundary scaling: leading powers for every regime.
for p in [.25,.5,.75,1.,1.5,2.,4.]:
    a,b=1.,4.
    for epsilon in [1e-10,1e-12,1e-14]:
        dx=(flux(p,epsilon,a)-flux(p,epsilon,b))
        if p<1:
            limit=-(1-p)*(b**p-a**p)/p
            check(abs(dx/(epsilon**(1-p))/limit -1)<(.03 if p>.25 else .08), (p,epsilon,dx,limit))
        elif p==1:
            limit=-(b-a)
            check(abs(dx*log(1/epsilon)/limit -1)<.15,(p,epsilon))
        else:
            limit=-(p-1)*(b-a)/p
            check(abs(dx/limit-1)<.02,(p,epsilon))

print(f'PASS: {checks} finite diagnostics; first geometric touchdown t={t:.15f}')
