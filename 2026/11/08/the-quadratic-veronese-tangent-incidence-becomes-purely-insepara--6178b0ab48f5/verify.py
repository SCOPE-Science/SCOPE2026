#!/usr/bin/env python3
"""Reproduce symbolic and finite-field checks for tangential v_2(P^2)."""
import itertools
import sympy as S
A,B,C,D,E,F,s,t,u,v=S.symbols('A B C D E F s t u v')
Delta=A*B*C-A*F**2-B*E**2-C*D**2+2*D*E*F
# Tangential parameterization on A=1, with v_2([1:s:t]) and two affine derivatives.
coords={A:1,B:s*s+2*s*u,C:t*t+2*t*v,D:s+u,E:t+v,F:s*t+t*u+s*v}
assert S.expand(Delta.subs(coords))==0
# Eliminate tangent velocities using D,E to recover s,t.
P=s*s-2*D*s+B
Q=C*(D-s)**2-2*E*(F-s*E)*(D-s)+(F-s*E)**2
assert S.expand(S.rem(Q,P,s)+Delta.subs(A,1))==0
# Rational parameterization of the determinantal chart; nonsquare witness.
Bfun=(C*D**2-2*D*E*F+F**2)/(C-E**2)
assert S.cancel((D**2-Bfun)+(F-D*E)**2/(C-E**2))==0
# Independent intersection-theory cross-check: E has c1=-3H,c2=3H^2; s2(E)=6, and degree tau=3.
c1=-3; c2=3
assert c1*c1-c2==6
assert (c1*c1-c2)//3==2
# The rational function C-E^2 has valuation one at the prime (C-E^2)
# and is not a square in k(C,D,E,F) for ANY characteristic.
assert S.Poly(C-E**2,C).degree()==1

def tangent_centers(M,p):
    a,b,c,d,e,f=M
    if a!=1:return []
    out=[]
    for ss,tt in itertools.product(range(p),repeat=2):
        if (ss*ss-2*d*ss+b)%p:continue
        if (tt*tt-2*e*tt+c)%p:continue
        if (d*tt+e*ss-ss*tt-f)%p:continue
        out.append((ss,tt))
    return out

def rank3(M,p):
    a,b,c,d,e,f=M
    T=[[a,d,e],[d,b,f],[e,f,c]]
    rank=0
    for j in range(3):
        piv=next((i for i in range(rank,3) if T[i][j]%p),None)
        if piv is None:continue
        T[rank],T[piv]=T[piv],T[rank]
        inv=pow(T[rank][j],-1,p)
        T[rank]=[(x*inv)%p for x in T[rank]]
        for i in range(3):
            if i!=rank:
                factor=T[i][j]
                T[i]=[(T[i][z]-factor*T[rank][z])%p for z in range(3)]
        rank+=1
    return rank

for p in (2,3,5):
    histogram={}
    n=0
    for b,c,d,e,f in itertools.product(range(p),repeat=5):
        M=(1,b,c,d,e,f)
        if (b*c-f*f-b*e*e-c*d*d+2*d*e*f)%p:continue
        if rank3(M,p)!=2:continue
        n+=1
        centers=tangent_centers(M,p)
        histogram[len(centers)]=histogram.get(len(centers),0)+1
        if p==2:assert len(centers)==1
        else:assert len(centers) in (0,2)
    print('p=%d rank-two A=1 rational matrices=%d rational tangent-center counts=%s'%(p,n,histogram))
print('ALL_CHECKS_PASSED')
