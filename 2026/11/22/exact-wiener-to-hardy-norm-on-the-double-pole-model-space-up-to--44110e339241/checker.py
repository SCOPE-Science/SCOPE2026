"""Exact algebraic checks for a two-dimensional rational Fourier norm."""
import sympy as sp

r=sp.symbols('r', real=True)
S=sp.factor(1-r*r)
M=sp.Matrix([[(1+r*r)/S**3, 2*r/S**3], [2*r/S**3, (1+r*r)/S**3]])
Minv=sp.Matrix([[1-r**4,-2*r*S],[-2*r*S,1-r**4]])
assert all(sp.simplify(v)==0 for v in (M*Minv-sp.eye(2)))
v0=sp.Matrix([1,0]); v1=sp.Matrix([2*r,1])/(1-r)
v2=sp.Matrix([r*r,r])/(1-r)**2
G=lambda v,w:sp.factor((v.T*Minv*w)[0])
A=2*r**3*(1+r)
B=r**2*(1+r)**2
C=r*(1+r)**2*(1-2*r*r)/(1-r)
assert sp.simplify(G(v0,v1)-A)==0
assert sp.simplify(G(v0,v2)+B)==0
assert sp.simplify(G(v1,v2)-C)==0
assert sp.simplify(B*C-A*(B+C)-r**3*(1+r)**3*(1-2*r)*(1+2*r))==0
v=v0-v1-v2
W=sp.simplify(Minv*v)
assert all(sp.simplify(W[i]-(1-r*r)*e)==0 for i,e in enumerate([1+2*r*r,-(1+4*r)]))
formula=2*(1+r)/(1-r)*(1+2*r*r*(1-r)**2)
assert sp.simplify(G(v,v)-formula)==0
# Verify the generating identity coefficient by coefficient with exact rational numbers.
for rr in [sp.Rational(j,10) for j in range(1,6)]:
    aa=1+2*rr*rr; bb=-(1+4*rr)
    coefs=[aa]+[sp.expand((k+1)*rr**k*aa+k*rr**(k-1)*bb) for k in range(1,20)]
    assert all(c<0 for c in coefs[1:])
    bound=sp.simplify(abs(aa)+abs(2*rr*aa+bb)/(1-rr)+rr*abs(rr*aa+bb)/(1-rr)**2)
    gram=sp.simplify((sp.Matrix([aa,bb]).T*M.subs(r,rr)*sp.Matrix([aa,bb]))[0])
    assert sp.simplify(bound**2-gram*formula.subs(r,rr))==0
assert sp.simplify(formula.subs(r,sp.Rational(1,2))-sp.Rational(27,4))==0
assert sp.simplify(formula.subs(r,0)-2)==0
print('PASS: exact Gram inverse; exact phase correlations; endpoint polynomial; extremizers; five rational checks')
