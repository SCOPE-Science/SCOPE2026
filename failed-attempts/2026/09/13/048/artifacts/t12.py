from eisen import *
import math
def kmul(A,B,P):
    X1,Y1,Z1=A; X2,Y2,Z2=B
    c0=eadd(emul(X1,X2),emul(P,eadd(emul(Y1,Z2),emul(Z1,Y2))))
    c1=eadd(eadd(emul(X1,Y2),emul(Y1,X2)),emul(emul(P,Z1),Z2))
    c2=eadd(eadd(emul(X1,Z2),emul(Z1,X2)),emul(Y1,Y2))
    return (c0,c1,c2)
def ksigma(A): return (A[0],emul(OMEGA,A[1]),emul(W2,A[2]))
def knorm(A,P):
    X,Y,Z=A
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))
def transversal(pi):
    N=enorm(pi); q=int(math.isqrt(N))
    if q*q==N: return [(a,b) for a in range(q) for b in range(q)]
    else: return [(a,0) for a in range(N)]
def cube_roots_mod(m,pi):
    mm=emod(m,pi); return [c for c in transversal(pi) if econg(epowmod(c,3,pi),mm,pi)]

def cocycle_chars(Th,P,testprimes):
    S=ksigma(Th); S1=ksigma(S); N=knorm(Th,P)
    Qnum=kmul(kmul(S,S,P),S1,P)
    out=[]
    for q in testprimes:
        if eeq(q,P): continue
        if edivides(q,N): continue
        if cubic_symbol(P,q)!=0: continue
        rts=cube_roots_mod(P,q)
        if len(rts)!=3: continue
        cn=cubic_symbol(N,q)
        row=[]
        for r in rts:
            v=eadd(eadd(Qnum[0],emul(Qnum[1],r)),emul(Qnum[2],emul(r,r)))
            if edivides(q,v): row.append('0')
            else:
                cv=cubic_symbol(v,q)
                row.append((cv-cn)%3)
        out.append((q,row))
    return out

pi1=(1,3); Th=((-6,-6),(-6,-3),(-3,1))
primes=enum_primary_primes(2000)
tests=[pi for pi,N in primes if pi!=pi1][:80]
ch=cocycle_chars(Th,pi1,tests)
ntriv=sum(1 for _,row in ch if set(row)=={0})
print(f"primes tested: {len(ch)}, all-trivial rows: {ntriv}")
for q,row in ch[:25]: print(e2str(q),enorm(q),row)
