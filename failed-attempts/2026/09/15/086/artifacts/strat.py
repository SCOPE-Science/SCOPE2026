import sys, itertools, cmath
sys.path.insert(0,'output/artifacts')
from exact2 import F,ZERO,ONE,II,ZETA8,mat_eye,mat_mul,mat_vec,mat_add,mat_scale,rref,ker_basis,charpoly,eval_poly_at,factor_roots
from exactM2 import M_of, lincomb, decomp, COMBOS, restrict, complement, quotient
Z=ZETA8
# W0 action on T coords: s1(t1,t2)=(1/t1,t1*t2); s2(t1,t2)=(t1*t2^3,1/t2)
def s1(t): return (ONE/t[0], t[0]*t[1])
def s2(t): return (t[0]*t[1]*t[1]*t[1], ONE/t[1])
def orbit(t):
    seen=[]; stack=[t]
    while stack:
        u=stack.pop()
        if any(u[0]==v[0] and u[1]==v[1] for v in seen): continue
        seen.append(u); stack.append(s1(u)); stack.append(s2(u))
    return seen
# 8th-root grid orbit classification
roots=[Z**k for k in range(8)]
pts=[(a,b) for a in roots for b in roots]
orbs=[]
used=set()
key=lambda t:(t[0],t[1])
for t in pts:
    if (t[0],t[1]) in used: continue
    o=orbit(t)
    orbs.append(o)
    for u in o: used.add((u[0],u[1]))
print("num W0-orbits on mu8^2:", len(orbs))
for o in sorted(orbs,key=len):
    print(f"  size {len(o)} rep=({o[0][0]},{o[0][1]})")
