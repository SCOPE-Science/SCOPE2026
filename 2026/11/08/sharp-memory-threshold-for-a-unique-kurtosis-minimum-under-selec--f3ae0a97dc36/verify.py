#!/usr/bin/env python3
"""Exact symbolic verification of the memory-dependent resetting kurtosis theorem.

Requires SymPy. No stochastic sampling is used to certify global statements.
Run: python verify.py
"""
import sympy as sp

G, R, Z = sp.symbols('g r z', positive=True)


def stationary_moments(degree, preceding):
    """Solve all degree-n stationary monomial-generator equations in x,q."""
    mat = sp.zeros(degree + 1)
    rhs = sp.zeros(degree + 1, 1)
    for i in range(degree + 1):
        j = degree - i
        mat[i, i] = i + j / G + (R if i else 0)
        if i:
            mat[i, i - 1] = -i
        if j:
            mat[i, i + 1] = -j / G
        if i >= 2:
            rhs[i] += i * (i - 1) * preceding[i - 2]
        if j >= 2:
            rhs[i] += j * (j - 1) * preceding[i] / G
    sol = [sp.cancel(x) for x in mat.inv() * rhs]
    assert all(sp.cancel(v) == 0 for v in mat * sp.Matrix(sol) - rhs)
    return sol


m2 = stationary_moments(2, [sp.Integer(1)])
m4 = stationary_moments(4, m2)
U = G * (R + 1) + 1
V = G * (R + 2) + 1
W = G * (R + 2) + 2
H = G**3 * (R**3 + 6*R**2 + 9*R + 3) + G**2 * (5*R**2 + 13*R + 9) + G*(7*R + 9) + 3
J = G**3 * (R**3 + 9*R**2 + 26*R + 24) + G**2 * (6*R**2 + 31*R + 36) + G*(11*R + 24) + 6
assert sp.cancel(m2[-1] - 2*U/(R*V)) == 0
assert sp.cancel(m4[-1] - 24*W*H/(R**2*V*J)) == 0
K = sp.factor(6*W*V*H/(U**2*J)-3)
assert sp.cancel(K-(m4[-1]/m2[-1]**2-3)) == 0
print('PASS: exact stationary 2nd/4th moments and normalized excess kurtosis')

# The sign of the resetting-rate derivative is a seventh-degree polynomial P.
P = sp.cancel(sp.diff(K, R) * U**3 * J**2 / (6*G**2))
assert sp.denom(P) == 1
p = sp.Poly(sp.expand(P), R)
assert p.degree() == 7
Q0=22*G**4+25*G**3-15*G-6
Q1=60*G**3+55*G**2-5*G-16
Q2=906*G**4+1856*G**3+1134*G**2+105*G-61
expect=[
 6*(G+1)**2*(2*G+1)*Q0,
 6*G*(G+1)**2*(2*G+1)*Q1,
 G**2*(G+1)*Q2,
 G**3*(682*G**4+1744*G**3+1542*G**2+523*G+49),
 G**4*(324*G**3+647*G**2+415*G+86),
 G**5*(94*G**2+131*G+46),
 G**6*(15*G+11),
 G**7,
]
assert all(sp.expand(p.nth(i)-expect[i])==0 for i in range(8))
print('PASS: all eight resetting-derivative coefficient identities')

# Each Q has precisely one positive root by Descartes' rule. Exact rational
# intervals establish the order: root(Q2) < root(Q1) < root(Q0).
def signseq(f):
    return [sp.sign(c) for c in sp.Poly(f,G).all_coeffs() if c != 0]
for poly in [Q2,Q1,Q0]:
    signs=signseq(poly)
    assert sum(a!=b for a,b in zip(signs,signs[1:]))==1
for poly,a,b in [
    (Q2,sp.Rational(1,10),sp.Rational(1,5)),
    (Q1,sp.Rational(2,5),sp.Rational(1,2)),
    (Q0,sp.Rational(7,10),sp.Rational(3,4)),
]:
    assert poly.subs(G,a)<0 and poly.subs(G,b)>0
