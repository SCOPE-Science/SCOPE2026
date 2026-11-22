#!/usr/bin/env python3
"""Reproduce conservative interval checks for the 0.1% relative-read filter.
Only Python standard-library modules are used. No experimental data are used.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from math import factorial

K = 1000
GAMMA = Decimal(1) / Decimal(4)
M = 30
BASE_PREC = 90
INTERVAL_PREC = 70

def exp_interval_minus(x):
    """Safe outward envelope of Decimal.exp rounded at 90 significant digits."""
    with localcontext() as ctx:
        ctx.prec = BASE_PREC
        val = (-x).exp()  # documented correctly rounded, ROUND_HALF_EVEN
        eps = Decimal('1e-82')
        return val*(1-eps), val*(1+eps)

def binary(op, a, b, up=False):
    with localcontext() as ctx:
        ctx.prec = INTERVAL_PREC
        ctx.rounding = ROUND_CEILING if up else ROUND_FLOOR
        if op == 'mul': return a*b
        if op == 'add': return a+b
        if op == 'div': return a/b
        raise ValueError(op)

def poisson_vector_cdf(mu, needed):
    lo, hi = exp_interval_minus(mu)
    cumulative_lo, cumulative_hi = Decimal(0), Decimal(0)
    wanted = set(needed)
    saved = {}
    for j in range(max(needed)+1):
        cumulative_lo = binary('add', cumulative_lo, lo)
        cumulative_hi = binary('add', cumulative_hi, hi, True)
        if j in wanted: saved[j] = (cumulative_lo,cumulative_hi)
        lo = binary('div', binary('mul',lo,mu),Decimal(j+1))
        hi = binary('div', binary('mul',hi,mu,True),Decimal(j+1),True)
    return saved

def interval_q(s):
    with localcontext() as ctx:
        ctx.prec=BASE_PREC
        mu_c=GAMMA*s
        mu_g=(Decimal(K)-GAMMA)*s
        needed=[(K-1)*c for c in range(1,M+1)]
        cdf=poisson_vector_cdf(mu_g,needed)
        pc_lo,pc_hi=exp_interval_minus(mu_c)
        lo=Decimal(0); hi=Decimal(0)
        for c in range(1,M+1):
            pc_lo=binary('div',binary('mul',pc_lo,mu_c),Decimal(c))
            pc_hi=binary('div',binary('mul',pc_hi,mu_c,True),Decimal(c),True)
            fl,fu=cdf[(K-1)*c]
            lo=binary('add',lo,binary('mul',pc_lo,fl))
            hi=binary('add',hi,binary('mul',pc_hi,fu,True),True)
        # The omitted Poisson tail (c > M) is below this positive geometric bound.
        # Explicitly: exp(-mu_c)*mu_c**(M+1)/(M+1)! /(1-mu_c/(M+2))
        # and exp(-mu_c) <= 1.
        t_upper=Decimal(1)
        for r in range(1,M+2):
            t_upper=binary('div',binary('mul',t_upper,mu_c,True),Decimal(r),True)
        lower_den = binary('add',Decimal(1),-binary('div',mu_c,Decimal(M+2),True))
        t_upper=binary('div',t_upper,lower_den,True)
        hi=binary('add',hi,t_upper,True)
        return lo,hi

def main():
    pts=[Decimal(3)/20]
    for j in range(1,8):
        pts.extend([Decimal(j)-Decimal(3)/20,Decimal(j)+Decimal(3)/20])
    bounds={s:interval_q(s) for s in pts}
    assert len(bounds)==15
    for j in range(1,8):
        x=Decimal(j)-Decimal(3)/20
        left=Decimal(j-1)+Decimal(3)/20
        right=Decimal(j)+Decimal(3)/20
        assert bounds[x][0]>bounds[left][1],(j,'left')
        assert bounds[x][0]>bounds[right][1],(j,'right')
        print('j=%d, P(left) in [%.12f, %.12f], P(peak) in [%.12f, %.12f], P(right) in [%.12f, %.12f]'%(
            j,*map(float,bounds[left]),*map(float,bounds[x]),*map(float,bounds[right])))
    # Intrinsic non-flatness: as s->0, q_K(s)->0 whereas q_K(s)>0 for s>0;
    # q_K is real analytic because it is an absolutely locally uniformly
    # convergent sum of finite Poisson event terms.
    print('PASS: 14 strict interval inequalities certify >= 7 distinct strict local maxima.')

if __name__=='__main__':main()
