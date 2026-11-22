#!/usr/bin/env python3
"""Independent integer-recurrence verification of the rational enumerator.
No external dependencies. Finite arithmetic checks supplement the proof.
"""
from math import comb


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def edge_coefficients(q,r,nmax):
    # Compute z^2 binom(q,2) N(z)^2 / ((1-z) D(z)^2)
    S=[0]+[1]*r
    D=[1]+[-(q-1)]*r
    N=[1]+[1]*(r-1)+[-1]   # 1 + (z+...+z^r) - 2 z^r
    P=multiply([1,-1],multiply(D,D))
    numerator=[0,0]+[comb(q,2)*a for a in multiply(N,N)]
    numerator += [0]*max(0,nmax+1-len(numerator))
    out=[0]*(nmax+1)
    for n in range(nmax+1):
        out[n]=numerator[n]-sum(P[j]*out[n-j] for j in range(1,min(n,len(P)-1)+1))
    return out


def context_dp(q,r,nmax):
    # Prefix DP using the length of the final monochromatic run.
    H=[1]
    tails=[0]*(r+1)
    for n in range(1,nmax+1):
        new=[0]*(r+1)
        new[1]=q if n==1 else (q-1)*sum(tails)
        for t in range(2,r+1):new[t]=tails[t-1]
        tails=new
        # Symmetry makes exactly 2/q of max-length runs end in a fixed pair.
        H.append(sum(tails)-2*(tails[r]//q))
        assert tails[r]%q == 0
    return H


def check(q,r,nmax):
    H=context_dp(q,r,nmax)
    K=[sum(H[i]*H[k-i] for i in range(k+1)) for k in range(nmax+1)]
    by_boundary=[0]*(nmax+1)
    for n in range(2,nmax+1):
        by_boundary[n]=comb(q,2)*sum(K[k] for k in range(n-1))
    via_rational=edge_coefficients(q,r,nmax)
    assert via_rational == by_boundary,(q,r,via_rational,by_boundary)
    assert via_rational[2] == comb(q,2)
    return via_rational


if __name__=='__main__':
    for q in range(2,10):
        for r in range(1,9):
            val=check(q,r,100)
            print(f'q={q} r={r} n=2,6,12: {val[2]}, {val[6]}, {val[12]}')
    assert check(2,2,12) == [0,0,1,5,13,29,61,121,233,437,805,1461,2621]
    print('ALL 64 PARAMETER SETS / ALL LENGTHS THROUGH 100 MATCHED')
