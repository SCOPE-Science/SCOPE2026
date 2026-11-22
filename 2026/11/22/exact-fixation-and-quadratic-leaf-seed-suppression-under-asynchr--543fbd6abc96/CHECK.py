#!/usr/bin/env python3
"""Exact independent absorbing-chain verification of an asynchronous conformity model.

Uses only the Python standard library.  No numerical experiment substitutes
for the theorem's asymptotic proof.
"""
from fractions import Fraction as F
from math import erf, exp, pi, sqrt


def closed_formula(m):
    assert isinstance(m, int) and m >= 1
    d = m * (m + 1)
    R = [F(1)]
    for j in range(1, m + 1):
        R.append(R[-1] * F(d + 2 * (m - j + 1), d + 2*j))
    C = 1 / (F(1) + sum((F(2*j, d)*R[j] for j in range(1, m+1)), F(0)))
    v = [F(0)]
    for j in range(1, m + 1):
        v.append(v[-1] + C*F(2*j, d)*R[j])
    u = [v[j] + C*R[j] for j in range(m + 1)]
    assert R[-1] == 1 and u[-1] == 1 and v[0] == 0
    return u, v


def linear_solve(a, rhs):
    a = [row[:] + [rhs[i]] for i, row in enumerate(a)]
    n = len(a)
    for i in range(n):
        pivot = next(k for k in range(i, n) if a[k][i])
        a[i], a[pivot] = a[pivot], a[i]
        scale = a[i][i]
        a[i] = [z/scale for z in a[i]]
        for j in range(n):
            if j != i:
                scale = a[j][i]
                if scale:
                    a[j] = [a[j][k] - scale*a[i][k] for k in range(n+1)]
    return [r[-1] for r in a]


def independent_chain(m):
    # Unknown variables (hub=1, k=0,...,m-1), (hub=0, k=1,...,m).
    # Absorbing boundaries (hub=0,k=0)->0, (hub=1,k=m)->1.
    d = m*(m+1)
    states = [(1,k) for k in range(m)] + [(0,k) for k in range(1,m+1)]
    index = {st:j for j,st in enumerate(states)}
    a = [[F(0) for _ in states] for _ in states]
    rhs = [F(0) for _ in states]
    for i,(hub,k) in enumerate(states):
        transitions = []
        if hub == 1:
            transitions = [((1,k+1),F(m-k,2)),((0,k), F((m-k)**2,d))]
        else:
            transitions = [((0,k-1),F(k,2)),((1,k),F(k*k,d))]
        for nxt,rate in transitions:
            a[i][i] += rate
            if nxt == (1,m):
                rhs[i] += rate
            elif nxt == (0,0):
                pass
            else:
                a[i][index[nxt]] -= rate
    z = linear_solve(a,rhs)
    return ([z[index[1,k]] if k<m else F(1) for k in range(m+1)],
            [F(0) if k==0 else z[index[0,k]] for k in range(m+1)])


def run():
    n_checks=0
    for m in range(1,11):
        u,v=closed_formula(m)
        u2,v2=independent_chain(m)
        assert u == u2 and v == v2
        n_checks += 2*(m+1)
        for k in range(m):
            assert u[k+1]>=u[k]
            assert v[k+1]>=v[k]
            assert u[k]>v[k]
            n_checks+=3
    c=1/(1+exp(.5)*sqrt(pi/2)*erf(1/sqrt(2)))
    print('Independent exact rational Markov-chain comparisons:', n_checks)
    print('Asymptotic hub-only fixation constant:',format(c,'.15f'))
    print('Asymptotic leaf-only scaled fixation constant:',format(2*c,'.15f'))
    for m in (1,2,3,5,10,20,100,1000):
        u,v=closed_formula(m)
        print('m=%d hub=%.12f leaf=%.12f scaled_leaf=%.12f'%(m,float(u[0]),float(v[1]),float(v[1]*m*m)))
    print('All exact checks passed; asymptotic limit follows from the written uniform-product argument.')

if __name__=='__main__':run()
