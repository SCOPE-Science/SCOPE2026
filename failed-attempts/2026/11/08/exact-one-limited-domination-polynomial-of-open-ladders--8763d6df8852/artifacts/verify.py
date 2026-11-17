#!/usr/bin/env python3
"""Exact standard-library verification of the one-limited ladder polynomial.
Polynomial coefficients are Python integers; no numerical tolerance is used.
"""
from collections import defaultdict
from itertools import product
from math import comb

# Univariate integer polynomials in z, stored as tuples.
def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return tuple(p)
def add(p,q):
    n=max(len(p),len(q));return trim(tuple((p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)))
def neg(p):return tuple(-a for a in p)
def sub(p,q):return add(p,neg(q))
def mul(p,q):
    if not p or not q:return ()
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if a:
            for j,b in enumerate(q):
                if b:out[i+j]+=a*b
    return trim(out)
def zp(k,c=1):return (0,)*k+(c,) if c else ()
Z=();ONE=(1,)
def times_shift(p,k):return (0,)*k+p if p else ()

def valid(l,c,r):
    for row in range(2):
        selected=(c>>row)&1
        ns=[(c>>(1-row))&1]
        if l is not None:ns.append((l>>row)&1)
        if r is not None:ns.append((r>>row)&1)
        if selected:
            if len(ns)-sum(ns)>1:return False
        elif sum(ns)<1:return False
    return True

states=[(a,b) for a in range(4) for b in range(4)]
pos={q:i for i,q in enumerate(states)}
N=len(states)
trans=[[] for _ in states];L=[Z]*N;R=[0]*N
for i,(a,b) in enumerate(states):
    if valid(None,a,b):L[i]=zp(a.bit_count()+b.bit_count())
    if valid(a,b,None):R[i]=1
    for c in range(4):
        if valid(a,b,c):trans[i].append((pos[(b,c)],c.bit_count()))
assert sum(map(len,trans))==26

def vector_coeffs(k):
    v=[ONE if x else Z for x in R]
    out=[]
    for j in range(k+1):
        out.append(sum_poly(mul(L[i],v[i]) for i in range(N)))
        v2=[Z]*N
        for i in range(N):
            for dst,shift in trans[i]:v2[i]=add(v2[i],times_shift(v[dst],shift))
        v=v2
    return out

def sum_poly(ps):
    p=Z
    for q in ps:p=add(p,q)
    return p

def poly_lambda_mul(a,b):
    out=[Z]*(len(a)+len(b)-1)
    for i,p in enumerate(a):
        for j,q in enumerate(b):out[i+j]=add(out[i+j],mul(p,q))
    return out

# An explicit annihilating polynomial H(lambda,z) for the 16-state T.
# T is the transition matrix with entries z^(number of new selected vertices).
H=[Z]*8+[ONE]
H=poly_lambda_mul(H,[neg(zp(1)),ONE])
H=poly_lambda_mul(H,[zp(3),neg(zp(1)),ONE])
# B(lambda)=lambda^5-z^2 lambda^4-z^3 lambda^3
# -(z^5+2z^4)lambda^2 -(z^6+z^5+z^4)lambda-z^6
B=[neg(zp(6)),neg(add(add(zp(6),zp(5)),zp(4))),neg(add(zp(5),zp(4,2))),neg(zp(3)),neg(zp(2)),ONE]
H=poly_lambda_mul(H,B)
assert len(H)==17 and H[-1]==ONE

# Horner evaluation of H(T) with sparse right-multiplication by T.
def check_annihilator():
    M=[[Z for _ in range(N)] for __ in range(N)]
    for coef in reversed(H):
        nxt=[[Z for _ in range(N)] for __ in range(N)]
        for row in range(N):
            for i in range(N):
                p=M[row][i]
                if not p: continue
                for dst,shift in trans[i]:
                    nxt[row][dst]=add(nxt[row][dst],times_shift(p,shift))
            nxt[row][row]=add(nxt[row][row],coef)
        M=nxt
    assert all(not p for row in M for p in row),"The proposed exact annihilator failed"
    print('EXACT_MATRIX_POLYNOMIAL_IDENTITY_OK dimension=16 degree=16')

check_annihilator()

# Q(t,z) in increasing t-degree, denominator of the ladder generating function.
Q=[ONE,neg(zp(2)),neg(zp(3)),neg(add(zp(5),zp(4,2))),neg(add(add(zp(6),zp(5)),zp(4))),neg(zp(6))]
# The finite recurrence-verification step is rigorous because H is monic of degree 16.
A=vector_coeffs(21)
for j in range(16):
    residual=sum_poly(mul(Q[i],A[j+5-i]) for i in range(6))
    assert not residual,('recurrence fails',j,residual)
print('EXACT_ORDER_FIVE_RECURRENCE_OK first_16_residuals_and_annihilator')
num=[sum_poly(mul(Q[i],A[j-i]) for i in range(j+1)) for j in range(5)]
expected=[
    add(add(zp(4),zp(3,4)),zp(2,4)),
    add(add(zp(5,2),zp(4,5)),zp(3,2)),
    sum_poly([zp(7),zp(6,5),zp(5,6),zp(4,4)]),
    sum_poly([zp(8),zp(7,3),zp(6,5),zp(5,2)]),
    add(zp(8),zp(7,2))
]
assert num==expected,(num,expected)
print('EXACT_RATIONAL_NUMERATOR_OK degrees_t=0..4')

# Independent subset-check of the original definition, not the transfer rule.
def brute(n):
    edges=[]
    for i in range(n):edges.append((2*i,2*i+1))
    for i in range(n-1):
        for r in range(2):edges.append((2*i+r,2*(i+1)+r))
    nei=[set() for _ in range(2*n)]
    for a,b in edges:nei[a].add(b);nei[b].add(a)
    counts=defaultdict(int)
    for bits in range(1<<(2*n)):
        if all((bits>>v&1) or any(bits>>u&1 for u in nei[v]) for v in range(2*n)) and all(not(bits>>v&1) or sum(not(bits>>u&1) for u in nei[v])<=1 for v in range(2*n)):
            counts[bits.bit_count()]+=1
    return trim(tuple(counts[i] for i in range(2*n+1)))
for n in range(2,9):
    assert A[n-2]==brute(n),n
    count=A[n-2][n]
    assert count==(4 if n%2==0 else 2)
    assert not any(A[n-2][:n]),n
print('DIRECT_SUBSET_ENUMERATION_OK n=2..8')
for n in range(2,80):
    p=vector_coeffs(n-2)[n-2]
    assert p[n]==(4 if n%2==0 else 2)
    assert not any(p[:n])
print('MINIMUM_PATTERN_AND_COUNTS_OK n=2..79')
print('VERIFY_OK')
