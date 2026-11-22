"""Direct finite-state and analytic checks for entropy of reset walks on cycles.

Run: python3 verify.py (uses the Python standard library only).
The finite checks are diagnostic; the proof of statements for all ring sizes is in RESULT.md.
"""
from fractions import Fraction
from math import sqrt, log, isclose

COUNT = 0

def check(condition, msg):
    global COUNT
    if not condition:
        raise AssertionError(msg)
    COUNT += 1


def solve_fraction(matrix, rhs):
    n = len(rhs)
    a = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            raise ValueError('singular matrix')
        a[col], a[pivot] = a[pivot], a[col]
        factor = a[col][col]
        a[col] = [v / factor for v in a[col]]
        for i in range(n):
            if i != col:
                factor = a[i][col]
                if factor:
                    a[i] = [x - factor * y for x, y in zip(a[i], a[col])]
    return [row[-1] for row in a]


def direct(n, rate):
    p = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        p[i][0] += rate
        p[i][(i - 1) % n] += (1 - rate) / 2
        p[i][(i + 1) % n] += (1 - rate) / 2
    eq = [[p[j][i] - int(i == j) for j in range(n)] for i in range(n)]
    eq[-1] = [Fraction(1)] * n
    rhs = [Fraction(0)] * (n - 1) + [Fraction(1)]
    stationary = solve_fraction(eq, rhs)
    check(sum(stationary) == 1, 'stationary normalization')
    for j in range(n):
        check(sum(stationary[i] * p[i][j] for i in range(n)) == stationary[j],
              'stationarity')
    def entropy(row):
        return -sum(float(a) * log(float(a)) for a in row if a)
    h = sum(float(stationary[i]) * entropy(p[i]) for i in range(n))
    return stationary, h


def analytic(n, gamma):
    z = 1 - gamma
    disc = sqrt(1 - z * z)
    q = z / (1 + disc)  # stable equivalent of (1-disc)/z
    a = z / 2
    B = -gamma * log(gamma) - z * log(z / 2)
    delta = (gamma + a) * log(gamma + a) - gamma * log(gamma) - a * log(a)
    pref = gamma / disc
    root_neighbor = pref * (q + q ** (n - 1)) / (1 - q ** n)
    h = B - 2 * root_neighbor * delta
    h_inf = B - 2 * pref * q * delta
    exact_gap = 2 * delta * pref * (1 + q*q) * q**(n-1) / (1 - q**n)
    return h, h_inf, exact_gap, root_neighbor, q


def main():
    for n in range(3, 15):
        for gamma in (Fraction(1, 11), Fraction(1, 4), Fraction(1, 3),
                      Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)):
            pi, hd = direct(n, gamma)
            h, hinf, gap, pin, q = analytic(n, float(gamma))
            check(isclose(h, hd, abs_tol=2e-12), f'analytic vs exact-state entropy n={n} r={gamma}')
            check(isclose(pin, float(pi[1]), abs_tol=2e-12), 'analytic vs exact neighbor occupation')
            check(isclose(hinf-h, gap, abs_tol=3e-13), 'exact finite-size gap identity')
            check(gap > 0 and 0 < q < 1, 'strict finite-size deficit')
            if n < 14:
                hnext = analytic(n+1, float(gamma))[0]
                check(hnext > h, 'strict order at sampled parameters')
    # Test exact periodized resolvent independently of matrix inversion.
    for g in (0.01, 0.1, 0.25, 0.66, 0.9):
        z = 1 - g
        q = z / (1 + sqrt(1-z*z))
        check(isclose(z*(q+1/q), 2, rel_tol=1e-12), 'Green-function recurrence')
        check(0 < q < 1, 'decaying Green-function root')
    print('PASS: {} exact-rational-stationarity and analytic comparisons'.format(COUNT))

if __name__ == '__main__':
    main()
