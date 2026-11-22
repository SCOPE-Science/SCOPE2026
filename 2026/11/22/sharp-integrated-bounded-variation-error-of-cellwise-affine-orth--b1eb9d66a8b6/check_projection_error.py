#!/usr/bin/env python3
"""Exact rational checks for the one-cell affine projection BV-to-L1 error law."""
from fractions import Fraction as F
from random import Random


def p(t):
    return 24*t**3 - 48*t**2 + 27*t - 4


def q(t):
    return 72*t**6-216*t**5+246*t**4-132*t**3+30*t**2-1


def e1(t):
    return t*(6*t*t-9*t+4)**2/(6*(1-t))


def e2(t):
    return (2*t*t-2*t+1)*(18*t**4-36*t**3+24*t*t-6*t+1)/(6*t*(1-t))


def integral_abs_affine(l, r, y_l, y_r):
    # Exact integral of |affine function| from its two endpoint values.
    if y_l*y_r >= 0:
        return (r-l)*(abs(y_l)+abs(y_r))/2
    return (r-l)*(y_l*y_l+y_r*y_r)/(2*(abs(y_l)+abs(y_r)))


def projected_step(t, x):
    return 1-t+6*t*(1-t)*(x-F(1,2))


def direct_step_error(t):
    a=1-4*t+3*t*t
    b=6*t*(1-t)
    if t in (0,1):
        return F(0)
    cuts = sorted(set([F(0),t,F(1)] +
                      [z for z in (-a/b,(1-a)/b) if 0<z<1]))
    ans=F(0)
    for l,r in zip(cuts,cuts[1:]):
        mid=(l+r)/2
        shift=1 if mid>t else 0
        ans += integral_abs_affine(l,r,a+b*l-shift,a+b*r-shift)
    return ans


def mixed_error(jumps):
    # A finite signed sum of jumps on one cell; compute its residual exactly.
    if not jumps:
        return F(0)
    cuts=sorted(set([F(0), F(1)]+[t for t,w in jumps]))
    res=F(0)
    for l,r in zip(cuts,cuts[1:]):
        shift=sum((w for t,w in jumps if t<(l+r)/2),F(0))
        def val(s):
            return sum((w*projected_step(t,s) for t,w in jumps),F(0))-shift
        res += integral_abs_affine(l,r,val(l),val(r))
    return res


def main():
    rng=Random(20110215)
    assert p(F(0))==-4 and p(F(1,3))==F(5,9)
    assert e1(F(1,3))==e2(F(1,3))==F(25,108)
    assert e2(F(1,2))==F(5,24)
    assert e1(F(1,4))==F(289,1152)
    assert e1(F(1,4))>F(1,4)
    for n in range(2,110):
        for i in range(1,n):
            t=F(i,n)
            observed=direct_step_error(t)
            target=e1(t) if t<=F(1,3) else e2(t) if t<=F(1,2) else (
                e1(1-t) if t>=F(2,3) else e2(1-t))
            assert observed == target,(t,observed,target)
    print('EXACT_STEP_ERROR_FORMULAS_PASS')
    for i in range(1,100):
        t=F(i,200)
        assert direct_step_error(t)==direct_step_error(1-t)
    print('EXACT_SYMMETRY_AND_ENDPOINT_PASS')
    # Check the polynomial identity for the second regime and its sign.
    for i in range(1,101):
        u=F(i,600)
        assert q(F(1,2)-u)==(288*u**6-96*u**4-6*u*u-1)/4
        assert q(F(1,2)-u)<0
    print('EXACT_SECOND_BRANCH_POLYNOMIAL_PASS')
    lo,hi=F(234328,1000000),F(234329,1000000)
    assert p(lo)<0<p(hi)
    for _ in range(100):
        mid=(lo+hi)/2
        if p(mid)<0: lo=mid
        else: hi=mid
    tstar=(lo+hi)/2
    assert abs(float(tstar)-0.234328086180391)<1e-14
    assert abs(float(e1(tstar))-0.251497656507972)<1e-14
    print('EXACT_CUBIC_ROOT_BRACKET_AND_NUMERICAL_CONSTANT_PASS')
    count=0
    # Sharp proof gives k > 1/4; rational 0.252 safely exceeds it.
    upper=F(252,1000)
    for _ in range(1800):
        pts=sorted(set(F(rng.randrange(1,120),120) for j in range(rng.randrange(1,7))))
        jumps=[(t,F(rng.randrange(-9,10),rng.randrange(1,10))) for t in pts]
        norm=sum((abs(w) for t,w in jumps),F(0))
        assert mixed_error(jumps)<=upper*norm
        count+=1
    print('EXACT_SIGNED_MULTIJUMP_CHECKS_PASS',count)
    print('ALL_AFFINE_BV_L1_CHECKS_PASS')

if __name__ == '__main__':
    main()
