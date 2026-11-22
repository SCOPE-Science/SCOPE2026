"""Exact symbolic checks for two-round, three-type coupon occupancy stability."""
import itertools
import sympy as S

x, y, z, t = S.symbols('x y z t', real=True)
Z = (2*t+1)**2
f = t*x + t**2*y + t*z + (t**2+t)*x*y + (t**2+1)*x*z + (t**2+t)*y*z
assert S.factor(f.subs({x:1,y:1,z:1})-Z) == 0
pairs = [(x,y,z),(x,z,y),(y,z,x)]
expected = {
 (x,y): t*((t**3+t**2+t+1)*z**2 + (t**3+t)*z + t**2),
 (x,z): t**2*((t+1)**2*y**2 + (-t**2+2*t+1)*y + 1),
 (y,z): t*((t**3+t**2+t+1)*x**2 + (t**3+t)*x + t**2),
}
checks = 0
for a,b,c in pairs:
    delta = S.factor(S.diff(f,a)*S.diff(f,b)-f*S.diff(f,a,b))
    assert S.expand(delta - expected[(a,b)]) == 0
    assert S.factor(S.discriminant(delta,c) - t**4*(t**2+1)*(t**2-4*t-3)) == 0
    checks += 2
assert S.factor((S.diff(f,x)*S.diff(f,z)-f*S.diff(f,x,z)).subs({t:5,y:S.Rational(7,36)}) + S.Rational(325,36)) == 0
checks += 1
# Independent enumeration from the two categorical distributions, not from f.
for theta in (S.Rational(1,9), S.Rational(1,2), S.Integer(1), S.Rational(3,2), S.Rational(9,2), S.Integer(5), S.Integer(7), S.Integer(17)):
    a = [theta, theta, S.Integer(1)]
    b = [S.Integer(1), theta, theta]
    den = (2*theta+1)**2
    val = S.Integer(0)
    for i,j in itertools.product(range(3),repeat=2):
        monom = S.prod((x,y,z)[k] for k in sorted({i,j}))
        val += a[i]*b[j]*monom
    assert S.factor(val - f.subs(t,theta)) == 0
    # Pairwise negative covariance, and 1+Bernoulli occupancy count.
    p = [S.factor(a[i]*(2*theta+1)+b[i]*(2*theta+1)-a[i]*b[i]) for i in range(3)]
    for i,j in itertools.combinations(range(3),2):
        pij = a[i]*b[j]+a[j]*b[i]
        assert S.simplify(pij/den-p[i]*p[j]/den**2) < 0
        checks += 1
    pgf = S.factor(val.subs({x:x,y:x,z:x})/den)
    q = S.factor(sum(a[i]*b[i] for i in range(3))/den)
    assert S.factor(pgf-(q*x+(1-q)*x*x)) == 0
    checks += 2
# At exactly the transition the Rayleigh quadratics become perfect squares.
threshold=2+S.sqrt(7)
for a,b,c in pairs:
    d=S.diff(f,a)*S.diff(f,b)-f*S.diff(f,a,b)
    assert S.simplify(S.discriminant(d,c).subs(t,threshold)) == 0
    checks += 1
print('PASS: {} symbolic/rational independent checks'.format(checks))
print('Sharp transition t=2+sqrt(7) and t=5 witness verified.')
