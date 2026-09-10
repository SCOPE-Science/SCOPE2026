# Bounded recovery test: A(2)_* basis + cobar complex dimensions in stems 52-56.
# A(2)_* = F2[x,y,z]/(x^8,y^4,z^2), |x|=1,|y|=3,|z|=7.
from collections import defaultdict
import itertools

basis_by_deg = defaultdict(list)
for i in range(8):
    for j in range(4):
        for k in range(2):
            if i==0 and j==0 and k==0: continue
            d = i*1 + j*3 + k*7
            basis_by_deg[d].append((i,j,k))
b = {d: len(v) for d,v in basis_by_deg.items()}
print("dim A(2)_* =", 8*4*2)
print("augmentation-ideal degree distribution b_d (d:dim):")
for d in range(0,24):
    print(d, b.get(d,0))
# cobar C^s in internal degree t: dim = sum_{d1+...+ds=t} prod b_di
from functools import lru_cache
maxT = 64
# polynomial P(u)=sum b_d u^d; C^s dims = coeff of P^s
import numpy as np
P = [0]*(24)
for d in range(24):
    P[d]=b.get(d,0)
def conv(a,c):
    r=[0]*(len(a)+len(c)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(c):
            r[i+j]+=x*y
    return r
Pw=[1]
for s in range(1,9):
    Pw=conv(Pw,P)
    print(f"s={s} maxdeg={len(Pw)-1}")
    for stem in [52,53,54,55,56]:
        t=stem+s
        dim = Pw[t] if t < len(Pw) else 0
        print(f"  stem {stem} (t={t}): dim C^s_t = {dim}")
