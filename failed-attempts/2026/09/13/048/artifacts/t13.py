# Interesting: rows are OFTEN constant [c,c,c] (e.g. [1,1,1],[2,2,2]) — that's exactly what Galois-equivariance
# predicts... no wait. If Q=sigma(Th)/Th were a cube, ALL rows would be [0,0,0]. Constant-nonzero rows [1,1,1]
# mean Q has the same nontrivial char at all 3 primes above q. Since Gal(K1/K) permutes the 3 primes and fixes
# Q's class? sigma(Q)=sigma^2(Th)sigma(Th)... sigma(Q)=Q? N=pi2 fixed: sigma(Q)=sigma^2(Th)sigma(Th)/(sigma(Th)... 
# sigma(Q) = sigma(S^2 S1/N) = S1^2 Th/N. And Q*N... Q has norm N(Q)=N(S)^2N(S1)/N^3 = N^3/N^3=1 (as K1 element if
# exact; here Qnum/N with N in K). Hmm the constant rows suggest Q = c * (cube) with c in K^*: indeed if Q differs
# from a K-rational element by a cube, chars are constant across the fiber. Q*u with u in K: chars shift by (u/q)
# uniformly. So cocycle class might be "reducible" to K: Q = u*C^3 with u in K^*? Then adjust theta by K-element?
# Changing Th -> Th*gamma (gamma in K): N changes by gamma^3, fine (N=pi2*W^3 form preserved up to cube), and
# Q=sigma(Th)/Th is UNCHANGED (gamma fixed by sigma). So K-scaling doesn't fix it. Changing Th by K1-cube doesn't
# change Q class either. So this theta's class is stuck: need a DIFFERENT solution (different W).
#
# Search: N(X,Y,Z) = pi2*W^3 with W non-cube small, then filter by cocycle local test.
from eisen import *
import math
def knormXYZ(X,Y,Z,P):
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))
def kmul(A,B,P):
    X1,Y1,Z1=A; X2,Y2,Z2=B
    c0=eadd(emul(X1,X2),emul(P,eadd(emul(Y1,Z2),emul(Z1,Y2))))
    c1=eadd(eadd(emul(X1,Y2),emul(Y1,X2)),emul(emul(P,Z1),Z2))
    c2=eadd(eadd(emul(X1,Z2),emul(Z1,X2)),emul(Y1,Y2))
    return (c0,c1,c2)
def ksigma(A): return (A[0],emul(OMEGA,A[1]),emul(W2,A[2]))
def transversal(pi):
    N=enorm(pi); q=int(math.isqrt(N))
    if q*q==N: return [(a,b) for a in range(q) for b in range(q)]
    else: return [(a,0) for a in range(N)]
def cube_roots_mod(m,pi):
    mm=emod(m,pi); return [c for c in transversal(pi) if econg(epowmod(c,3,pi),mm,pi)]

pi1=(1,3); pi2=(1,6)
# enumerate W in small box, RHS=pi2*W^3; enumerate (X,Y,Z) in box, group by N value
B=8
Ws={}
for a in range(-3,4):
    for b in range(-3,4):
        W=(a,b)
        if eeq(W,ZERO): continue
        W3=emul(emul(W,W),W)
        Ws[W]=emul(pi2,W3)
print("nW:",len(Ws))
# norm map
from collections import defaultdict
nmap=defaultdict(list)
rng=list(range(-B,B+1))
pts=[(a,b) for a in rng for b in rng]
print("npts:",len(pts))
import time; t0=time.time()
for X in pts:
    for Y in pts:
        for Z in pts:
            if X==ZERO and Y==ZERO and Z==ZERO: continue
            nmap[knormXYZ(X,Y,Z,pi1)].append((X,Y,Z))
print("nnorms:",len(nmap),"time",time.time()-t0)
hits=[]
for W,rhs in Ws.items():
    # rhs up to unit? N=unit*rhs also OK (unit absorbs into... N(unit)=unit^3? N_{K1/K}(u)=u^3 for u in K — adjusting
    # by K-unit changes N by cube. For K1-units use: allow unit multiples: N = u*rhs, u unit. Since units are cubes?
    # In Z[w], every unit is a 6th root; mod cubes, units/ cubes = C2? units = mu_6, cubes in mu_6 = {1, w^3=1...}
    # w is NOT a cube in Z[w] (x^3=w has no solution: norms 1, check 6 units). So allow all 6 unit multiples.
    for u in UNITS:
        t=emul(u,rhs)
        if t in nmap:
            hits.append((W,u,nmap[t][:3]))
print("nhit W-classes:",len(hits))
for W,u,sols in hits[:20]:
    print("W=",e2str(W),"u=",e2str(u),[list(map(e2str,s)) for s in sols])
