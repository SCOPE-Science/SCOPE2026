"""Independent finite checks for square gaps of interval-generated semigroups."""
from math import ceil, floor, isqrt, sqrt


def predicted(a, k):
    assert a >= 2 and k >= 1
    return sum(ceil(sqrt((q + 1) * a)) - 1 - isqrt(q * (a + k))
               for q in range((a - 1) // k + 1))


def predicted_exact(a, k):
    # Integer arithmetic is used to avoid floating-point rounding at squares.
    return sum(isqrt((q + 1) * a - 1) - isqrt(q * (a + k))
               for q in range((a - 1) // k + 1))


def direct(a, k):
    # Coin-change dynamic programming uses generator reachability, not the
    # quotient/remainder criterion or the proof's gap interval decomposition.
    max_root = a
    cap = max_root * max_root
    reachable = bytearray(cap + 1)
    reachable[0] = 1
    gens = list(range(a, a + k + 1))
    for g in gens:
        if g > cap:
            break
        for n in range(g, cap + 1):
            if reachable[n - g]:
                reachable[n] = 1
    return sum(not reachable[j * j] for j in range(1, max_root + 1))


def partial_predicted_exact(a, k, N):
    # Exact integer-root count via the quotient-block intervals, truncated at N.
    return sum(max(0, min(N, isqrt((q + 1) * a - 1)) - isqrt(q * (a + k)))
               for q in range(min((a - 1) // k, N * N // a) + 1))


def partial_direct(a, k, N):
    cap = max(1, N * N)
    reachable = bytearray(cap + 1)
    reachable[0] = 1
    for g in range(a, a + k + 1):
        if g > cap:
            break
        for v in range(g, cap + 1):
            if reachable[v - g]:
                reachable[v] = 1
    return sum(not reachable[n*n] for n in range(1, N + 1))


def F(t):
    J = floor(1 / t)
    return sum(sqrt(q + 1) - sqrt((1 + t) * q) for q in range(J + 1))


def main():
    cases = 0
    for a in range(2, 65):
        for k in range(1, min(2 * a, 75) + 1):
            exact = predicted_exact(a, k)
            brute = direct(a, k)
            assert exact == brute, (a, k, exact, brute)
            assert predicted(a, k) == exact, (a, k)
            cases += 1
    print('Independent dynamic-programming comparisons passed:', cases)
    partial_cases = 0
    for a in range(2, 45):
        for k in (1, 2, max(1, a // 3), a):
            for N in (0, 1, isqrt(a), a // max(1, isqrt(k)), a):
                if N > a:
                    continue
                assert partial_predicted_exact(a, k, N) == partial_direct(a, k, N), (a, k, N)
                partial_cases += 1
    print('Cumulative root-profile comparisons passed:', partial_cases)
    large = 0
    for a in (100, 101, 999, 1000, 2025, 10000, 100001):
        for k in (1, 2, 3, 7, 17, isqrt(a), a // 3, a // 2, a - 1, a, a + 1):
            if k < 1:
                continue
            N = predicted_exact(a, k)
            error = abs(N - sqrt(a) * F(k / a))
            assert error <= (a + k - 1) // k + 1e-7, (a, k, error)
            if k >= a:
                assert N == isqrt(a - 1)
            large += 1
    print('Uniform-bound and plateau comparisons passed:', large)
    profile_cases = 0
    for a in (1000, 10000, 100000):
        for k in (isqrt(a), int(a ** 0.7), a // 5):
            for s in (0.0, 0.1, 0.25, 0.5, 0.75, 1.0):
                N = floor(s * a / sqrt(k))
                actual = partial_predicted_exact(a, k, N)
                approximated = (a / sqrt(k)) * (s - s**3 / 3)
                assert abs(actual - approximated) <= 5 * (sqrt(a) + a / k)
                profile_cases += 1
    print('Mesoscopic cumulative-profile bound samples passed:', profile_cases)
    for a in (1000, 10000, 100000):
        k = isqrt(a)
        N = predicted_exact(a, k)
        print('Mesoscopic sample', a, k, N, 'ratio', round(N / (2 * a / (3 * sqrt(k))), 7))

if __name__ == '__main__':
    main()
