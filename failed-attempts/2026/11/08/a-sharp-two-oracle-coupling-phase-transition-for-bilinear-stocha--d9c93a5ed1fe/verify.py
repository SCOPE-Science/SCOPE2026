"""Exact-rational checks for paired-oracle extragradient on a two-component bilinear game.

This checks stated polynomial and finite-dimensional identities; it is not a
substitute for the proof of inequalities over continuous parameter ranges.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product

n = 0

def check(x):
    global n
    assert x
    n += 1


def norm_sq(v):
    return v[0] * v[0] + v[1] * v[1]


def J(v):
    return (v[1], -v[0])


def direct(z, a, b, eta):
    j = J(z)
    w = (z[0] - eta*a*j[0], z[1] - eta*a*j[1])
    jw = J(w)
    return (z[0] - eta*b*jw[0], z[1] - eta*b*jw[1])


def factor(a, b, x):
    return (1-x*a*b)**2 + x*b*b


def qs(a,b,x):
    return 1-(a*a+b*b)*x/2+(a**4+b**4)*x*x/2


def qa(a,b,x):
    return 1+((a*a+b*b)/2-2*a*b)*x+a*a*b*b*x*x


def qc(a,b,x,p):
    return p*qs(a,b,x)+(1-p)*qa(a,b,x)


for a,b in [(F(1,3),F(2,3)), (F(1),F(2)), (F(2),F(5)),
            (F(3,2), F(7,3)), (F(1),F(4))]:
    for eta in [F(1,4),F(1,3),F(1,2),F(2,3),F(1)]:
        x=eta*eta
        for z in [(F(1),F(0)), (F(1),F(2)), (F(-2),F(3))]:
            for A,B in product((a,b),repeat=2):
                zn=direct(z,A,B,eta)
                check(norm_sq(zn) == factor(A,B,x)*norm_sq(z))
        for p in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            ensemble = (p*factor(a,a,x) + p*factor(b,b,x) +
                       (1-p)*factor(a,b,x)+(1-p)*factor(b,a,x))/2
            check(ensemble == qc(a,b,x,p))
        check(qs(a,b,x)-qa(a,b,x) ==
              x*(b-a)**2*(-1+x*(a+b)**2/2))
        check(qs(a,b,x) == (factor(a,a,x)+factor(b,b,x))/2)
        check(qa(a,b,x) == (factor(a,b,x)+factor(b,a,x))/2)
        # All feasible couplings with uniform two-point marginals are mixtures.
        for p in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            check(min(qs(a,b,x),qa(a,b,x))<=qc(a,b,x,p)
                  <=max(qs(a,b,x),qa(a,b,x)))
        xs=(a*a+b*b)/(a**4+b**4)
        xa=(4*a*b-a*a-b*b)/(2*a*a*b*b)
        check(qs(a,b,xs)==1)
        check(qa(a,b,xa)==1)
        # Optimal same-sample step and exact minimal multiplier.
        xfast=(a*a+b*b)/(2*(a**4+b**4))
        check(qs(a,b,xfast)==1-(a*a+b*b)**2/(8*(a**4+b**4)))
        check(qs(a,b,xfast)<=qs(a,b,x))
        if a<b:
            u=(a*a+b*b)/(a*b)
            check(u>2)
            if u<4:
                xantifast=(4*a*b-a*a-b*b)/(4*a*a*b*b)
                check(qa(a,b,xantifast)==1-(4-u)**2/16)
                check(qs(a,b,xfast)<qa(a,b,xantifast))
                check(qa(a,b,xantifast)<=qa(a,b,x))
            else:
                check(qa(a,b,x)>1)

# Exact rational witness: at eta^2=1/3, same-sample and independent
# coupling increase mean-squared error, antithetic coupling contracts.
a,b,x=F(1),F(2),F(1,3)
check(qs(a,b,x)==F(10,9))
check(qa(a,b,x)==F(17,18))
check(qc(a,b,x,F(1,2))==F(37,36))
check((a*a+b*b)/(a**4+b**4)==F(5,17))
check((4*a*b-a*a-b*b)/(2*a*a*b*b)==F(3,8))
check(F(2)/(a+b)**2==F(2,9))
check(qs(a,b,F(5,34))==F(111,136))
check(qa(a,b,F(3,16))==F(55,64))

# The heterogeneity comparison is reduced exactly to a quadratic in
# u=b/a+a/b; its positive root is 1+sqrt(5).
for b in [F(9,8),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4)]:
    a=F(1)
    u=b+1/b
    xa=(4*b-1-b*b)/(2*b*b)
    xs=(1+b*b)/(1+b**4)
    check((xa-xs)*2*b*b*(1+b**4)==
          -(b-1)**2*(b**4-2*b**3-2*b*b-2*b+1))
    check((b**4-2*b**3-2*b*b-2*b+1)/b**2==u*u-2*u-4)

print('VERIFICATION_OK')
print('exact_rational_assertions:',n)
print('exact_witness: same=10/9, iid=37/36, antithetic=17/18 at a=1,b=2,eta_squared=1/3')
print('limits: finite rational tests are not a proof of universal coupling and stability claims')
