"""Reproducibility checks for the planar absolute-value escape theorem.
Finite tests supplement, but do not replace, the analytic quadrant proof.
"""
import sympy as sp
from fractions import Fraction
import random

a=sp.symbols('a', positive=True)
J1=sp.Matrix([[1,a],[1,-a]])
J3=sp.Matrix([[-1,a],[1,a]])
J4=sp.Matrix([[1,a],[1,a]])
lam=sp.symbols('lam')
p1=sp.factor(J1.charpoly(lam).as_expr())
p3=sp.factor(J3.charpoly(lam).as_expr())
assert sp.expand(p1-(lam**2+(a-1)*lam-2*a))==0
assert sp.expand(p3-(lam**2-(a-1)*lam-2*a))==0
assert all(sp.expand(f.subs(lam,1))<0 for f in [p1.subs(a,sp.Rational(3,2)),p3.subs(a,sp.Rational(3,2))])
assert sp.factor(p1.subs(lam,-1))==2-3*a
assert sp.factor(p3.subs(lam,-1))==-a
assert sp.factor(p1.subs(lam,1))==-a
assert sp.factor(p3.subs(lam,1))==2-3*a
mu=sp.factor(sp.trace(J4*J1))
assert mu==1+2*a-a*a
assert sp.factor((J4*J1).det())==0
q=sp.factor((a+2)/(a*(2-a)))
r=sp.Matrix([(1+a)*q-1,(1-a)*q-1])
assert sp.simplify(r[0]+a*r[1]-1-q)==0
assert sp.simplify(mu*q-(a+2)-q)==0
P1=sp.Matrix([2+1/a,1/a]);P3=sp.Matrix([1/(3*a-2),3/(3*a-2)])
assert sp.simplify(J1*P1-sp.Matrix([1,1])-P1)==sp.zeros(2,1)
assert sp.simplify(J3*P3-sp.Matrix([1,1])-P3)==sp.zeros(2,1)

def F(p, b):
    x,y=p
    return (abs(x)+b*y-1, x-b*abs(y)-1)

for b in [Fraction(1),Fraction(6,5),Fraction(3,2),Fraction(7,4)]:
    t=Fraction(b+2,b*(2-b))
    v=F((t,t),b)
    assert v[0]>0 and v[1]<0
    assert F(v,b)==(t,t)
    p=(Fraction(2)+1/b,1/b)
    assert F(p,b)==p

# Exhaustive rational grid within the lower-left invariant cone, each image stays there.
for b in [Fraction(1),Fraction(6,5),Fraction(2),Fraction(3)]:
    for xi in range(-20,1):
        for yi in range(-20,xi+1):
            x,y=Fraction(xi,7),Fraction(yi,7)
            u,v=F((x,y),b)
            assert u<=0 and v<=u

# Positive diagonal returns through Q4 or enters invariant Q3, as the proof predicts.
for b in [Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(3)]:
    m=1+2*b-b*b
    for j in range(1,201):
        t=Fraction(j,13)
        u,v=F((t,t),b)
        assert v<0
        if t>1/(1+b):
            assert u>0
            assert F((u,v),b)==(m*t-(b+2),)*2

# Sample orbits in bounded windows: no persistent bounded nonperiodic trajectories observed.
random.seed(237)
counts={}
for b in [1,1.5,2,2.5,3]:
    escaped=0
    for _ in range(1000):
        p=(random.uniform(-6,6),random.uniform(-6,6))
        for n in range(900):
            p=F(p,b)
            if max(abs(p[0]),abs(p[1]))>1e8:
                escaped+=1
                break
    counts[b]=escaped
    assert escaped>=995,(b,escaped)
print('VERIFY_OK symbolic_matrices=3 exact_2cycles=4 invariant_cone_grid=1844 diagonal_returns=1000 numerical_escape_samples='+str(counts))
