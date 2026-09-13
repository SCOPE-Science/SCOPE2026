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
pi1=(1,3); Th=((-6,-6),(-6,-3),(-3,1))
# check exact divisibility: is sigma(Th) divisible by Th in O_K1? Compute Q_num/N with exact check and print remainders
S=ksigma(Th); B1=ksigma(S); # B1 = sigma^2(Th)
from eisen import edivmod
def kmul3(A,B,C,P): return kmul(kmul(A,B,P),C,P)
Qn=kmul3(Th,S,B1,pi1)  # should equal N(Th)=pi2
print("N via product:",list(map(e2str,Qn)))
# Q_num = S*B1*B2 where B2=Th: Q_num/N(Th): N(Th)=pi2 in K
Qn2=kmul(kmul(S,B1,pi1),Th,pi1)
print("same:",list(map(e2str,Qn2)))
# Now Q = S/Th = S*S1*T1/(N) with S1=sigma(S), T1=sigma^2(S)?? No: 1/Th = sigma(Th)sigma^2(Th)/N(Th)
T=Th; S1=ksigma(S); T1=ksigma(S1)
Qn3=kmul(kmul(S,S1,pi1),T1,pi1)
print("Qnum:",list(map(e2str,Qn3)), "denom pi2=",e2str((1,6)))
for c in Qn3:
    q,r=edivmod(c,(1,6))
    print(e2str(c),"-> q=",e2str(q),"r=",e2str(r))
