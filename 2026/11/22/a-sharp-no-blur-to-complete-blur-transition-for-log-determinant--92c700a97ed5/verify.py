#!/usr/bin/env python3
"""Standalone finite checks for a two-pixel log-determinant blur transition.

Checks are supplementary to the analytical proof, not an exhaustive search
or a proof of the continuum assertion.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from itertools import product

checks = 0

def check(c, info):
    global checks
    assert c, info
    checks += 1

def D(q):
    if isinstance(q, Q):
        return Decimal(q.numerator)/Decimal(q.denominator)
    return Decimal(str(q))

def objective(a, l, d, B, w):
    return (l*B/(a+l) + w*(a+d).ln())/2

def tau(a, l, d):
    if a == 1:
        return (1+d)/(1+l)**2
    return (1-a)/((a+l)*(1+l)*((1+d)/(a+d)).ln())

def j1(l, d, B):
    return l*B*(1+d)/(1+l)**2

def j0(l, d, B):
    return B/((1+l)*((1+d)/d).ln())

with localcontext() as context:
    context.prec = 70
    one = Decimal(1)
    zero = Decimal(0)
    # Check exact rational derivative numerator and the algebraic reduction
    # of the two-pixel Tikhonov term on a finite rational parameter grid.
    vals = [Q(1, 100), Q(1, 8), Q(1, 2), Q(1, 1), Q(3, 2), Q(7, 1)]
    for lr, dr, ar in product(vals, vals, [Q(i, 16) for i in range(1, 16)]):
        C = lr
        wr = Q(1, 5)
        # Clearing positive denominators gives P(a).
        P = wr*(ar+lr)**2-C*(ar+dr)
        df = -C/(ar+lr)**2 + wr/(ar+dr)
        check(P == df*(ar+lr)**2*(ar+dr), ('derivative',lr,dr,ar))
        # True reconstructed Fourier variance/error formula is the minimized
        # quadratic, not an optimizer of a different model.
        y = Q(2, 3)
        x = ar*y/(ar*ar+lr)
        direct = (ar*x-y)**2/2+lr*x*x/2
        collapsed = lr*y*y/(2*(ar*ar+lr))
        check(direct == collapsed, ('projection',lr,ar))

    # Grid checks of the endpoint-only secant envelope for broad scales,
    # including parameters where the minimizing endpoint changes.
    lv = [D(Q(1, 10)), D(Q(1, 2)), D(1), D(3), D(10)]
    dv = [D(Q(1, 10000)), D(Q(1, 100)), D(Q(1, 4)), D(2), D(20)]
    for l,d in product(lv,dv):
        t0, t1 = tau(zero,l,d),tau(one,l,d)
        for k in range(1,100):
            a=D(Q(k,100))
            tt=tau(a,l,d)
            check(tt>min(t0,t1)-D('1e-55'), ('secant',l,d,k))

    # In the first-order regime, test global classification and separated
    # metastable local minimum at deterministic exact parameters.
    l=one;d=D(Q(1,100));B=one
    w0=j0(l,d,B);wloc=j1(l,d,B)
    check(w0<wloc,'nonempty first order regime')
    check(w0<D(Q(1,5))<wloc,'metastability interval')
    for w in [w0/2,w0,w0+(wloc-w0)/3,D(Q(1,5)),wloc*2]:
        f0=objective(zero,l,d,B,w)
        f1=objective(one,l,d,B,w)
        for k in range(1,200):
            a=D(Q(k,200))
            fv=objective(a,l,d,B,w)
            if w<w0:
                check(fv>f1,('identity global',w,k))
            elif w==w0:
                check(fv>f0 and fv>f1,('two endpoint global',w,k))
            else:
                check(fv>f0,('complete blur global',w,k))
    # Exact example barrier: stationarity polynomial has opposite endpoint
    # signs, hence one root in (0,1) and a unique strict interior maximum.
    wr=Q(1,5); lr=Q(1,1);dr=Q(1,100); Cr=Q(1,1)
    check(wr*(lr)**2-Cr*dr>0,'positive derivative at zero')
    check(wr*(1+lr)**2-Cr*(1+dr)<0,'negative derivative at one')
    amax=(one-2*D(wr)*one-(one*(one+4*D(wr)*(D(dr)-one))).sqrt())/(2*D(wr))
    check(zero<amax<one,'barrier in admissible interval')
    fm=objective(amax,l,d,B,D(wr))
    check(fm>objective(zero,l,d,B,D(wr)) and fm>objective(one,l,d,B,D(wr)),'strict barrier')
    print('PASS:',checks,'finite assertions; example a_barrier=',str(amax),
          '; w_global=',str(w0),'; w_local=',str(wloc))
