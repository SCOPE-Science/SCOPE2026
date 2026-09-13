# NOTE: hits with W are REDUNDANT: theta=(X+Yt+Zt^2)/W all differ by K1-cubes? No — different W give different
# theta classes in K1^*/K1^*3 only if... theta1/theta2 has norm = cube => ratio has norm 1... The cocycle class
# [sigma(Th)/Th] is invariant under Th -> Th*gamma^3 AND under Th->Th*gamma (gamma in K, as shown). But different
# (X,Y,Z,W) solutions may give genuinely different classes. HOWEVER: the number of Redei extensions is finite
# (classified by H^1... ). The cocycle condition might be satisfiable by only some.
#
# But wait — 69s for B=8 is slow. More importantly, MANY "hits" are the same theta up to scale: (X,Y,Z,W) ~ scale.
# Let me directly test cocycle local-triviality for a sample of DISTINCT theta classes.
# Normalize: theta=(X+Yt+Zt^2)/W. Qnum=S^2 S1 (S=sigma num part... careful: sigma acts on whole theta incl. W;
# W in K fixed by sigma, so Q=sigma(Th)/Th same formula with num parts). chars need care with denominators:
# evaluate num and divide by char of W parts.
from eisen import *
import math
def kmul(A,B,P):
    X1,Y1,Z1=A; X2,Y2,Z2=B
    c0=eadd(emul(X1,X2),emul(P,eadd(emul(Y1,Z2),emul(Z1,Y2))))
    c1=eadd(eadd(emul(X1,Y2),emul(Y1,X2)),emul(emul(P,Z1),Z2))
    c2=eadd(eadd(emul(X1,Z2),emul(Z1,X2)),emul(Y1,Y2))
    return (c0,c1,c2)
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

primes=enum_primary_primes(1500)
pi1=(1,3)
TESTS=[pi for pi,N in primes if pi!=pi1][:60]

def cocycle_score(X,Y,Z,W,P):
    """fraction of test primes where all-3 chars of Q vanish. Qnum=S^2S1/N with N=knorm; adjust W: theta=num/W,
    sigma(theta)/theta = sigma(num)/num (W cancels). So W irrelevant for class! Only (X,Y,Z) matters."""
    Th=(X,Y,Z)
    S=ksigma(Th); S1=ksigma(S); N=knormXYZ(X,Y,Z,P)
    Qnum=kmul(kmul(S,S,P),S1,P)
    tot=0; ok=0
    for q in TESTS:
        if eeq(q,P) or edivides(q,N): continue
        if cubic_symbol(P,q)!=0: continue
        rts=cube_roots_mod(P,q)
        if len(rts)!=3: continue
        cn=cubic_symbol(N,q)
        if cn is None: continue
        tot+=1
        good=True
        for r in rts:
            v=eadd(eadd(Qnum[0],emul(Qnum[1],r)),emul(Qnum[2],emul(r,r)))
            if edivides(q,v): good=False; break
            cv=cubic_symbol(v,q)
            if (cv-cn)%3!=0: good=False; break
        if good: ok+=1
    return ok,tot

# sample distinct thetas from t13 hits + original
cands=[((-6,-6),(-6,-3),(-3,1)),((-6,-3),(-6,-6),(6,0)),((-6,-3),(-3,-6),(3,0)),
 ((-5,-1),(-6,-4),(4,-2)),((-8,-7),(-4,-2),(-4,0)),((-8,-4),(-2,-1),(1,2)),
 ((-8,-8),(-5,1),(-4,3)),((-6,0),(-3,-3),(-3,-3)),((-2,-2),(-2,-2),(0,2)),
 ((-6,-6),(-3,0),(3,3)),((-7,-8),(-8,-1),(-3,2)),((-8,-4),(-4,-2),(0,2))]
for c in cands:
    X,Y,Z=c
    n=knormXYZ(X,Y,Z,pi1)
    print(list(map(e2str,c)),"N=",e2str(n),"score=",cocycle_score(X,Y,Z,(1,0),pi1))
