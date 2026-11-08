#!/usr/bin/env python3
"""Exact Laurent-transfer and independent quartic Newton power-sum check."""
from itertools import product
from math import comb, factorial

S=(-1,0,1)
states=list(product(S,repeat=2))

def choices(a,b,c):
    h=2*b-a-c
    if b==0:return (0,) if h==0 else ()
    if b==1:return tuple(range(1,h))
    return tuple(range(h+1,0))

def transfer_counts(maxn):
    # Entries of M^n as dictionaries exponent -> coefficient.
    edges=[]
    for u,(a,b) in enumerate(states):
        for v,(bb,c) in enumerate(states):
            if b==bb:
                d=choices(a,b,c)
                if d:edges.append((u,v,d))
    curr=[{0:1} if i==j else {} for i in range(9) for j in range(9)]
    out={}
    for n in range(1,maxn+1):
        nex=[{} for _ in range(81)]
        for i in range(9):
            for u,v,ds in edges:
                cell=curr[i*9+u]
                dest=nex[i*9+v]
                for exp,k in cell.items():
                    for d in ds:dest[exp+d]=dest.get(exp+d,0)+k
        curr=nex
        out[n]=sum(curr[i*9+i].get(0,0) for i in range(9))
    return out

def plus(a,b):
    c=a.copy()
    for k,v in b.items():c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}

def neg(a):return {k:-v for k,v in a.items()}
def mul(a,b):
    c={}
    for k,v in a.items():
        for l,w in b.items():c[k+l]=c.get(k+l,0)+v*w
    return c

def scale(a,k):return {i:k*v for i,v in a.items() if k*v}

def quartic_counts(maxn):
    s={1:1}
    A=[{0:4},s,plus(mul(s,s),{0:4})]
    A.append(plus(plus(mul(s,A[2]),scale(A[1],2)),{0:3}))
    A.append(plus(plus(plus(mul(s,A[3]),scale(A[2],2)),A[1]),{0:-4}))
    B=[{0:4},neg(s),plus(mul(s,s),{0:-4})]
    B.append(plus(plus(neg(mul(s,B[2])),scale(B[1],-2)),{0:3}))
    B.append(plus(plus(plus(neg(mul(s,B[3])),scale(B[2],-2)),B[1]),{0:-4}))
    for n in range(5,maxn+1):
        A.append(plus(plus(plus(mul(s,A[-1]),scale(A[-2],2)),A[-3]),scale(A[-4],-1)))
        B.append(plus(plus(plus(neg(mul(s,B[-1])),scale(B[-2],-2)),B[-3]),scale(B[-4],-1)))
    def trinomial(k):return sum(factorial(k)//(factorial(j)*factorial(j)*factorial(k-2*j)) for j in range(k//2+1))
    return {n:1+sum(v*trinomial(k) for k,v in plus(A[n],B[n]).items()) for n in range(1,maxn+1)}

def main():
    t=transfer_counts(17); q=quartic_counts(17)
    expected={3:19,4:47,5:171,6:517,7:1793,8:5927,9:20287,10:69307,11:238283,12:823865,13:2854021}
    for n in range(3,18):
        assert t[n]==q[n],(n,t[n],q[n])
        if n in expected:assert t[n]==expected[n]
        print(f'C_{n}={t[n]}: matrix/central-trinomial OK')
    # Check the proposed quartic factorization by direct symbolic determinant.
    try:
        import sympy as sp
        z,L=sp.symbols('z L')
        mat=sp.zeros(9)
        for i,(a,b) in enumerate(states):
            for j,(bb,c) in enumerate(states):
                if b==bb:mat[i,j]=sum(z**k for k in choices(a,b,c))
        w=z+1+1/z
        claimed=(L-1)*(L**4-w*L**3-2*L**2-L+1)*(L**4+w*L**3+2*L**2-L+1)
        assert sp.cancel(mat.charpoly(L).as_expr()-claimed)==0
        print('SYMBOLIC_CHARPOLY_OK')
    except ImportError:
        print('SYMpy unavailable: optional symbolic determinant check skipped')
    print('TRANSFER_OK')
if __name__=='__main__':main()
