import sympy as sp

u = sp.symbols('u')
F = (1+u)*sp.exp(-2*u)-1
Fser = sp.series(F, u, 0, 10).removeO().expand()
G = sp.series(F.subs(u, F), u, 0, 10).removeO().expand()
Wjump1 = sp.series(1/F**2 - 1/u**2, u, 0, 4)
Wjump2 = sp.series(1/G**2 - 1/u**2, u, 0, 4)

print('F(u) =', Fser)
print('F(F(u)) =', G)
print('one-step reciprocal-square jump =', Wjump1)
print('two-step reciprocal-square jump =', Wjump2)

assert sp.expand(Fser).coeff(u,1) == -1
assert sp.expand(Fser).coeff(u,3) == sp.Rational(2,3)
assert sp.expand(G).coeff(u,3) == -sp.Rational(4,3)
assert sp.expand(G).coeff(u,5) == sp.Rational(8,15)
assert sp.limit(1/F**2 - 1/u**2, u, 0) == sp.Rational(4,3)
assert sp.limit(1/G**2 - 1/u**2, u, 0) == sp.Rational(8,3)

# For G(u)=u-a u^3+b u^5+..., the 1/W coefficient in the
# reciprocal-square increment is 3 a^2 - 2 b.
a = sp.Rational(4,3)
b = sp.Rational(8,15)
c = sp.simplify(3*a*a - 2*b)
log_coeff_even = sp.simplify(c/(2*a))
print('3 a^2 - 2 b =', c)
print('log coefficient after summation =', log_coeff_even)
assert c == sp.Rational(64,15)
assert log_coeff_even == sp.Rational(8,5)
print('VERIFIED')
