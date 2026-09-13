# 81 good classes out of 19683. Now search theta in good classes with N=pi2*cube, box B=8.
# Lift: X = g0 + m3*(a,b) with small (a,b).
from eisen import *
from u3lib import *
import time
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
pi1=(-5,-3); pi2=(-2,3)
rts=[c for c in cl3 if econg(epowmod(c,3,m3),emod(pi1,m3),m3)]
def good_class(X,Y,Z):
    S=ksigma((X,Y,Z))
    for r in rts:
        tv=emod(eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r))),m3)
        sv=emod(eadd(eadd(S[0],emul(S[1],r)),emul(S[2],emul(r,r))),m3)
        if tv not in CUBES or sv not in CUBES: return False
    return True
goods=[]
for X in cl3:
    for Y in cl3:
        for Z in cl3:
            if X==ZERO and Y==ZERO and Z==ZERO: continue
            if good_class(X,Y,Z): goods.append((X,Y,Z))
print("ngood:",len(goods))
# for each good class, search lifts: coeffs = g + m3*t, t in small box T=3
T=3
t0=time.time(); found=[]
for gi,(X0,Y0,Z0) in enumerate(goods):
    ok=False
    for a in range(-T,T+1):
     for b in range(-T,T+1):
      DX=emul(m3,(a,b))
      X=eadd(X0,DX)
      for c in range(-T,T+1):
       for d in range(-T,T+1):
        DY=emul(m3,(c,d))
        Y=eadd(Y0,DY)
        for e in range(-T,T+1):
         for f in range(-T,T+1):
          DZ=emul(m3,(e,f))
          Z=eadd(Z0,DZ)
          N=knormXYZ(X,Y,Z,pi1)
          if eeq(N,ZERO) or not edivides(pi2,N): continue
          q,_=edivmod(N,pi2)
          for u in UNITS:
              if cube_root_Zw(emul(q,u)) is not None:
                  found.append((X,Y,Z))
                  ok=True; break
          if ok: break
         if ok: break
        if ok: break
       if ok: break
      if ok: break
     if ok: break
    print(f"class {gi}: {'FOUND '+str(list(map(e2str,found[-1]))) if ok else 'none'}")
print(f"done {time.time()-t0:.0f}s nfound={len(found)}")
