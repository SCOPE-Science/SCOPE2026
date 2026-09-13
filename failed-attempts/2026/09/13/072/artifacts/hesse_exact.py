"""Exact Hesse arithmetic over QQ via polarization + Vieta. E: 6(x^3+y^3+z^3)-36xyz scaled:
General S(a,b,c): E: -(abc)(x^3+y^3+z^3)+(a^3+b^3+c^3)xyz = 0. O=(1:-1:0)."""
from fractions import Fraction as Q
def F(P, a,b,c):
    x,y,z = P
    return -(a*b*c)*(x**3+y**3+z**3) + (a**3+b**3+c**3)*x*y*z
def pol(P, Qd, R, a,b,c):
    # full polarization B(P,Q,R) = coeff of s t u in F(sP+tQ+uR)
    # F = A(x^3+y^3+z^3) + B xyz with A=-(abc), B=(a^3+b^3+c^3)
    A = -(a*b*c); B = (a**3+b**3+c**3)
    s = Q(0)
    for i in range(3):
        s += A*(P[i]*Qd[i]*R[i])  # x^3 polarization: 6 P_i Q_i R_i? F(sP+tQ+uR) coef of stu from A x^3: A*6 P_iQ_iR_i
    # careful: d^3/dsdtd u [A (sP_i+tQ_i+uR_i)^3] at 0 = 6 A P_i Q_i R_i
    s = Q(0)
    for i in range(3):
        s += 6*A*P[i]*Qd[i]*R[i]
    # xyz term: coef of stu in B(sPx+tQx+uRx)(sPy+tQy+uRy)(sPz+tQz+uRz) = B * sum over bijections
    import itertools as it
    for perm in it.permutations([0,1,2]):
        # assign s->P? We want coef where s,t,u each appear once: terms like (s P_i)(t Q_j)(u R_k) with {i,j,k}={0,1,2}
        pass
    # direct: coef = B*(P0(Q1R2+Q2R1) + P1(Q0R2+Q2R0) + P2(Q0R1+Q1R0))
    s += B*(P[0]*(Qd[1]*R[2]+Qd[2]*R[1]) + P[1]*(Qd[0]*R[2]+Qd[2]*R[0]) + P[2]*(Qd[0]*R[1]+Qd[1]*R[0]))
    return s
def third(P, Qd, a,b,c):
    # line sP+tQ: c2=B(P,P,Q), c1=B(P,Q,Q), c0=F(Q)
    c2 = pol(P,P,Qd,a,b,c); c1 = pol(P,Qd,Qd,a,b,c); c0 = F(Qd,a,b,c)
    R = (c1*P[0]-c2*Qd[0], c1*P[1]-c2*Qd[1], c1*P[2]-c2*Qd[2]) if c0==0 else (c0*P[0]-c1*Qd[0], c0*P[1]-c1*Qd[1], c0*P[2]-c1*Qd[2])
    return R
def peq(P,Qd):
    # projective equality over QQ: cross = 0
    cr = (P[1]*Qd[2]-P[2]*Qd[1], P[2]*Qd[0]-P[0]*Qd[2], P[0]*Qd[1]-P[1]*Qd[0])
    return all(v==0 for v in cr)
O = (Q(1),Q(-1),Q(0))
def neg(P,a,b,c): return third(O,P,a,b,c)
def add(P,Qd,a,b,c):
    R = third(P,Qd,a,b,c); S = third(O,R,a,b,c); return S
def mul(n,P,a,b,c):
    R=O; Qd=P; k=n
    while k:
        if k&1: R=add(R,Qd,a,b,c)
        Qd=add(Qd,Qd,a,b,c); k>>=1
    return R
def order(P,a,b,c,N=12):
    for k in range(1,N+1):
        if peq(mul(k,P,a,b,c),O): return k
    return None
if __name__=="__main__":
    import sys
    a,b,c = Q(1),Q(2),Q(3)
    t=(a,b,c)
    print("F(t)=",F(t,a,b,c),"F(O)=",F(O,a,b,c))
    print("smooth mu^3!=1:", ((a**3+b**3+c**3)**3 != 27*(a*b*c)**3))
    print("order of (1:2:3):", order(t,a,b,c,14))
    # associativity sanity
    P=(Q(1),Q(2),Q(3))
    print("P+O==P:", peq(add(P,O,a,b,c),P))
    print("P+(-P)==O:", peq(add(P,neg(P,a,b,c),a,b,c),O))
