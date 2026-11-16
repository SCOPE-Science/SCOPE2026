#!/usr/bin/env python3
"""Standalone exact and independent numerical checks for a cube-face Slepian spectrum."""
import sympy as sp
import numpy as np

p, sq = sp.pi, sp.sqrt(3)
A,B,C,E = sp.symbols('A B C E')
Omega=2*p/3
T1=8*sq/27
T3=2*sq/27
rels = [A-3*B-T1, 2*C-3*B-3*E+T1,4*E-B-C+T3,A+4*B+2*C+2*E-Omega]
sol=sp.solve(rels, (A,B,C,E), dict=True)
assert len(sol)==1
sol=sol[0]
assert sol == {A:2*p/15+52*sq/135,B:2*p/45+4*sq/135,C:2*p/15-26*sq/135,E:2*p/45-8*sq/135},sol
norms=[16*p/5,4*p/15,4*p/15,16*p/15,4*p/15]
local=[3*A-12*B+Omega, B, B, 2*(C-E), E]
vals=[sp.simplify(v.subs(sol)/n) for v,n in zip(local,norms)]
expected=[sp.Rational(1,6)+sq/(4*p),sp.Rational(1,6)+sq/(9*p),sp.Rational(1,6)+sq/(9*p),sp.Rational(1,6)-sq/(4*p),sp.Rational(1,6)-2*sq/(9*p)]
assert all(sp.simplify(a-b)==0 for a,b in zip(vals,expected)),(vals,expected)
assert sp.simplify(sum(vals)-sp.Rational(5,6))==0
assert all(sp.N(vals[i])>sp.N(vals[j]) for i,j in [(0,1),(1,4),(4,3)])
# An independent 2D Gauss-Legendre integration of all 25 entries.
from numpy.polynomial.legendre import leggauss
for n in (24,40,64,100):
    nodes,w=leggauss(n)
    u,v=np.meshgrid(nodes,nodes,indexing='ij')
    wu,wv=np.meshgrid(w,w,indexing='ij')
    denom=1+u*u+v*v
    x=1/np.sqrt(denom); y=u*x; z=v*x
    qs=np.stack((3*x*x-1,x*y,x*z,y*y-z*z,y*z),axis=-1)
    weights=(wu*wv)/(denom**1.5)
    gram=np.einsum('ijk,ijl,ij->kl',qs,qs,weights,optimize=True)
    scaled=gram/(np.sqrt(np.array([float(t) for t in norms]))[:,None]*np.sqrt(np.array([float(t) for t in norms]))[None,:])
    err=float(np.max(np.abs(scaled-np.diag(np.array([float(a) for a in expected])))))
    print(f'quadrature order={n}, max abs matrix error={err:.3g}')
    assert err < (2e-10 if n==24 else 4e-14), (n,err)
print('PASS: symbolic moments, eigenvalues and strict ordering; independent full Gram quadrature')
for i,val in enumerate(vals):print(f'Q{i}: {val} ≈ {float(val):.15f}')
