#!/usr/bin/env python3
"""Exact prime-field checks for a Cartier rank stratification; stdlib only.
No assertion for algebraically closed fields is inferred from the finite census.
"""
from collections import Counter
from itertools import product
from math import comb
P = 5
BASIS = [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)]

def mul(f,g):
    h=[0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):
            h[i+j]=(h[i+j]+x*y)%P
    return h

def powpoly(f,n):
    a=[1]
    for _ in range(n):a=mul(a,f)
    return a

def cartier_matrix(a,b,c,d):
    f=[0,d,c,b,a,0,1]
    f_powers=[powpoly(f,j) for j in range(4)]
    n=len(BASIS)
    M=[[0]*n for _ in range(n)]
    for col,(i,j) in enumerate(BASIS):
        for h in range(j+1):
            pwr=f_powers[j-h]
            factor=(-1)**(j-h)*comb(j,h)
            for k in range(4):
                e=5*k+4-i
                if 0<=e<len(pwr):
                    coefficient=pwr[e]*factor%P
                    if coefficient:
                        row=BASIS.index((k,h))
                        M[row][col]=(M[row][col]+coefficient)%P
    return M

def rank(A):
    A=[r[:] for r in A]
    m=len(A); n=len(A[0]); r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]%P),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        v=pow(A[r][j],-1,P)
        A[r]=[v*u%P for u in A[r]]
        for i in range(m):
            if i!=r:
                t=A[i][j]
                A[i]=[(u-t*w)%P for u,w in zip(A[i],A[r])]
        r+=1
    return r

def predicted_rank(a,b,c):
    delta=(b*b-a*c+2*a*a*a)%P
    if delta: return 4
    if a==b==c==0: return 0
    return 3

def translate(a,b,c,d,h):
    # Coefficients after x->x+h; remove h*x^5 via an Artin--Schreier y-shift.
    aa=a
    bb=(b-a*h)%P
    cc=(c+a*h*h+3*b*h)%P
    dd=(d+h**5-a*h**3+3*b*h*h+2*c*h+h)%P
    return aa,bb,cc,dd

def main():
    counter=Counter()
    for a,b,c,d in product(range(P),repeat=4):
        observed=rank(cartier_matrix(a,b,c,d))
        predicted=predicted_rank(a,b,c)
        assert observed==predicted,(a,b,c,d,observed,predicted)
        counter[observed]+=1
        delta=(b*b-a*c+2*a**3)%P
        for h in range(P):
            A,B,C,D=translate(a,b,c,d,h)
            assert (B*B-A*C+2*A**3)%P==delta
            assert rank(cartier_matrix(A,B,C,D))==observed
    assert counter==Counter({0:5,3:120,4:500})
    print('F5 parameter tuples:',sum(counter.values()))
    print('Cartier ranks:',dict(sorted(counter.items())))
    print('Translation tests:',P*sum(counter.values()))
    print('ALL_CHECKS_PASSED')
if __name__=='__main__': main()
