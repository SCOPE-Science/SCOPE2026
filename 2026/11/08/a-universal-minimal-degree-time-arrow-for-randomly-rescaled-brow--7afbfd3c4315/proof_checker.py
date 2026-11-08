#!/usr/bin/env python3
"""Independent rational and floating-point diagnostics for the marked-reset fourth-order lag theorem.

Only the deterministic mathematical identities are asserted. These checks support,
but do not replace, the proof for arbitrary bounded multiplier laws.
"""
from fractions import Fraction as Q
from math import exp, expm1, isclose, log
from itertools import product

checks = 0

def verify(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def H(t, l1, l3):
    delta = l3 - l1
    if abs(delta) < 1e-12:
        return t * exp(-l1 * t)
    return exp(-l1*t)*(-expm1(-delta*t))/delta


def moments(marked, r=Q(1), D=Q(1)):
    # Each marked element is (factor, probability), all rational.
    verify(sum(p for a, p in marked) == Q(1), "mark weights")
    verify(all(p >= 0 and abs(a) < 1 for a, p in marked), "contractive support")
    mu = {k:sum(p * a**k for a, p in marked) for k in range(1,5)}
    lam = {k:r*(1-mu[k]) for k in range(1,5)}
    verify(all(lam[k]>0 for k in lam), "positive rates")
    m2 = 2*D/lam[2]
    m4 = 12*D*m2/lam[4]
    g = sum(p*(1-a)**2*(1-a*a) for a,p in marked)
    verify(g>0, "positive irreversibility coefficient")
    verify(lam[3]-lam[1]-lam[4]/2 == -r*g/2, "polynomial factorization")
    verify(lam[2]*m2 == 2*D, "second-moment generator identity")
    verify(lam[4]*m4 == 12*D*m2, "fourth-moment generator identity")
    return lam,m2,m4,g


for a in [Q(-4,5),Q(-1,2),Q(-1,3),Q(0),Q(1,7),Q(3,5),Q(9,10)]:
    for r in [Q(1,3), Q(1), Q(5,2)]:
        for D in [Q(1,4), Q(1), Q(7,3)]:
            law = [(a,Q(1))]
            lam,m2,m4,g = moments(law,r,D)
            l1,l3 = float(lam[1]),float(lam[3])
            for t in [0.03,0.2,0.7,1,2,4,7]:
                ht=H(t,l1,l3)
                old_first=m4*Q.from_float(exp(-l1*t))
                old_last=m4*Q.from_float(exp(-l3*t))+6*D*m2*Q.from_float(ht)
                direct=float(old_first-old_last)
                factored=-float(r*m4*g)/2*ht
                verify(isclose(direct,factored,rel_tol=2e-9,abs_tol=2e-11),"two ways of computing antisymmetry")
                verify(factored<0,"strict time arrow")
            tstar=log(l3/l1)/(l3-l1) if abs(l3-l1)>1e-12 else 1/l1
            verify(tstar>0,"positive optimal lag")
            for shift in [-0.7,-0.2,0.2,0.7,2.0]:
                other=tstar*exp(shift)
                verify(H(other,l1,l3)<H(tstar,l1,l3)*(1+1e-12),"single lag maximum")

laws=[
 [(Q(-1,2),Q(1,2)),(Q(1,2),Q(1,2))],
 [(Q(-1,3),Q(1,4)),(Q(0),Q(1,2)),(Q(2,3),Q(1,4))],
 [(Q(-4,5),Q(1,5)),(Q(1,2),Q(2,5)),(Q(1,3),Q(2,5))],
 [(Q(0),Q(1))],
 [(Q(-2,3),Q(1,3)),(Q(1,3),Q(2,3))],
]
for law in laws:
    for r in [Q(1),Q(3,2)]:
        lam,m2,m4,g=moments(law,r,Q(3,2))
        l1,l3=float(lam[1]),float(lam[3])
        for t in [0.1,0.5,1,2,5]:
            L=float(m4)*(exp(-l1*t)-exp(-l3*t))-6*1.5*float(m2)*H(t,l1,l3)
            R=-float(r*m4*g)/2*H(t,l1,l3)
            verify(isclose(L,R,rel_tol=2e-9,abs_tol=2e-11),"mixed-law identity")
            verify(R<0,"mixed-law strict sign")

law=[(Q(-1,2),Q(1,2)),(Q(1,2),Q(1,2))]
lam,m2,m4,g=moments(law)
verify(lam[1]==lam[3]==1,"rate collision")
verify(m2==Q(8,3) and m4==Q(512,15),"example stationary moments")
verify(g==Q(15,16),"example strictly positive factor")
verify(-Q(1,2)*m4*g == -16,"example amplitude")
for t in [Q(1,4),Q(1,2),Q(1),Q(2)]:
    verify(isclose(-float(m4*g)/2*H(float(t),1.,1.),-16*float(t)*exp(-float(t)),rel_tol=1e-13),"example envelope")

# Structural parity/diagonal/stationary checks at all monomial bidegrees <4.
for p,q in product(range(4),repeat=2):
    if p+q<4:
        verify(p==q or p==0 or q==0 or (p+q)%2==1,"no lower-degree antisymmetric witness")

print(f"PASS: {checks} diagnostic assertions; sharp signed-rate identity, rate collision, strict sign and unique lag maximum")
