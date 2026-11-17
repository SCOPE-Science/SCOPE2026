#!/usr/bin/env python3
"""Finite boundary certificate for a cyclic Rule-22 maximum-preimage theorem.
Pure Python 3; uses only integer arithmetic.  Prints verification results.
"""
from itertools import combinations

Z = ((1,0,0,0),(0,0,0,1),(0,1,0,0),(0,0,1,1))
O = ((0,1,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
I = tuple(tuple(int(i==j) for j in range(4)) for i in range(4))

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))

def trace(a):
    return sum(a[i][i] for i in range(4))

def fiber(seq):
    a=I
    for bit in seq:
        a=mm(a,O if bit else Z)
    return trace(a)

zero_counts=[]
checked=0
closest=[]
for n in range(1,25):
    best0=fiber((0,)*n)
    zero_counts.append(best0)
    best_other=-1
    for k in range(1,min(3,n)+1):
        for pos in combinations(range(n),k):
            s=[0]*n
            for j in pos:s[j]=1
            count=fiber(s)
            checked+=1
            best_other=max(best_other,count)
            assert count < best0,(n,pos,count,best0)
    closest.append((n,best0,best_other))
# Trace(Z**n) = 1 + T_n with T_1=T_2=1, T_3=4 and T_(n+3)=T_(n+2)+T_n.
T={0:3,1:1,2:1}
for n in range(3,25): T[n]=T[n-1]+T[n-3]
for n in range(1,25): assert zero_counts[n-1] == 1+T[n],(n,zero_counts[n-1],T[n])
print('FINITE_BOUNDARY_PASS',checked,'cases', 'n=1..24')
print('COUNTS_N1_TO12',zero_counts[:12])
print('MIN_GAP',min(u-v for _,u,v in closest))
print('LAST_BOUNDARY',closest[-1])
