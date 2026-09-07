import sympy as sp, json, numpy as np
from collections import deque

D=json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/G1.json"))
E1=[tuple(e) for e in D["E1"]]
N1=20
S=json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/s2_search.json"))
tree=set(S["tree"]); non_tree=S["nontree"]
mask=13
signs={}
for idx in range(30):
    if idx in tree: signs[idx]=1
    else:
        j=non_tree.index(idx)
        signs[idx]=1 if ((mask>>j)&1) else -1
s2=[signs[i] for i in range(30)]
print("s2 signs:",s2)
# verify floating rho
M=np.zeros((N1,N1))
for idx,(u,v) in enumerate(E1):
    M[u,v]+=signs[idx]; M[v,u]+=signs[idx]
ev=np.linalg.eigvalsh(M); print("signed ev:",np.round(ev,6),"rho",abs(ev).max())

MS=sp.zeros(20)
for idx,(u,v) in enumerate(E1):
    MS[u,v]=signs[idx]; MS[v,u]=signs[idx]
x=sp.Symbol('x')
cp=MS.charpoly(x)
poly=sp.Poly(cp.as_expr(),x)
print("degree",poly.degree())
coeffs=poly.all_coeffs()
print("coeffs:",coeffs)
json.dump({"s2":s2,"charpoly_coeffs":[int(c) for c in coeffs]},
  open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/s2_charpoly.json","w"))
print("factored:",sp.factor(cp.as_expr()))
