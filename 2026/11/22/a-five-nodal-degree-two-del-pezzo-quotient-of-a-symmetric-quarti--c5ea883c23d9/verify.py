"""Exact algebraic identities for an explicit quartic-surface quotient.

Requires SymPy as declared in requirements.txt. This checks the identity and
branch intersections; the proof of normality and finite map is mathematical.
"""
import sympy as S

x,y,z,w=S.symbols('x y z w')
vars=(x,y,z,w)
W=x**3*y+x*y**3+z**3*w+z*w**3
s=x+y;t=z+w;p=x*y;q=z*w
U=s+t;d=s-t;e=p-q
A=U**2;B=s*t;C=p+q;Z=4*U*d*e-U**2*d**2
Q=A**2-4*A*B+8*A*C-16*B*C-16*C**2
for perm in [(y,x,z,w),(x,y,w,z),(z,w,x,y)]:
    change=dict(zip(vars,perm))
    for value in (W,A,B,C,Z):
        assert S.expand(value-value.subs(change,simultaneous=True))==0
assert S.expand(Z**2-A*(A-4*B)*Q+16*W*U**2*d**2)==0
AA,BB,CC=S.symbols('A B C')
quad=AA**2-4*AA*BB+8*AA*CC-16*BB*CC-16*CC**2
conic_matrix=S.Matrix([[1,-2,4],[-2,0,-8],[4,-8,-16]])
assert conic_matrix.det()==128
assert S.factor(quad.subs(AA,0))==-16*CC*(BB+CC)
assert S.factor(quad.subs(AA,4*BB))==16*CC*(BB-CC)
assert quad.subs({AA:0,BB:0,CC:1})==-16
points=[(0,0,1),(0,1,0),(0,1,-1),(4,1,0),(4,1,1)]
for a,b,c in points:
    assert a*(a-4*b)*quad.subs({AA:a,BB:b,CC:c})==0
assert len(set(points))==5
print('PASS: all exact invariant, relation and five-node branch checks')
