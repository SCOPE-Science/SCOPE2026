#!/usr/bin/env python3
"""Exact-arithmetic checks for critical-point coordinate eliminants.
Run: python verify.py ; requires SymPy >=1.12. No downloads/data files.
Finite tests illustrate the theorem; the arbitrary-degree proof is in RESULT.md.
"""
from math import gcd
import sympy as S

x,y=S.symbols('x y')
u,v,s=S.symbols('u v s')

def polys(m, a, b):
    P=sum(S.Integer(a[j])*y**j for j in range(m+1))
    Q=sum(S.Integer(b[j])*y**j for j in range(m+1))
    F=P+x*Q
    A=S.expand(u*F+s*x*Q)
    B=S.expand(v*F+s*y*S.diff(F,y))
    D=S.expand(v*P*Q+(u+s)*y*S.diff(P,y)*Q-u*y*P*S.diff(Q,y))
    return P,Q,A,B,D

def check(m,k):
    a=[(2*j*j+3*j+2+k)%13+1 for j in range(m+1)]
    b=[(j*j+5*j+3+2*k)%17+1 for j in range(m+1)]
    P,Q,A,B,D=polys(m,a,b)
    # General identity of the x-linear resultant, before specializing u,v,s.
    assert S.expand(S.resultant(A,B,x)-s*D)==0
    param={u:2+k,v:5+2*k,s:3+k}
    Pv=S.expand(P);Qv=S.expand(Q)
    Av=S.expand(A.subs(param));Bv=S.expand(B.subs(param))
    Rx=S.Poly(S.resultant(Av,Bv,y),x)
    assert all(int(c) % (param[s]**m)==0 for c in Rx.all_coeffs())
    Rx=S.Poly(S.expand(Rx.as_expr()/S.Integer(param[s])**m),x)
    lo=param[u]**m*S.resultant(Pv,y*S.diff(Pv,y),y)
    hi=(param[u]+param[s])**m*S.resultant(Qv,y*S.diff(Qv,y),y)
    assert Rx.degree()==2*m
    assert Rx.TC()==lo,(m,k,'trailing',Rx.TC(),lo)
    assert Rx.LC()==hi,(m,k,'leading',Rx.LC(),hi)
    Ry=S.Poly(D.subs(param),y)
    assert Ry.degree()==2*m
    assert Ry.TC()==param[v]*a[0]*b[0]
    assert Ry.LC()==(param[v]+m*param[s])*a[m]*b[m]
    return S.degree(S.gcd(Rx,Rx.diff()),x), S.degree(S.gcd(Ry,Ry.diff()),y)

if __name__=='__main__':
    count=0;witness=[]
    for m in range(1,6):
        for k in range(1,5):
            g=check(m,k)
            witness.append((m,k,g));count+=1
    assert any(g==(0,0) for m,k,g in witness if m==5)
    assert all(any(g==(0,0) for mm,k,g in witness if mm==m) for m in range(1,6))
    print('SEGRE_VERONESE_COORDINATE_ELIMINANTS_OK',count)
    print('GENERIC_SEPARABILITY_WITNESSES',[(m,k) for m,k,g in witness if g==(0,0)][:8])
    print('INFINITE_DEGREE_AND_IRREDUCIBILITY_FROM_WRITTEN_PROOF')
