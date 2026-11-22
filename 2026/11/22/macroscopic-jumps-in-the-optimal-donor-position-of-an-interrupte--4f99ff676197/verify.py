#!/usr/bin/env python3
"""Exact consistency checks for a finite-flower pollen-transfer benchmark.

Standard library only. Finite checks supplement the analytical proof; they
are not a certificate of the asymptotic theorem.
"""
from fractions import Fraction as Q
from math import log, ceil


def direct(n, j, q, r, w):
    """Enumerate every possible length of a pollinator's visit sequence."""
    assert 1 <= j <= n and Q(0) < q < Q(1) and Q(0) < r < Q(1)
    female, exported = Q(0), Q(0)
    for length in range(1, n + 1):
        prob = q ** (length - 1) * (1-q if length < n else 1)
        deposited = sum((1-r) * r ** (i-1) for i in range(1, min(j, length + 1)))
        female += prob * deposited
        if length >= j:
            exported += prob * r ** (length-j)
    return w*female + exported


def closed(n, j, q, r, w):
    d = 1-q*r
    return (w*(1-r)+(1-q)*q**(j-1)-w*(1-r)*(q*r)**(j-1)
            +(1-r)*q**n*r**(n-j))/d


def difference(n, j, q, r, w):
    g = (w*(1-r)*(1-q*r)*r**(j-1)-(1-q)**2
         +q*q*(1-r)**2*(q*r)**(n-j-1))
    return q**(j-1)*g/(1-q*r)


def test():
    count=0
    for n in range(2, 14):
        for qi in (1,2,3,5,7,8,9):
            q=Q(qi,10)
            for ri in (1,3,5,8,9):
                r=Q(ri,10)
                for wi in (1,2,5):
                    w=Q(wi,3)
                    vals=[]
                    for j in range(1,n+1):
                        a=direct(n,j,q,r,w)
                        b=closed(n,j,q,r,w)
                        assert a == b, (n,j,q,r,w,a,b)
                        count+=1
                        vals.append(b)
                    for j in range(1,n):
                        assert vals[j]-vals[j-1] == difference(n,j,q,r,w)
                        count+=1
    # Strict, exact sign witness for a jump spanning six positions.
    n=10; r=Q(1,2); w=Q(1)
    lo=Q(791094,1000000); hi=Q(791095,1000000)
    lo_scores=[closed(n,j,lo,r,w) for j in range(1,n+1)]
    hi_scores=[closed(n,j,hi,r,w) for j in range(1,n+1)]
    assert lo_scores[9] < lo_scores[3]
    assert hi_scores[9] > hi_scores[3]
    # On 0<=q<=1, |dF_j/dq|<155 for n=10: bound each
    # female term by sum_{i=1}^{n-1} i <=45, each export term
    # derivative by <=n, at most n such terms, plus final <=n.
    # Therefore |d(F_4-F_j)/dq| < 400 for each j.
    width=hi-lo
    for j in range(1,10):
        if j==4:continue
        assert lo_scores[3]-lo_scores[j-1] > Q(400)*width,(j,float(lo_scores[3]-lo_scores[j-1]))
        count+=1
    # At the root of F_10-F_4 in this bracket, both dominate
    # every other position by the derivative bound and IVT.
    from math import isfinite
    for n in (60,100,200,500,1000):
        K=4/(-log(.5))
        J=min(n-1,ceil(K*log(n)))
        assert J<n
        for factor in (2.,.5):
            qf=1-factor*log(n)/n
            rf=.5; wf=1.
            d=1-qf*rf
            def fl(j):
                return (wf*(1-rf)+(1-qf)*qf**(j-1)-wf*(1-rf)*(qf*rf)**(j-1)
                    +(1-rf)*qf**n*rf**(n-j))/d
            v=[fl(j) for j in range(1,n+1)]
            assert all(isfinite(x) for x in v)
            # For sufficiently large n this confirms the proved endpoint regimes.
            if n>=500:
                if factor==2.: assert v[-1] < max(v[:J])
                else: assert v[-1] > max(v[:-1])
            count+=1
    print('PASS:',count,'exact or numerical consistency assertions.')
    print('n=10 coexistence root bracket:',lo,hi)
    print('All other n=10 positions are strictly dominated over the bracket.')
    print('The large-n claim follows analytically, not from these finite cases.')


if __name__ == '__main__':
    test()
