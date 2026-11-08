#!/usr/bin/env python3
"""Exact Cartier-coefficient checks for a genus-four dihedral hyperelliptic pencil.

Uses only the Python standard library. Computations are corroborative; the
all-prime assertions in the accompanying proof use modular exponents.
"""
from math import comb

P = 7

def pa_add(a, b, p):
    n = max(len(a), len(b))
    return tuple(( (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n))

def pa_mul(a, b, p):
    out = [0] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return tuple(out)

def poly_mul(a, b, p):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            prod = pa_mul(u,v,p)
            out[i+j] = pa_add(out.get(i+j,()),prod,p)
    return out

def matrix_at_prime(p):
    base = {0:(1,),5:(0,1),10:(1,)}
    power = {0:(1,)}
    for _ in range((p-1)//2):
        power = poly_mul(power,base,p)
    return [[power.get(i*p-j,()) for j in range(1,5)] for i in range(1,5)]

M = matrix_at_prime(7)
z=(0,)
a=(0,3)
b=(3,0,3)
expected = [[z,a,z,z],[z,z,z,b],[b,z,z,z],[z,z,a,z]]
assert all(all((tuple(row[j])+(0,)*5)[:5] == (tuple(expected[i][j])+(0,)*5)[:5] for j in range(4)) for i,row in enumerate(M))

for p in (3,7,13,17,23,37,43):
    if p%5 not in (2,3):
        continue
    rows=matrix_at_prime(p)
    for i in range(1,5):
        for j in range(1,5):
            if j != (p*i)%5:
                assert not any(rows[i-1][j-1]), (p,i,j)
    j_sequence=[]
    cur=1
    for _ in range(4):
        j_sequence.append(cur)
        cur=(p*cur)%5
    assert cur==1 and len(set(j_sequence))==4

# Hasse--Witt ranks at the explicit exceptional algebraic parameters.
# In F_49 = F_7[t]/(t*t+1), t is a root of a^2+1.
def value(coeffs, x):
    v=(0,0)
    for c in reversed(coeffs):
        v=((v[0]*x[0]-v[1]*x[1]+c)%7,(v[0]*x[1]+v[1]*x[0])%7)
    return v

for x,rank in [((0,0),2),((0,1),2),((0,6),2),((1,0),4),((2,0),4),((3,0),4)]:
    nonzero=sum(value(M[i][j],x)!=(0,0) for i in range(4) for j in range(4))
    # A monomial matrix has rank equal to its number of nonzero entries.
    assert nonzero==rank,(x,nonzero,rank)

print('PASS: exact genus-four Cartier matrix, 4-cycle support, 3 exceptional parameters')
