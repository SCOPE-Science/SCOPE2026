#!/usr/bin/env python3
"""Reproduce finite-field rank and nilpotency-index tests for Jordan-type fibers.
Only uses the Python standard library. Inputs are hardcoded test families.
"""
from itertools import product
from collections import Counter


def jordan(partition, p):
    n = sum(partition)
    A = [[0] * n for _ in range(n)]
    offset = 0
    for sz in partition:
        for i in range(sz - 1):
            A[offset+i][offset+i+1] = 1 % p
        offset += sz
    return A


def multiply(A, B, p):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for h in range(n):
            a = A[i][h]
            if a:
                for j in range(n):
                    C[i][j] = (C[i][j] + a * B[h][j]) % p
    return C


def dual_product(L, R, p):
    A, B = L
    C, D = R
    ac = multiply(A, C, p)
    bd = multiply(A, D, p)
    bc = multiply(B, C, p)
    return ac, [[(bd[i][j] + bc[i][j]) % p for j in range(len(A))] for i in range(len(A))]


def matzero(A):
    return all(v == 0 for row in A for v in row)


def direct_index(A, B, p):
    n = len(A)
    power = ([[int(i == j) for j in range(n)] for i in range(n)], [[0]*n for _ in range(n)])
    for h in range(1, 2*n+1):
        power = dual_product(power, (A, B), p)
        if matzero(power[0]) and matzero(power[1]):
            return h
    raise AssertionError('nilpotency-index upper bound violated')


def rho(partition, ell):
    return sum(max(0, a+b-ell) for a in partition for b in partition)


def power_rank(A, ell, p):
    n = len(A)
    # The i-th column vector is the flattening of T_ell(E_i), the linearized power.
    powers = [[[int(i == j) for j in range(n)] for i in range(n)]]
    for _ in range(ell):
        powers.append(multiply(powers[-1], A, p))
    image = [[0]*(n*n) for _ in range(n*n)]
    for h in range(n*n):
        B = [[0]*n for _ in range(n)]
        B[h//n][h%n] = 1
        T = [[0]*n for _ in range(n)]
        for i in range(ell):
            U = multiply(multiply(powers[i], B, p), powers[ell-1-i], p)
            for r in range(n):
                for s in range(n):
                    T[r][s] = (T[r][s]+U[r][s])%p
        for r in range(n):
            for s in range(n):
                image[r*n+s][h] = T[r][s]
    piv = 0
    for col in range(n*n):
        row = next((r for r in range(piv,n*n) if image[r][col] % p), None)
        if row is None: continue
        image[piv], image[row] = image[row], image[piv]
        inverse = pow(image[piv][col], -1, p)
        for j in range(col,n*n):
            image[piv][j] = (image[piv][j]*inverse)%p
        for r in range(piv+1,n*n):
            z = image[r][col]
            if z:
                for j in range(col,n*n):
                    image[r][j] = (image[r][j]-z*image[piv][j])%p
        piv+=1
    return piv


def partitions(n, maxi=None):
    if not n:
        yield ()
    else:
        for k in range(min(n, n if maxi is None else maxi), 0, -1):
            for tail in partitions(n-k,k):
                yield (k,)+tail


def check_ranks():
    count=0
    for p in (2,3,5):
        for n in range(1,7):
            for part in partitions(n):
                A=jordan(part,p)
                for ell in range(max(part),2*max(part)+1):
                    actual=power_rank(A,ell,p)
                    expect=rho(part,ell)
                    assert actual==expect,(p,part,ell,actual,expect)
                    count+=1
    return count


def check_exhaustive():
    cases=((2,(1,)),(2,(2,)),(2,(1,1)),(3,(2,)),(2,(2,1)),(2,(1,1,1)),(2,(3,)),(3,(2,1)),(2,(2,2)))
    total=0
    for p,part in cases:
        n=sum(part)
        A=jordan(part,p)
        obs=Counter()
        for vals in product(range(p),repeat=n*n):
            B=[list(vals[i*n:(i+1)*n]) for i in range(n)]
            obs[direct_index(A,B,p)]+=1
        k=max(part)
        exp={k:p**(n*n-rho(part,k))}
        for ell in range(k+1,2*k+1):
            exp[ell]=p**(n*n-rho(part,ell))-p**(n*n-rho(part,ell-1))
        exp={ell:c for ell,c in exp.items() if c}
        assert obs==exp,(p,part,obs,exp)
        print('EXHAUSTIVE_PASS',p,part,dict(sorted(obs.items())))
        total+=1
    return total


def gf4_mul(x, y):
    # GF(4) = GF(2)[t] / (t*t+t+1), integer encoding 0,1,t,t+1.
    a = 0
    for shift in range(2):
        if (y >> shift) & 1:
            a ^= (x << shift)
    if a & 8:
        a ^= (0b111 << 1)
    if a & 4:
        a ^= 0b111
    return a


def gf4_matmul(X, Y):
    n = len(X)
    return [[_gf4_dot(X[i], [Y[k][j] for k in range(n)]) for j in range(n)] for i in range(n)]


def _gf4_dot(X,Y):
    s = 0
    for a,b in zip(X,Y):
        s ^= gf4_mul(a,b)
    return s


def gf4_index(A, B):
    n = len(A)
    C=[[int(i==j) for j in range(n)] for i in range(n)]
    D=[[0]*n for _ in range(n)]
    for ell in range(1,2*n+1):
        CC = gf4_matmul(C,A)
        DD1 = gf4_matmul(C,B)
        DD2 = gf4_matmul(D,A)
        C,D = CC, [[DD1[i][j]^DD2[i][j] for j in range(n)] for i in range(n)]
        if matzero(C) and matzero(D):
            return ell
    raise AssertionError('GF4 upper bound')


def check_gf4():
    for part in ((1,), (2,), (1,1), (2,1)):
        n=sum(part)
        A=jordan(part,2)
        obs=Counter()
        for vals in product(range(4), repeat=n*n):
            B=[list(vals[i*n:(i+1)*n]) for i in range(n)]
            obs[gf4_index(A,B)]+=1
        k=max(part)
        exp={k:4**(n*n-rho(part,k))}
        for ell in range(k+1,2*k+1):
            exp[ell]=4**(n*n-rho(part,ell))-4**(n*n-rho(part,ell-1))
        exp={ell:c for ell,c in exp.items() if c}
        assert obs==exp,(part,obs,exp)
        print('GF4_PASS',part,dict(sorted(obs.items())))
    return 4


if __name__=='__main__':
    print('RANK_TESTS_PASS',check_ranks())
    print('EXHAUSTIVE_TESTS_PASS',check_exhaustive())
    print('GF4_TESTS_PASS',check_gf4())
