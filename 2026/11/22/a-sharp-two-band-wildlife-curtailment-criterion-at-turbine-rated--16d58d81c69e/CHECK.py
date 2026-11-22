"""Reproduce the exact-example inequalities and numerical integrals.

Only Python standard library required. The general theorem is proved in RESULT.md;
finite numerical testing here is supplementary, not an infinite proof.
"""
import math


def bisect(fn, lo, hi, n=100):
    flo, fhi = fn(lo), fn(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(n):
        md = (lo + hi) / 2
        fm = fn(md)
        if fm == 0:
            return md
        if flo * fm < 0:
            hi, fhi = md, fm
        else:
            lo, flo = md, fm
    return (lo + hi) / 2


def power(v):
    return min(v ** 3, 8.0)


def hazard(v):
    return v ** 4 * math.exp(-v)


def ratio(v):
    return hazard(v) / power(v) if v > 0 else 0.0


def cumulative_energy(v):
    if v <= 2:
        return 6 - math.exp(-v) * (v**3 + 3*v**2 + 6*v + 6)
    return 6 - 38*math.exp(-2) + 8*(math.exp(-2) - math.exp(-v))


def cumulative_hazard(v):
    y = 2*v
    return 0.75 * (1 - math.exp(-y) * sum(y**j / math.factorial(j) for j in range(5)))


def hazard_tail(v):
    y = 2*v
    return 0.75 * math.exp(-y)*sum(y**j / math.factorial(j) for j in range(5))


assert (8/3) < math.e < 3
assert 2*math.exp(-2) < 0.3 < math.exp(-1) < 32*math.exp(-4)
roots = [bisect(lambda z: ratio(z) - .3, a, b)
         for a,b in ((.01,1),(1,2),(2,4),(4,12))]
a,b,c,d = roots
assert 0 < a < 1 < b < 2 < c < 4 < d
for i in range(20001):
    v = i/1000
    expected = (v < a or b < v < c or v > d)
    actual = ratio(v) < .3
    assert expected == actual or min(abs(v-r) for r in roots) < 1e-8
E0 = 6 - 30*math.exp(-2)
R0 = .75
E = cumulative_energy(a) + cumulative_energy(c)-cumulative_energy(b) + E0-cumulative_energy(d)
R = cumulative_hazard(a) + cumulative_hazard(c)-cumulative_hazard(b) + hazard_tail(d)
h = bisect(lambda z: hazard_tail(z)-R,2,6)
Ecut = E0-cumulative_energy(h)
assert R>0 and R<R0
assert E>Ecut and E-Ecut>.16
assert abs(E - .35308503008804165)<1e-9
assert abs(R - .09967373841468531)<1e-9
assert abs(Ecut-.1892213112860873)<1e-9
print('roots: '+', '.join(f'{x:.12f}' for x in roots))
print('optimal risk %.12f, energy %.12f' % (R,E))
print('cut-in root %.12f, cut-in energy %.12f' % (h,Ecut))
print('additional energy %.12f (%.4f%% vs cut-in)' % (E-Ecut, 100*(E/Ecut-1)))
print('All 20001 grid topology comparisons and analytic integral checks passed.')
