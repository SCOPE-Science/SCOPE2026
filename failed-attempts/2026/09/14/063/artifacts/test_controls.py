import sys; sys.path.insert(0,'output/artifacts')
from qscat import *
import sympy as sp

print("== pentagon control: n=1, p1=p2=1 ==")
Q,E,bad = solve(1,{0:1},{0:1},4)
for v in sorted(Q): print(v, sp.expand(Q[v]), "bar:", is_barinv(Q[v]), "Lef:", lefschetz_decomp(Q[v]))
print("residual nonzero:", {k:str(v) for k,v in bad.items()})

print("== acyclic Kronecker: n=2, p1=p2=1 ==")
Q,E,bad = solve(2,{0:1},{0:1},4)
for v in sorted(Q): print(v, sp.expand(Q[v]), "bar:", is_barinv(Q[v]), "Lef:", lefschetz_decomp(Q[v]))
print("residual nonzero:", {k:str(v) for k,v in bad.items()})

print("== Lefschetz-in [2],[2], n=2 ==")
Q,E,bad = solve(2,{1:1,-1:1},{1:1,-1:1},4)
for v in sorted(Q): print(v, sp.expand(Q[v]), "bar:", is_barinv(Q[v]), "Lef:", lefschetz_decomp(Q[v]))
print("residual nonzero:", {k:str(v) for k,v in bad.items()})

print("== Lefschetz-in [3],[3], n=2 ==")
Q,E,bad = solve(2,{2:1,0:1,-2:1},{2:1,0:1,-2:1},3)
for v in sorted(Q): print(v, sp.expand(Q[v]), "bar:", is_barinv(Q[v]), "Lef:", lefschetz_decomp(Q[v]))
print("residual nonzero:", {k:str(v) for k,v in bad.items()})
