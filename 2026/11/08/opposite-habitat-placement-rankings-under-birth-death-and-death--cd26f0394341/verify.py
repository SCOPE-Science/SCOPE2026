"""Exact finite-state checks for site-heterogeneous Moran fixation on a 3-path.

Requires Python 3 and SymPy. Run with `python3 verify.py`.
"""
import sympy as sp
from fractions import Fraction

r, s = sp.symbols('r s', positive=True)
NEIGHBORS = ((1,), (0, 2), (1,))
TRANSIENT = tuple(range(1, 7))


def symbolic_fixation(fitness, rule):
    """Solve all six nonabsorbing first-step equations with exact arithmetic."""
    a = sp.zeros(6, 6)
    b = sp.zeros(6, 1)
    for row, bits in enumerate(TRANSIENT):
        f = [fitness[j] if bits & (1 << j) else sp.Integer(1)
             for j in range(3)]
        if rule == 'Bd':
            w = sum(f)
            steps = [(i, j, f[i] / (w * len(NEIGHBORS[i])))
                     for i in range(3) for j in NEIGHBORS[i]]
        elif rule == 'dB':
            steps = [(i, j, f[i] / (3 * sum(f[k] for k in NEIGHBORS[j])))
                     for j in range(3) for i in NEIGHBORS[j]]
        else:
            raise ValueError(rule)
        for i, j, probability in steps:
            nxt = bits | (1 << j) if bits & (1 << i) else bits & ~(1 << j)
            if nxt == bits:
                continue
            a[row, row] += probability
            if nxt == 7:
                b[row] += probability
            elif nxt:
                a[row, TRANSIENT.index(nxt)] -= probability
    values = a.inv() * b
    # Check all six first-step recurrences, not only the mean.
    assert all(sp.cancel(v) == 0 for v in a * values - b)
    return sp.factor(sum(values[TRANSIENT.index(1 << j)] for j in range(3)) / 3)


def verify_symbolically():
    bd_leaf = symbolic_fixation((r, s, s), 'Bd')
    bd_hub = symbolic_fixation((s, r, s), 'Bd')
    db_leaf = symbolic_fixation((r, s, s), 'dB')
    db_hub = symbolic_fixation((s, r, s), 'dB')

    expected_bd_leaf = s * (12*r*s**3 + 20*r*s**2 + 10*r*s + 8*r + 4*s**3 + 11*s**2 + 10*s) / (3*(s+2)*(2*s**2+s+2)*(2*r*s+s+2))
    expected_bd_hub = r * (6*r*s+r+8*s) / (3*(r+2)*(2*r*s+r+2))
    expected_db_leaf = (5*r*s+3*r+3*s+1) / (9*(r+1)*(s+1))
    expected_db_hub = (5*s+1) / (9*(s+1))
    for actual, expected in [(bd_leaf, expected_bd_leaf), (bd_hub, expected_bd_hub),
                             (db_leaf, expected_db_leaf), (db_hub, expected_db_hub)]:
        assert sp.cancel(actual - expected) == 0
    poly = (6*r**2*s**4 + 9*r**2*s**3 + 15*r**2*s**2 + 18*r*s**3
            + 34*r*s**2 + 14*r*s + 4*r + 8*s**3 + 22*s**2 + 20*s)
    d = 3*(r+2)*(s+2)*(2*s**2+s+2)*(2*r*s+r+2)*(2*r*s+s+2)
    assert sp.cancel(bd_hub - bd_leaf - 2*(r-s)*poly/d) == 0
    assert sp.cancel(db_hub - db_leaf + 2*(r-s)/(9*(r+1)*(s+1))) == 0
    assert all(coef > 0 for coef in sp.Poly(poly, r, s).coeffs())
    return (bd_leaf, bd_hub, db_leaf, db_hub)


def fraction_chain(fitness, rule):
    """Independent Fraction elimination; no symbolic solver is used here."""
    n = 6
    m = [[Fraction(0) for _ in range(n+1)] for _ in range(n)]
    for row, bits in enumerate(TRANSIENT):
        f = [fitness[j] if bits & (1 << j) else Fraction(1) for j in range(3)]
        if rule == 'Bd':
            w = sum(f)
            steps = [(i, j, f[i]/w/len(NEIGHBORS[i]))
                     for i in range(3) for j in NEIGHBORS[i]]
        else:
            steps = [(i, j, f[i]/sum(f[k] for k in NEIGHBORS[j])/3)
                     for j in range(3) for i in NEIGHBORS[j]]
        for i,j,p in steps:
            nxt = bits | (1 << j) if bits & (1 << i) else bits & ~(1 << j)
            if nxt == bits: continue
            m[row][row] += p
            if nxt == 7: m[row][-1] += p
            elif nxt: m[row][TRANSIENT.index(nxt)] -= p
    for col in range(n):
        pivot = next(i for i in range(col, n) if m[i][col])
        m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [v/p for v in m[col]]
        for row in range(n):
            if row == col: continue
            p = m[row][col]
            m[row] = [a-p*b for a,b in zip(m[row],m[col])]
    return sum(m[j][-1] for j in (0, 1, 3))/3


def main():
    expected = verify_symbolically()
    count = 0
    for rv in (Fraction(1,5), Fraction(1,2), Fraction(1), Fraction(2), Fraction(5), Fraction(12)):
        for sv in (Fraction(1,4), Fraction(1), Fraction(3), Fraction(7)):
            samples = ((rv,sv,sv,'Bd'),(sv,rv,sv,'Bd'),
                       (rv,sv,sv,'dB'),(sv,rv,sv,'dB'))
            for j,(a,b,c,rule) in enumerate(samples):
                actual = fraction_chain((a,b,c),rule)
                symbolic = Fraction(expected[j].subs({r:sp.Rational(rv.numerator,rv.denominator),
                                                       s:sp.Rational(sv.numerator,sv.denominator)}))
                assert actual == symbolic, (rv,sv,rule,j,actual,symbolic)
                count += 1
    print('PASS: symbolic six-state identities, four closed forms, two sign factorizations, and',
          count, 'independent exact-Fraction comparisons.')


if __name__ == '__main__':
    main()
