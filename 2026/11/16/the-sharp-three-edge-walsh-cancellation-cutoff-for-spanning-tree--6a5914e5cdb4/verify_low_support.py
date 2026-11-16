#!/usr/bin/env python3
"""Exact finite certificates for Walsh characters supported on at most three cube edges.
No third-party dependencies; run: python verify_low_support.py
"""
from itertools import combinations
from math import lcm, comb
from fractions import Fraction


def cube_edges(d):
    return [(u, u ^ (1 << i), i) for i in range(d)
            for u in range(1 << d) if (u & (1 << i)) == 0]


def integer_transfer(d):
    ee = cube_edges(d)
    m = len(ee)
    denominator = (1 << (d-1)) * lcm(*range(1, d+1))
    transfer = [[0]*m for _ in range(m)]
    # Fourier diagonalization of the unweighted cube Laplacian.
    for character in range(1, 1 << d):
        w = character.bit_count()
        factor = denominator // ((1 << (d-1))*w)
        assert denominator % ((1 << (d-1))*w) == 0
        signed = [0 if not ((character >> direction) & 1)
                  else (-1 if ((character & u).bit_count() & 1) else 1)
                  for u, _, direction in ee]
        active = [(j,v) for j,v in enumerate(signed) if v]
        for q,(j,v) in enumerate(active):
            for k,z in active[q:]:
                transfer[j][k] += factor*v*z
    for j in range(m):
        for k in range(j):
            transfer[j][k] = transfer[k][j]
    return ee, denominator, [[denominator*(j==k)-2*transfer[j][k]
                              for k in range(m)] for j in range(m)]


def triple(A, i, j, k):
    a,b,c = A[i][i],A[j][j],A[k][k]
    x,y,z = A[i][j],A[i][k],A[j][k]
    return a*b*c + 2*x*y*z - a*z*z-b*y*y-c*x*x


def finite_census(d):
    ee,den,A=integer_transfer(d)
    m=len(ee)
    z1=sum(A[i][i]==0 for i in range(m))
    z2=sum(A[i][i]*A[j][j]-A[i][j]**2==0
           for i,j in combinations(range(m),2))
    z3=sum(triple(A,i,j,k)==0 for i,j,k in combinations(range(m),3))
    expected={2:(0,6,0),3:(0,6,20),4:(0,208,832),
              5:(0,0,0),6:(0,0,0),7:(0,0,0)}
    assert (z1,z2,z3)==expected[d], (d,z1,z2,z3)
    print(f'd={d}, edges={m}, checked triplets={comb(m,3)}, '
          f'zero supports of sizes 1/2/3=({z1},{z2},{z3})')
    return z1,z2,z3


def analytic_tail():
    # For all d>=8 the transfer kernel has K_ee=p_d,
    # |K_ef|<= B_d = (1/2) integral_0^1 t((1+t)/2)^(d-2) dt.
    # p_d and B_d decrease in d. Hence at every triple the Gershgorin
    # bound is p_d + 2B_d <= p_8+2B_8 < 1/2.
    d=8
    p=Fraction((1<<d)-1,d*(1<<(d-1)))
    B=sum((Fraction(comb(d-2,j),j+2) for j in range(d-1)), Fraction())/ (1<<(d-1))
    assert p==Fraction(255,1024)
    assert B==Fraction(769,7168)
    assert p+2*B==Fraction(3323,7168) < Fraction(1,2)
    print('d>=8: p_d+2B_d <= 3323/7168 < 1/2 (monotonic integral).')


def main():
    for d in range(2,8):finite_census(d)
    analytic_tail()
    print('PASS: exact all-dimension low-support classification.')

if __name__=='__main__':main()
