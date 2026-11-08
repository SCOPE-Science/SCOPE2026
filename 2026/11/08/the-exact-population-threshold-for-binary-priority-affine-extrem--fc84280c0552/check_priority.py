#!/usr/bin/env python3
"""Exact, standalone checks for binary-priority potential-share identities.

Use: python3 check_priority.py
No third-party dependencies; checks rational Fourier/Hodge coefficients directly
against explicit service ranks, plus symbolic closed forms for selected sizes.
"""
from fractions import Fraction as F
from math import comb


def difference_data(n, steps):
    # f(rank+1)-f(rank)=-steps[rank-1] for rank = 1,...,n-1
    assert n >= 2 and len(steps) == n-1 and all(x > 0 for x in steps)
    pay = [0]
    for x in steps:
        pay.append(pay[-1] - x)
    by_i = []
    for i in range(n):
        others = [j for j in range(n) if j != i]
        vals = []
        for mask in range(1 << (n-1)):
            s = {j: (mask >> p) & 1 for p,j in enumerate(others)}
            # 0-based service position when agent i is high/low
            high = sum(s[j] for j in range(i))
            low = i + sum(s[j] for j in range(i+1, n))
            vals.append(pay[high]-pay[low])
        # Walsh coefficients for signs (-1)^s; all exact rational
        h = 1
        while h < len(vals):
            for a in range(0,len(vals),2*h):
                for k in range(a,a+h):
                    u, v = vals[k], vals[k+h]
                    vals[k], vals[k+h] = u+v, u-v
            h *= 2
        coeff = {}
        for t,c in enumerate(vals):
            global_mask = sum(1 << j for p,j in enumerate(others) if (t >> p)&1)
            coeff[global_mask] = F(c,1 << (n-1))
        by_i.append(coeff)
    return by_i


def energy(n, steps):
    c = difference_data(n,steps)
    total = sum((v*v for d in c for v in d.values()), F(0))
    potential=F(0)
    for mask in range(1,1<<n):
        g = sum((c[i][mask ^ (1<<i)] for i in range(n) if mask&(1<<i)),F(0))
        potential += g*g/F(mask.bit_count())
    return total, total-potential


def formula(n):
    total = F(n*n*(n-1)*(13*n*n-n-2), 192)
    residual = F(n*(n-1)*(n+1)*(25*n-18),384)
    return total,residual


def q_form(n,steps):
    t,h = energy(n,steps)
    return h-t/F(n)


def psd_check(n):
    # Q(steps)=H-T/n; Q annihilates all-ones affine increments.
    # Construct all symmetric coefficients from canonical-unit vectors.
    d=n-1
    zs=[]
    for j in range(d):
        steps = [int(k==j) for k in range(d)]
        # allow zero increment only to check the quadratic form
        zs.append(energy_unrestricted(n,steps))
    diag = [h-t/F(n) for t,h in zs]
    matrix = [[F(0) for _ in range(d)] for __ in range(d)]
    for j in range(d):
        matrix[j][j]=diag[j]
        for k in range(j):
            v=[int(l==j or l==k) for l in range(d)]
            t,h=energy_unrestricted(n,v)
            off=(h-t/F(n)-diag[j]-diag[k])/2
            matrix[j][k]=matrix[k][j]=off
    assert all(sum(row)==0 for row in matrix), (n,"null direction")
    # Positive definiteness on the first d-1 coordinates implies PSD
    # with one-dimensional kernel spanned by ones.
    a=[r[:d-1] for r in matrix[:d-1]]
    if d==1:
        assert matrix[0][0]==0
        return
    for j in range(d-1):
        pivot=a[j][j]
        assert pivot > 0, (n,j,pivot)
        for k in range(j+1,d-1):
            for l in range(j+1,d-1):
                a[k][l] -= a[k][j]*a[j][l]/pivot
        for k in range(j+1,d-1):
            a[k][j]=F(0)
            a[j][k]=F(0)


def energy_unrestricted(n,steps):
    # Same exact direct enumeration, but include non-strict test vectors.
    # Shift all increments by +1 and cancel quadratic linear terms via
    # polarization is unnecessary: reconstruct directly with local copy.
    c = difference_data_unrestricted(n,steps)
    total = sum((v*v for d in c for v in d.values()), F(0))
    potential=F(0)
    for mask in range(1,1<<n):
        g = sum((c[i][mask ^ (1<<i)] for i in range(n) if mask&(1<<i)),F(0))
        potential += g*g/F(mask.bit_count())
    return total,total-potential


def difference_data_unrestricted(n,steps):
    # Inline zero-allowed Walsh routine for basis-vector matrix checks.
    pay=[0]
    for x in steps:pay.append(pay[-1]-x)
    out=[]
    for i in range(n):
        others=[j for j in range(n) if j!=i]
        a=[]
        for mask in range(1<<(n-1)):
            s={j:(mask>>p)&1 for p,j in enumerate(others)}
            a.append(pay[sum(s[j] for j in range(i))]-pay[i+sum(s[j] for j in range(i+1,n))])
        h=1
        while h<len(a):
            for j in range(0,len(a),2*h):
                for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
            h*=2
        out.append({sum(1<<j for p,j in enumerate(others) if mask>>p&1):F(v,len(a)) for mask,v in enumerate(a)})
    return out


def main():
    for n in range(2,10):
        steps=list(range(1,n))
        t,h=energy(n,steps)
        assert (t,h)==formula(n),(n,t,h,formula(n))
        # Directly check every coefficient in the symbolic degree-two
        # expansion, using the (-1)^s Walsh convention of the transform.
        for i,d in enumerate(difference_data(n,steps),start=1):
            assert d[0] == F(n*n + 2*n*i - n - 4*i + 2,8)
            for mask,actual in d.items():
                js = [j+1 for j in range(n) if mask & (1<<j)]
                if len(js)==1:
                    expected = F(i,4) if js[0]<i else -F(n+i-1,4)
                elif len(js)==2:
                    expected = -F(1,4) if max(js)<i else F(1,4) if min(js)>i else F(0)
                elif len(js)>=3:
                    expected = F(0)
                else:
                    continue
                assert actual==expected,(n,i,js,actual,expected)
        ratio=1-h/t
        predicted=1-F((n+1)*(25*n-18),2*n*(13*n*n-n-2))
        assert ratio==predicted
        difference=ratio-F(n-1,n)
        assert difference==F((n-2)*(n-7),2*n*(13*n*n-n-2))
        if n>=8:assert difference>0
        print('N=',n,'T=',t,'H=',h,'potential_share=',ratio,'above_affine=',difference)
    for n in range(2,7):
        psd_check(n)
        print('N=',n,'exact small-population PSD PASS')
    n=7
    t,h=energy(n,[9,8,6,4,2,1])
    assert 1-h/t == F(53454277,62354880),(1-h/t)
    print('N=7 published witness verified: share=',1-h/t)
    print('All exact-rational checks passed.')

if __name__ == '__main__':
    main()
