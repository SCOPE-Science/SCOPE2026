# None pass fully. Scores low. Hmm. Let me reconsider the cocycle condition itself.
# Maybe the condition for R/K Galois is NOT sigma(Th)/Th = cube. Let me derive properly.
# R = K1(u), u^3 = Th. sigma in Gal(K1/K), sigma(t)=w t. Extend sigma to R: need v in R with v^3 = sigma(Th).
# v = a+bu+cu^2 (a,b,c in K1); v^3 = sigma(Th) is a norm-type equation. v exists iff sigma(Th) is a cube in R^*,
# i.e. sigma(Th) mod cubes lies in <Th> subgroup of R^*/R^*3... Since R^*=K1(u), R^*/R^*3 is bigger.
# sigma(Th) = ? Using N(Th)=pi2: sigma(Th) = pi2/(Th sigma^2(Th)). So in R^*/R^*3: [sigma Th] = [pi2][Th]^{-1}[s2Th]^{-1}.
# For extendability need [sigma Th] in <[Th]>? No: v^3=sigma(Th) with v in R means [sigma Th]=1 in R^*/R^*3, i.e.
# sigma(Th) = Th^k * (cube in K1)? Since R=K1(u), R^*/R^*3 = K1^*/K1^*3 x <u>/<u^3>... precisely:
# R^*/R^*3 has basis: classes of K1-generators plus [u] with [u]^3=[Th]. [sigma Th]=1 in R^*/R^*3 iff
# [sigma Th] = [Th]^k in K1^*/K1^*3 for some k (then (u^k)^3 = Th^k ~ sigma Th up to K1-cube, adjust by K1 element).
# k is constrained by norms: N(sigma Th)=pi2, N(Th^k c^3)=pi2^k N(c)^3 => pi2 = pi2^k * cube in K^* => k=1 mod 3.
# So condition: sigma(Th)/Th^k... for k=1: sigma(Th)/Th = cube; k=4: same class. So k ≡ 1: condition IS
# sigma(Th)/Th ∈ K1^*3?? Wait k=1 gives sigma(Th)/Th = cube. k=-2: sigma(Th)*Th^2=cube? N: pi2*pi2^2=pi2^3=cube. OK
# also possible! k ≡ 1 mod 3 covers k=1,-2,4,.... k=-2: sigma(Th)*Th^2 = cube? Hmm wait [sigmaTh]=[Th]^k with k≡1:
# k=1: sigmaTh/Th; k=-2: sigmaTh*Th^2... but -2≡1 mod 3. YES so alternative condition: sigma(Th)*Th^2 ∈ cubes.
# More generally the extension might not need sigma to extend with sigma^3=id; the Galois group is Heisenberg
# where lifts have order 3 and don't commute. The condition for EXISTENCE of some lift: [sigmaTh] ∈ <[Th]>.
# Let me test BOTH conditions locally: (a) sigmaTh/Th cubes? (b) sigmaTh*Th^2 cubes? via local chars.
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

def score_combo(X,Y,Z,k,P):
    """test [sigmaTh] == [Th]^k locally: M = sigmaTh * Th^{-k}... use M = sigmaTh*Th^{3-k}/... clear: M=S*T^{m}
    with m chosen so total exponent... [S]-[T]^k=0 iff S*T^{3-k}... no: [S][T]^{-k}: represent as S*T^{3k' }... 
    simplest: M = S * T^j with j=(3-(k%3))%3, then compare char(M) vs char(T)^k... Let me just compute: want
    (S(r))/(T(r))^k to be a cube for each root r. Direct."""
    Th=(X,Y,Z); S=ksigma(Th)
    tot=0; ok=0
    for q in TESTS:
        if eeq(q,P): continue
        if cubic_symbol(P,q)!=0: continue
        rts=cube_roots_mod(P,q)
        if len(rts)!=3: continue
        # skip if any eval is 0
        tot+=1; good=True
        for r in rts:
            sv=eadd(eadd(S[0],emul(S[1],r)),emul(S[2],emul(r,r)))
            tv=eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r)))
            if edivides(q,sv) or edivides(q,tv): good=False; break
            if (cubic_symbol(sv,q)-k*cubic_symbol(tv,q))%3!=0: good=False; break
        if good: ok+=1
    return ok,tot

cands=[((-6,-6),(-6,-3),(-3,1)),((-8,-7),(-4,-2),(-4,0)),((-8,-8),(-5,1),(-4,3)),
 ((-6,0),(-3,-3),(-3,-3)),((-5,-1),(-6,-4),(4,-2))]
for c in cands:
    X,Y,Z=c
    print(list(map(e2str,c)),"k=1:",score_combo(X,Y,Z,1,pi1),"k=0:",score_combo(X,Y,Z,0,pi1),"k=2:",score_combo(X,Y,Z,2,pi1))
