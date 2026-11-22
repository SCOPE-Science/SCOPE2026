#!/usr/bin/env python3
"""Exact finite-state checks for heterogeneous pairwise Fermi imitation.

Only Python standard library is required. Rational probabilities p_i are
Fermi acceptance values 1/(1+exp(beta*c_i)) for suitable positive costs.
Tests are finite checks; the general theorem is established analytically.
"""
from fractions import Fraction as Q
from itertools import combinations

def transition(n, eta, p):
    assert n >= 2 and Q(0) < eta < Q(1)
    assert len(p) == n and all(Q(0) < z < Q(1, 2) for z in p)
    u, v = eta / (2*n), (1-eta) / (n*(n-1))
    rows = []
    for state in range(1 << n):
        active = [i for i in range(n) if state & (1 << i)]
        row = [Q(0)] * (1 << n)
        for i in range(n):
            if i in active:
                prob = u + v * (n-len(active)) * (1-p[i])
            else:
                prob = u + v * sum((p[j] for j in active), Q(0))
            row[state ^ (1 << i)] = prob
        row[state] = 1 - sum(row)
        assert row[state] > 0 and all(x >= 0 for x in row)
        assert sum(row) == 1
        rows.append(row)
    return rows, u, v

def check(n, eta, p):
    P, u, v = transition(n, eta, p)
    # Every pair of nonmatching contribution costs violates the explicit
    # near-full cooperator elementary-square Kolmogorov cycle identity.
    for i, j in combinations(range(n), 2):
        base = ((1 << n)-1) ^ (1 << i) ^ (1 << j)
        si, sj, full = base | (1 << i), base | (1 << j), (1 << n)-1
        forward = P[base][si]*P[si][full]*P[full][sj]*P[sj][base]
        backward = P[base][sj]*P[sj][full]*P[full][si]*P[si][base]
        A = u + v * sum((p[k] for k in range(n) if k not in (i,j)), Q(0))
        assert forward / backward == ((A+v*p[i])*(u+v*(1-p[j])) / ((A+v*p[j])*(u+v*(1-p[i]))))
        assert (forward > backward) == (p[i] > p[j]) if p[i]!=p[j] else forward==backward
    return P

def check_homogeneous(n, eta, p):
    P, u, v = transition(n, eta, [p]*n)
    w=[Q(1)]
    for k in range(n):
        w.append(w[-1] * (u+v*k*p)/(u+v*(n-k-1)*(1-p)))
    Z=sum((w[s.bit_count()] for s in range(1<<n)),Q(0))
    pi=[w[s.bit_count()]/Z for s in range(1<<n)]
    assert sum(pi)==1
    for s in range(1<<n):
        for j in range(n):
            t=s^(1<<j)
            assert pi[s]*P[s][t]==pi[t]*P[t][s]
    assert all(sum(pi[s]*P[s][t] for s in range(1<<n))==pi[t] for t in range(1<<n))

def check_two():
    p=[Q(1,4),Q(1,3)]; eta=Q(1,5)
    P,u,v=transition(2,eta,p)
    q=[1-z for z in p]
    pi=[(2*u+v*sum(q))/(2*(4*u+v)),u/(4*u+v),u/(4*u+v),
        (2*u+v*sum(p))/(2*(4*u+v))]
    assert pi==[Q(5,9),Q(1,12),Q(1,12),Q(5,18)]
    assert all(sum(pi[s]*P[s][t] for s in range(4))==pi[t] for t in range(4))
    cycle=[0,1,3,2]
    product_forward=Q(1);product_backward=Q(1)
    for j in range(4):
        a,b=cycle[j],cycle[(j+1)%4]
        product_forward*=P[a][b]
        product_backward*=P[b][a]
    assert product_forward/product_backward==Q(57,77)
    J=pi[0]*P[0][1]-pi[1]*P[1][0]
    assert J==u*v*(p[0]-p[1])/(2*(4*u+v))==Q(-1,720)
    # Same entire stationary snapshot law, but no circulation.
    Ph,_,_=transition(2,eta,[Q(7,24),Q(7,24)])
    assert all(sum(pi[s]*Ph[s][t] for s in range(4))==pi[t] for t in range(4))
    for s in range(4):
        for t in range(4):
            assert pi[s]*Ph[s][t]==pi[t]*Ph[t][s]
    print('two-person stationary law:', pi)
    print('oriented current:', J, 'cycle forward/reverse:', product_forward/product_backward)

if __name__=='__main__':
    for n in (2,3,4,5):
        for eta in (Q(1,5),Q(1,2),Q(4,5)):
            check(n,eta,[Q(i+1,2*n+5) for i in range(n)])
            for pp in (Q(1,5),Q(1,3)):
                check_homogeneous(n,eta,pp)
    check_two()
    print('PASS: 12 heterogeneous chains, 24 homogeneous reversibility cases, two-player exact tests')
