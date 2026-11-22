#!/usr/bin/env python3
"""Reproduce Fibonomial ternary triangular-spectrum identities using only Python 3."""
from collections import Counter
from math import comb

# Small integer-polynomial arithmetic in coefficient-list representation.
def add(a, b):
    z = [0] * max(len(a), len(b))
    for i, v in enumerate(a): z[i] += v
    for i, v in enumerate(b): z[i] += v
    return trim(z)

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)

def scale(a, m): return trim([m*x for x in a])
def matmul(A, B):
    assert len(A[0]) == len(B)
    return [[trim(sum_polys([mul(A[i][j], B[j][k]) for j in range(len(B))])) for k in range(len(B[0]))] for i in range(len(A))]

def sum_polys(ps):
    result = [0]
    for p in ps: result = add(result, p)
    return result

def identity(d): return [[[int(i == j)] for j in range(d)] for i in range(d)]

T = [[[6], [0,3]], [[3], [0,6]]]
M = [[[0,3], [3], [0,3]], [[0], [6], [0,3]], [[0], [3], [0,6]]]
# Verify the 3-state matrix independently from digit-pair enumeration.
M_generated = [[[0] for _ in range(3)] for _ in range(3)]
for state in range(3):
    for a in range(3):
        for b in range(3):
            incoming_carry = 1 if state == 2 else 0
            outgoing_carry = (a+b+incoming_carry)//3
            if state == 0 and b == 0:
                dest, exponent = 0, 1
            else:
                dest = 1+outgoing_carry
                exponent = outgoing_carry
            M_generated[state][dest] = add(M_generated[state][dest], [0]*exponent+[1])
assert M == M_generated, (M, M_generated)

# Matrix powers give A_L and B_L independently of rational-function recurrence.
TP = identity(2)
MP = identity(3)
Hs = []
for L in range(7):
    A, B = TP[0][0], MP[0][1]
    H = add(scale(A,10), mul([0,6],B))
    Hs.append(H)
    assert sum(H) == (4*3**L)*(4*3**L+1)//2, (L,H)
    assert H[0] == 10*6**L, (L,H)
    if L >= 1:
        assert len(H) == L+1 and H[L] == 18*6**(L-1), (L,H)
    if L >= 2:
        rhs = add(scale(Hs[L-1],6), mul([0,6],Hs[L-1]))
        rhs = add(rhs, scale(mul([0,1],Hs[L-2]),-27))
        assert H == rhs, (L,H,rhs)
    TP=matmul(TP,T); MP=matmul(MP,M)
assert Hs[0] == [10]
assert Hs[1] == [60,18]
assert Hs[2] == [360,198,108]

# Directly calculate Fibonacci numbers and all Fibonomial factorial valuations.
# This is independent of the Kummer and transfer-matrix derivation.
max_m=4*3**5-1
fib=[0,1]
for n in range(2,max_m+1): fib.append(fib[-1]+fib[-2])
factorial_v=[0]*(max_m+1)
def v3(a):
    out=0
    while a%3==0:
        out+=1; a//=3
    return out
for n in range(1,max_m+1): factorial_v[n]=factorial_v[n-1]+v3(fib[n])
for L in range(6):
    N=4*3**L
    hist=[0]*(L+1)
    for n in range(N):
        for k in range(n+1):
            exp=factorial_v[n]-factorial_v[k]-factorial_v[n-k]
            assert 0<=exp<=L,(n,k,exp,L)
            hist[exp]+=1
    assert hist==Hs[L], (L,hist,Hs[L])
    print('L=',L,'rows=',N,'Fibonomial entries=',N*(N+1)//2,'histogram=',hist)
# Validate the elementary v3(F_n) formula for all usable n.
for n in range(1,max_m+1):
    expected=0 if n%4 else 1+v3(n//4)
    assert v3(fib[n])==expected
print('PASS: elementary Fibonacci valuations, all triangular fibers (L=0..5), digit transitions, rational recurrence (L=0..6).')
