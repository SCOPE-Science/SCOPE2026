"""Recovery test: VE1 base facts for PII w=-1/t (lane-1584).

Checks:
  (i)   w(t)=-1/t solves PII with alpha=1;
  (ii)  VE1 coefficient q = 6*w**2 + t equals t + 6/t**2;
  (iii) indicial exponents at t=0;
  (iv)  resonance numerators on the r=-2 branch for n=1..8;
  (v)   bounded Riccati search u=P(t)/t with deg P = 1..4.
Requires: sympy.
"""
import sympy as sp

t = sp.Symbol('t')
w = -1 / t

# (i) rational solution check
assert sp.simplify(sp.diff(w, t, 2) - (2 * w**3 + t * w + 1)) == 0
print("PII alpha=1 rational solution w=-1/t: OK")

# (ii) VE1 coefficient
q = 6 * w**2 + t
assert sp.simplify(q - (t + 6 / t**2)) == 0
print("VE1 coefficient q = t + 6/t**2: OK")

# (iii) indicial exponents: r(r-1) = 6
r = sp.Symbol('r')
print("indicial roots:", sp.solve(r * (r - 1) - 6, r))

# (iv) resonance numerators, r0=-2 branch:
# ((n-2)(n-3)-6) a_n = a_{n-3}, a_0=1, a_1=a_2=0
a = {0: sp.Rational(1), 1: sp.Integer(0), 2: sp.Integer(0)}
for n in range(1, 9):
    denom = (n - 2) * (n - 3) - 6
    num = a.get(n - 3, 0)
    print("n=%d denom=%d num=%s resonance=%s" % (n, denom, num, denom == 0))
    if denom != 0:
        a[n] = num / denom
    else:
        # Resonance: numerator is 0 (log-free), so fix the free parameter to 0
        # for this particular solution and continue the recurrence.
        assert num == 0
        a[n] = sp.Integer(0)
print("a3 =", a[3], "(particular, free param at n=5 set to 0)")

# (v) bounded Riccati search u = P(t)/t
for d in [1, 2, 3, 4]:
    coeffs = sp.symbols('a0:%d' % (d + 1))
    P = sum(coeffs[i] * t**i for i in range(d + 1))
    u = P / t
    expr = sp.diff(u, t) + u**2 - (t + 6 / t**2)
    num = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(num, t)
    sol = sp.solve(poly.coeffs(), coeffs, dict=True)
    print("d=%d neqs=%d nsols=%d" % (d, len(poly.coeffs()), len(sol)))

print("RECOVERY DONE")
