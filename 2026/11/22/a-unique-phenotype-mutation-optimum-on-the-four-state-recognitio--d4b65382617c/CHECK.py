"""Exact symbolic identities for the four-state recognition-cycle optimum.

Run: python CHECK.py   (requires SymPy)
The mathematical proof that the derivative numerator has a unique positive
root uses Descartes' rule of signs and the coefficient inequalities in RESULT.md.
"""
import sympy as sp

nu, q = sp.symbols('nu q', positive=True)

# Discrete Fourier transform of (1,q,q*q,q) on the four-cycle:
weights = [(1 + q)**2, 1-q*q, (1-q)**2, 1-q*q]
assert all(sp.simplify(a-b)==0 for a,b in zip(weights,[(1+q)**2, 1-q*q, (1-q)**2, 1-q*q]))
# An independent four-point discrete Fourier transform from the recognition kernel.
kernel = [sp.Integer(1), q, q**2, q]
transform = [sp.expand(sum(kernel[j]*sp.I**(-p*j) for j in range(4))) for p in range(4)]
assert all(sp.simplify(a-b)==0 for a,b in zip(transform,weights))

def F(s):
    return weights[0] / sp.Integer(s) + (weights[1] + weights[3])/(s+2*nu) + weights[2]/(s+4*nu)

N = 9*F(1)-6*F(3)+5*F(5)
D = -3*F(1)+6*F(3)+5*F(5)
B = sp.cancel(N/D)
U = (48*q*nu**4 + 184*q*nu**3 + 216*q*nu**2 + 77*q*nu
     + 80*nu**4 + 360*nu**3 + 544*nu**2 + 321*nu + 60)
T = sp.prod((a*nu+s) for a in (2,4) for s in (1,3,5))
assert sp.cancel(D - 64*nu*(1-q)*U/T) == 0
coefficients = [
  -13500,
  -450*(77*q+321),
  -30*(240*q*q+9213*q+21245),
  -480*(45*q*q+1720*q+3056),
  4*(3015*q**3+22891*q*q-266653*q-461921),
  32*(2381*q**3+16861*q*q-6565*q-35073),
  32*(5751*q**3+33709*q*q+33821*q+535),
  128*(1739*q**3+8677*q*q+11087*q+3873),
  256*(561*q**3+2459*q*q+3181*q+1271),
  2048*(q+1)**2*(23*q+45),
  2048*(q+1)**2*(3*q+5),
]
H = sp.Add(*(coefficients[j]*nu**j for j in range(11)))
assert sp.cancel(sp.diff(B,nu)-H/(2*nu**2*(1-q)*U**2)) == 0
# Two-sided exact signs of the coefficients for every q in (0,1)
assert 2381+16861-35073 < 0
assert 3015+22891-461921 < 0
assert all(sp.simplify(sp.sympify(x).subs(q, sp.Rational(1,2))) < 0 for x in coefficients[:6])
assert all(sp.simplify(sp.sympify(x).subs(q, sp.Rational(1,2))) > 0 for x in coefficients[6:])
# Representative exact-rational check, with a reproducible isolate for the root.
p = sp.Poly(H.subs(q, sp.Rational(1,2)),nu)
a, b = sp.Rational(1168,1000), sp.Rational(1170,1000)
assert p.eval(a) < 0 < p.eval(b)
root = sp.nsolve(p.as_expr(), 1.17)
assert abs(float(root)-1.168773523305237) < 1e-11
assert abs(float(B.subs({q:sp.Rational(1,2),nu:root}))-13.984680815057002) < 1e-9
print('PASS: exact spectral transform, positive denominator, degree-10 derivative, coefficient sign envelope, root interval and threshold.')
