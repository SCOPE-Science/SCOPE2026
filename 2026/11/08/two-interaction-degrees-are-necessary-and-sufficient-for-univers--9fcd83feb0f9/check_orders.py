"""Exact checks for homogeneous-interaction support sufficiency and obstruction.

This program checks algebraic jet identities and the prescribed full vector-field
Jacobian at rational examples. The arbitrary-dimensional theorem uses a
separate symbolic proof; finite checks are only consistency tests.
"""
from fractions import Fraction
import sympy as sp


def verify_case(n, p, q, r, S):
    assert 1 <= n and 2 <= p < q
    x = sp.symbols('x0:' + str(n))
    t = sum(x) / sp.Integer(n)
    anchor = (q * t**p - p * t**q) / sp.Integer(q - p)
    jets = [x[j] * t**(p-1) - t**p + (t**q - t**p)/sp.Integer(q-p)
            for j in range(n)]
    one = {z: 1 for z in x}
    assert sp.simplify(anchor.subs(one) - 1) == 0
    assert all(sp.simplify(sp.diff(anchor,z).subs(one)) == 0 for z in x)
    for j in range(n):
        assert sp.simplify(jets[j].subs(one)) == 0
        for k in range(n):
            assert sp.simplify(sp.diff(jets[j],x[k]).subs(one) - int(j==k)) == 0
    for i in range(n):
        growth = (sp.Rational(r[i]) + sum(sp.Rational(S[i][j])*x[j]
                  for j in range(n))
                  -(sp.Rational(r[i])+sum(sp.Rational(S[i][j]) for j in range(n)))*anchor
                  +sum((-int(i==j)-sp.Rational(S[i][j]))*jets[j]
                       for j in range(n)))
        assert sp.simplify(growth.subs(one)) == 0
        for j in range(n):
            assert sp.simplify(sp.diff(x[i]*growth, x[j]).subs(one)
                               +int(i==j)) == 0
    # Anchor and jets are sums of homogeneous pieces of exactly the chosen degrees.
    # Check Euler's operator at each endpoint after splitting by symbolic scaling.
    u = sp.Symbol('u')
    for f in [anchor]+jets:
        scaled = sp.expand(f.subs({x[i]:u*x[i] for i in range(n)}, simultaneous=True))
        z = sp.Poly(scaled,u)
        assert set(z.monoms()).issubset({(p,),(q,)})


def verify_radial(n, m, sigma):
    # Negative unit intrinsic growth, pairwise competition -sigma everywhere.
    # On the ray through any positive equilibrium, the universal scalar law is
    # c' = c[-1 - sigma*T*c + (1+sigma*T)*c**m].
    c,T=sp.symbols('c T', positive=True)
    v=c*(-1-sp.Rational(sigma)*T*c+(1+sp.Rational(sigma)*T)*c**m)
    assert sp.factor(v.subs(c,1))==0
    assert sp.simplify(sp.diff(v,c).subs(c,1)-(m+(m-1)*sigma*T))==0
    if sigma==0:
        # Antiderivative of 1/[c(c^m-1)] on (1,infty) is
        # (1/m)*log(1-c**(-m)); at infinity it tends to zero.
        primitive=sp.log(1-c**(-m))/sp.Integer(m)
        assert sp.simplify(sp.diff(primitive,c)-1/v)==0


if __name__=='__main__':
    count=0
    for n in (1,2,3,4):
        r = [sp.Rational((-1)**i*(2*i+1),i+2) for i in range(n)]
        S = [[sp.Rational((i+1)*(j-2),i+j+3) for j in range(n)]
             for i in range(n)]
        for p,q in ((2,3),(2,5),(3,4),(4,7)):
            verify_case(n,p,q,r,S);count+=1
    for n in (1,2,3,4):
        for m in (2,3,4,7,11):
            for sigma in (0,1):
                verify_radial(n,m,sigma);count+=1
    print('PASS: %d exact symbolic tests' % count)
