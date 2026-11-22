"""Reproduce exact polynomial certificates for two-time sensing of Brownian quadratic energy.
Run: python verify.py (requires SymPy).
"""
import sympy as S
x, y, u = S.symbols('x y u')
c = 1-x-y
F = S.expand((x-S.Rational(2,3)*x*x)**2 + y*y*(c+y/3)**2
             + 2*x*y*(c+y/2)**2)
Fx,Fy = S.diff(F,x),S.diff(F,y)
R = (303872*x**6+748224*x**5-2700756*x**4+1719468*x**3
     +21627*x**2-139968*x-11664)
A = 4272*x**5-4346*x**4+389*x**3+432*x**2+36*x
Dcoef = 6288*x**4-5774*x**3-54*x**2+432*x+36
witness = S.Rational(457,2916)
assert S.factor(S.resultant(Fx,Fy,y)) == x**3*R/S.Integer(2125764)
sub = S.subresultants(Fx,Fy,y)
assert S.expand(sub[-2]-(A+Dcoef*y)/2916)==0
assert F.subs({x:S.Rational(1,2),y:S.Rational(1,3)})==witness

def bernstein_coefficients(P,lo=0,hi=1,n=None):
    P=S.Poly(S.expand(S.sympify(P).subs(x,lo+(hi-lo)*u)),u)
    n=n or P.degree()
    assert n >= P.degree()
    return [S.factor(sum(P.nth(k)*S.binomial(j,k)/S.binomial(n,k)
              for k in range(j+1))) for j in range(n+1)]

# Certificate: no value at boundary c=0 can exceed a feasible interior witness.
G=S.expand(F.subs(y,1-x))
assert G == (x**4-5*x**3+3*x**2+x+2)/18
cert=bernstein_coefficients(witness-G,n=12)
assert len(cert)==13 and all(t>0 for t in cert)
# On x=0 or y=0 the function is z^2(1-2z/3)^2,
# at most 9/64 for z in [0,1] (differentiate explicitly).
z=S.symbols('z')
edge = z**2*(1-S.Rational(2,3)*z)**2
assert S.factor(S.diff(edge,z)) == S.Rational(2,9)*z*(2*z-3)*(4*z-3)
assert edge.subs(z,S.Rational(3,4)) == S.Rational(9,64)
assert witness>S.Rational(9,64)
# Descartes sign variation = 3; three disjoint strict positive-root brackets prove completeness.
nonzero=[S.sign(v) for v in S.Poly(R,x).all_coeffs() if v]
assert sum(nonzero[i]!=nonzero[i+1] for i in range(len(nonzero)-1)) == 3
brackets = [(S.Rational(518,1000),S.Rational(519,1000)),
            (S.Rational(735,1000),S.Rational(736,1000)),
            (S.Rational(1208,1000),S.Rational(1209,1000))]
for lo,hi in brackets:
    assert R.subs(x,lo)*R.subs(x,hi)<0
# Determine feasibility for stationary y=-A/Dcoef using *whole-interval* exact
# Bernstein coefficient sign enclosures (not mere endpoint testing).
for lo,hi,desired in [(brackets[0][0],brackets[0][1],+1),
                      (brackets[1][0],brackets[1][1],-1)]:
    assert all(q>0 for q in bernstein_coefficients(A,lo,hi))
    assert all(q<0 for q in bernstein_coefficients(Dcoef,lo,hi))
    boundary_gap=-A-(1-x)*Dcoef
    assert all(S.sign(q)==desired for q in bernstein_coefficients(boundary_gap,lo,hi))
# Algebraic sample values + independent covariance integral representation.
M11=x-S.Rational(2,3)*x**2
M22=y*(c+y/3)
M12sq=x*y*(c+y/2)**2
assert S.simplify(F-(M11**2+M22**2+2*M12sq))==0
# One-point and linear-quadrature comparison, all exact.
assert S.Rational(1,3)-2*F.subs({x:S.Rational(2,5),y:S.Rational(2,5)})==S.Rational(131,5625)
assert S.Rational(1,3)-2*F.subs({x:S.Rational(1,2),y:S.Rational(1,3)})==S.Rational(29,1458)
assert S.Rational(1,3)-2*edge.subs(z,S.Rational(3,4))==S.Rational(5,96)
print('PASS: exact symbolic identity, resultant, and stationary subresultant')
print('PASS: 13 strict Bernstein boundary coefficients and 6 interval-sign certificates')
print('PASS: 3 positive-root brackets plus Descartes exhaustiveness')
print('PASS: quadratic-energy covariance and comparison arithmetic')
xx=S.nroots(R,maxsteps=200)
r=[S.re(t) for t in xx if abs(float(S.im(t)))<1e-12 and 0<float(S.re(t))<1]
q=r[0]; gap=-A.subs(x,q)/Dcoef.subs(x,q)
print('interior optimal observations:',S.N(q,14),S.N(q+gap,14))
print('minimum squared Bayes risk:',S.N(S.Rational(1,3)-2*F.subs({x:q,y:gap}),14))
