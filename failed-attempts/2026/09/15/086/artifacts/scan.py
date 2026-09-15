import numpy as np, cmath
from meataxe import comp_factors_dims, gen_weight_spaces
from engine import principal_series_mats

def orbit_of(t):
    def s1(t):
        t1,t2=t; return (1/t1, t1*t2)
    def s2(t):
        t1,t2=t; return (t1*t2**3, 1/t2)
    seen=[]; stack=[t]
    def key(z): return (round(z[0].real,9),round(z[0].imag,9),round(z[1].real,9),round(z[1].imag,9))
    ks=set()
    while stack:
        u=stack.pop()
        k=key(u)
        if k in ks: continue
        ks.add(k); seen.append(u)
        stack.append(s1(u)); stack.append(s2(u))
    return seen

# Davis t_{1,-1} ambiguous: which coords? Try all sign/unit combos and find [1,2,2]-type or [1,1,2,3,3]-merger
cands=[]
vals=[1,-1,1j,-1j]
for a in vals:
    for b in vals:
        cands.append((complex(a),complex(b)))
# also 8th roots
for k in range(8):
    z=cmath.exp(2j*cmath.pi*k/8)
    for w in [1,-1,1j,-1j]:
        cands.append((z,complex(w))); cands.append((complex(w),z))
cands=list(dict.fromkeys(cands))
print(f"{len(cands)} candidates")
import collections
groups={}
for t in cands:
    try:
        dims,_=comp_factors_dims(t,seed=0)
    except Exception as e:
        dims=("ERR",)
    key=tuple(dims)
    groups.setdefault(key,[]).append(t)
for k,v in sorted(groups.items(),key=lambda kv:-len(kv[1])):
    print(k, len(v), v[:12])
