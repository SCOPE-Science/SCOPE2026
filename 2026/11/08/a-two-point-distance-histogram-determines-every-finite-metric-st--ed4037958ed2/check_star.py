"""Exact and numerical checks for distance laws on finite metric stars.

Run: python check_star.py
Uses only the Python standard library.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import isclose
from random import Random


def atoms(lengths):
    a = tuple(Q(v) for v in lengths)
    k = len(a)
    if k < 3 or min(a) <= 0:
        raise ValueError('At least three strictly positive arms required')
    out = Counter()
    for v in a:
        out[v] -= k - 2
    for x, y in combinations(a, 2):
        out[x + y] += 1
    return {x: y for x, y in out.items() if y}


def recover(lengths_atoms, k):
    """Recover sorted positive lengths from the signed atomic measure."""
    if k < 3:
        raise ValueError('Requires a branch point of degree >=3')
    residual = Counter(lengths_atoms)
    result = []
    while len(result) < k:
        active = [v for v, c in residual.items() if c]
        if not active:
            raise AssertionError('Nonzero lengths missing')
        b = min(active)
        coeff = residual[b]
        if coeff >= 0 or (-coeff) % (k - 2):
            raise AssertionError(('Wrong leading sign or multiplicity', b, coeff))
        mult = (-coeff) // (k - 2)
        if mult <= 0 or len(result) + mult > k:
            raise AssertionError('Invalid new multiplicity')
        for _ in range(mult):
            for old in result:
                residual[old + b] -= 1
            residual[b] += k - 2
            result.append(b)
    if any(v for v in residual.values()):
        raise AssertionError(('Residual atoms remain', residual))
    return sorted(result)


def density(t, lengths):
    """Exact piecewise linear distance density for rational t and arm lengths."""
    a = tuple(Q(x) for x in lengths)
    t = Q(t)
    L = sum(a)
    pos = lambda v: max(Q(0), v)
    return 2 / (L*L) * (sum(pos(x-t) for x in a)
        + sum(pos(t)-pos(t-x)-pos(t-y)+pos(t-x-y)
              for x,y in combinations(a,2)))


def expected_mean(lengths):
    a = tuple(Q(x) for x in lengths)
    L = sum(a)
    return sum((L*x*x-x*x*x*Q(2,3)) for x in a)/(L*L)


def simulated_mean(lengths, trials=100000, seed=421):
    r = Random(seed)
    a = tuple(float(x) for x in lengths)
    L = sum(a)
    def point():
        s = r.random()*L
        for i, width in enumerate(a):
            if s < width:
                return i,s
            s -= width
        return len(a)-1,a[-1]
    out = 0.0
    for _ in range(trials):
        i,x=point();j,y=point()
        out += abs(x-y) if i==j else x+y
    return out/trials


def test():
    cases = [
        [1,2,3],                  # An arm equals a sum of two smaller ones
        [1,1,2,2],                # Repeated arms, several coincidences
        [2,3,5,7,11],            # Resonances between breakpoints
        [Q(1,2), Q(3,4), Q(5,4)],
        [4,4,4,4,4,4],           # All coincidences at two masses
        [1,2,3,4,5,6,7,8],
        [Q(1,5), Q(2,3), Q(7,4)],
    ]
    r=Random(19)
    for k in range(3,10):
        for _ in range(10):
            cases.append([Q(r.randint(1,31),r.randint(1,9)) for j in range(k)])
    kink_checks = 0
    for a in cases:
        a = tuple(Q(x) for x in a)
        L = sum(a);k=len(a)
        assert recover(atoms(a),k) == sorted(a)
        assert density(Q(0), a) == 2/L
        m = min(a)
        assert (density(m/3,a)-density(Q(0),a))/(m/3) == Q(k*(k-3),1)/(L*L)
        # Distributional kink weights reproduce the derivative differences.
        nu=atoms(a)
        for x,w in list(nu.items())[:min(3,len(nu))]:
            kink_checks += 1
            locs=sorted(set(a)|{u+v for u,v in combinations(a,2)}|{Q(0)})
            near=[abs(x-y) for y in locs if x!=y]
            eps=min(near)/4
            left=(density(x,a)-density(x-eps,a))/eps
            right=(density(x+eps,a)-density(x,a))/eps
            assert right-left == 2*Q(w)/(L*L), (a,x,w)
        # Integrated area is exactly one: integrate all linear intervals.
        knots=sorted({Q(0), *a, *(x+y for x,y in combinations(a,2))})
        integ = sum((density(l,a)+density(h,a))*(h-l)/2 for l,h in zip(knots,knots[1:]))
        assert integ == 1,(a,integ)
    # k=1 and k=2 are geometrically intervals with the same density.
    for total in [Q(1),Q(17,3),Q(10)]:
        for s in [Q(1,4),Q(3,7)]:
            two=[s*total,(1-s)*total]
            for t in [total*Q(j,19) for j in range(20)]:
                assert density(t,[total])==density(t,two)
    ex=[1,2,4,7]
    analytic=float(expected_mean(ex))
    empirical=simulated_mean(ex, 140000)
    assert abs(analytic-empirical) < .018, (analytic,empirical)
    print(f'CHECK_OK exact_inverse_cases={len(cases)} integrated_laws={len(cases)} kink_checks={kink_checks} interval_equivalence=checked monte_carlo_pairs=140000 analytic_mean={analytic:.9f} empirical_mean={empirical:.9f}')

if __name__=='__main__':
    test()
