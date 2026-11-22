"""Supplementary reproducibility checks for a sharp five-point real L4 convolution norm.
Run: python check.py (requires sympy and numpy). Finite tests complement the proof.
"""
import itertools
import math
import numpy as np
import sympy as sp

r,t=sp.symbols('r t', real=True)
q=sp.sqrt(5)
a=(q-1)/4
b=-(q+1)/4
N=sp.expand(6*(a**4+b**4*r**4)+24*a*a*b*b*r*r-8*a**3*b*r-8*a*b**3*r**3)
D=sp.expand(6*(1+r**4)+24*r*r-8*r-8*r**3)
P=sp.expand((-15-6*q)*r**6+(45+27*q)*r**5+(-15-3*q)*r**4+19*q*r**3+(15-3*q)*r**2+(-45+27*q)*r+15-6*q)
assert sp.simplify(sp.diff(N,r)*D-N*sp.diff(D,r)-P)==0
assert sp.simplify(a-sp.cos(2*sp.pi/5))==0
assert sp.simplify(b-sp.cos(4*sp.pi/5))==0
Q=sp.Poly(sp.expand(sum(P.coeff(r,i)*(4*t)**i*(1+t)**(6-i) for i in range(7))),t)
H=sp.Poly(sp.expand(P.subs(r,4+t)),t)
assert [sp.sign(Q.nth(i)) for i in range(7)] == [1,1,1,1,1,1,-1]
assert [sp.sign(H.nth(i)) for i in range(7)] == [-1]*7
assert sp.sign(P.subs(r,sp.Rational(362064679,100000000)))==1
assert sp.sign(P.subs(r,sp.Rational(362064680,100000000)))==-1
root=float(sp.nroots(sp.Poly(P,r),maxsteps=200)[1]) if False else 3.62064679016704
# The polynomial signs plus Descartes prove a unique positive root.
assert abs(float(P.subs(r,root))) < 1e-8
c=float((N/D).subs(r,root))**0.25
assert abs(c-0.8634764599843693)<1e-12
assert c > float(-b) and c < 1

# Check fourth-power character resonance coefficients from every four-tuple.
counts={}
for comb in itertools.product((1,-1,2,-2),repeat=4):
    if sum(comb)%5==0:
        key=tuple(sorted(comb))
        counts[key]=counts.get(key,0)+1
assert counts=={
    (-2,-2,-2,1):4,(-2,-2,2,2):6,(-2,-1,-1,-1):4,
    (-2,-1,1,2):24,(-1,-1,1,1):6,(-1,2,2,2):4,(1,1,1,2):4}

rng=np.random.default_rng(20260914)
w=np.exp(2j*np.pi/5)
for trial in range(1200):
    u=complex(*rng.normal(size=2));v=complex(*rng.normal(size=2))
    x=np.array([2*np.real(u*w**j+v*w**(2*j)) for j in range(5)])
    y=(np.roll(x,-1)+np.roll(x,1))/2
    direct=np.mean(x**4)
    formula=6*(abs(u)**4+abs(v)**4)+24*abs(u*v)**2+8*np.real(u**3*v)+8*np.real(v**3*u.conjugate())
    assert abs(direct-formula)<1e-9*max(1,direct)
    assert np.mean(y**4)<= (c**4+1e-10)*direct
    assert abs(np.mean(x))<1e-12

# Equality witness: u=1, v=-r solves both resonance-phase constraints.
x=np.array([2*np.real(w**j-root*w**(2*j)) for j in range(5)])
y=(np.roll(x,-1)+np.roll(x,1))/2
assert abs((np.mean(y**4)/np.mean(x**4))**0.25-c)<1e-12
# For the cyclic derivative, the map is invertible on mean-zero real vectors.
Delta=np.array([[(int((j+1)%5==k)-int((j-1)%5==k)) for k in range(5)] for j in range(5)],dtype=float)
assert np.linalg.matrix_rank(np.vstack((Delta,np.ones(5))))==5
print('PASS: exact sextic derivative, one-root sign certificates, five-point resonance enumeration, 1200 random tests, equality witness, difference-map invertibility')
print('root:',root,'sharp L4 norm:',c,'spectral L2 norm:',float(-b))
