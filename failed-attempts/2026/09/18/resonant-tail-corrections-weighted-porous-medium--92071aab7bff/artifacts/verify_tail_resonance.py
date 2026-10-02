from fractions import Fraction
import sympy as sp

m, p, sigma, N, xi = sp.symbols('m p sigma N xi', positive=True)
D = sigma*(m-1) + 2*(p-1)
alpha = (sigma+2)/D
beta = (m-p)/D
q = sigma/(p-1)
r = 2 + (m-1)*q
h = 1/beta
s = m*q

checks = {
    'leading_balance': sp.simplify(alpha + beta*q - 1/(p-1)),
    'forced_rate': sp.simplify(r - D/(p-1)),
    'homogeneous_rate': sp.simplify(h - D/(m-p)),
    'denominator_identity': sp.simplify(1-beta*r - (2*p-1-m)/(p-1)),
    'resonance_factor': sp.factor(r-h),
}

g = xi**(-s)
radial = sp.simplify(sp.diff(g, xi, 2) + (N-1)/xi*sp.diff(g, xi))
radial_target = s*(s-N+2)*xi**(-s-2)
checks['radial_laplacian'] = sp.simplify(radial-radial_target)

for name, value in checks.items():
    print(f'{name}: {value}')

print('\nRepresentative rates for p=2, sigma=1, N=1:')
for mv in [sp.Rational(5,2), sp.Integer(3), sp.Integer(4)]:
    vals = {m: mv, p: 2, sigma: 1, N: 1}
    rv = sp.simplify(r.subs(vals))
    hv = sp.simplify(h.subs(vals))
    sv = sp.simplify(s.subs(vals))
    regime = 'forced' if rv < hv else ('resonant' if rv == hv else 'homogeneous')
    print(f'm={mv}: r={rv}, h={hv}, s={sv}, regime={regime}')

# At p=2, m=3, sigma=1, N=1, c_* = 1.
# A0 = c_*^(m-1) s(s-N+2) = 3*4 = 12 and beta=1/4,
# so the resonant relative-error coefficient is A0/beta = 48.
print('resonant_example_log_coefficient:', 48)
