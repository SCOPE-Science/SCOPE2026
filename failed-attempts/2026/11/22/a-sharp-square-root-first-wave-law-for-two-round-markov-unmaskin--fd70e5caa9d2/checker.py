"""Reproducibility checks for exact two-round Markov masking identities.

All computations use Python's standard library. Finite enumeration is a
consistency check; it does not replace the infinite-chain convexity proof.
"""
from itertools import product
from math import exp, log, log1p, sqrt


def entropy(probabilities):
    return -sum(v * log(v) for v in probabilities if v)


def mutual_information(rho, distance):
    z = rho ** distance
    if abs(z) >= 1:
        return log(2)
    return ((1 + z) * log1p(z) + (1 - z) * log1p(-z)) / 2


def formula(length, rho, fraction):
    remain = 1 - fraction
    result = (length - 1) * mutual_information(rho, 1)
    result -= 2 * fraction * sum((length - d) * remain**d *
                               mutual_information(rho, d)
                               for d in range(1, length))
    result += fraction**2 * sum((length - d) * (d - 1) *
                                remain**(d - 1) * mutual_information(rho, d)
                                for d in range(2, length))
    return result


def enumeration(length, rho, fraction):
    paths = list(product((0, 1), repeat=length))
    full = {w: 0.5 * __import__('functools').reduce(
        lambda a, pair: a * ((1 + rho) / 2 if pair[0] == pair[1]
                            else (1 - rho) / 2), zip(w, w[1:]), 1.0)
        for w in paths}
    hsub = {}
    for mask in range(1 << length):
        selected = [i for i in range(length) if (mask >> i) & 1]
        marg = {}
        for w, weight in full.items():
            k = tuple(w[i] for i in selected)
            marg[k] = marg.get(k, 0.0) + weight
        hsub[mask] = entropy(marg.values())
    result = length * fraction * log(2) - hsub[(1 << length) - 1]
    for mask in range(1 << length):
        pop = mask.bit_count()
        weight = fraction**pop * (1 - fraction)**(length - pop)
        result += weight * sum(hsub[mask | (1 << i)] - hsub[mask]
                               for i in range(length) if not (mask >> i) & 1)
    return result


def infinite_formula(rho, p):
    # Absolute convergence is rapid for fixed rho < 1 and 0 < p < 1.
    q = 1 - p
    acc = mutual_information(rho, 1)
    d = 1
    while True:
        i = mutual_information(rho, d)
        delta = -2 * p * q**d * i
        if d > 1:
            delta += p * p * (d - 1) * q**(d - 1) * i
        acc += delta
        if d > 25 and q**d * (1 + p * d) < 1e-16:
            break
        if d > 200000:
            raise ArithmeticError('tail convergence limit')
        d += 1
    return acc


def main():
    cases = 0
    largest_error = 0.0
    for length in range(2, 7):
        for rho in (-0.73, -0.31, 0.17, 0.65, 0.91):
            for p in (0.08, 0.27, 0.5, 0.73, 0.93):
                a, b = formula(length, rho, p), enumeration(length, rho, p)
                error = abs(a - b)
                largest_error = max(largest_error, error)
                assert error < 5e-12, (length, rho, p, a, b)
                cases += 1
    # Strictly convex kernel by exact factored formula in the proof.
    for a in (0.001, 0.1, 0.5, 0.9, 0.999):
        for p in (0.02, 0.1, 0.5, 0.95):
            d2 = 2 * a * (1 - a)**2 * (2 + a * (1 - p)) / (1 - a * (1 - p))**4
            assert d2 > 0
    # For a long chain, compare a numerical minimizer with the predicted
    # square-root persistence law; this is an illustration, not a proof.
    from math import fsum
    for eps in (1e-3, 1e-4):
        rho = exp(-eps)
        predicted = sqrt(eps / (2 * log(2)))
        candidates = [predicted * (0.7 + i * .006) for i in range(101)]
        vals = [(infinite_formula(rho, p), p) for p in candidates]
        best, pbest = min(vals)
        assert pbest < 0.5
        assert best < infinite_formula(rho, 0.5)
        assert abs(pbest/predicted - 1) < 0.15
    print(f'PASS: {cases} exhaustive-weighted finite Markov instances; '
          f'max |difference|={largest_error:.3g}; '
          'positive convexity kernel; high-persistence scaling checks.')


if __name__ == '__main__':
    main()
