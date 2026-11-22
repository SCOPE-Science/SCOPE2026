"""Exact arithmetic sanity checks for the replication-clock timing identifiability theorem.

Requires Python 3.10+ and SymPy. Finite checks corroborate, but do not replace,
the uniform pole-order and positivity proofs in RESULT.md.
"""
from sympy import Matrix, Poly, Rational, binomial, cancel, factor, fraction, limit, oo, simplify, symbols

s = symbols('s')

def laplace(lam, stages, k, alpha, amp):
    """Independent conditional-event decomposition from a Markov chain."""
    A, B = s + k + alpha, s + amp*k
    before = sum(binomial(lam+j-1, j)*k**lam*alpha**j/A**(lam+j)
                 for j in range(stages))
    after = alpha**stages*(amp*k)**lam/(A**stages*B**lam)*sum(
        binomial(stages+m-1, m)*(B/(amp*A))**m
        for m in range(lam))
    return cancel(before + after)

def rational_pole_multiplicity(expression, root):
    _, den = fraction(cancel(expression))
    p = Poly(den, s)
    count = 0
    while p.eval(root) == 0:
        q, rem = p.div(Poly(s-root, s))
        assert rem.is_zero
        p, count = q, count+1
    return count

def direct_ctmc(lam, stages, k, alpha, amp, laplace_point):
    """Exact resolvent of absorbing finite continuous-time Markov chain."""
    states = [(i, j) for j in range(stages+1) for i in range(lam)]
    index = {st: i for i, st in enumerate(states)}
    n = len(states)
    A = Matrix.zeros(n)
    b = Matrix.zeros(n, 1)
    for idx, (i, j) in enumerate(states):
        birth = k if j < stages else k*amp
        A[idx, idx] = laplace_point+birth+(alpha if j<stages else 0)
        if i+1 < lam:
            A[idx, index[(i+1, j)]] = -birth
        else:
            b[idx, 0] += birth
        if j < stages:
            A[idx, index[(i, j+1)]] = -alpha
    return A.inv()*b, index[(0, 0)]

# Pole orders and small-time production-rate invariants, nonresonant and resonant.
for lam in range(1, 6):
    for stages in range(1, 5):
        for amp in (Rational(3), Rational(4)):
            k, alpha = Rational(1), Rational(2)
            h = laplace(lam, stages, k, alpha, amp)
            assert limit(s**lam*h, s, oo) == k**lam
            r, q = k+alpha, k*amp
            if r == q:
                assert rational_pole_multiplicity(h, -r) == lam+stages
            else:
                assert rational_pole_multiplicity(h, -r) == lam+stages-1
                assert rational_pole_multiplicity(h, -q) == lam

# Nonidentifiable one-protein, one-stage pair and sharp two-protein repair.
h_a = laplace(1, 1, Rational(1), Rational(2), Rational(4))
h_b = laplace(1, 1, Rational(1), Rational(3), Rational(3))
assert simplify(h_a-h_b) == 0
assert simplify(h_a-(s+12)/((s+3)*(s+4))) == 0
assert simplify(laplace(2, 1, Rational(1), Rational(2), Rational(4))-(s*s+48*s+144)/((s+3)**2*(s+4)**2)) == 0
assert simplify(laplace(2, 1, Rational(1), Rational(3), Rational(3))-(s*s+42*s+144)/((s+3)**2*(s+4)**2)) == 0

# Closed difference of the (lambda+1)-st inverse-Laplace asymptotic coefficient.
x, y = symbols('x y')
for lam in range(1, 10):
    left = lam*(x-y)+(y-1)*sum(x**j for j in range(1,lam+1))-(x-1)*sum(y**j for j in range(1,lam+1))
    right = (x-1)*(y-1)*sum((lam-j)*(x**j-y**j) for j in range(1,lam))
    assert simplify(left-right) == 0

for lam, stages, k, alpha, amp, z in [
    (3, 2, Rational(2), Rational(3), Rational(5,2), Rational(7)),
    (2, 1, Rational(1), Rational(2), Rational(4), Rational(5)),
    (1, 3, Rational(2), Rational(2), Rational(2), Rational(5)),
]:
    arr, initial = direct_ctmc(lam, stages, k, alpha, amp, z)
    assert simplify(arr[initial]-laplace(lam, stages, k, alpha, amp).subs(s,z)) == 0

print('PASS: 40 exact pole-order checks; inverse-power coefficients; exchange ambiguity;')
print('PASS: two-protein resolution; 9 symbolic factorization identities; 3 CTMC resolvents.')
