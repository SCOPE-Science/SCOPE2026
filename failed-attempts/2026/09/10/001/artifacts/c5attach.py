#!/usr/bin/env python3
"""Lane-486: C5 single-vertex attachment classification (P5 probe).
Stdlib only. For base C5 (0..4, cycle edges), classify all 32 neighbour
masks of a new vertex 5 by whether the 6-vertex graph contains induced P5.
Machine-checked certificate for sharpness-family local structure."""
import itertools
C5e = {(0,1),(1,2),(2,3),(3,4),(4,0)}
C5e |= {(b,a) for a,b in list(C5e)}
LOG = []
def log(s):
    LOG.append(s); print(s, flush=True)
def hasP5(n, E):
    for S in itertools.combinations(range(n),5):
        for p in itertools.permutations(S):
            ok = True
            for k in range(4):
                a,b = p[k],p[k+1]
                if not ((a,b) in E or (b,a) in E):
                    ok=False; break
            if not ok: continue
            others=[(p[i],p[j]) for i in range(5) for j in range(i+1,5) if j-i!=1]
            good=True
            for a,b in others:
                if (a,b) in E or (b,a) in E:
                    good=False; break
            if good: return True
    return False
allowed=[]; forbidden=[]
for mask in range(32):
    E=set(C5e); v=5
    for i in range(5):
        if (mask>>i)&1: E.add((min(i,v),max(i,v)))
    (forbidden if hasP5(6,E) else allowed).append(mask)
log(f"allowed({len(allowed)}): {allowed}")
log(f"forbidden({len(forbidden)}): {forbidden}")
for m in allowed:
    log(f"allow mask {m:02d} N={sorted(i for i in range(5) if (m>>i)&1)}")
log("C5ATTACH_OK")
with open("output/artifacts/c5attach.log","w") as f: f.write("\n".join(LOG)+"\n")
