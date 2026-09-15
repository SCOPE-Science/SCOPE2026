"""Decoupling test: fix N=4 tree, vary beta, look at root-child SUBTREE marginal.
If beta truly decouples in limit, the joint law of first k levels should stabilize as N grows
for fixed beta AND change little with beta at fixed large N. Quantify via exact N=2,3
root-level occupancy law + child-subtree correlations across beta.
Also test: total-variation proxy = L1 distance of (eta_root, eta_child0, eta_child1) law
between beta=0.2 and beta=3.0 for N=2 vs N=3.
"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location("ex", "output/artifacts/exact_small.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)

def marginal_root_children(q,N,alpha,beta):
    G,lvl,S = ex.build(q,N,alpha,beta)
    pi = ex.stat(G)
    n=len(pi)
    # sites: root 0; level1 sites 1..q
    from collections import defaultdict
    d={}
    for st in range(n):
        key=((st>>0)&1,)+tuple((st>>s)&1 for s in range(1,1+q))
        d[key]=d.get(key,0)+pi[st]
    return d

for N in [2,3]:
    d_lo=marginal_root_children(2,N,0.5,0.2)
    d_hi=marginal_root_children(2,N,0.5,3.0)
    keys=sorted(set(d_lo)|set(d_hi))
    tv=0.5*sum(abs(d_lo.get(k,0)-d_hi.get(k,0)) for k in keys)
    print(f"N={N} TV(root+level1 | beta .2 vs 3.0) = {tv:.5f}")
    for k in keys:
        print(f"   {k}: lo={d_lo.get(k,0):.4f} hi={d_hi.get(k,0):.4f}")
