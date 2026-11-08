#!/usr/bin/env python3
"""Exact finite checks for root-cluster / singleton-component covariance.

Uses only Python's standard library. All checks are exact rational identities;
exhaustive checks cover every recursive-tree parent choice and percolation mask
for the stated finite sizes. Asymptotic assertions require the written proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def products(n, p):
    a = u = f = F(1)
    for t in range(1, n):
        a *= 1 + p / t
        u *= 1 - p / t
        f *= 1 + 2 * p / t
    return a, u, f


def formulas(n, p):
    a, u, f = products(n, p)
    b = ((1-p)*n + 2*p*u)/(1+p)
    joint = u + (1-p)*(n-1)*a/(1+p)
    cov = ((1+p)*u - (1-p)*a - 2*p*a*u)/(1+p)
    var_c = 2*f - a - a*a
    return a, b, joint, cov, var_c


def moment_recursion(n, p):
    a = b = m = q = u = F(1)
    v = F(0)
    for t in range(1, n):
        next_a = a * (1+p/t)
        next_b = b * (1-p/t) + (1-p)
        next_m = m + (1-p)*a - p*u/t
        next_q = (1+2*p/t)*q + p*a/t
        next_v = ((1-2*p/t)*v + p*(1-p)
                  + p*(3-2*p)*b/t - p*p*b*b/(t*t))
        next_u = u*(1-p/t)
        a,b,m,q,v,u=next_a,next_b,next_m,next_q,next_v,next_u
    return a,b,m,m-a*b,q-a*a,v


def brute(n, numer, denom):
    total = csum = isum = cisum = csqsum = F(0)
    parent_sets = product(*(range(j) for j in range(1,n)))
    norm = factorial(n-1)*denom**(n-1)
    for parents in parent_sets:
        for mask in range(1 << (n-1)):
            degrees = [0] * n
            connected = [False] * n
            connected[0] = True
            k = mask.bit_count()
            for j in range(1, n):
                if mask & (1 << (j-1)):
                    parent = parents[j-1]
                    connected[j] = connected[parent]
                    degrees[j] += 1
                    degrees[parent] += 1
            c = sum(connected)
            isolated = degrees.count(0)
            w = F(numer**k*(denom-numer)**(n-1-k),norm)
            total += w
            csum += w*c
            isum += w*isolated
            cisum += w*c*isolated
            csqsum += w*c*c
    assert total == 1, (n,numer,denom,total)
    return csum,isum,cisum,cisum-csum*isum,csqsum-csum*csum


def run():
    checks = 0
    for p in (F(0),F(1,8),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(7,8),F(1)):
        for n in range(1,81):
            a,b,joint,cov,vc=formulas(n,p)
            r=moment_recursion(n,p)
            assert (a,b,joint,cov,vc)==r[:5],(n,p,'recurrence',r)
            checks += 5
            if n>=2 and F(0)<p<F(1):
                assert cov<0,(n,p,cov)
                checks += 1
            else:
                assert cov==0,(n,p,cov)
                checks += 1
    for n in range(1,8):
        for num,den in ((1,3),(1,2),(2,3)):
            p=F(num,den)
            a,b,joint,cov,vc=formulas(n,p)
            brute_values=brute(n,num,den)
            assert (a,b,joint,cov,vc)==brute_values,(n,num,den,brute_values)
            checks+=5
    print(f'PASS: {checks} exact assertions; complete parent-and-mask enumeration through n=7.')

if __name__=='__main__':
    run()
