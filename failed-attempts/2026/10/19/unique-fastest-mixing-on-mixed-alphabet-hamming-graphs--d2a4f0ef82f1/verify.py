"""Exact finite-dimensional checks for optimal mixed-alphabet Hamming walks."""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod
import numpy as np

checks = 0

def check(ok, info):
    global checks
    assert ok, info
    checks += 1


def exact_candidate(q):
    d = len(q)
    s = sum((F(k - 1, k) for k in q), F(0))
    t = min(F(2, d + 1), F(1) / s)
    mu = F(1) - t
    states = list(product(*(range(k) for k in q)))
    n = len(states)
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, u in enumerate(states):
        for j, v in enumerate(states):
            if i == j:
                P[i][j] = F(1) - t * s
            else:
                differences = [a for a in range(d) if u[a] != v[a]]
                if len(differences) == 1:
                    P[i][j] = t / q[differences[0]]
    return states, P, mu, t


def verify(q):
    d = len(q)
    states, P, mu, t = exact_candidate(q)
    N = len(states)
    for i in range(N):
        check(sum(P[i]) == 1, ('row', q, i))
        check(all(v >= 0 for v in P[i]), ('negative', q, i))
        check(all(P[i][j] == P[j][i] for j in range(N)), ('sym', q, i))
    spectra = []
    for k in range(1, d+1):
        for inds in combinations(range(d), k):
            spectra += [F(1)-k*t] * prod(q[i]-1 for i in inds)
    check(len(spectra)==N-1, ('dimension', q))
    check(max(abs(x) for x in spectra)==mu, ('spectral', q))
    B = np.array([[float(a) for a in row] for row in P])
    observed = np.sort(np.linalg.eigvalsh(B))
    expected = np.array(sorted([F(1)] + spectra), dtype=float)
    check(np.max(np.abs(observed-expected)) < 5e-12, ('eigen', q))
    check(P[0][0] == 0 if sum(F(k-1,k) for k in q) >= F(d+1,2) else P[0][0] > 0, ('phase', q))
    return float(mu)

for d in (2,3,4):
    for q in product((2,3,4,5), repeat=d):
        if prod(q)>100:
            continue
        verify(q)

# Unequal two-factor products checked additionally by independent linear programming.
from scipy.optimize import linprog
for p in range(2,14):
    for q in range(2,14):
        s = F(p-1,p)+F(q-1,q)
        t = min(F(2,3),F(1)/s)
        theoretical = F(1)-t
        # LP minimizes u subject to |1-x|, |1-y|, |1-x-y| <= u.
        A=[[1,0,-1],[-1,0,-1],[0,1,-1],[0,-1,-1],
           [1,1,-1],[-1,-1,-1],[(p-1)/p,(q-1)/q,0]]
        b=[1,-1,1,-1,1,-1,1]
        sol=linprog([0,0,1],A_ub=A,b_ub=b,bounds=[(0,None)]*3,method='highs')
        check(sol.success and abs(sol.fun-float(theoretical))<1e-9, ('LP',p,q))

# Perturbed *unrestricted*, nonsymmetric-under-automorphisms (but reversible)
# feasible stochastic matrices for a selection of product graphs.
import random
rng=random.Random(24681357)
for q in ((2,3),(3,5),(2,2,5),(2,3,4)):
    states,_,mu,_=exact_candidate(q)
    N=len(states)
    E=[(i,j) for i in range(N) for j in range(i+1,N)
       if sum(a!=b for a,b in zip(states[i],states[j]))==1]
    deg=max(sum(i==a or i==b for a,b in E) for i in range(N))
    for z in range(10):
        B=np.zeros((N,N))
        for i,j in E:
            B[i,j]=B[j,i]=rng.random()/(2*deg)
        for i in range(N):
            B[i,i]=1-sum(B[i,:])
        lam=np.linalg.eigvalsh(B)
        m=max(abs(x) for x in lam[:-1])
        check(m+1e-10>=float(mu), ('unrestricted',q,z))

print('VERIFY_OK',checks,'checks')
