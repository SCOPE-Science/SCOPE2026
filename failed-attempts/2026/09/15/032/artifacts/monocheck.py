"""Monotonicity / beta-ordering test (exact, N=3, q=2): compare stationary vectors
for beta=0.2 vs beta=3.0 at fixed alpha, and alpha-ordering. Uses exact solve.
Also: correlation-sign test E[p(1-c)] vs rho_p*(1-rho_c)-ish; FKG check proxy:
E[occ,occ]-rho_p*rho_c sign at edges.
"""
import numpy as np
from exact_small import build, stat, level_means, J_of  # noqa
import sys
sys.path.insert(0, 'output/artifacts')

import numpy as np
import importlib.util
spec = importlib.util.spec_from_file_location("ex", "output/artifacts/exact_small.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)

def full_stats(q,N,alpha,beta):
    G,lvl,S = ex.build(q,N,alpha,beta)
    pi = ex.stat(G)
    rho = ex.level_means(pi,lvl,S,N,q)
    return pi,lvl,S,rho

q,N,alpha=2,3,0.5
for beta in [0.2,1.0,3.0]:
    pi,lvl,S,rho=full_stats(q,N,alpha,beta)
    print(f"beta={beta} rho={np.round(rho,6)} J={ex.J_of(alpha,rho[0]):.6f}")
# FKG proxy at edge root->child0, N=3
G,lvl,S=ex.build(q,N,alpha,1.0)[:3]
import itertools
pi=ex.stat(G)
n=len(pi)
start=[0,1,3]
def edge_corr(p,c):
    e11=sum(pi[st] for st in range(n) if ((st>>p)&1) and ((st>>c)&1))
    rp=sum(pi[st] for st in range(n) if (st>>p)&1)
    rc=sum(pi[st] for st in range(n) if (st>>c)&1)
    return e11,rp,rc,e11-rp*rc
print("edge(0->1): E11,rp,rc,cov=",edge_corr(0,1))
print("edge(1->3): E11,rp,rc,cov=",edge_corr(1,3))
print("siblings(1,2): E11,rp,rc,cov=",edge_corr(1,2))
