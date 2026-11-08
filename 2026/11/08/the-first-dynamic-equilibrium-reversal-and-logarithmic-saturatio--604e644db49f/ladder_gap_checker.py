"""Exact rational enclosures for the dynamic/static adsorption crossing.
Uses published integral/algebraic expressions, alternating Taylor bounds and
composite trapezoid error. Python standard library; run: python ladder_gap_checker.py.
"""
from fractions import Fraction as F
from math import factorial

# All choices are fixed in advance. The hard case is blockade range nine.
MESH={1:256,2:256,3:256,4:256,5:256,6:256,7:512,8:1024,9:8192,10:2048}
TAYLOR_ODD=39


def positive_exp_neg_bounds(v):
    """For rational v>=0, exact Taylor inequalities L<=exp(-v)<=U."""
    assert v>=0
    term=F(1); total=term; lower=None
    for k in range(1,TAYLOR_ODD+2):
        term *= -v/k
        total += term
        if k==TAYLOR_ODD: lower=total
    assert total>=lower
    return lower,total


def root_bracket(b):
    """Rational bracket of the unique positive polynomial root, by bisection."""
    def poly(t):
        q=t**b
        return q*(1+t)*(1-q)/(1-t)-1
    lo,hi=F(1,2),F(1)
    assert poly(lo)<0
    # dyadic bisection yields convenient root rational denominators
    for i in range(51):
        mid=(lo+hi)/2
        if poly(mid)>0: hi=mid
        else: lo=mid
    assert poly(lo)<0<poly(hi)
    return lo,hi


def scaled_static_bounds(b):
    a,c=root_bracket(b)
    # Reciprocal scaled density is sum of increasing and decreasing terms.
    def increasing(t):return 2*t/(b*(1-t*t))
    def decreasing(t):
        q=t**b
        return (1-2*q)/(1-q)
    elo=increasing(a)+decreasing(c)
    ehi=increasing(c)+decreasing(a)
    assert 0<elo<ehi
    return 1/ehi,1/elo


def scaled_dynamic_bounds(b):
    H=sum((F(1,j) for j in range(1,b+1)),F())
    v0=2*H-F(1,b)
    edlo,edhi=positive_exp_neg_bounds(v0)
    N=MESH[b]
    total_lo=F(0);total_hi=F(0)
    for i in range(N+1):
        y=F(N-i,N)  # =1-u
        v=sum((2*(1-y**j)/j for j in range(1,b+1)),F())-(1-y**b)/b
        assert v>=0
        lo,hi=positive_exp_neg_bounds(v)
        weight=1 if i in (0,N) else 2
        total_lo += weight*lo
        total_hi += weight*hi
    quadr_lo=F(b,2*N)*total_lo
    quadr_hi=F(b,2*N)*total_hi
    # |(exp(-v))''| <= 6 b^2 ; composite trapezoid over [0,1].
    # Multiplication by b gives at most b^3/(2 N^2) total scaled error.
    err=F(b**3,2*N*N)
    return b*edlo/2+quadr_lo-err,b*edhi/2+quadr_hi+err


def run():
    for b in range(1,11):
        slo,shi=scaled_static_bounds(b)
        dlo,dhi=scaled_dynamic_bounds(b)
        assert (shi<dlo) if b<=9 else (slo>dhi), f'uncertified b={b}'
        print(f'b={b:2d} N={MESH[b]:5d} static=[{float(slo):.11f},{float(shi):.11f}] '
              f'dynamic=[{float(dlo):.11f},{float(dhi):.11f}] '
              f'gap=[{float(slo-dhi):+.11f},{float(shi-dlo):+.11f}]',flush=True)
    print('PASS: complete exact rational interval certificate for first crossover at b=10')

if __name__=='__main__':run()
