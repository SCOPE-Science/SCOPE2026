"""Exact independent finite-horizon checks for a uniform-edge-grown 2-complex.

Run with Python 3. The general asymptotic and positivity statements are proved
analytically in RESULT.md; the finite checks here are not infinite certificates.
"""
from fractions import Fraction as F
from math import isclose, pi, sqrt

assertions = 0

def check(condition, explanation):
    global assertions
    assert condition, explanation
    assertions += 1


def means_and_covariances(n_max):
    # The state n=4 has two vertices of graph-degree two in every history.
    md, ml, mk, cv = F(8, 3), F(2), F(4, 3), F(0)
    data = {4: (md, ml, mk, cv)}
    for n in range(4, n_max):
        m = 2*n-3
        force = 2*md*ml / m**2 - mk/m - F(2, (2*n-5)*m)
        cv_next = (1-F(1, m))*cv + force
        mk_next = (1-F(2, m))*mk + md/m
        ml_next = (1-F(2, m))*ml + 1
        md_next = (1+F(1, m))*md
        md, ml, mk, cv = md_next, ml_next, mk_next, cv_next
        data[n+1] = (md, ml, mk, cv)
    return data


def state_stats(edges, n):
    deg = [0]*n
    neighbors = [set() for _ in range(n)]
    for a,b in edges:
        deg[a] += 1
        deg[b] += 1
        neighbors[a].add(b)
        neighbors[b].add(a)
    d = deg[0]
    l = sum(t==2 for t in deg)
    k = sum(deg[v]==2 for v in neighbors[0])
    return d,l,k


def exact_path_enumeration(n_max=8):
    states = [frozenset(((0,1),(0,2),(1,2)))]
    empirical = {}
    for n in range(3,n_max+1):
        checks = [state_stats(s,n) for s in states]
        total = len(states)
        md = F(sum(x[0] for x in checks), total)
        ml = F(sum(x[1] for x in checks), total)
        mk = F(sum(x[2] for x in checks), total)
        mdl = F(sum(x[0]*x[1] for x in checks), total)
        empirical[n] = (md,ml,mk,mdl-md*ml)
        for s in states:
            check(len(s)==2*n-3, 'deterministic edge count')
            assert all(not (a!=b and a >= n) for a,b in s)
        if n<n_max:
            evolved = []
            for edges in states:
                for u,v in edges:
                    evolved.append(edges | frozenset(((u,n),(v,n))))
            states = evolved
    return empirical


analytic = means_and_covariances(150)
empirical = exact_path_enumeration(8)
for n in range(4,9):
    check(empirical[n]==analytic[n], 'exhaustive path average not equal to recurrence')
for n,(md,ml,mk,cv) in analytic.items():
    check(ml==F(n*n-4*n+6, 2*n-5), 'known exact marginal')
    check(mk==md/3+F(4,3*(2*n-5)), 'neighbor closure')
    if n>=5:
        check(cv>0,'positive covariance')
    if n<150:
        m=2*n-3
        force=2*md*ml/m**2-mk/m-F(2,(2*n-5)*m)
        algebraic=(md*(2*n*n-8*n+21)-10*m)/F(3*(2*n-5)*m*m)
        check(force==algebraic,'positive-forcing factorization')
        check(force>0,'positive forcing')
# A finite large-n diagnostic only; convergence is established by a proof.
md,ml,mk,cv = [float(t) for t in analytic[150]]
for n in range(150,30000):
    m = 2*n-3
    force = 2*md*ml/m**2-mk/m-2/((2*n-5)*m)
    cv = (1-1/m)*cv+force
    mk = (1-2/m)*mk+md/m
    ml = (1-2/m)*ml+1
    md = (1+1/m)*md
check(isclose(cv/sqrt(30000),sqrt(pi)/12,rel_tol=0.002), 'asymptotic diagnostic')
print(f'PASS: {assertions} exact assertions and one floating-point asymptotic diagnostic')
print(f'At n=30000, covariance/sqrt(n)={cv/sqrt(30000):.9f}; limit={sqrt(pi)/12:.9f}')
