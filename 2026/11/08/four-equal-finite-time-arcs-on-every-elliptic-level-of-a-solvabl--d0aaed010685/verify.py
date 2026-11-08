"""Exact algebra and numerical flight-time checks for the rational planar flow.
Requires Python 3, SymPy, and mpmath. This program is corroboration of a proof.
"""
import math
from fractions import Fraction
import sympy as sp
import mpmath as mp

x, y, a, b, p, q = sp.symbols('x y a b p q', real=True)
B = sp.Matrix([[1, a], [-b, -1]])
G = sp.Matrix([[b, 1], [1, a]])
S = sp.Matrix([[p, (a*p+b*q)/2], [(a*p+b*q)/2, q]])
D = sp.expand((a*p+b*q)**2-4*p*q)
V = B*sp.Matrix([x, y])
Q = sp.expand((sp.Matrix([x,y]).T*S*sp.Matrix([x,y]))[0])
K = (p*x*x-q*y*y)/2
checks = [
    (sp.expand(B*B-(1-a*b)*sp.eye(2)), sp.zeros(2)),
    (sp.expand(B.T*G+G*B), sp.zeros(2)),
    (sp.factor(sum(sp.diff(K,z)*v for z,v in zip((x,y), V))-Q), 0),
    (sp.factor(sp.trace(G.inv()*S)), 0),
    (sp.factor(S.det()+D/4), 0),
    (sp.factor(sp.trace(G.inv()*sp.diag(p/2,-q/2))**2-4*sp.det(sp.diag(p/2,-q/2))/G.det() - D/(4*(a*b-1)**2)),0),
    (sp.factor(D-(a*p-b*q)**2-4*(a*b-1)*p*q),0),
]
for idx,(got,want) in enumerate(checks,1):
    assert got == want, f'exact identity #{idx}: {got} != {want}'
print('7 exact symbolic identities PASS')

mp.mp.dps=55
params=[(2,2,1,0),(2,3,1,-1),(3,4,1,2),(-2,-2,1,1),(-3,-2,2,-5),(mp.mpf('1.25'),mp.mpf('1.1'),mp.mpf('-0.25'),mp.mpf('0.8'))]
for j,(aa,bb,pp,qq) in enumerate(params,1):
    aa,bb,pp,qq=map(mp.mpf,(aa,bb,pp,qq))
    w=mp.sqrt(aa*bb-1)
    Delta=(aa*pp+bb*qq)**2-4*pp*qq
    assert Delta>0
    h=abs(bb)  # x0=1, y0=0, H=sign(a)*b=abs(b)
    # X(s)= (cos(ws)+sin(ws)/w, -b sin(ws)/w)
    X=lambda s: (mp.cos(w*s)+mp.sin(w*s)/w, -bb*mp.sin(w*s)/w)
    Qfun=lambda s: (lambda xx,yy: pp*xx*xx+(aa*pp+bb*qq)*xx*yy+qq*yy*yy)(*X(s))
    q0=Qfun(0)
    qprime=mp.diff(Qfun,mp.mpf(0))
    phase=mp.atan2(qprime/(2*w),q0)
    expected=h*mp.sqrt(Delta)/(2*(aa*bb-1))
    for k in range(4):
        sl=(phase+mp.pi/2+k*mp.pi)/(2*w)
        sr=sl+mp.pi/(2*w)
        assert abs(Qfun(sl))<mp.mpf('1e-45')
        assert abs(Qfun(sr))<mp.mpf('1e-45')
        estimate=mp.quad(lambda s: abs(Qfun(s)),[sl, (sl+sr)/2, sr])
        assert abs(estimate-expected)<mp.mpf('1e-44'),(j,k,estimate,expected)
    print(f'case {j}: four equal flight times PASS; lifespan={mp.nstr(expected,18)}')
print('24 numerical arc-integral checks PASS')
