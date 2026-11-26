"""Symbolic and sample verification of alternating-mesh BDF3 parasitic spectra.

Requires Python 3.10+ and SymPy. The analytic proof is contained in RESULT.md;
finite samples here only cross-check, not certify, universal assertions.
"""
import sympy as S
r = S.symbols('r', positive=True)

def transition(h0,h1,h2):
    nodes = (S.Integer(0), -h0, -h0-h1, -h0-h1-h2)
    vandermonde = S.Matrix([[t**k for t in nodes] for k in range(4)])
    w = list(vandermonde.inv()*S.Matrix([0,1,0,0]))
    # derivative of interpolation polynomial at newest node
    a = S.factor(-(w[0]+w[1])/w[0])
    b = S.factor(w[3]/w[0])
    return S.Matrix([[a,b],[1,0]])

A=transition(r,S.Integer(1),r)
B=transition(S.Integer(1),r,S.Integer(1))
assert A == S.Matrix([[r**2*(4*r+3)/(5*r*r+5*r+1),-r*(r+1)/(5*r*r+5*r+1)],[1,0]])
assert S.simplify(B-S.Matrix([[(3*r+4)/(r*(r*r+5*r+5)),-(r+1)/(r*r+5*r+5)],[1,0]]))==S.zeros(2)
M=S.simplify(B*A)
D=(r*r+5*r+5)*(5*r*r+5*r+1)
t=-(r**4-r**3-5*r*r-r+1)/D
d=r*(r+1)**2/D
assert S.factor(M.trace()-t)==0
assert S.factor(M.det()-d)==0
checks = {
  '1 - 5 trace + 25 det': (1-5*t+25*d, 2*(5*r**4+25*r**3+38*r**2+25*r+5)/D),
  '1 + 5 trace + 25 det': (1+5*t+25*d, 6*r*(10*r*r+21*r+10)/D),
  '1 - 25 det': (1-25*d, (5*r**4+5*r**3+r*r+5*r+5)/D),
}
for key,(lhs,rhs) in checks.items():
    assert S.factor(lhs-rhs)==0,key
assert S.limit(t,r,S.oo)==S.Rational(-1,5)
assert S.limit(d,r,S.oo)==0
assert S.limit(t,r,0,dir='+')==S.Rational(-1,5)
assert S.limit(d,r,0,dir='+')==0
assert S.factor(t-t.subs(r,1/r))==0
assert S.factor(d-d.subs(r,1/r))==0

# Independent substitution into published coefficient representation.
x,y=S.symbols('x y')
c0=(1+2*x)/(1+x)+x*y/(1+y+x*y)
c1=-x/(1+x)-x*y/(1+y+x*y)-x*y*y*(1+x)/((1+y+x*y)*(1+y))
c2=x*y*y*(1+x)/((1+y+x*y)*(1+y))
for h0,h1,h2,mat in [(r,S.Integer(1),r,A),(S.Integer(1),r,S.Integer(1),B)]:
    q={x:h0/h1,y:h1/h2}
    via_coeff=S.Matrix([[-h0/h1*c1.subs(q)/c0.subs(q),-h0/h2*c2.subs(q)/c0.subs(q)],[1,0]])
    assert S.simplify(mat-via_coeff)==S.zeros(2)

# Spot checks by direct derivative recurrence and exact characteristic roots.
for num in [S.Rational(1,1000), S.Rational(1,10),S.Rational(1,2), S.Integer(1),S.Integer(2),S.Integer(10),S.Integer(1000)]:
    mm=M.subs(r,num)
    for eig in mm.eigenvals():
        assert abs(complex(S.N(eig,30))) < S.Rational(1,5)
print('VERIFY_OK: symbolic recurrences, Schur factors, reciprocal symmetry, endpoint sharpness, 7 eigenvalue spot checks')
