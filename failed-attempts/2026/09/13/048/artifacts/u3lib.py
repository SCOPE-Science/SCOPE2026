from eisen import *
import math
def ksigma(A): return (A[0],emul(OMEGA,A[1]),emul(W2,A[2]))
def knormXYZ(X,Y,Z,P):
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))
def transversal(pi):
    N=enorm(pi); q=int(math.isqrt(N))
    if q*q==N: return [(a,b) for a in range(q) for b in range(q)]
    else: return [(a,0) for a in range(N)]
def cube_roots_mod(m,pi):
    mm=emod(m,pi); return [c for c in transversal(pi) if econg(epowmod(c,3,pi),mm,pi)]
def evalK1(Th,r,pi): return emod(eadd(eadd(Th[0],emul(Th[1],r)),emul(Th[2],emul(r,r))),pi)
def charval(v,pi):
    if edivides(pi,v): return None
    return cubic_symbol(v,pi)
def central_value(Th,pi1,pi):
    STh=ksigma(Th)
    rts=cube_roots_mod(pi1,pi)
    if len(rts)!=3: return None
    vals=set()
    for r in rts:
        a=charval(evalK1(Th,r,pi),pi); b=charval(evalK1(STh,r,pi),pi)
        if a is None or b is None: return None
        vals.add((b-a)%3)
    if len(vals)==1: return vals.pop()
    return ('MIXED',vals)
def cube_root_Zw(q):
    n=enorm(q)
    if eeq(q,ZERO): return ZERO
    B=int(round(n**(1/6)))+2
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            e=(a,b)
            if eeq(emul(emul(e,e),e),q): return e
    return None
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
              if cube_root_Zw(c) is not None:
                  sols.append((X,Y,Z))
                  return sols
    return sols
