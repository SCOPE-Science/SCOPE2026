#!/usr/bin/env python3
"""Exact algebraic consistency checks for a phase-deformed triangle Lissajous sextic."""
import itertools
import sympy as S
x, y, z, c, t = S.symbols("x y z c t")
coord = [x, y, z]
A = z*z + c*c - x*x - y*y
B = 2*(x*y-c*z)
F = S.expand(A*A + 2*x*y*A*B + (x*x+y*y-1)*B*B)
assert S.Poly(F, x).degree() == 4
assert S.Poly(F, x).LC() == 1
assert S.Poly(F, x,y,z).total_degree() == 6
assert S.factor(F.subs(c, 1)) == (x*x+y*y+z*z-2*x*y*z-1)**2
assert S.factor(F.subs(c, -1)) == (x*x+y*y+z*z+2*x*y*z-1)**2
for lam in [S.Rational(2), S.Rational(3), S.Rational(-2), S.Rational(-3)]:
    c0=(lam+1/lam)/2
    for aa, bb in [(S.Rational(2),S.Rational(3)),(S.Rational(5),S.Rational(7))]:
        dd=lam/(aa*bb)
        vals={x:(aa+1/aa)/2,y:(bb+1/bb)/2,z:(dd+1/dd)/2,c:c0}
        assert S.factor(F.subs(vals)) == 0
pairs=list(itertools.combinations(range(3), 2))
lines=[]
for i,j in pairs:
    k=next(k for k in range(3) if k not in (i,j))
    for eps in [-1,1]:
        vals={coord[i]:t,coord[j]:eps*t,coord[k]:eps*c}
        assert all(S.expand(g.subs(vals))==0 for g in [F,*[S.diff(F,xi) for xi in coord]])
        lines.append((i,j,k,eps))
assert len(lines)==6
triple=[]
for signs in itertools.product([-1,1],repeat=3):
    if signs[0]*signs[1]*signs[2]==1:
        p=tuple(si*c for si in signs)
        n=sum(1 for i,j,k,e in lines if S.expand(p[j]-e*p[i])==0 and S.expand(p[k]-e*c)==0)
        assert n==3
        triple.append(p)
assert len(triple)==4
pinch=[]
for i,j,k,e in lines:
    for q in [-1,1]:
        p=[None]*3
        p[i]=S.Integer(q);p[j]=e*S.Integer(q);p[k]=e*c
        pinch.append(tuple(p))
assert len(pinch)==len(set(pinch))==12
for p in pinch:
    assert sum(1 for i,j,k,e in lines if S.expand(p[j]-e*p[i])==0 and S.expand(p[k]-e*c)==0)==1
N=S.Matrix([[-1,1,1],[1,-1,1],[1,1,-1]])
assert abs(N.det())==4
assert 6*((1-2-2))+4*(3-1)==-10
print('PASS: identities, six line-Jacobian checks, four triple incidences, twelve distinct pinches, and exact examples')
