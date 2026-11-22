"""Exact-rational independent checks of a periodic two-clock transport theorem.

Run: python3 checks/check_transport.py
Only Python standard library is required.
"""
from fractions import Fraction as Q
from itertools import combinations


def exact_linear(M, b):
    n = len(b)
    A = [[Q(x) for x in row] + [Q(b[i])] for i, row in enumerate(M)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if A[k][j])
        A[j], A[pivot] = A[pivot], A[j]
        c = A[j][j]
        A[j] = [x / c for x in A[j]]
        for i in range(n):
            if i != j:
                c = A[i][j]
                A[i] = [A[i][k] - c * A[j][k] for k in range(n + 1)]
    return [A[i][-1] for i in range(n)]


def generator_derivative(n, p, q, taus):
    """Independent rate-matrix/tilted-eigenvalue-derivative computation."""
    S = sum(taus)
    V = n * (p - q) / S
    A = [[Q(0)] * (n - 1) for _ in range(n - 1)]
    rhs = [Q(0)] * (n - 1)
    for i in range(n - 1):
        rates = [((i + 1) % n, p / taus[i]),
                 ((i - 1) % n, q / taus[i])]
        rhs[i] = V - (p - q) / taus[i]
        for j, rate in rates:
            if j < n - 1:
                A[i][j] += rate
            A[i][i] -= rate
    h = exact_linear(A, rhs) + [Q(0)]
    # The eigenvector derivative must be centered under the stationary measure.
    pi_h = sum(taus[i] * h[i] for i in range(n)) / S
    raw = n * (p + q) / S
    cross = Q(2, 1) * sum(p * h[(i + 1) % n] -
                            q * h[(i - 1) % n] for i in range(n)) / S
    return V, raw + cross - 2 * V * pi_h


def corrector_variance(n, p, q, taus):
    """Explicit geometric-convolution formula, not matrix inversion."""
    S = sum(taus)
    V = n * (p - q) / S
    r = q / p
    avg = S / n
    d = []
    for i in range(n):
        z = sum(r ** j * (taus[(i - j) % n] - avg)
                for j in range(n))
        d.append((p - q) * n * z / (S * p * (1 - r ** n)))
    assert sum(d) == 0
    assert all(p*d[i]-q*d[(i-1)%n] ==
               (p-q)*(n*taus[i]/S-1) for i in range(n))
    return V, (p + q) / S * sum((1 + t) ** 2 for t in d)


def energy(n, A, r):
    return sum(r ** ((b - a) % n) + r ** ((a - b) % n)
               for a, b in combinations(A, 2))


def balanced(n, k):
    return tuple(i*n//k for i in range(k))


def main():
    # Independently constructed matrix and convolution evaluations.
    cases = 0
    for n in range(4, 10):
        for p, q in [(Q(3),Q(1)), (Q(5),Q(2)), (Q(7),Q(4))]:
            for a, b in [(Q(2),Q(2)), (Q(2),Q(1,2)),
                         (Q(2,3),Q(3,4))]:
                for gap in range(1,n):
                    taus = [Q(1)]*n
                    taus[0] = a
                    taus[gap] = b
                    assert generator_derivative(n,p,q,taus) == corrector_variance(n,p,q,taus)
                    cases += 1
    # All subsets for small periods: optimality plus equality classification.
    subsets = 0
    r = Q(2,5)
    for n in range(4, 13):
        for k in range(2, n):
            possibilities = [tuple((0,)+t) for t in combinations(range(1,n), k-1)]
            vals = [(energy(n, A, r), A) for A in possibilities]
            emin, emax = min(x[0] for x in vals), max(x[0] for x in vals)
            assert energy(n,balanced(n,k),r) == emin
            assert energy(n,tuple(range(k)),r) == emax
            for val, A in vals:
                gaps = [(A[(i+1)%k]-A[i])%n for i in range(k)]
                is_balanced = all(max(sum(gaps[(i+j)%k] for j in range(m)) for i in range(k))
                                  - min(sum(gaps[(i+j)%k] for j in range(m)) for i in range(k)) <= 1
                                  for m in range(1,k))
                is_block = max(gaps) == n-k+1
                assert (val==emin) == is_balanced
                assert (val==emax) == is_block
                subsets += 1
    # Exact contrasting case: n=6, p=3, q=1, two slow clocks.
    v = []
    for gap in (1,2,3):
        tau=[Q(1)]*6
        tau[0] = tau[gap] = Q(2)
        v.append(corrector_variance(6,Q(3),Q(1),tau)[1])
    assert v == [Q(1161,364),Q(18225,5824),Q(81,26)]
    assert v[0]>v[1]>v[2]
    print('PASS: exact independent tilted-generator and convolution checks:',cases)
    print('PASS: all cyclic placements and exact equality cases:',subsets)
    print('PASS: six-site dispersion examples:',*(str(x) for x in v))

if __name__=='__main__':
    main()
