#!/usr/bin/env python3
"""Symbolic and numerical diagnostics for the three-generation two-bough tree theorem.

Dependencies: sympy and numpy. Run: python VERIFY.py
All infinite statements are proved in the associated mathematics; finite checks are only diagnostics.
"""
from fractions import Fraction
from math import sqrt, isclose
import sympy as sp
import numpy as np

M, H, L = sp.symbols('M H L', integer=True)
s = 1 + M*(L+1)
A = 2*s*(s+1)
B = 2*M*(L+1)*(2*s-L)
C = 4*M*L*s
G0 = sp.cancel(M*(2*M-1)**2*(C*L/(2*M-1)**2 - B))
G1 = sp.cancel(M*(2*M-1)**2*(C*L/(2*M-1)**2 + A/M - B))
assert sp.degree(G0,L)==3 and sp.degree(G1,L)==3
for poly in (G0, G1):
    coeff = sp.Poly(poly, L).all_coeffs()
    for m in range(2,24):
        v=[int(c.subs(M,m)) for c in coeff]
        assert v[0]>0 and all(t<0 for t in v[1:]), (m,v)

# These four signed polynomial identities are proof certificates for ALL M >= 3.
L_root = 4*M*M - 8*M + 6
L_child = 4*M*M - 6*M + 5
for poly, sub, sign in [
    (G1,L_root-1,-1),(G1,L_root,+1),
    (G0,L_child-1,-1),(G0,L_child,+1),
]:
    coeff = sp.Poly(sp.expand(poly.subs(L,sub).subs(M,H+3)), H).all_coeffs()
    assert all(sign*c>0 for c in coeff), (sub, [str(c) for c in coeff])

# Exceptional small branch-degree case M=2.
for ell,expected_g0,expected_g1 in [(5,-1,-1),(6,-1,+1),(7,-1,+1),(8,+1,+1)]:
    g0=sp.sign(G0.subs({M:2,L:ell}))
    g1=sp.sign(G1.subs({M:2,L:ell}))
    assert (g0,g1)==(expected_g0,expected_g1)

checks=0

def coefficients(m,ell):
    s=1+m*(ell+1)
    return 2*s*(s+1), 2*m*(ell+1)*(2*s-ell), 4*m*ell*s

def solve(m,ell):
    a,b,c=coefficients(m,ell)
    y0=1/(2*m)
    t=b-c*ell/(2*m-1)**2
    # Derivative signs at the shared boundary; strict phase order.
    if t>a/m:
        # root holds, depth-one vertex does not hold
        lo,hi=y0,1/m
        def der(y):
            return a*m/(1-m*y)**2-b/y**2+c*ell/(1-y)**2
        assert der(lo)<0
        for _ in range(100):
            mid=(lo+hi)/2
            if der(mid)<0: lo=mid
            else: hi=mid
        y=(lo+hi)/2
        x=1-m*y
        label='root'
    elif t<0:
        y=sqrt(b)/(sqrt(b)+sqrt(c*ell))
        assert y<y0
        x=.5
        label='child'
    else:
        y=y0
        x=.5
        label='none'
    z=(1-y)/ell
    assert x>0 and y>0 and z>0 and x<=.5+1e-8 and x+m*y<=1+1e-8
    return label,x,y,z

def build_transition(m,ell,x,y,z):
    n=3+2*m+2*m*ell
    P=np.zeros((n,n))
    for hub in (1,2):
        P[0,hub]=P[hub,0]=x
        for j in range(m):
            g=3+(hub-1)*m+j
            P[hub,g]=P[g,hub]=y
            for t in range(ell):
                leaf=3+2*m+((hub-1)*m+j)*ell+t
                P[g,leaf]=P[leaf,g]=z
    diag=1-P.sum(axis=1)
    assert min(diag)>-1e-11
    P+=np.diag(diag)
    assert np.max(abs(P-P.T))<1e-13
    assert np.max(abs(P.sum(axis=1)-1))<1e-13
    return P

for m in list(range(2,32)):
    r=6 if m==2 else 4*m*m-8*m+6
    c=8 if m==2 else 4*m*m-6*m+5
    for ell in sorted(set([2,3,5,max(2,r-1),r,r+1,max(2,c-1),c,c+1,2*c])):
        label,x,y,z=solve(m,ell)
        expected='root' if ell<r else ('child' if ell>=c else 'none')
        assert label==expected, (m,ell,label,expected)
        checks+=1

for m,ell in [(2,2),(2,5),(2,6),(2,7),(2,8),(2,10),(3,3),(3,17),(3,18),(3,22),(3,23),(4,2)]:
    label,x,y,z=solve(m,ell)
    P=build_transition(m,ell,x,y,z)
    vals=np.linalg.eigvalsh(np.eye(len(P))-P)
    assert abs(vals[0])<1e-9 and min(vals[1:])>1e-9
    k_spec=float(sum(1/vals[1:]))
    a,b,c=coefficients(m,ell)
    k_tree=(a/x+b/y+c/z)/len(P)
    assert isclose(k_spec,k_tree,rel_tol=1e-10,abs_tol=1e-8),(m,ell,k_spec,k_tree)
    # A legal asymmetric perturbation decreases exactly one edge and increases its endpoint holding probabilities.
    d=.002*min(x,y,z)
    Q=P.copy();edge=(0,1); Q[edge]-=d;Q[edge[::-1]]-=d;Q[0,0]+=d;Q[1,1]+=d
    vv=np.linalg.eigvalsh(np.eye(len(Q))-Q)
    k_other=sum(1/vv[1:])
    assert k_other>k_spec+1e-7,(m,ell,k_spec,k_other)
    checks+=2

print('PASS symbolic all-integer cutoff certificates and',checks,'finite diagnostics')
