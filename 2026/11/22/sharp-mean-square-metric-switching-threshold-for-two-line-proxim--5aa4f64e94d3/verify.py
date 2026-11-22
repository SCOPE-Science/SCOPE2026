#!/usr/bin/env python3
"""Exact-rational diagnostics for random scalar-metric two-line splitting.

The infinite-horizon assertions are established analytically in RESULT.md;
these checks independently exercise reductions, moments and sharp witnesses.
Standard library only; run `python verify.py`.
"""
from fractions import Fraction as Q
from itertools import product

Z=Q(0); O=Q(1)
checks=0

def ok(statement, msg):
    global checks
    assert statement, msg
    checks+=1

def MM(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def MV(A,x):
    return tuple(sum(A[i][k]*x[k] for k in range(2)) for i in range(2))

def mat(p, w, m):
    # p=c*c and w=c*s; rational if the line has rational slope.
    return ((p,w/m),(-w*m,p))

def N2(x):return sum(t*t for t in x)

def mv_direct(a,b,c,s,m):
    # z=a(c,s), u=b(-s,c), Euclidean projections on U and V.
    z=(a*c,a*s);u=(-b*s,b*c)
    y=(z[0]-u[0]/m,z[1]-u[1]/m)
    x=(y[0],Z)
    tmp=(x[0]+u[0]/m,x[1]+u[1]/m)
    coef=c*tmp[0]+s*tmp[1]
    znew=(c*coef,s*coef)
    unew=(u[0]+m*(x[0]-znew[0]),u[1]+m*(x[1]-znew[1]))
    return (c*znew[0]+s*znew[1],-s*unew[0]+c*unew[1]), znew, unew

for cc,ss,den in [(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29),(9,40,41),(12,35,37)]:
    c=Q(cc,den);s=Q(ss,den);p=c*c;w=c*s
    ok(p+s*s==1,"unit line")
    for m in [Q(1,2),Q(1),Q(6,5),Q(2),Q(3),Q(5)]:
        for a,b in [(Q(1),Q(2)),(Q(-3,7),Q(5,4)),(Q(0),Q(1))]:
            coords,z,u=mv_direct(a,b,c,s,m)
            ok(coords==MV(mat(p,w,m),(a,b)),"proximal reduction")
            ok(z[0]*(-s)+z[1]*c==0,"primal invariant subspace")
            ok(u[0]*c+u[1]*s==0,"dual invariant subspace")
    for r in [Q(1),Q(6,5),Q(3,2),Q(2),Q(3),Q(5)]:
        v=(r*r+1/(r*r))/2
        lam=p*p+p*(1-p)*v
        L=mat(p,w,r);R=mat(p,w,1/r)
        # E T^T T = lambda*identity from two independent equally likely cases.
        for x in ((Q(1),Q(0)),(Q(0),Q(1)),(Q(2),Q(-3))):
            av=(N2(MV(L,x))+N2(MV(R,x)))/2
            ok(av==lam*N2(x),"conditional mean-square law")
            # Enumerate words, not evidence of a general infinite-horizon proof.
            for depth in range(0,6):
                sumn=Z
                for seq in product((L,R),repeat=depth):
                    y=x
                    for T in seq:y=MV(T,y)
                    sumn+=N2(y)
                ok(sumn/Q(2**depth)==(lam**depth)*N2(x),"iid word moment")
        # Factorization of stability condition; it is strict for p in (0,1).
        ok(lam-1==(p-1)*(1-(v-1)*p),"stability factorization")
        # Two-cycle trace and determinant agree with direct matrix product.
        P=MM(R,L);tr=P[0][0]+P[1][1];det=P[0][0]*P[1][1]-P[0][1]*P[1][0]
        ok(tr==2*p*p-p*(1-p)*(r*r+1/(r*r)),"two-cycle trace")
        ok(det==p*p,"two-cycle determinant")
        ok(1-tr+det==(1-p)*(1+p+p*(r*r+1/(r*r))),"Jury upper endpoint")
        ok(1+tr+det==1+3*p*p-p*(1-p)*(r*r+1/(r*r)),"Jury lower endpoint")

# The exact sharp arithmetic example, with p=9/10, cs=3/10.
p=Q(9,10);w=Q(3,10);r=Q(2)
lam=p*p+p*(1-p)*((r*r+1/(r*r))/2)
ok(lam==Q(801,800),"mean-square divergent rational example")
P=MM(mat(p,w,Q(1,2)),mat(p,w,r))
tr=P[0][0]+P[1][1];det=P[0][0]*P[1][1]-P[0][1]*P[1][0]
ok(tr==Q(99,80) and det==Q(81,100),"periodic witness")
ok(tr*tr-4*det<0 and det<1,"complex-conjugate stable two-cycle")
ok(Q(2)+Q(1,2)>0,"positive metrics")
print(f"VERIFY_OK {checks} exact-rational assertions; exact iid growth and stable alternating witness")