# The constant is negative below Q0's root; the higher coefficients switch
# sign at smaller positive G (or are always positive), so there is exactly one
# sign change in P's coefficient sequence for all 0<G<gamma_c.
assert all(all(c > 0 for c in sp.Poly(sp.expand(v),G).all_coeffs() if c != 0) for v in expect[3:])
print('PASS: Descartes root signs, strict root order and uniqueness certificate')

# For fixed r, derivative in bath-friction ratio g is strictly negative:
# its factored numerator has *only positive integer coefficients*.
S = sp.cancel(-sp.diff(K,G) * U**3 * J**2 / (6*G))
assert sp.denom(S)==1
monomials = sp.Poly(sp.expand(S), G, R).terms()
assert len(monomials)>30 and all(c>0 for (_,c) in monomials)
print('PASS: exact all-positive coefficient certificate for -d(kurtosis)/dg')

# Boundaries and asymptotic optimizer scale.
assert sp.factor(sp.limit(K,R,0) - 3*(2*G+1)/(2*G**2+2*G+1))==0
assert sp.limit(K,R,sp.oo)==3
assert sp.limit(K,G,0)==3
kinf=3*R*(R**3+7*R**2+15*R+11)/((R+1)**2*(R+3)*(R+4))
assert sp.factor(sp.limit(K,G,sp.oo)-kinf)==0
assert sp.factor(sp.together(3-kinf)).as_numer_denom()[0].subs(R,1)>0
assert sp.factor(sp.limit(G*sp.diff(K,R),G,0))==0
zpoly=sp.factor(sp.limit(P.subs(R,Z/G),G,0))
assert sp.expand(zpoly-(Z-1)*(Z+1)**2*(Z+2)**2*(Z+3)**2)==0
expanded=sp.Poly(sp.expand(P.subs(R,Z/G)), G)
z0=expanded.nth(0)
z1=expanded.nth(1)
assert sp.cancel(-z1.subs(Z,1)/sp.diff(z0,Z).subs(Z,1)+sp.Rational(5,6))==0
print('PASS: limiting kurtosis, simple small-memory optimizer root and -5/6 correction')

# Independently solve the monomial-generator linear equations at exact rational
# parameters, without substituting into the symbolic rational simplification.
for gamma in [sp.Rational(1,20),sp.Rational(1,3),sp.Rational(1,1),sp.Rational(2,1),sp.Rational(13,1)]:
    for rate in [sp.Rational(1,10),sp.Rational(1,1),sp.Rational(5,1),sp.Rational(25,1)]:
        mat2 = sp.zeros(3)
        vec2 = sp.zeros(3,1)
        for i in range(3):
            j=2-i
            mat2[i,i]=i+j/gamma+(rate if i else 0)
            if i:mat2[i,i-1]=-i
            if j:mat2[i,i+1]=-sp.Rational(j,1)/gamma
            if i==2:vec2[i]+=2
            if j==2:vec2[i]+=sp.Rational(2,1)/gamma
        a2=mat2.LUsolve(vec2)
        assert a2[-1]==(2*U/(R*V)).subs({G:gamma,R:rate})
        mat4=sp.zeros(5); vec4=sp.zeros(5,1)
        for i in range(5):
            j=4-i
            mat4[i,i]=i+j/gamma+(rate if i else 0)
            if i:mat4[i,i-1]=-i
            if j:mat4[i,i+1]=-sp.Rational(j,1)/gamma
            if i>=2:vec4[i]+=i*(i-1)*a2[i-2]
            if j>=2:vec4[i]+=sp.Rational(j*(j-1),1)/gamma*a2[i]
        a4=mat4.LUsolve(vec4)
        assert a4[-1]==(24*W*H/(R**2*V*J)).subs({G:gamma,R:rate})
print('PASS: 40 independent exact-rational fixed-parameter linear systems')
print('ALL CHECKS PASS')
