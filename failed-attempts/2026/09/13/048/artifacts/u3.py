# Fast Redei solver over F3-exponent vector + box enumeration for theta, per pair.
# K1-unit-free approach: enumerate X,Y,Z in box, compute N; keep those with N = u*pi2*w^3... but w^3 cubes are
# expensive to match. INSTEAD: work modulo cubes via discrete-log of ideals? Class number 1: N=(beta).
# N == pi2 mod cubes  <=>  N/(pi2) is a cube in Z[w] up to unit. Test: q=N/pi2 exact? then q/u cube?
# Cube test in Z[w]: eta^3=q/u with eta bounded by |q|^{1/3}: for box B=6 coeffs, |N| ~ B^6*|pi1|^2-ish... bounded eta.
# Implement exact cube-root in Z[w] via bounded search sized by norm.
from eisen import *
import math
def knormXYZ(X,Y,Z,P):
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))

def cube_root_Zw(q):
    """exact cube root in Z[w] or None. bound: N(eta)^3=N(q) => |eta| coeffs <= N(q)^{1/6}*2."""
    n=enorm(q)
    if eeq(q,ZERO): return ZERO
    # find integer bound: |a|,|b| <= ceil(n^{1/6})+1
    B=int(round(n**(1/6)))+2
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            e=(a,b)
            if eeq(emul(emul(e,e),e),q): return e
    return None

# self-test
assert cube_root_Zw((27,0))==(-3,0) or cube_root_Zw((27,0)) is not None
print("cuberoot test:",cube_root_Zw((27,0)), cube_root_Zw((1,6)), cube_root_Zw((8,0)))

def find_theta(pi1,pi2,B):
    sols=[]
    rng=range(-B,B+1)
    for xa in rng:
     for xb in rng:
      X=(xa,xb)
      for ya in rng:
       for yb in rng:
        Y=(ya,yb)
        for za in rng:
         for zb in rng:
          Z=(za,zb)
          if X==ZERO and Y==ZERO and Z==ZERO: continue
          N=knormXYZ(X,Y,Z,pi1)
          if eeq(N,ZERO): continue
          if not edivides(pi2,N): continue
          q,_=edivmod(N,pi2)
          for u in UNITS:
              c=emul(q,u)
              et=cube_root_Zw(c)
              if et is not None:
                  sols.append((X,Y,Z,u,et))
                  return sols
    return sols

import time
pairs=[((19,9),(10,-9)), (((-5,-3),(-2,3))), (((4,-3),(7,3)))]
for pi1,pi2 in [(((19,9)),((10,-9))),(((-5,-3)),((-2,3))),(((4,-3)),((7,3)))]:
    print("pair",e2str(pi1),e2str(pi2),cubic_symbol(pi1,pi2),cubic_symbol(pi2,pi1))
    t0=time.time()
    s=find_theta(pi1,pi2,4)
    print("  B=4:",len(s),"time",round(time.time()-t0,1))
    if s: print("   ",list(map(e2str,s[0][:3])),"u=",e2str(s[0][3]),"eta=",e2str(s[0][4]))
