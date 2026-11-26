"""Exact finite-state checks for the stationary SIS mode-onset result.

Run with: python3 checker.py
Only standard-library modules are needed. All finite computations use Fraction.
"""
from fractions import Fraction as F
from random import Random
from math import floor, sqrt


def ratios(n, a, b):
    return [F(n-k,k+1)*(a+b*k) for k in range(n)]


def threshold(n, a):
    return min(((F(k+1)-a*(n-k))/F(k*(n-k)), k) for k in range(1,n))


def minimizer_candidates(n,a):
    C=1-float(a)*n
    B=1+float(a)
    x=(sqrt(C*(n+1))-C)/B
    low=max(1,min(n-1,floor(x)))
    return {low,max(1,min(n-1,low+1))},x


def weights(n,a,b):
    w=[F(1)]
    for r in ratios(n,a,b):
        w.append(w[-1]*r)
    return w


def local_modal_components(w):
    # Collapse maximal constant runs before counting local maxima.
    parts=[]
    i=0
    while i<len(w):
        j=i
        while j+1<len(w) and w[j+1]==w[i]:
            j+=1
        if (i==0 or w[i]>w[i-1]) and (j==len(w)-1 or w[j]>w[j+1]):
            parts.append((i,j))
        i=j+1
    return parts


def run():
    checks=0
    rng=Random(41093)
    for n in range(2,37):
        for t in range(31):
            # Allow both sides of the boundary a=1/n and equality.
            a=F(rng.randrange(1,4*n+3),n*(4*n+3))
            if t%5==0: a=F(1,n)
            b=F(rng.randrange(1,300),rng.randrange(100,450))
            rr=ratios(n,a,b)
            w=weights(n,a,b)
            for k in range(n):
                assert w[k+1]/w[k]==rr[k]
                # Stationary detailed balance with death rate k+1.
                assert w[k]*(n-k)*(a+b*k)==w[k+1]*(k+1)
                checks+=2
            if a<F(1,n):
                tc, arg=threshold(n,a)
                candidates,x=minimizer_candidates(n,a)
                assert arg in candidates
                assert all((rr[k]>1)==(b>((F(k+1)-a*(n-k))/F(k*(n-k)))) for k in range(1,n))
                assert (any(rr[k]>1 for k in range(1,n)))==(b>tc)
                assert (w[1]<w[0])
                assert len(local_modal_components(w))==(2 if b>tc else 1)
                checks+=5
            else:
                assert len(local_modal_components(w))==1
                checks+=1
            # The positive adjacent-ratio indices form an interval.
            pos=[k for k in range(n) if rr[k]>1]
            assert pos==list(range(min(pos),max(pos)+1)) if pos else True
            checks+=1
    n=16;a=F(1,32);b=F(1,10)
    assert threshold(n,a)==(F(41,448),2)
    assert local_modal_components(weights(n,a,b))==[(0,0),(5,5)]
    assert ratios(n,a,b)[1]==F(63,64)
    assert ratios(n,a,b)[2]==F(259,240)
    assert ratios(n,a,b)[5]==F(187,192)
    checks+=5
    print('PASS exact-rational checks:',checks)
    print('n=16, a=1/32, b=1/10: threshold=41/448, modes={0,5}')
    print('The continuum and large-n asymptotic parts are proved analytically, not by this finite test.')

if __name__=='__main__':
    run()
