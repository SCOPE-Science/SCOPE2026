#!/usr/bin/env python3
"""Finite, independent checks of tagged-card overhand-shuffle identities."""
from math import cos, pi, log, exp

def matrix(n, p):
    q = 1.0 - p
    k = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for left in range(i + 1):
            pl = p * q**left if left < i else q**left
            for right in range(n - i):
                pr = p * q**right if right < n-i-1 else q**right
                k[i][i+right-left] += pl * pr
    return k

def eigen(n, p, j):
    q = 1.0 - p
    ell = 2 * (1 - cos(j*pi/n))
    return (p*p + (-1)**j * q**(n+1) * ell)/(p*p + q*ell)

checks = 0
for n in [3,4,5,8,13,25,50,80]:
    for p in [0.1, 0.37, 0.75]:
        k = matrix(n,p)
        lower = p*(1-p)**(n-1)
        for row in k:
            assert abs(sum(row) - 1.0) < 1e-12
            checks += 1
            for x in row:
                assert x >= lower - 1e-12
                checks += 1
        for j in range(n):
            eig = eigen(n,p,j)
            basis = [cos(j*pi*(i+0.5)/n) for i in range(n)]
            for i in range(n):
                lhs = sum(k[i][z]*basis[z] for z in range(n))
                assert abs(lhs - eig*basis[i]) < 1e-12
                checks += 1
for c in [0.3,1.0,2.5]:
    for n in [100,300,800,2000]:
        p=c/n
        t=round(log(n)/(2*c))
        for i in [1,n//2,n]:
            chi=sum(2*cos(j*pi*(i-0.5)/n)**2*eigen(n,p,j)**(2*t)
                    for j in range(1,n))
            target=n*exp(-2*c*t)
            assert chi >= -1e-12
            assert abs(chi-target) <= 0.3*max(1.0,target)
            checks += 2
print('PASS:',checks,'finite numerical/identity checks')
