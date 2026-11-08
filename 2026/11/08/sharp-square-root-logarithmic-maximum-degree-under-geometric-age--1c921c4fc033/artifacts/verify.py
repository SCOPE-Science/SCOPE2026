"""Exact finite checks for the geometric-age recursive graph's attachment laws.

Run with Python 3 standard library only. These checks support the finite
identities in the proof; they are not a certification of the infinite limit.
"""
from fractions import Fraction
from itertools import product

CHECKS = 0


def check(condition, message="finite identity mismatch"):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def attachment(t, q):
    return tuple((1 - q) * q ** (t - 1 - k) / (1 - q ** t) for k in range(t))


def exhaustive(n, m, q):
    probs = [attachment(t, q) for t in range(1, n + 1)]
    born = [tuple(range(t)) for t in range(1, n + 1) for _ in range(m)]
    hist = {(k, d): Fraction(0) for k in range(n + 1) for d in range(m * n + 1)}
    sum_prob = Fraction(0)
    expected_m = Fraction(0)
    for assignment in product(*born):
        counts = [0] * (n + 1)
        w = Fraction(1)
        idx = 0
        for t in range(1, n + 1):
            for _ in range(m):
                parent = assignment[idx]
                idx += 1
                counts[parent] += 1
                w *= probs[t - 1][parent]
        for k, d in enumerate(counts):
            hist[k, d] += w
        sum_prob += w
        expected_m += max(counts) * w
        check(sum(counts) == m * n)
        check(max(counts) <= m * n)
    check(sum_prob == 1, "probabilities did not normalize")
    for k in range(n + 1):
        check(sum(hist[k, d] for d in range(m * n + 1)) == 1)
        mean = sum(d * hist[k, d] for d in range(m * n + 1))
        target_mean = sum(m * probs[t - 1][k] for t in range(k + 1, n + 1))
        check(mean == target_mean, "indegree mean mismatch")
        for z in (2, 3):
            exact_mgf = sum(z ** d * hist[k, d] for d in range(m * n + 1))
            product_mgf = Fraction(1)
            for t in range(k + 1, n + 1):
                product_mgf *= (1 + probs[t - 1][k] * (z - 1)) ** m
            check(exact_mgf == product_mgf, "indegree generating function mismatch")
    check(Fraction(0) <= expected_m <= m * n)


def run():
    for q in (Fraction(1, 2), Fraction(1, 3)):
        for t in range(1, 17):
            p = attachment(t, q)
            check(sum(p) == 1)
            for k in range(t):
                age = t - k - 1
                check((1 - q) * q ** age <= p[k] <= q ** age)
                check(p[k] == q ** age / sum(q ** j for j in range(t)))
        for m in (1, 2):
            for n in range(1, 6):
                exhaustive(n, m, q)
            for h in range(1, 5):
                k = 2
                probability = Fraction(1)
                for j in range(h):
                    probability *= attachment(k + j + 1, q)[k] ** m
                lower = (1 - q) ** (m * h) * q ** (m * h * (h - 1) // 2)
                check(probability >= lower, "consecutive full-attachment event bound")
    print(f"VERIFIED {CHECKS} exact finite rational assertions")


if __name__ == '__main__':
    run()
