# Cubes mod lambda^3 are just {0,1,-1} (rational). Condition: Th(r), sTh(r) in {0,+-1} mod lambda^3 for all 9 roots.
# Search smarter: precompute N-map once (B=6), then filter. Also reduce: theta determined mod cubes; but brute force
# over box with early exit. B=5: 11^6=1.77M iterations, each knorm ~fast. Use PyPy? Just run with timeout 600.
from eisen import *
from u3lib import *
import time
pi1=(-5,-3); pi2=(-2,3)
m3=(-3,-6)
def classes_mod(m):
    import math
    B=int(math.isqrt(enorm(m)))+2
    seen=[]
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            c=(a,b)
            if any(econg(c,s,m) for s in seen): continue
            seen.append(c)
    return seen
cl3=classes_mod(m3)
CUBES=set(emod(epowmod(c,3,m3),m3) for c in cl3)
rts=[c for c in cl3 if econg(epowmod(c,3,m3),emod(pi1,m3),m3)]
print("nroots:",len(rts),"cubes:",sorted(map(e2str,CUBES)))
def lam3_good(X,Y,Z):
    S=ksigma((X,Y,Z))
    for r in rts:
        tv=emod(eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r))),m3)
        sv=emod(eadd(eadd(S[0],emul(S[1],r)),emul(S[2],emul(r,r))),m3)
        if tv not in CUBES or sv not in CUBES: return False
    return True
print("current good?",lam3_good((-4,-4),(-4,-4),(4,0)))
