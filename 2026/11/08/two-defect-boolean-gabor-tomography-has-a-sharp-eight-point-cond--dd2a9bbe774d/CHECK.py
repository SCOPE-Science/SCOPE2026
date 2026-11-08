"""Direct exact checks for two-defect Boolean Gabor projector spectra.
Run: python3 CHECK.py. Uses Python's standard library only.
"""
from collections import Counter
from math import sqrt


def parity(a):
    return a.bit_count() % 2


def window(N, z, w):
    g = [1 + 0j] * N
    g[0] += z
    g[1] += w
    return g


def ambiguity(N, z, w):
    g = window(N, z, w)
    result = []
    for a in range(N):
        for b in range(N):
            result.append(sum(g[x ^ a] * g[x].conjugate() * (-1 if parity(x & b) else 1)
                              for x in range(N)))
    return result


def table(N, z, w):
    u, v = z.real, z.imag
    s, t = w.real, w.imag
    hz, hw = abs(z)**2 + 2*u, abs(w)**2 + 2*s
    E = w + z.conjugate() + w*z.conjugate()
    return [
        (N + hz + hw, 1),
        (hz + hw, N//2-1),
        (hz - hw, N//2),
        (N + 2*E.real, 1),
        (2*E.real, N//2-1),
        (2j*E.imag, N//2),
        (N + 2*(u+s), N-2),
        (2*(u+s), (N-2)*(N//4-1)),
        (2*(u-s), (N-2)*N//4),
        (-2j*(v+t), (N-2)*N//4),
        (-2j*(v-t), (N-2)*N//4),
    ]


def arithmetic_rank(values, p=1009):
    """Rank by exact Gaussian elimination on a finite field."""
    n = len(values)
    a = [list(row) for row in values]
    rank = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(rank, n) if a[j][c] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][c] % p, -1, p)
        a[rank][c:] = [(x*inv) % p for x in a[rank][c:]]
        for j in range(rank+1, n):
            coef = a[j][c] % p
            if coef:
                a[j][c:] = [(x - coef*y) % p for x, y in zip(a[j][c:], a[rank][c:])]
        rank += 1
        if rank == n:
            break
    return rank


def gram_rank(N, z, w):
    # Each full orbit projector is vectorized into N^2 Gaussian integers.
    # This route never uses ambiguity expressions or the rank formula.
    assert 469*469 % 1009 == 1008
    g = window(N, z, w)
    projectors = []
    for a in range(N):
        for b in range(N):
            v = [g[x ^ a] * (-1 if parity(x & b) else 1) for x in range(N)]
            proj = [v[x] * v[y].conjugate() for x in range(N) for y in range(N)]
            projectors.append([int(round(t.real + 469*t.imag)) % 1009 for t in proj])
    return arithmetic_rank(projectors)


def main():
    samples = [(1+1j, 2+3j), (-2, 2j), (-2+2j, 0),
               (1, 1), (1, 1j), (-1-2j, -3+4j), (0, 0),
               (1j, 0), (0, 2), (2+2j, 1j)]
    tests = 0
    for N in (8, 16, 32):
        for z, w in samples:
            vals = ambiguity(N, z, w)
            analytic = Counter()
            for amp, mult in table(N, z, w):
                assert mult >= 0
                analytic[complex(round(amp.real), round(amp.imag))] += mult
            assert sum(analytic.values()) == N*N
            assert Counter(vals) == analytic, (N, z, w)
            assert sum(a == 0 for a in vals) == sum(mult for amp, mult in table(N,z,w) if abs(amp)<1e-9)
            tests += 1
    for z,w in samples[:5]:
        assert gram_rank(8, z,w) == sum(mult for amp,mult in table(8,z,w) if amp != 0)
    for N in (8, 16, 32, 64):
        r=sqrt(N/2)
        for z,w in ((-r+1j*r, 0), (-r-1j*r, 0), (-r, 1j*r), (-r, -1j*r),
                    (0, -r+1j*r), (0, -r-1j*r), (1j*r, -r), (-1j*r, -r)):
            t=table(N,z,w)
            nonzero = [abs(amp) for amp,mult in t if mult]
            condition = max(nonzero)/min(nonzero)
            assert abs(condition - (sqrt(2*N)-1)) < 1e-9, (N,z,w,condition)
    print('TWO_DEFECT_BOOLEAN_GABOR_EXACT_CHECKS_PASS',tests,'spectral enumerations, 5 exact modular projector ranks, 32 sharp optimizers')

if __name__ == '__main__':
    main()
