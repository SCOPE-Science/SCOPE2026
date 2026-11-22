#!/usr/bin/env python3
"""Reproduce finite numerical checks for the ball--cube metric-projection theorem.

The analytic proof, not finite tests, establishes the universal quantifiers.
Python standard library only. Run: python CHECK.py
"""
import math
import random


def coefficient(n, q):
    assert n >= 2 and q > 0
    if q >= math.sqrt(n):
        return 1.0, None
    candidate = 1.0
    witness = None
    for k in range(n - 1):
        if k >= q*q:
            continue
        m = n-k
        c = 1.0/math.sqrt(q*q-k)
        lower = math.sqrt(max(0.0, 1.0-(m-1)*c*c))
        upper = min(1.0, c)
        unconstrained = math.sqrt((1.0-1.0/math.sqrt(m))/2.0)
        a = min(upper, max(lower, unconstrained))
        value = 1.0-a*a + math.sqrt(m-1)*a*math.sqrt(1-a*a)
        if value > candidate:
            candidate, witness = value, (k, m, a, lower, upper)
    return candidate, witness


def project(v, q):
    clipped = [max(-1.0, min(1.0, z)) for z in v]
    if sum(z*z for z in clipped) <= q*q:
        return clipped
    left, right = 1.0, max(2.0, max(abs(z) for z in v)*math.sqrt(len(v))/q*2)
    def mass(s):
        return sum(min(1.0, abs(z)/s)**2 for z in v)
    while mass(right) > q*q:
        right *= 2
    for _ in range(100):
        mid = 0.5*(left+right)
        if mass(mid) > q*q:
            left = mid
        else:
            right = mid
    scale = 0.5*(left+right)
    return [max(-1.0, min(1.0, z/scale)) for z in v]


def central_jacobian(v, q, h=1e-5):
    n = len(v)
    matrix = []
    for j in range(n):
        up, dn = list(v), list(v)
        up[j] += h
        dn[j] -= h
        p_plus, p_minus = project(up, q), project(dn, q)
        matrix.append([(x-y)/(2*h) for x,y in zip(p_plus, p_minus)])
    return max(sum(abs(matrix[j][i]) for j in range(n)) for i in range(n))


def witness_input(n, q, k, a, lam=0.0001, gap=0.0001):
    m = n-k
    rho = math.sqrt(q*q-k)
    tail = math.sqrt((1-a*a)/(m-1))
    values = [1.0+lam+0.1] * k
    values += [(1.0+lam)*rho*a]
    values += [(1.0+lam)*rho*tail]*(m-1)
    return values


def run():
    checks = 0
    rng = random.Random(17223)
    for n in range(2, 18):
        for j in range(1, 14):
            q = math.sqrt(n)*(j/14.0)
            formula, detail = coefficient(n, q)
            assert 1.0 <= formula <= math.sqrt(n)+1e-10
            checks += 1
            for rep in range(13):
                v = [rng.uniform(-4,4) for _ in range(n)]
                observed = central_jacobian(v, q)
                assert observed <= formula+2e-5, (n,q,formula,observed)
                checks += 1
    for n in [2,3,4,5,13,30,70]:
        for q in [0.1,0.5,1.0]:
            formula,_ = coefficient(n,q)
            assert abs(formula-(1+math.sqrt(n))/2) < 1e-12
            checks += 1
    for n in [3,4,5,13,30,70]:
        near,_ = coefficient(n, math.sqrt(n)*(1-1e-8))
        assert abs(near-(2-2/n)) < 2e-5
        at,_ = coefficient(n, math.sqrt(n))
        assert at == 1.0
        checks += 2
    n,q=13,math.sqrt(5)
    answer, info=coefficient(n,q)
    exact=(3+math.sqrt(33))/4
    ball_only=4*(1+math.sqrt(3))/5
    assert abs(answer-exact)<1e-12 and info[0]==1
    assert exact>ball_only and exact>(1+math.sqrt(11))/2
    checks+=3
    for a in [0.49,0.499,0.4999]:
        v=witness_input(n,q,1,a)
        observed=central_jacobian(v,q,h=1e-6)
        theoretical=(1-a*a+math.sqrt(11)*a*math.sqrt(1-a*a))/(1+0.0001)
        assert abs(observed-theoretical)<3e-5,(observed,theoretical)
        checks+=1
    print('PASS:',checks,'finite checks; formula at n=13, q=sqrt(5) =',format(answer,'.12f'))
    print('Sharp comparison:',format(exact-ball_only,'.12f'),
          'one-capped face excess above ball-only face')
    print('Universal theorem supported by analytic proof, not by finite testing.')

if __name__=='__main__':
    run()
