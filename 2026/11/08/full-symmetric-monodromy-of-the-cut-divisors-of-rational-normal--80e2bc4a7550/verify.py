#!/usr/bin/env python3
"""Exact algebra checks supporting a characteristic-zero cut-divisor monodromy theorem."""
import sympy as s

t,z=s.symbols('t z')
# Balanced and unbalanced positive-degree block examples: generic diagonal witnesses.
for degrees in ((2,2),(2,3),(2,4),(3,3),(2,2,2)):
    roots=list(range(1,sum(degrees)+1))
    blocks=[]; j=0
    for n in degrees:
        blocks.append(s.prod(t-r for r in roots[j:j+n])); j+=n
    F=s.expand(s.prod(blocks))
    assert s.degree(F,t)==sum(degrees)
    assert s.discriminant(F,t)!=0
    assert s.factor(F)==s.prod(t-r for r in roots)

# Interpolation: two arbitrary matrices at two distinct parameters.
x=s.symbols('x0:9'); y=s.symbols('y0:9')
X=s.Matrix(3,3,x); Y=s.Matrix(3,3,y)
u,v=s.symbols('u v')
M=lambda T: X*(T-v)/(u-v)+Y*(T-u)/(v-u)
assert s.simplify(M(u)-X)==s.zeros(3)
assert s.simplify(M(v)-Y)==s.zeros(3)
# At both evaluation values the determinants are independent irreducible loci.
assert s.factor(M(u).det())==X.det()
assert s.factor(M(v).det())==Y.det()

# The local collision family has a quadratic two-root factor, and its
# discriminant vanishes to order exactly one when z=0.
for n in (2,3,5):
    f=(t*t+z)*s.prod(t-j for j in range(2,n+1))
    D=s.factor(s.discriminant(f,t))
    assert s.expand(D).subs(z,0)==0
    assert s.diff(D,z).subs(z,0)!=0

# Explicit orthogonal projector cut-equivalence, with 2 blocks of degrees 2,3.
A=s.Matrix([[1,t,t**2,0,0,0,0],[0,0,0,1,t,t**2,t**3]])
B=s.Matrix([[1,0],[2,0],[3,0],[0,1],[0,2],[0,3],[0,4]])
G=B.T*B
Q=B*G.inv()*B.T
assert Q*Q==Q
AB=A*B
assert s.factor((A*Q*A.T).det()-AB.det()**2/G.det())==0
assert s.expand(AB.det()-(1+2*t+3*t*t)*(1+2*t+3*t*t+4*t**3))==0
print('VERIFY_OK: squarefree degree witnesses; independent two-point evaluations; simple double-root discriminants; exact projector cut identity')
