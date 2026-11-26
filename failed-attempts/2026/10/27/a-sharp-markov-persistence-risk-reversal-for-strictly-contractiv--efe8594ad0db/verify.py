"""Independent symbolic and exact-rational checks for a two-state Markov-SGD example.

Requires Python 3 and SymPy. Run: python verify_markov.py
"""
from fractions import Fraction
from itertools import product
import sympy as sp

rho = sp.symbols('rho', real=True)
P = sp.Matrix([[(1 + rho)/2, (1 - rho)/2],
               [(1 - rho)/2, (1 + rho)/2]])
a = sp.Matrix([sp.Rational(-1, 2), sp.Rational(1, 4)])
c = sp.Matrix([sp.Integer(1), sp.Integer(-1)])
pi = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
A = sp.diag(*a)
first = (sp.eye(2) - P*A).inv() * P*sp.diag(*c)*pi
second = (sp.eye(2) - P*sp.diag(*[z*z for z in a])).inv() * (
    P*sp.diag(*[2*a[i]*c[i] for i in range(2)])*first + P*pi)
uf = sp.Matrix([rho/3, -2*rho/3])
vf = sp.Matrix([
    2*(10*rho**2 + rho - 16)/(9*(rho - 6)),
    -8*(2*rho**2 - rho + 4)/(9*(rho - 6))
])
assert all(sp.simplify(x-y) == 0 for x, y in zip(first, uf))
assert all(sp.simplify(x-y) == 0 for x, y in zip(second, vf))
R = sp.factor(sum(vf))
assert sp.simplify(R - sp.Rational(10, 9) - 4*(1-rho**2)/(9*(6-rho))) == 0
assert sp.simplify(R - sp.Rational(32,27) - 2*rho*(1-6*rho)/(27*(6-rho))) == 0
assert sp.simplify(sp.diff(R,rho)-4*(rho**2-12*rho+1)/(9*(rho-6)**2)) == 0
critical=6-sp.sqrt(35)
assert 0 < critical < 1
assert sp.simplify(R.subs(rho, critical) - (58-8*sp.sqrt(35))/9) == 0
assert R.subs(rho,-1) == R.subs(rho,1) == sp.Rational(10,9)
assert R.subs(rho,0) == sp.Rational(32,27)
assert sp.simplify(sum(uf)+rho/3)==0

# Independent path enumeration from X_0=0 and a stationary initial state.
# Compare the enumerated E[X_n^2] with the two-state moment recursion.
assertions = 0
for rr in [Fraction(-3,4), Fraction(-1,2), Fraction(0), Fraction(1,6),
           Fraction(1,4), Fraction(1,2), Fraction(3,4)]:
    PP = [[(1+rr)/2,(1-rr)/2],[(1-rr)/2,(1+rr)/2]]
    aa = [Fraction(-1,2),Fraction(1,4)]
    cc = [Fraction(1),Fraction(-1)]
    dist = {(0,Fraction(0)):Fraction(1,2),(1,Fraction(0)):Fraction(1,2)}
    u = [Fraction(0),Fraction(0)]
    v = [Fraction(0),Fraction(0)]
    for n in range(1,8):
        newdist={}
        for (i,x),w in dist.items():
            y=aa[i]*x+cc[i]
            for j in (0,1):
                key=(j,y)
                newdist[key]=newdist.get(key,Fraction(0))+w*PP[i][j]
        dist=newdist
        u1=[Fraction(0),Fraction(0)]
        v1=[Fraction(0),Fraction(0)]
        for i in (0,1):
            U=aa[i]*u[i]+cc[i]/2
            V=aa[i]**2*v[i]+2*aa[i]*cc[i]*u[i]+Fraction(1,2)
            for j in (0,1):
                u1[j]+=PP[i][j]*U
                v1[j]+=PP[i][j]*V
        u,v=u1,v1
        assert sum(x*w for (_,x),w in dist.items()) == sum(u)
        assertions+=1
        assert sum(x*x*w for (_,x),w in dist.items()) == sum(v)
        assertions+=1
        assert sum(dist.values()) == 1
        assertions+=1
    assert sp.Rational(sum(v)) >= 0
    assertions+=1
print(f'PASS: exact symbolic identities and {assertions} independent rational checks')
