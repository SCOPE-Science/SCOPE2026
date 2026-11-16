#!/usr/bin/env python3
"""Exact spectrum certificate for four harmonic planes over the seven-cycle.

Uses the ring Z[u,v]/(1+u+...+u^6,1+v+v^2), with u^7=v^3=1.
No floating point operation occurs in the certification itself.
"""
import itertools
from collections import Counter
from math import comb

Z=(0,)*12
ONE=(1,)+(0,)*11

def basis(exponent7=0, exponent3=0):
    i=exponent7%7; j=exponent3%3
    a=((-1,)*6) if i==6 else tuple(int(t==i) for t in range(6))
    if j==0: return a+(0,)*6
    if j==1: return (0,)*6+a
    return tuple(-v for v in a+a)

PROD=[]
for ia in range(12):
    row=[]
    for ib in range(12):
        row.append(basis((ia%6)+(ib%6),(ia//6)+(ib//6)))
    PROD.append(row)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def scale(a,n):return tuple(x*n for x in a)
def mul(a,b):
    c=[0]*12
    for i,ai in enumerate(a):
        if not ai: continue
        for j,bj in enumerate(b):
            if not bj: continue
            d=PROD[i][j]; n=ai*bj
            for k in range(12): c[k]+=n*d[k]
    return tuple(c)

def matmul(A,B):
    n=len(A); out=[[Z]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]==Z: continue
            for j in range(n):
                if B[k][j]==Z: continue
                out[i][j]=add(out[i][j],mul(A[i][k],B[k][j]))
    return out

def trace(A):return tuple(sum(A[i][i][j] for i in range(len(A))) for j in range(12))

char_exponents={1:0,2:2,3:1,4:1,5:2,6:0}

def matrix_B(S):
    hh=[]
    for d in range(7):
        z=Z
        for m in S: z=add(z,basis(m*d,0))
        hh.append(z)
    B=[]
    for u in range(7):
        row=[]
        for v in range(7):
            if not u and not v: q=scale(ONE,12)
            elif not u: q=scale(ONE,12)
            elif not v: q=scale(ONE,5)
            else: q=add(scale(ONE,5),scale(basis(0,char_exponents[v]-char_exponents[u]),7))
            row.append(mul(q,hh[(u-v)%7]))
        B.append(row)
    return B

def characteristic(B):
    n=len(B); powers=[None]
    Bk=[row[:] for row in B]
    for k in range(1,n+1):
        powers.append(trace(Bk))
        if k<n: Bk=matmul(Bk,B)
    elem=[ONE]
    for k in range(1,n+1):
        rhs=Z
        for i in range(1,k+1):
            z=mul(elem[k-i],powers[i])
            rhs=add(rhs,z if i%2 else neg(z))
        assert all(c%k==0 for c in rhs),(k,rhs)
        elem.append(tuple(c//k for c in rhs))
    coeff=[elem[k] if k%2==0 else neg(elem[k]) for k in range(n+1)]
    assert all(t[1:]==(0,)*11 for t in coeff),coeff
    return tuple(t[0] for t in coeff)

def expected_coeffs():
    # polynomial coefficients descending in t, implemented without symbolic tools
    def mp(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):z[i+j]+=x*y
        return z
    # low to high in the centered variable y=t-42
    base_a=mp(mp([-42,1],[(-1176),0,1]),mp([-294,0,1],[-294,0,1]))
    # t-84 = y-42
    base_b=mp(mp([-42,1],[-1029,0,1]),[21609,0,-735,0,1])
    def shift(coeff):
        z=[0]*len(coeff)
        for i,c in enumerate(coeff):
            for j in range(i+1):z[j]+=c*comb(i,j)*(-42)**(i-j)
        return tuple(reversed(z))
    return shift(base_a),shift(base_b)

def main():
    A,B=expected_coeffs(); groups={A:[],B:[]}
    for S in itertools.combinations(range(7),4):
        got=characteristic(matrix_B(S))
        assert got in groups, (S,got)
        groups[got].append(S)
    assert len(groups[A])==21 and len(groups[B])==14
    for name,coeff in [('A',A),('B',B)]:
        print('class',name,'count',len(groups[coeff]),'representative',groups[coeff][0])
        print(' charpoly B coefficients:',coeff)
    print('PASS: all 35 exact integer-cyclotomic matrices have the declared characteristic polynomials')
if __name__=='__main__':main()
