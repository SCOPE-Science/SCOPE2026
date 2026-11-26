#!/usr/bin/env python3
"""Exhaustively verify square-zero multiplication rank strata in k[x,y]/(x^2,y^n).
No third-party modules. Includes the extension field GF(4)."""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (2,3,4,5)
        self.q = q
        self.char = 2 if q in (2,4) else q
        self.add = (lambda a,b: a ^ b) if q==4 else (lambda a,b: (a+b)%q)
        if q==4:
            def mul(a,b):
                z=0
                while b:
                    if b&1: z ^= a
                    b >>= 1
                    a <<= 1
                    if a&4:a ^= 7 # X^2 + X + 1
                return z
            self.mul=mul
        else:
            self.mul=lambda a,b:(a*b)%q
        self.neg=lambda a: a if self.char==2 else (-a)%q
        self.inv={a:next(b for b in range(1,q) if self.mul(a,b)==1) for a in range(1,q)}


def mul_poly(a,b,F,n):
    out=[0]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:n-i]):
                if y:out[i+j]=F.add(out[i+j],F.mul(x,y))
    return out


def rank(mat,F):
    M=[row[:] for row in mat]
    nr=len(M); nc=len(M[0]); rr=0
    for c in range(nc):
        pivot=next((i for i in range(rr,nr) if M[i][c]),None)
        if pivot is None:continue
        M[rr],M[pivot]=M[pivot],M[rr]
        inv=F.inv[M[rr][c]]
        M[rr]=[F.mul(inv,v) for v in M[rr]]
        for i in range(rr+1,nr):
            factor=M[i][c]
            if factor:
                M[i]=[F.add(M[i][j],F.neg(F.mul(factor,M[rr][j]))) for j in range(nc)]
        rr+=1
        if rr==nr:break
    return rr


def mul_rank(a,b,F):
    n=len(a); M=[[0]*(2*n) for _ in range(2*n)]
    for j in range(n):
        for k in range(n-j):
            M[j+k][j]=a[k]
            M[n+j+k][j]=b[k]
            M[n+j+k][n+j]=a[k]
    return rank(M,F)


def formula_cumulative(n,q,p,r):
    if p==2:return q**(r+r//2)
    return q**r+sum((q-1)*q**(h-1)*q**min(r,n-h) for h in range(1,r//2+1))


def run_case(q,n):
    F=Field(q);hist=Counter();checked=0;sz=0
    for word in product(range(q),repeat=2*n):
        a=word[:n];b=word[n:]
        aa=mul_poly(a,a,F,n)
        ab=mul_poly(a,b,F,n)
        if any(aa) or (F.char!=2 and any(ab)):
            continue
        # Optional explicit linear-multiplication check.
        r=mul_rank(a,b,F)
        if r>n:raise AssertionError(('square zero rank bound',q,n,a,b,r))
        hist[r]+=1;checked+=1
    for r in range(n+1):
        observed=sum(hist[x] for x in range(r+1))
        predicted=formula_cumulative(n,q,F.char,r)
        if observed!=predicted:
            raise AssertionError(('cumulative mismatch',q,n,r,observed,predicted,dict(hist)))
    if checked!=sum(hist.values()):raise AssertionError('bad total')
    return checked


def main():
    cases=[(2,n) for n in range(1,7)]+[(3,n) for n in range(1,6)]+[(4,n) for n in range(1,5)]+[(5,n) for n in range(1,4)]
    c=0
    for q,n in cases:
        c+=run_case(q,n)
    print('SQUARE_ZERO_MULTIPLICATION_JORDAN_CENSUS_OK',len(cases),c)

if __name__=='__main__':main()
