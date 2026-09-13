# Correct Galois test: R/K Galois iff sigma(Th)/Th is a cube in K1? Let's recompute carefully.
# 1/Th = sigma(Th)*sigma^2(Th)/N(Th). So S/Th = S*S1*T1/N with S=sigma(Th), S1=sigma^2(Th), T1=sigma^3(Th)=Th.
# Above I wrongly used S*S1*T1 with T1=sigma^2(S)=sigma^3(Th)=Th — wait that IS right: S1=sigma(S)=sigma^2(Th),
# T1=sigma(S1)=sigma^3(Th)=Th. So Qnum=S*S1*Th = N(Th) = pi2, Q = pi2/pi2 = 1?!
# That's wrong: 1/Th = sigma(Th) sigma^2(Th)/N(Th) is correct, so S/Th = S*S1*N/N... no:
# S/Th = S * (S1*T1')/N where T1' = sigma^2(Th)... let me just: 1/Th = sigma(Th)*sigma^2(Th)/N(Th) = S*S1/N.
# So S/Th = S*S*S1/N. I mistakenly multiplied by Th instead of S. Redo.
from eisen import *
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
def kpow(A,n,P):
    R=((1,0),(0,0),(0,0))
    while n>0:
        if n&1: R=kmul(R,A,P)
        A=kmul(A,A,P); n>>=1
    return R
pi1=(1,3); Th=((-6,-6),(-6,-3),(-3,1))
S=ksigma(Th); S1=ksigma(S)
Qnum=kmul(kmul(S,S,pi1),S1,pi1)
print("Qnum=S^2 S1:",list(map(e2str,Qnum)))
N=knorm(Th,pi1); print("N=",e2str(N))
Q=[]
ok=True
for c in Qnum:
    q,r=edivmod(c,N)
    print(e2str(c),"q=",e2str(q),"r=",e2str(r))
    if not eeq(r,ZERO): ok=False
    Q.append(q)
print("exact?",ok)
Q=tuple(Q)
print("Q=sigma(Th)/Th:",list(map(e2str,Q)))
print("N(Q) should be 1:",e2str(knorm(Q,pi1)))
# search cube root of Q in box
def find_cuberoot(Q,P,B):
    rng=range(-B,B+1)
    n=0
    for a in rng:
     for b in rng:
      for c in rng:
       for d in rng:
        for e in rng:
         for f in rng:
            E=((a,b),(c,d),(e,f))
            n+=1
            if kpow(E,3,P)==Q: return E
    return None
print("cube search B=3 (7^6=117k pow computations)...")
R=find_cuberoot(Q,pi1,3)
print("cuberoot:",None if R is None else list(map(e2str,R)))
