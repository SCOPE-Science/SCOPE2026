#!/usr/bin/env python3
"""Finite symbolic and numerical consistency checks for a planar Gaussian Fourier eigenfunction theorem."""
from math import pi
import numpy as np
import sympy as sp

x,y=sp.symbols('x y',real=True)
s=sp.pi*(x*x+y*y)
pieces=[-4*s+2*s*s,
        sp.pi*(x*x-y*y)*(3-2*s),
        2*sp.pi*x*y*(3-2*s),
        sp.pi**2*(x**4-6*x*x*y*y+y**4),
        4*sp.pi**2*x*y*(x*x-y*y)]

def on_x(Q): return sp.expand(sp.I*(sp.diff(Q,x)-2*sp.pi*x*Q)/(2*sp.pi))
def on_y(Q): return sp.expand(sp.I*(sp.diff(Q,y)-2*sp.pi*y*Q)/(2*sp.pi))
def ft_poly(P):
    out=0
    for (i,j),coef in sp.Poly(P,x,y).terms():
        v=sp.Integer(1)
        for _ in range(i):v=on_x(v)
        for _ in range(j):v=on_y(v)
        out+=coef*v
    return sp.simplify(sp.expand(out))

for i,P in enumerate(pieces):
    assert sp.simplify(sp.expand(ft_poly(P)-P))==0, ('Fourier eigenfunction basis',i)

# P = s[-A(phi) + sB(phi)]: independent polynomial relation A=2B+B''/2.
t=sp.symbols('t',real=True)
a,c,b,d=sp.symbols('a c b d',real=True)
U=a*sp.cos(t)+c*sp.sin(t)
V=b*sp.cos(2*t)+d*sp.sin(2*t)
B=2-2*U+V
A=4-3*U
assert sp.trigsimp(2*B+sp.diff(B,t,2)/2-A)==0

phi=np.arange(1<<17)*2*pi/(1<<17)
checks=0
for aa,cc,bb,dd in [(0,0,0,0),(.1,-.15,.2,.11),(.42,.12,.25,-.22),
                      (.9,0,.33,0), (1.34,0,.72,0),(-.6,.7,.2,-.12)]:
    u=aa*np.cos(phi)+cc*np.sin(phi)
    v=bb*np.cos(2*phi)+dd*np.sin(2*phi)
    Bv=2-2*u+v
    assert Bv.min()>0,(aa,cc,bb,dd,Bv.min())
    Av=4-3*u
    Bprime=2*aa*np.sin(phi)-2*cc*np.cos(phi)-2*bb*np.sin(2*phi)+2*dd*np.cos(2*phi)
    area=np.mean(np.maximum(Av/Bv,0))
    rhs=2+.5*np.mean((Bprime/Bv)**2)+np.mean(np.maximum(-Av,0)/Bv)
    assert abs(area-rhs)<5e-12,(area,rhs)
    assert area>=2-1e-12
    if aa or bb or cc or dd:assert area>2+1e-3
    checks+=1

# Nonnegative B can have a zero, forcing nonintegrable angular negative radius.
for eps in [1.e-2,1.e-3,1.e-4]:
    # a=1, B(phi)=2-2cos(phi); A(phi)=4-3cos(phi).
    ratio=(4-3*np.cos(eps))/(2-2*np.cos(eps))
    assert ratio*eps**2>0.95
    checks+=1
print('CHECK_OK symbolic_Fourier_eigenbases=5 angular_exact_identities=%d singular_boundary_tests=3'% (checks-3))
