#!/usr/bin/env python3
"""Exact symbolic checks and finite rational tests for a five-cycle kernel."""
import sympy as sp
from itertools import product

x,w=sp.symbols('x w', positive=True)
L=sp.zeros(5)
for i in range(5):
    j=(i+1)%5
    c=w if i==4 else sp.Integer(1)
    L[i,i]+=c; L[j,j]+=c
    L[i,j]-=c; L[j,i]-=c
M=x*sp.eye(5)+L
G=M.inv()
Q=x*x+5*x+5
D=x*x+3*x+1+(2*x+4)*w
h=(x*x+3*x+1)/(x*Q)
E=Q*D
fA=h+(1-w)*(x+2)**2/E
fB=h+(1-w)/E
fC=h
for i,g in [(0,fA),(4,fA),(1,fB),(3,fB),(2,fC)]:
    assert sp.cancel(G[i,i]-g)==0
P_A=sp.factor(x*Q*D*fA)
P_B=sp.factor(x*Q*D*fB)
F=3*x**4+(12+4*w)*x**3+(11+10*w)*x**2-(1+4*w)
H=x**6+8*x**5+(22-2*w)*x**4+(22-14*w)*x**3+(2-34*w)*x**2-(8+32*w)*x-(3+12*w)
qA=-sp.diff(fA,x)/fA
qB=-sp.diff(fB,x)/fB
qC=-sp.diff(fC,x)/fC
assert sp.cancel(qC-qB-(w-1)*F/((x*x+3*x+1)*D*P_B))==0
assert sp.cancel(qB-qA-(w-1)*H/(P_A*P_B))==0
assert sp.cancel((fA-fC)-(x+2)**2*(fB-fC))==0
count=8
# Exact rational sign brackets for w=1/2; uniqueness is proved in the text.
for polynomial, left, right in [
    (F, sp.Rational(372419,10**6),sp.Rational(372420,10**6)),
    (H, sp.Rational(1023614,10**6),sp.Rational(1023615,10**6)),
]:
    assert polynomial.subs({w:sp.Rational(1,2),x:left})<0
    assert polynomial.subs({w:sp.Rational(1,2),x:right})>0
    count+=2
for ww in [sp.Rational(k,20) for k in range(1,20)]:
    fn=sp.Poly(F.subs(w,ww),x)
    hn=sp.Poly(H.subs(w,ww),x)
    af=float(sp.nroots(fn,maxsteps=200)[-1]) if False else max(float(sp.re(r)) for r in sp.nroots(fn,maxsteps=200) if abs(float(sp.im(r)))<1e-10 and float(sp.re(r))>0)
    be=max(float(sp.re(r)) for r in sp.nroots(hn,maxsteps=200) if abs(float(sp.im(r)))<1e-10 and float(sp.re(r))>0)
    assert 0<af<be
    count+=1
for xx,ww in product([sp.Rational(k,7) for k in range(1,22)], [sp.Rational(k,11) for k in range(1,11)]):
    V=M.subs({x:xx,w:ww}).inv()
    scores=[sp.factor(sum(V[j,i]**2 for j in range(5))/V[i,i]) for i in range(5)]
    fd=[sp.factor(z.subs({x:xx,w:ww})) for z in (fA,fB,fC)]
    qd=[sp.factor(z.subs({x:xx,w:ww})) for z in (qA,qB,qC)]
    assert [V[i,i] for i in [0,1,2]]==fd
    assert [scores[i] for i in [0,1,2]]==qd
    assert scores[0]==scores[4] and scores[1]==scores[3]
    assert fd[0]>fd[1]>fd[2]
    count+=4
print(f'PASS {count} exact and algebraic/numerical-root tests; root numerics are supplementary, not proof')
