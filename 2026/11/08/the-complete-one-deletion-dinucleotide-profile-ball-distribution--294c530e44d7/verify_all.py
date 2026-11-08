#!/usr/bin/env python3
"""Exact integer certificate for binary single-deletion dinucleotide-profile balls.

No third-party modules. Execute: python3 verify_all.py
"""
from collections import defaultdict
from math import comb

# All polynomials are low-degree coefficient vectors in ascending order.
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def prod(*args):
    x=[1]
    for a in args:x=mul(x,a)
    return x

def factor_poly(inner, offset, scalar):
    return [0]*offset + [scalar*v for v in inner]

zminus=[-1,1]; zplus=[1,1]; twozminus=[-1,2]
f1=[1,-1,1]        # 1-z+z^2
f2=[-1,1,1]        # -1+z+z^2
f3=[-1,1,0,1]      # -1+z+z^3
f4=[-1,2,-1,1]     # -1+2z-z^2+z^3
D3=prod(zminus,zplus,f1,f2,f3,f4)
D4=mul(D3,twozminus)
FORMULAS={
 1:(factor_poly([-2,1],2,2),zminus),
 2:(factor_poly([-2,1,1,2,2],3,-2),prod(f2,f3)),
 3:(factor_poly([1,-1,-4,7,-5,0,1,8,-9,9,-5,1],3,2),D3),
 4:(factor_poly([3,-13,20,-18,29,-67,99,-81,48,-24,3],5,-2),D4),
 5:(factor_poly([2,-6,9,-29,77,-107,86,-51,28,-9,1],6,-2),D4),
 6:(factor_poly([-6,24,-36,30,-20,12,-6,1],9,2),D4),
}

# Bit-pair indices 00,01,10,11. Six distinct deletion-induced changes:
# A: -00, B: -11, C: +00-01-10, D: +11-01-10,
# E: -01 (boundary), F: -10 (boundary).
END=(0,4,5,1)
TRI=(0,0,2,1,0,3,1,1) # abc indexed 4*a+2*b+c

def distribution(N):
    """Counts from exact finite feature automaton, including n=0,1 zero rows."""
    result=[[0]*7 for _ in range(N+1)]
    if N<2:return result
    states={(p,1<<END[p]):1 for p in range(4)}
    for n in range(2,N+1):
        for (p,mask),weight in states.items():
            final_mask=mask | (1<<END[p])
            result[n][final_mask.bit_count()]+=weight
        assert sum(result[n])==2**n,(n,'word-count-conservation')
        if n==N:break
        nxt=defaultdict(int)
        for (p,mask),weight in states.items():
            for c in (0,1):
                q=(p%2)*2+c
                t=2*p+c
                nxt[(q,mask | (1<<TRI[t]))]+=weight
        states=nxt
    return result

def gf_coeffs(num,den,N):
    assert den[0] in (-1,1)
    coef=[0]*(N+1)
    for n in range(N+1):
        rest=sum(den[k]*coef[n-k] for k in range(1,min(n,len(den)-1)+1))
        v=(num[n] if n<len(num) else 0)-rest
        assert v%den[0]==0
        coef[n]=v//den[0]
    return coef

def main():
    # The all-length proof: an allowed-feature subset T gives a 4x4 rational
    # transfer matrix; its denominator has degree <=4 and numerator <=5.
    # 64 such terms imply degree(P)<=257 and degree(Q)<=256 for each distribution GF.
    # For the six target rational functions below, deg(P)<=16, deg(Q)<=13.
    # Cross-multiplied differences have degree <=max(257+13,256+16)=272.
    # Matching coefficients 0..279 forces that polynomial to vanish identically.
    N=279
    assert max(len(p)-1 for p,q in FORMULAS.values())<=16
    assert max(len(q)-1 for p,q in FORMULAS.values())<=13
    dp=distribution(N)
    for j in range(1,7):
        num,den=FORMULAS[j]
        expected=gf_coeffs(num,den,N)
        for n in range(N+1):
            assert dp[n][j]==expected[n],(j,n,dp[n][j],expected[n])
    assert next(n for n in range(2,N+1) if dp[n][6])==9
    print('ALL_SIX_RATIONAL_GFS_VERIFIED_BY_DEGREE_BOUND')
    print('DEGREE_BOUND=272 COEFFICIENTS_TESTED=0..279')
    print('MAXIMUM=6 FIRST_AT_LENGTH=9')
    for n in range(2,15):
        print('n=',n,'profile_ball_size_distribution=',dp[n][1:7])
    print('VERIFY_OK')

if __name__=='__main__':main()
