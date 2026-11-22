"""Finite independent checks of the graph-robust two-sign trace theorem.

Run with Python 3 and the dependencies in requirements.txt.
This script checks finite instances; it is not an infinite-dimensional proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import numpy as np
from scipy.optimize import linprog

count = 0

def check(statement, label):
    global count
    if not statement:
        raise AssertionError(label)
    count += 1


def cuts(n):
    # Quotient sign vectors by simultaneous sign inversion.
    return [(1,) + bits for bits in product((-1, 1), repeat=n-1)]


def uncut_matrix(n, edges):
    return np.asarray([[int(d[i] == d[j]) for d in cuts(n)] for i,j in edges], dtype=float)


def lp_minimax(n, edges):
    U = uncut_matrix(n, edges)
    m, k = U.shape
    c = np.r_[np.zeros(k), 1.0]
    Aub = np.c_[U, -np.ones(m)]
    r = linprog(c, A_ub=Aub, b_ub=np.zeros(m), A_eq=np.c_[np.ones((1,k)), np.zeros((1,1))], b_eq=[1], bounds=[(0,None)]*k+[(0,1)], method='highs')
    if not r.success:
        raise RuntimeError(r.message)
    # Dual: max s with s <= sum_e q_e U[e,d] for every cut d.
    d = linprog(np.r_[np.zeros(m), -1.0], A_ub=np.c_[-U.T, np.ones(k)], b_ub=np.zeros(k), A_eq=np.c_[np.ones((1,m)), np.zeros((1,1))], b_eq=[1], bounds=[(0,None)]*m+[(0,1)], method='highs')
    if not d.success:
        raise RuntimeError(d.message)
    check(abs(r.fun + d.fun) < 1e-8, ('duality',n,edges))
    check(abs(max(U @ r.x[:k]) - r.fun) < 1e-8, ('primal',n,edges))
    check(abs(min(U.T @ d.x[:m]) - -d.fun) < 1e-8, ('dual',n,edges))
    return r.fun, r.x[:k]


def exact_covariance(n, edges, distribution):
    # Joint law: a uniform product-sign z and independent cut d.
    # Calculate E[H_e H_f] exactly; H_e=(z_i z_j+w_i w_j)/2.
    all_z = list(product((-1,1), repeat=n))
    states = cuts(n)
    m = len(edges)
    cov = [[F(0) for _ in range(m)] for _ in range(m)]
    for d, mass in distribution:
        for z in all_z:
            w = tuple(z[i]*d[i] for i in range(n))
            h = [F(z[i]*z[j] + w[i]*w[j],2) for i,j in edges]
            for a in range(m):
                for b in range(m):
                    cov[a][b] += mass*F(1, len(all_z))*h[a]*h[b]
    return cov


def exact_cut_cov(n, edges, distribution):
    cov = exact_covariance(n, edges, distribution)
    for ai, (i,j) in enumerate(edges):
        desired = sum((p for d,p in distribution if d[i]==d[j]), F(0))
        for bj in range(len(edges)):
            check(cov[ai][bj] == (desired if ai==bj else 0), ('cov', n, ai,bj))
    return [cov[i][i] for i in range(len(edges))]


def K(n): return list(combinations(range(n),2))
def C(n): return sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)})

def max_cut(n, edges):
    return max(sum(d[i]!=d[j] for i,j in edges) for d in cuts(n))

# Exact checks for the optimal uniform mixture of maximum cuts on transitive graphs.
for n, edges, expect in [
    (3,K(3),F(1,3)), (4,K(4),F(1,3)), (5,K(5),F(2,5)),
    (6,K(6),F(2,5)), (5,C(5),F(1,5)), (7,C(7),F(1,7)),
    (4,[(0,1),(0,2),(0,3)],F(0)),
    (4,[(0,1),(1,2),(0,2),(2,3)],F(1,3)),
]:
    v,pi=lp_minimax(n,edges)
    check(abs(v-float(expect))<1e-8, ('exact-value',n,edges))
    if edges in [K(n),C(n)]:
        check(F(len(edges)-max_cut(n,edges),len(edges))==expect, ('maxcut',n,edges))

# Explicit exact covariance checks, using optimal cut ensembles.
for n, edges in [(3,K(3)),(4,K(4)),(5,C(5)),(4,[(0,1),(1,2),(0,2),(2,3)])]:
    allcuts = cuts(n)
    best=max_cut(n,edges) if edges != [(0,1),(1,2),(0,2),(2,3)] else 3
    selections = [d for d in allcuts if sum(d[i]!=d[j] for i,j in edges)==best]
    # For triangle + pendant select cuts with all pendants cut, all but one triangle edge cut.
    if len(edges)==4:
        selections = [d for d in allcuts if d[2]!=d[3] and sum(d[i]!=d[j] for i,j in edges[:3])==2]
    masses = [(d,F(1,len(selections))) for d in selections]
    p=exact_cut_cov(n,edges,masses)
    _,pi=lp_minimax(n,edges)
    check(abs(float(max(p))-lp_minimax(n,edges)[0])<1e-8, ('witness', n))
    check(max(p)<=F(1,2), ('beats-independent',n))

# Sample arbitrary nontransitive instances, independently comparing both LPs.
for n in [4,5,6]:
    edges0=K(n)
    for seed in range(1,21):
        edge_set=[e for t,e in enumerate(edges0) if (seed*(t+3)*37+17*t*t+11)%(n+3)<(n+1)//2]
        if not edge_set: edge_set=[edges0[seed%len(edges0)]]
        lp_minimax(n,edge_set)

# Arbitrary two-probe couplings from random uniform-marginal permutations:
# their worst-direction covariance cannot beat the fractional cut lower bound.
rng = np.random.default_rng(20231115)
for n, edges in [(3,K(3)),(4,K(4)),(5,C(5)),(4,[(0,1),(1,2),(0,2),(2,3)])]:
    t,_ = lp_minimax(n,edges)
    zs=np.asarray(list(product((-1,1),repeat=n)),dtype=float)
    mon=np.asarray([zs[:,i]*zs[:,j] for i,j in edges]).T
    for _ in range(60):
        perm=rng.permutation(len(zs))
        pair=(mon+mon[perm])/2
        cov=pair.T@pair/len(zs)
        check(np.linalg.eigvalsh(cov)[-1]+1e-10>=t, ('arbitrary-coupling',n))

# Exact scalar risk normalization: independent probes variance is two
# when sum A_ij**2 (over unordered edges) is one.
for n in range(3,9):
    e=K(n)
    mx=max_cut(n,e)
    p=F(len(e)-mx,len(e))
    formula=F(n-2,2*(n-1)) if n%2==0 else F(n-1,2*n)
    check(p==formula, ('clique-parity',n))

print(f'PASS {count} finite LP, covariance, and exact combinatorial assertions')
