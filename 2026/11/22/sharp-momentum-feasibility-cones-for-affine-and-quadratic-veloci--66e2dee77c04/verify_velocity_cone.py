#!/usr/bin/env python3
"""Exact rational diagnostics for low-degree velocity-moment feasibility cones."""
from fractions import Fraction as F
from itertools import combinations


def grid(n):
    return [F(-1) + F(2*j, n-1) for j in range(n)]


def mom(p, v):
    m = sum((p(x) for x in v), F(0))
    j = sum((x*p(x) for x in v), F(0))
    return m, j


def formula(n):
    v = grid(n)
    mu2 = sum((x*x for x in v), F(0))/n
    delta = F(1, n-1)
    c = [abs((v[i]+v[i+1])/2) for i in range(n-1)]
    rr = [2*mu2*x/(mu2 + x*x-delta*delta) for x in c]
    return mu2, max(rr)


def check(n):
    v = grid(n)
    m1, m2 = formula(n)
    assert m1 == F(n+1, 3*(n-1))
    rays1 = [(lambda x, root=r: x-root) for r in (v[0],v[-1])]
    ratios1 = []
    for p in rays1:
        vals = [p(x) for x in v]
        if all(y>=0 for y in vals):
            m,j=mom(p,v)
            ratios1.append(j/m)
        elif all(y<=0 for y in vals):
            m,j=mom(lambda x, p=p:-p(x),v)
            ratios1.append(j/m)
    assert max(abs(y) for y in ratios1)==m1

    valid = []
    for i,j in combinations(range(n),2):
        def p(x,i=i,j=j):return (x-v[i])*(x-v[j])
        vals=[p(x) for x in v]
        if all(y>=0 for y in vals):
            m,jj=mom(p,v)
            valid.append((i,j,jj/m))
            assert j==i+1
        elif all(y<=0 for y in vals):
            m,jj=mom(lambda x,p=p:-p(x),v)
            valid.append((i,j,jj/m))
            assert i==0 and j==n-1
        else:
            assert (j>i+1 and (i,j)!=(0,n-1))
    assert len(valid)==n
    assert max(abs(q) for _,_,q in valid)==m2
    assert m2>m1
    if n==3: assert m2==1
    if n>=4: assert m2<1

    # Explicit nearby nonnegative data with momentum outside the polynomial cone.
    if n>=4:
        positive_extremizers=[(i,j) for i,j,q in valid if q==m2]
        assert positive_extremizers
        i,j=positive_extremizers[0]
        sign=1
        if (i,j)==(0,n-1): raise AssertionError('zero momentum extremizer')
        p=lambda x:(x-v[i])*(x-v[j])
        vals=[p(x) for x in v]
        if sum(x*y for x,y in zip(v,vals))<0:
            vals=list(reversed(vals))
        assert vals[-1]>0
        k=next(k for k in range(n-1) if vals[k]>0)
        eps=vals[k]/100
        shifted=vals.copy(); shifted[k]-=eps; shifted[-1]+=eps
        assert min(shifted)>=0
        total=sum(vals,F(0))
        assert sum(shifted,F(0))==total
        assert sum((x*y for x,y in zip(v,shifted)),F(0))>m2*total
        assert sum((z*z for z in [shifted[q]-vals[q] for q in range(n)]),F(0))==2*eps*eps

    return len(valid)+len(ratios1)+9


def main():
    tests=sum(check(n) for n in range(3,51))
    samples={n: tuple(str(x) for x in formula(n)) for n in (3,4,5,6,8,12)}
    assert samples[3]==('2/3','1')
    assert samples[4]==('5/9','5/6')
    assert samples[5]==('1/2','3/4')
    print(f'PASS: {tests} counted exact-rational structural cases, with supplementary assertions')
    for n,pair in samples.items():print(f'n={n} affine={pair[0]} quadratic={pair[1]}')
    print('The all-size result uses the analytical extreme-ray proof; finite tests are diagnostics only.')

if __name__=='__main__':main()
