#!/usr/bin/env python3
"""Reproduce algebraic identities and numerical witness for a Hill-saturated encounter hazard.

Uses only Python's standard library. Numerical tests supplement, not replace, the analytical theorem.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt, isfinite

checks = 0

def test(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def h(x, a, p):
    z = x**p
    B = (p - 1) - (p + 1)*a
    return (-z*z + B*z - a)/(x*(z+a)*(z+1))

def hazard(x, a, p, b):
    return exp(-b*x)*(a+x**p)/(x*(1+x**p))

def golden_max(f, lo, hi, iters=220):
    gr = (sqrt(5)-1)/2
    x1, x2 = hi - gr*(hi-lo), lo + gr*(hi-lo)
    v1, v2 = f(x1), f(x2)
    for _ in range(iters):
        if v1 > v2:
            hi, x2, v2 = x2, x1, v1
            x1 = hi - gr*(hi-lo)
            v1 = f(x1)
        else:
            lo, x1, v1 = x1, x2, v2
            x2 = lo + gr*(hi-lo)
            v2 = f(x2)
    x = (lo+hi)/2
    return x,f(x)

def bisect_root(f, lo, hi, iters=100):
    flo, fhi = f(lo), f(hi)
    test(flo*fhi < 0, 'root bracket')
    for _ in range(iters):
        mid=(lo+hi)/2
        fm=f(mid)
        if flo*fm>0: lo,flo=mid,fm
        else: hi,fhi=mid,fm
    return (lo+hi)/2

# Exact rational derivative identity: d log(R)/dx + b = H(x), p an integer.
for p in range(1,9):
    for an in range(1,17):
        a=Q(an,17)
        for xn in range(1,26):
            x=Q(xn,19)
            z=x**p
            explicit = (p*x**(p-1))/(a+z)-1/x-(p*x**(p-1))/(1+z)
            B=(p-1)-(p+1)*a
            quotient=(-z*z+B*z-a)/(x*(z+a)*(z+1))
            test(explicit==quotient, 'exact logarithmic derivative')

# Exact discriminant classification for rational exponent p (all algebra in p,a,z).
for numerator in range(11,71):
    p=Q(numerator,10)
    ac=((p-1)/(p+1))**2
    for an in range(1,101):
        a=Q(an,101)
        B=(p-1)-(p+1)*a
        discr=B*B-4*a
        positive_possible=(p>1 and a<ac)
        test((B>0 and discr>0)==positive_possible, 'positive quadratic roots criterion')
        if positive_possible:
            test(-a<0 and B>0 and B*B>4*a,'positive hump exists')

# Strict log-concavity can be evaluated from the exact Hessian identity.
for p in [1.1,1.2,1.5,2,2.7,4,8,15]:
    ac=((p-1)/(p+1))**2
    for fraction in [.03,.15,.42,.72,.93]:
        a=fraction*ac
        B=(p-1)-(p+1)*a
        disc=B*B-4*a
        lower=(B-sqrt(disc))/2
        upper=(B+sqrt(disc))/2
        for i in range(1,100):
            z=lower+(upper-lower)*i/100
            hessian=-(p*p*z*lower/(z-lower)**2 + p*p*z*upper/(upper-z)**2
                      +p*p*a*z/(z+a)**2 +p*p*z/(z+1)**2)
            test(hessian<0,'log-concavity of positive derivative bonus')

# Example: p=2, basal attraction a=1/25, capture-decay b=2/5.
p,a,b=2,1/25,2/5
B=(p-1)-(p+1)*a
disc=B*B-4*a
lo=((B-sqrt(disc))/2)**(1/p)
hi=((B+sqrt(disc))/2)**(1/p)
peak_x,bc=golden_max(lambda x:h(x,a,p),lo,hi)
test(abs(peak_x-.36335863346)<1e-7,'peak position')
test(abs(bc-.8303143486898)<1e-7,'critical attenuation')
bc_example = bc
x1=bisect_root(lambda x:h(x,a,p)-b,lo,peak_x)
x2=bisect_root(lambda x:h(x,a,p)-b,peak_x,hi)
test(abs(x1-.24926294605)<1e-7,'minimum position')
test(abs(x2-.62709913172)<1e-7,'maximum position')
test(hazard(x1,a,p,b)<hazard(x1+.01,a,p,b),'minimum')
test(hazard(x2,a,p,b)>hazard(x2+.01,a,p,b),'maximum')
test(hazard(.3,a,p,b)<hazard(.6,a,p,b),'integer group risk reversal')

# Near-coalescence leading law; a approaches ac from below.
for p in [1.3,2,3,6]:
    ac=((p-1)/(p+1))**2
    t=(p-1)/(p+1)
    for ratio in [1e-3,1e-4]:
        a=ac*(1-ratio)
        B=(p-1)-(p+1)*a
        D=B*B-4*a
        lo=((B-sqrt(D))/2)**(1/p)
        hi=((B+sqrt(D))/2)**(1/p)
        _,bc=golden_max(lambda x:h(x,a,p),lo,hi)
        predicted=p*(ac-a)/(t**(1+1/p)*(1+t)**2)
        test(abs(bc/predicted-1)<.02,'linear near-coalescence law')

# Small-baseline scaling of critical success attenuation.
for p in [1.5,2,3,5]:
    w=((p*p-p+2)+sqrt((p*p-p+2)**2+4*(p-1)))/(2*(p-1))
    u=w**(1/p)
    constant=((p-1)*u**p-1)/(u*(1+u**p))
    for a in [1e-6,1e-7]:
        B=(p-1)-(p+1)*a
        D=B*B-4*a
        lo=((B-sqrt(D))/2)**(1/p)
        hi=((B+sqrt(D))/2)**(1/p)
        _,bc=golden_max(lambda x:h(x,a,p),lo,hi)
        test(abs(a**(1/p)*bc/constant-1)<.03,'small-baseline scaling')

print('PASS',checks,'diagnostic assertions')
print('p=2 a=1/25 b=2/5: critical b =', format(bc_example,'.12g'),
      '; stationary x =',format(x1,'.12g'),format(x2,'.12g'))
