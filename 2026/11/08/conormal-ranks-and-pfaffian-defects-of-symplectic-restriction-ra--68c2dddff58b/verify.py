#!/usr/bin/env python3
"""Exact finite consistency checks for conormal alternating-rank calculations.

The general geometric proof and the classical Pfaffian resolution are in RESULT.md.
No external packages required.
"""
from fractions import Fraction
from math import factorial
from random import Random


def det(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    n = len(a)
    ans = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        d = a[j][j]
        ans *= d
        for i in range(j+1,n):
            c = a[i][j]/d
            for h in range(j+1,n):
                a[i][h] -= c*a[j][h]
            a[i][j] = 0
    return ans


def rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    n, m = len(a), len(a[0])
    r = 0
    for j in range(m):
        pivot = next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None:
            continue
        a[r],a[pivot] = a[pivot],a[r]
        d = a[r][j]
        a[r] = [z/d for z in a[r]]
        for i in range(n):
            if i != r:
                d = a[i][j]
                a[i] = [a[i][h]-d*a[r][h] for h in range(m)]
        r += 1
        if r == n:
            break
    return r


def pf(mat):
    n = len(mat)
    if n == 0:
        return 1
    assert n%2==0
    s = 0
    for j in range(1,n):
        sub = [[mat[a][b] for b in range(1,n) if b!=j]
               for a in range(1,n) if a!=j]
        s += (-1)**(j+1)*mat[0][j]*pf(sub)
    return s


def falling(a,h):
    z=1
    for j in range(h):
        z*=a-j
    return z


def check():
    for k in range(2,16):
        # Explicit alternating block matrix attains the generic maximum.
        a=[[0]*k for _ in range(k)]
        for i in range(0,k-1,2):
            a[i][i+1]=1
            a[i+1][i]=-1
        assert rank(a)==2*(k//2)
        # The relative conormal map A -> A o q has exactly this rank
        # for the surjective coordinate pairing q=[I_k,0].
        q=[row+[0]*k for row in a]
        assert rank(q)==rank(a)
        if k%2:
            r=(k-1)//2
            # P(t)=1-kt^r+kt^(r+1)-t^k is divisible by (1-t)^3.
            deriv=lambda h: (-k*falling(r,h)+k*falling(r+1,h)-falling(k,h)) if h else 0
            assert all(deriv(j)==0 for j in range(1,3))
            degree=-deriv(3)//6
            assert degree==k*(k*k-1)//24
            if k>=5:
                print('ODD_FIRST_DEFECT',k,'CODIM 3','DEGREE',degree)
        else:
            if k>=4:
                assert pf(a)**2==det(a)
                print('EVEN_FIRST_DEFECT',k,'CODIM 1','DEGREE',k//2)
    for k in (2,4,6,8):
        rr=Random(2026+k)
        a=[[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(i+1,k):
                a[i][j]=rr.randrange(-9,10)
                a[j][i]=-a[i][j]
        assert det(a)==pf(a)**2
    print('EXACT_CHECKS_PASS')

if __name__=='__main__':
    check()
