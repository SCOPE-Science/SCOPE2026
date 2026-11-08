"""Reproduce stationary radial-energy moment and sign calculations.

Requires sympy; executes independently from the report text.
"""
import sympy as sp

a, d, h = sp.symbols('a d h', positive=True)

def moments_by_generator(dim, rate, order=3):
    """Polynomial generator of (Y=|X|^2,Z=X dot N), with spherical refresh."""
    m = {(0, 0): sp.Integer(1)}
    for n in range(1, order + 1):
        for p in range(n+1):
            q = n-p
            if q == 0:
                ans = m[p-1, 1]
            else:
                num = (2*p*m[p-1, q+1] if p else sp.Integer(0)) + q*m[p, q-1]
                if q % 2 == 0:
                    k = q//2
                    sphere_moment = sp.prod(2*j-1 for j in range(1,k+1))/sp.prod(dim+2*j-2 for j in range(1,k+1))
                    num += rate*sphere_moment*m[p+k, 0]
                ans = num/(2*p+q+rate)
            m[p, q] = sp.cancel(ans)
    return [sp.factor(m[k,0]) for k in range(1,order+1)]

m1, m2, m3 = moments_by_generator(d,a)
expected_m1 = 1/(a+1)
expected_m2 = (a*d+2*a+6*d)/(d*(a+1)*(a+2)*(a+3))
expected_m3 = (a*a*d*d+6*a*a*d+8*a*a+18*a*d*d+72*a*d+120*d*d)/(d*d*(a+1)*(a+2)*(a+3)*(a+4)*(a+5))
for actual, expected in zip([m1,m2,m3],[expected_m1,expected_m2,expected_m3]):
    assert sp.cancel(actual-expected) == 0
variance = sp.factor(m2-m1**2)
third = sp.factor(m3-3*m2*m1+2*m1**3)
P = a**3+(3*d+2)*a**2+(4*d*d-3*d+1)*a-2*d*(d+3)
assert sp.cancel(variance-2*a*(a+d+1)/(d*(a+1)**2*(a+2)*(a+3))) == 0
assert sp.cancel(third-8*a*P/(d*d*(a+1)**3*(a+2)*(a+3)*(a+4)*(a+5))) == 0
assert sp.cancel(P.subs(a,1) - 2*(d-1)*(d-2)) == 0
assert sp.cancel(P.subs(a,sp.Rational(1,2)) + 9*(6*d-1)/8) == 0
assert sp.cancel(P.subs(d,1)-(a-1)*(a+2)*(a+4))==0
assert sp.cancel(P.subs(d,2)-(a-1)*(a+4)*(a+5))==0

# An independent coordinate-moment check using the cited renewal recurrence.
# Coordinates have moments E[U^(2k)] = Gamma(d/2) Gamma(k+1/2)/(sqrt(pi) Gamma(d/2+k)).
def coordinate_moments(dim, rate):
    m={0:sp.Integer(1)}
    cm=lambda k: sp.prod(2*j-1 for j in range(1,k+1))/sp.prod(dim+2*j-2 for j in range(1,k+1))
    for n in range(1,4):
        # From stationary dynamics: E[X^n U^m], n+m=2k.
        # A_lm = [l A_(l-1,m+1) + rate E[X^l] E[U^m]]/(l+rate).
        total=2*n
        z={0:cm(n)}
        for l in range(1,total):
            q=total-l
            z[l]=sp.cancel((l*z[l-1] + rate*(m[l//2] if l%2==0 else 0)*(cm(q//2) if q%2==0 else 0))/(l+rate))
        m[n]=sp.factor(z[total-1])
    return m

for D in [1,2,3,4,7,11]:
    for A in [sp.Rational(1,10),sp.Rational(1,2),sp.Rational(1),sp.Rational(7,3),sp.Rational(10)]:
        y=moments_by_generator(sp.Integer(D),A)
        cm=coordinate_moments(sp.Integer(D),A)
        # Rotation-invariant radius: E[R^(2n)] = E[X_1^(2n)]/E[U_1^(2n)].
        for n in [1,2,3]:
            angular=sp.Rational(sp.prod(2*j-1 for j in range(1,n+1)),sp.prod(D+2*j-2 for j in range(1,n+1)))
            assert sp.cancel(y[n-1]-cm[n]/angular)==0, (D,A,n)

# Independent special cases: Y is beta(1/2, a/2) in dimension 1,
# and beta(1,a) in dimension 2 (pure active, no thermal diffusion).
for D, b1, b2 in [(1,sp.Rational(1,2),a/2),(2,sp.Integer(1),a)]:
    mm=moments_by_generator(sp.Integer(D),a)
    for n in range(1,4):
        beta_m=sp.rf(b1,n)/sp.rf(b1+b2,n)
        assert sp.cancel(mm[n-1]-beta_m)==0

# Gaussian noncentral chi-square conditional cumulants, then total cumulance.
var3=variance.subs(d,3)
third3=third.subs(d,3)
thermal=sp.factor(third3+12*h*var3+24*h*h*m1+24*h**3)
Tpoly=sp.Poly(sp.factor(thermal.as_numer_denom()[0]/8),a)
assert sp.factor(thermal.subs(h,0)-third3)==0
assert sp.factor(thermal.subs(a,0)-(24*h*h+24*h**3))==0
assert sp.factor(sp.limit(thermal,a,sp.oo)-24*h**3)==0
assert sp.factor(sp.diff(thermal,h)-(12*var3+48*h*m1+72*h*h))==0

# Exact coefficient pattern: for h>0, all terms degree >=2 and the constant
# have positive coefficients. Only the linear coefficient can be negative.
for k in [0,2,3,4,5,6,7]:
    coeff=sp.Poly(Tpoly.nth(k),h)
    assert all(c>=0 for c in coeff.all_coeffs()) and coeff!=sp.Poly(0,h)

from sympy import nsolve
root0 = float(nsolve(P.subs(d,3),sp.Rational(9,10)))
astar,hstar = nsolve([thermal,sp.diff(thermal,a)], [a,h], [sp.Rational(14,100),sp.Rational(2,100)], prec=45)
assert abs(float(astar)-0.1398274820400415)<1e-12
assert abs(float(hstar)-0.01962977632357583)<1e-12
assert float(root0) > float(astar)
for A,H in [(sp.Rational(1,10),sp.Rational(1,1000)),(sp.Rational(1,2),sp.Rational(1,100)),(sp.Rational(1),sp.Rational(1,100)),(sp.Rational(2),sp.Rational(1,20))]:
    val=thermal.subs({a:A,h:H})
    assert sp.denom(sp.cancel(val))>0
print('PASS exact generator/coordinate moments for 30 (dimension,rate) pairs x 3 orders; symbolic radial and thermal identities; spherical beta limits; coefficient signs; threshold values')
print('a_c(3)=',root0,'(a_star,h_star)=',astar,hstar)
