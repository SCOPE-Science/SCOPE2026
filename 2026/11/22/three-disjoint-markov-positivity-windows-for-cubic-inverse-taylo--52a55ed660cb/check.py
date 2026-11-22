"""Exact [0/3] Pade Markov pure-birth positivity certificate.

Run: python check.py (requires SymPy >= 1.12).
All sign and Sturm decisions use exact rational arithmetic.
"""
import sympy as sp

x = sp.symbols('x')
E = x**3 + 3*x**2 + 6*x + 6
A = E / 6
B = -(x + x**2 + x**3/2)
C = x**2/2 + x**3/2
D = -x**3/6
c = []
for j in range(7):
    v = (sp.Integer(j == 0) - (B*c[j-1] if j >= 1 else 0)
          - (C*c[j-2] if j >= 2 else 0)
          - (D*c[j-3] if j >= 3 else 0)) / A
    c.append(sp.cancel(v))

P = 7*x**10+70*x**9+315*x**8+756*x**7+945*x**6+270*x**5-810*x**4-1080*x**3-324*x**2+216*x+216
U = x**10+15*x**9+120*x**8+450*x**7+855*x**6+495*x**5-810*x**4-1620*x**3-540*x**2+540*x+648
V = x**12+18*x**11+171*x**10+780*x**9+1755*x**8+810*x**7-5103*x**6-12960*x**5-12150*x**4-1080*x**3+8748*x**2+7776*x+3240

assert sp.factor(c[5] - 18*x**5*P/E**6) == 0
T = [sp.factor(1 - sum(c[:j],sp.Integer(0))) for j in range(1,7)]
assert sp.factor(T[4] - x**5*U/E**5) == 0
assert sp.factor(T[5] - x**6*V/E**6) == 0

for label, f in [('c0',c[0]),('c1',c[1]),('c2',c[2]),('c3',c[3]),('c4',c[4])]+[(f'T{k+1}',T[k]) for k in range(4)]:
    num, den = sp.fraction(sp.factor(f))
    assert all(a >= 0 for a in sp.Poly(num,x).all_coeffs()), label
    assert any(a > 0 for a in sp.Poly(num,x).all_coeffs()), label
    assert all(a >= 0 for a in sp.Poly(den,x).all_coeffs()), label

# Sturm sign variation with zero omitted, at zero and +infinity.
def variations(signs):
    u = [sp.sign(z) for z in signs if z != 0]
    return sum(u[j] != u[j+1] for j in range(len(u)-1))
def sturm_counts(poly):
    seq = sp.sturm(poly,x)
    v0 = variations([z.subs(x,0) for z in seq])
    vi = variations([sp.LC(sp.Poly(z,x)) for z in seq])
    return v0,vi
assert sturm_counts(P) == (5,3), sturm_counts(P)
assert sturm_counts(U) == (5,5), sturm_counts(U)
assert sturm_counts(V) == (7,5), sturm_counts(V)

# Exact, disjoint endpoint brackets; two positive roots for P,V.
brackets = [
    ('P1',P,sp.Rational(584462453,10**9),sp.Rational(584462454,10**9)),
    ('P2',P,sp.Rational(894300136,10**9),sp.Rational(894300137,10**9)),
    ('V1',V,sp.Rational(895263696,10**9),sp.Rational(895263697,10**9)),
    ('V2',V,sp.Rational(1840916903,10**9),sp.Rational(1840916904,10**9)),
]
for name, f, lo, hi in brackets:
    assert f.subs(x,lo)*f.subs(x,hi)<0, name
assert brackets[0][3] < brackets[1][2] < brackets[2][2] < brackets[3][2]

# Independently build exact inverse of 7-state Markov generator at rational timesteps.
n = 7
Q = sp.zeros(n)
for i in range(n-1):
    Q[i,i] = -1
    Q[i+1,i] = 1
assert all(sum(Q[:,j]) == 0 for j in range(n))
for z in [sp.Rational(1,2),sp.Rational(3,4),sp.Rational(89,100),sp.Rational(895,1000),sp.Integer(1),sp.Integer(2)]:
    G = sp.eye(n) - z*Q + (z*Q)**2/2 - (z*Q)**3/6
    R = G.inv()
    assert R == G.inv()
    assert all(sum(R[:,j]) == 1 for j in range(n))
    for j in range(n-1):
        for k in range(n-1-j):
            assert R[j+k,j] == c[k].subs(x,z), (j,k,z)
        assert R[n-1,j] == T[n-1-j-1].subs(x,z), (j,z)
    assert R[:,n-1] == sp.eye(n)[:,n-1]

# Explicit safe/unsafe samples; one tiny positive middle interval.
def all_nonneg(z):
    return all(v.subs(x,z)>=0 for v in c[:6] + T)
for z, expected in [(0,True),(sp.Rational(1,2),True),(sp.Rational(3,4),False),
                    (sp.Rational(8948,10000),True),(sp.Integer(1),False),(sp.Integer(2),True)]:
    assert all_nonneg(sp.Rational(z))==expected,(z,expected)
print('VERIFICATION_OK: exact recurrence, 9 positive coefficient factors, Sturm counts, rational root brackets, 6 inverse matrices')
