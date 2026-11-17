#!/usr/bin/env python3
"""Finite exact checks for the one-way three-state excitation theorem.

Only Python's standard library is required.  All arithmetic is integral.
"""
from collections import Counter
from itertools import product


def update(x):
    n = len(x)
    return tuple(2 if x[i] == 1 else (int(x[(i+1) % n] == 1) if x[i] == 0 else 0) for i in range(n))


def markers(x):
    n = len(x)
    return tuple(int(x[i] != 1 and x[(i+1) % n] == 0 and x[(i+2) % n] == 1) for i in range(n))


def mul(A, B):
    d = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]


def mat_trace(M, n):
    d = len(M)
    P = [[int(i == j) for j in range(d)] for i in range(d)]
    for _ in range(n):
        P = mul(P, M)
    return sum(P[i][i] for i in range(d))


def transfer_coefficients(n):
    # Q(z)=[[1,2,0],[1,1,1],[z,1,1]], calculated at integer points
    # and recovered exactly as a polynomial by finite differences.
    deg = n // 3
    ys = [mat_trace([[1,2,0],[1,1,1],[v,1,1]],n) for v in range(deg+1)]
    # Newton expansion in binomial basis, evaluated at t=0,1,...,deg.
    differences = []
    while ys:
        differences.append(ys[0])
        ys = [ys[i+1]-ys[i] for i in range(len(ys)-1)]
    # Evaluate at 0..deg with the integer binomial basis, or use recurrence
    # to recover ordinary z coefficients exactly via triangular conversion.
    from fractions import Fraction
    out = [Fraction(0) for _ in range(deg+1)]
    for k, a in enumerate(differences):
        # binom(z,k)=z(z-1)...(z-k+1)/k!
        p = [1]
        for j in range(k):
            q = [0]*(len(p)+1)
            for h,v in enumerate(p):
                q[h] -= j*v
                q[h+1] += v
            p = q
        from math import factorial
        for h,v in enumerate(p):
            # keep rational representation until summed below
            out[h] += Fraction(a*v,factorial(k))
    assert all(int(v)==v for v in out)
    return tuple(int(v) for v in out)


def spectral_extinction(n):
    # (1+sqrt(3))**n+(1-sqrt(3))**n+1, avoiding floats.
    a,b=2,2
    # P_0=2; P_1=2; P_n=2 P_{n-1}+2 P_{n-2}.
    if n==0: return 3
    if n==1: return 3
    for _ in range(2,n+1):
        a,b=b,2*b+2*a
    return b+1


def recurrent_count(n):
    R = [[1,1,0],[0,0,1],[1,0,0]]
    return mat_trace(R,n)


def main():
    # Infinite-family local identity is a 5-symbol identity; enumerate all 243.
    for word in product(range(3),repeat=5):
        cur=list(word)
        traces=[tuple(cur)]
        for _ in range(4):
            cur=[2 if cur[i]==1 else (int(cur[i+1]==1) if cur[i]==0 else 0)
                 for i in range(len(cur)-1)]
            traces.append(tuple(cur))
        # F^3 at site 1 equals F^4 at site 0.
        assert traces[4][0]==traces[3][1]
    print('LOCAL_IDENTITY all 243 five-symbol windows: PASS')
    for n in range(3,11):
        histogram=Counter();max_entry=0;periodic=set()
        for x in product(range(3),repeat=n):
            x1=update(x);x2=update(x1);x3=update(x2);x4=update(x3)
            assert x4 == x3[1:]+x3[:1]
            m=markers(x)
            assert all(not(m[i] and (m[(i+1)%n] or m[(i+2)%n])) for i in range(n))
            assert x3==tuple(2*m[i]+m[(i+1)%n] for i in range(n))
            histogram[sum(m)]+=1
            if x2[1:]+x2[:1]!=x3: max_entry=3
            periodic.add(x3)
        predicted=transfer_coefficients(n)
        assert tuple(histogram[k] for k in range(n//3+1))==predicted
        assert histogram[0]==spectral_extinction(n)
        assert len(periodic)==recurrent_count(n)
        assert max_entry==3
        print('n=%2d total=%6d pulse_hist=%s extinction=%6d recurrent=%3d cutoff=3 PASS'
              %(n,3**n,tuple(histogram[k] for k in range(n//3+1)),histogram[0],len(periodic)))

if __name__=='__main__':main()
