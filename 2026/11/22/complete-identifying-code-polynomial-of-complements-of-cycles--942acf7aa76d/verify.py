#!/usr/bin/env python3
"""Exact verification of the co-cycle identifying-code enumeration theorem.
Requires Python 3 and SymPy (for the 16-state determinant)."""
from collections import Counter, defaultdict
from math import comb
import sympy as sp

x, z, t = sp.symbols('x z t')
M = sp.zeros(16)
for state in range(16):
    a, b, c, d = ((state >> j) & 1 for j in (3, 2, 1, 0))
    for e in (0, 1):
        if c == 1 and a == 0 and e == 0:
            continue
        successor = ((state & 7) << 1) | e
        M[state, successor] += z**c * t**int(b == 0 and d == 0)
D = (sp.eye(16) - x*M).det(method='domain-ge')
F = (1-z*x-z*z*x**3+t*(z*x*x-x))*(1+z**3*x**4-z**4*x**6+t*(z*z*x**4-z*x*x))
assert sp.expand(D-F) == 0
print('DETERMINANT_IDENTITY_OK')

def independently_identifies(n, code):
    masks = []
    for v in range(n):
        closed = ((1<<n)-1) ^ (1<<((v-1)%n)) ^ (1<<((v+1)%n))
        sig=closed & code
        if sig==0:
            return False
        masks.append(sig)
    return len(set(masks))==n

def local_conditions(n,code):
    empty=0
    for i in range(n):
        if not ((code >> ((i-1)%n))&1) and not ((code >> ((i+1)%n))&1):
            empty+=1
        if ((code>>i)&1) and not ((code>>((i-2)%n))&1) and not ((code>>((i+2)%n))&1):
            return False
    return empty<=1

def trace_counts(n):
    counts=Counter()
    for s in range(16):
        states={(s,0,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (u,w,k),qty in states.items():
                a,b,c,d=((u>>j)&1 for j in (3,2,1,0))
                for e in (0,1):
                    if c and not(a or e): continue
                    k2=k+int(b==0 and d==0)
                    if k2>1:continue
                    nxt[(((u&7)<<1)|e,w+c,k2)]+=qty
            states=nxt
        for (u,w,k),qty in states.items():
            if u==s: counts[w]+=qty
    return counts

def A(m):
    counts=Counter({m:1})
    for r in range(1,m//3+1):
        counts[m-r]+=m*comb(m-2*r-1,r-1)//r
    return counts

def B(m):
    counts=Counter()
    for r in range(0,(m-4)//3+1):
        counts[m-r-2]+=m*comb(m-2*r-4,r)
    return counts

def mul(p,q):
    c=Counter()
    for a,u in p.items():
        for b,v in q.items():c[a+b]+=u*v
    return c

def binomial_formula(n):
    if n%2:return A(n)+B(n)
    m=n//2
    u=mul(A(m),A(m))
    for k,v in mul(A(m),B(m)).items():u[k]+=2*v
    return u

for n in range(5,17):
    brute=Counter()
    for code in range(1<<n):
        truth=independently_identifies(n,code)
        assert truth==local_conditions(n,code), (n,code)
        if truth: brute[code.bit_count()]+=1
    transfer=trace_counts(n)
    assert brute==transfer==binomial_formula(n), (n,brute,transfer,binomial_formula(n))
    print('EXHAUSTIVE_OK',n,'minimum',min(brute),'minimum_count',brute[min(brute)],'total',sum(brute.values()))
print('BINOMIAL_AND_TRANSFER_OK')
print('VERIFY_OK')
