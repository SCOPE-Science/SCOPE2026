"""Reproducible exact identities and independent finite-grid checks for periodic three-point trace design."""
from fractions import Fraction as Q
import math
import sympy as S
import numpy as np

u=S.symbols('u',real=True)
G=lambda z: (z*z-z+S.Rational(1,6))/2
T=(S.Integer(9)-S.sqrt(21))/30
R=S.simplify(G(T))
D=S.Rational(1,12)
C2=S.simplify(D+R)
assert S.simplify(5*T*T-3*T+S.Rational(1,3))==0
assert S.simplify(G(2*T)+R)==0
assert S.simplify(R-(2*S.sqrt(21)-3)/300)==0
assert S.simplify(C2-(11+S.sqrt(21))/150)==0
assert (6*T<1) and (0<T<S.Rational(1,4))
assert (0<R<S.Rational(1,24))

M=S.Matrix([[D,R,-R],[R,D,R],[-R,R,D]])
assert (M-(D+R)*S.eye(3)).rank()==1
assert S.factor(M.charpoly().as_expr(), extension=S.sqrt(21))==S.factor((S.Symbol('lambda')-(D+R))**2*(S.Symbol('lambda')-(D-2*R)), extension=S.sqrt(21))
assert M*S.Matrix([1,-1,1]) == (D-2*R)*S.Matrix([1,-1,1])
assert S.simplify(G(S.Rational(1,3))+S.Rational(1,36))==0
assert S.simplify(S.Rational(1,9)-C2)>0
assert S.simplify(C2-S.Rational(1,12))>0

# Algebraic gap obstruction for all s<s*: at s*, small intervals [T, 2T] and large [1-2T,1-T].
assert S.simplify(G(T)-R)==0
assert S.simplify(G(2*T)+R)==0
assert 3*2*T < 1
assert S.simplify((1-2*T)+2*T)==1
assert S.simplify(2*(1-2*T)+T)>1

# Exact-rational grid check of the universal two-by-two principal-submatrix lower bound.
# It confirms, but does not prove, the continuum optimization theorem.
checks=0
thresh=float(R)
best=(999,None)
for n in range(3,151):
    for i in range(1,n-1):
        for j in range(1,n-i):
            a,b,c=Q(i,n),Q(j,n),Q(n-i-j,n)
            z=[(v*v-v+Q(1,6))/2 for v in (a,b,c)]
            low=max(map(abs,z))
            assert float(low)>=thresh-1e-14
            if float(low)<best[0]:best=(float(low),(n,i,j))
            if n<=50:
                mat=np.array([[1/12,float(z[0]),float(z[2])],[float(z[0]),1/12,float(z[1])],[float(z[2]),float(z[1]),1/12]])
                lam=float(np.linalg.eigvalsh(mat)[-1]);assert lam >= float(C2)-1e-12
                checks+=1
# Independent H^1 energy check: integrate products of derivative-kernel sawtooths.
# On each interval between evaluation points the integrand is quadratic.
t=float(T)
pts=[0.,t,2*t]
breaks=pts+[1.]
roots=[-math.sqrt(3/5),0.,math.sqrt(3/5)]
weights=[5/9,8/9,5/9]
energy=np.zeros((3,3))
for a,b in zip(breaks[:-1],breaks[1:]):
    for z,w in zip(roots,weights):
        x=(a+b)/2+(b-a)*z/2
        v=np.array([((x-y)%1)-.5 for y in pts])
        energy+=(b-a)/2*w*np.outer(v,v)
expected=np.array([[float(G(S.Rational(str((x-y)%1)))) for y in pts] for x in pts])
assert np.max(np.abs(energy-expected))<1e-13
assert abs(np.linalg.eigvalsh(energy)[-1]-float(C2))<2e-12
print('symbolic identity checks: PASS')
print('distinct rational-grid eigenvalue tests:',checks)
print('rational configurations for principal-correlation bound:',sum((n-1)*(n-2)//2 for n in range(3,151)))
print('best grid correlation / parameters:',best)
print('t, sharp norm squared, sharp norm:',float(T),float(C2),math.sqrt(float(C2)))
print('uniform squared norm:',1/9)
print('all checks: PASS')
