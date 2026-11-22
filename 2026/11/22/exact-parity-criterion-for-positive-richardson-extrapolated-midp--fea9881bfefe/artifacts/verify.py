"""Reproduce exact-rational checks for midpoint Richardson quadrature.

Run with Python 3.10+ and no third-party dependencies. This program checks
finite families only; the all-chain conclusion follows from the proof.
"""
from fractions import Fraction
from itertools import product
from math import prod


def coefficients(N):
    d = len(N) - 1
    return [prod((Fraction(N[j]**2, N[j]**2 - N[k]**2)
                  for k in range(d + 1) if j != k), start=Fraction(1))
            for j in range(d + 1)]


def collected_weights(N, c):
    weights = {}
    for n, a in zip(N, c):
        for k in range(n):
            x = Fraction(2 * k + 1, 2 * n)
            weights[x] = weights.get(x, Fraction(0)) + a / n
    return weights


def blocks(ratios):
    start = 0
    for i, r in enumerate(ratios, start=1):
        if r % 2 == 0:
            yield start, i - 1
            start = i
    yield start, len(ratios)


def parity_prediction(ratios):
    d = len(ratios)
    return all((r % 2 == 1 or i % 2 != d % 2)
               for i, r in enumerate(ratios, start=1))


def check_chain(N):
    d = len(N) - 1
    ratios = [N[i] // N[i-1] for i in range(1, len(N))]
    c = coefficients(N)
    w = collected_weights(N, c)
    positive = all(z > 0 for z in w.values())
    assert positive == parity_prediction(ratios), (N, positive)
    assert sum(w.values(), Fraction(0)) == 1
    b = [abs(c[j] / N[j]) for j in range(d + 1)]
    assert all(b[j] < b[j+1] for j in range(d))
    assert max(w.values()) == b[-1]
    assert b[-1] == Fraction(1, N[-1]) * prod(
        (Fraction(N[-1]**2, N[-1]**2 - N[j]**2)
         for j in range(d)), start=Fraction(1))
    neg = sum((-z for z in w.values() if z < 0), Fraction(0))
    bad = list((s,t) for s,t in blocks(ratios) if (d-t) % 2 == 1)
    predicted_neg = -sum((sum(c[s:t+1], Fraction(0)) for s,t in bad),
                         Fraction(0))
    assert neg == predicted_neg, (N, neg, predicted_neg)
    assert sum((abs(z) for z in w.values()), Fraction(0)) == 1 + 2*neg
    for k in range(min(2*d+1, 5) + 1):
        assert sum((z*x**k for x,z in w.items()), Fraction(0)) == Fraction(1,k+1), (N,k)
    return positive, neg, c, w


def main():
    checks = positives = negatives = 0
    for d in range(1, 5):
        for ratios in product((2, 3, 4, 5), repeat=d):
            for base in (1, 2):
                N = [base]
                for r in ratios:
                    N.append(N[-1]*r)
                positive, _, _, _ = check_chain(N)
                checks += 1
                positives += int(positive)
                negatives += int(not positive)
    # All degree conditions, not just through degree 5, in representative chains
    for ratios in ((2,3), (3,2,3), (2,3,2,3), (3,3,3), (2,2,2)):
        N = [1]
        for r in ratios:
            N.append(N[-1]*r)
        w = collected_weights(N, coefficients(N))
        for k in range(2*len(ratios)+2):
            assert sum((z*x**k for x,z in w.items()), Fraction(0)) == Fraction(1,k+1)
    print('EXACT CHECKS PASS:',checks,'divisibility chains;',positives,
          'positive;',negatives,'nonpositive; degree up to 2d+1 on 5 examples')
    for ratios in ((2,), (3,), (2,3), (3,2), (3,2,3), (2,3,2,3)):
        N = [1]
        for r in ratios:
            N.append(N[-1]*r)
        positive, neg, c, w = check_chain(N)
        print('N=',N,'positive=',positive,'negative_mass=',neg,
              'norm=',1+2*neg,'largest_weight=',max(w.values()),
              'coefficients=',','.join(str(v) for v in c))


if __name__ == '__main__':
    main()
