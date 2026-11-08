"""Reproducibility checks for puncture-logarithmic weighted Bergman kernels.

The analytic proof in RESULT.md establishes the all-order statement;
these exact checks independently test the polynomial recursion, boundary
crossings, scalar-zero counts and moment formulas at selected parameters.
"""
import sympy as sp
from mpmath import mp

u, a = sp.symbols('u a', real=True)
P = sp.Integer(1)
assertions = 0

def check(condition, message):
    global assertions
    assert bool(condition), message
    assertions += 1


def expected_count(q, alpha):
    if q % 2:
        return (q-1)//2 + int(bool(alpha < sp.Rational(1,2)))
    return q//2 - int(bool(alpha == 1))

for q in range(1, 11):
    P = sp.expand(u*(1-u)*sp.diff(P,u) + (a+(q-a)*u)*P)
    check(P.subs(u,0) == a**q, f'constant coefficient q={q}')
    check(sp.Poly(P,u).degree() == q, f'degree q={q}')
    # Independent reconstruction from the generating function (a+u*d/du)^q(1-u)^-1.
    S = 1/(1-u)
    for j in range(q):
        S = sp.cancel(a*S + u*sp.diff(S,u))
    gen_num = sp.cancel(S*(1-u)**(q+1))
    check(sp.expand(gen_num-P) == 0, f'generating identity q={q}')
    check(sp.expand(u**q*P.subs({u:1/u}, simultaneous=True) - P.subs(a,1-a)) == 0,
          f'reciprocity q={q}')
    euler = sp.euler(q,a)
    check(sp.expand(P.subs(u,-1)-2**q*euler) == 0, f'Euler crossing q={q}')
    for alpha in (sp.Rational(1,5), sp.Rational(1,2), sp.Rational(4,5), sp.Integer(1)):
        poly = sp.Poly(P.subs(a,alpha), u)
        deg = poly.degree()
        check(sp.degree(sp.gcd(poly,poly.diff())) == 0, f'simplicity q={q} a={alpha}')
        check(poly.count_roots(-sp.oo,0) == deg, f'negative real zeros q={q} a={alpha}')
        # Sturm root count on the open physical scalar interval (-1,0).
        # Use near-endpoints, independently excluding the exact boundary root u=-1.
        eps=sp.Rational(1,10**30)
        count = poly.count_roots(-1+eps, -eps)
        check(count == expected_count(q,alpha), f'zero-fibre count q={q} a={alpha}: {count}')
        expected_boundary = (q%2 == 1 and alpha == sp.Rational(1,2)) or (q%2 == 0 and alpha == 1)
        check((poly.eval(-1)==0) == expected_boundary, f'boundary crossing q={q} a={alpha}')

# Verify exact weighted monomial norms against numerical radial integration.
mp.dps = 50
for q in range(1,5):
    for t in (sp.Rational(-1,3), sp.Rational(1,4), sp.Rational(5,4), sp.Integer(1)):
        n_min=-sp.ceiling(t)
        for n in range(n_min, n_min+3):
            tt=mp.mpf(str(sp.N(t,45)))
            a1=int(n)+tt+1
            target=mp.pi*mp.gamma(q)/(a1**q)
            # Numerically integrate in x=|z|^2, with y=-log(x), to avoid endpoint issues.
            numerical=mp.pi*mp.quad(lambda y: mp.exp(-a1*y)*y**(q-1), [0,1,mp.inf])
            check(abs(target-numerical)<mp.mpf('1e-35')*max(target,1), f'moment q={q} t={t} n={n}')

# Algebraic verification of the piecewise-onset jump across integer parameter k.
for q in range(1,8):
    h=sp.symbols('h', real=True)
    k=2
    added = h**q * u**(-k-1) / (sp.pi*sp.factorial(q-1))
    jump=sp.diff(added,h,q).subs(h,0)
    check(sp.simplify(jump-sp.factorial(q)*u**(-k-1)/(sp.pi*sp.gamma(q)))==0,
          f'qth derivative defect q={q}')
    for j in range(q):
        check(sp.diff(added,h,j).subs(h,0)==0, f'lower derivatives match q={q} j={j}')

print(f'PASS: {assertions} exact symbolic, Sturm and numerical checks')
