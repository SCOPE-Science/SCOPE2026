#!/usr/bin/env python3
"""Exact finite consistency checks for the three-dimensional twisted baker map."""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import comb

M=3
L=((2,0,0),(0,1,0),(0,0,1))
R=((0,0,-2),(1,0,0),(0,1,0))

def prod(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(M)) for j in range(M)) for i in range(M))

def count_expected(n):
    return sum(comb(n,j) for j in range(0,n+1,3))-1

all_words=0; real_words=0
for n in range(3,12):
    real_count=0
    for w in product((0,1),repeat=n):
        if not any(w):
            continue
        A=((1,0,0),(0,1,0),(0,0,1))
        r=0
        occupancy=[0,0,0]
        for bit in w:
            A=prod(R if bit else L,A)
            r=(r+bit)%3
            occupancy[r]+=1
        if r==0:
            assert all(A[i][j]==0 for i in range(3) for j in range(3) if i!=j)
            for i in range(3):
                assert abs(A[i][i])==2**occupancy[(-i)%3]
            assert sum(occupancy)==n
            real_count+=1
        else:
            # A signed 3-cycle, with cube scalar; its eigenvalues are not all real.
            B=prod(prod(A,A),A)
            assert all(B[i][j]==0 for i in range(3) for j in range(3) if i!=j)
            assert B[0][0]==B[1][1]==B[2][2]
        all_words+=1
    assert real_count==count_expected(n),(n,real_count,count_expected(n))
    real_words+=real_count
# For a cyclic 3-state lazy walk, P^k has geometrically decaying centered part.
P=((Fraction(1,2),Fraction(1,2),Fraction(0)),
   (Fraction(0),Fraction(1,2),Fraction(1,2)),
   (Fraction(1,2),Fraction(0),Fraction(1,2)))
assert all(sum(row)==1 for row in P)
# The Green-Kubo symmetric correction sums to zero:
# P/(I-P) = (S-I)^{-1}(S+I) on the mean-zero subspace, skew-symmetric there.
def mul3(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
center=[[Fraction(1 if i==j else 0)-Fraction(1,3) for j in range(3)]for i in range(3)]
Ppower=[[Fraction(int(i==j)) for j in range(3)]for i in range(3)]
for k in range(1,13):
    Ppower=mul3(Ppower,P)
    assert all(sum(Ppower[i][j] for j in range(3))==1 for i in range(3))
print('TWISTED_BAKER_3D_OCCUPATION_CHECK_OK', 'all_words=',all_words,'real_words=',real_words)
