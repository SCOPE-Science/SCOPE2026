"""Exact certificate for selected critical de Bruijn identifying codes.

Pure Python 3, standard library only. All graph vertices, all directed
predecessors up to the requested radius, and all identifying signatures
are checked; no random sampling or external solver is used.
"""
from hashlib import sha256

CASES = ((3, 3), (4, 3), (3, 4), (4, 4))  # (alphabet size, radius)


def digits(number, base, length):
    a = [0] * length
    for i in range(length - 1, -1, -1):
        a[i], number = number % base, number // base
    assert number == 0
    return a


def selected(number, q, t):
    a = digits(number, q, 2 * t - 1)
    return (sum(a[t:]) - sum(a[:t - 1])) % q != 0


def from_prefixes(v, q, n, t):
    # A predecessor reached in exactly r steps is any word with
    # suffix equal to the first n-r digits of v.
    seen = {v}
    for r in range(1, t + 1):
        prefix = v // (q ** r)
        block = q ** (n - r)
        for z in range(q ** r):
            seen.add(z * block + prefix)
    return seen


def from_reverse_paths(v, q, n, t):
    # Independent construction by repeated one-edge reverse moves.
    Q = q ** (n - 1)
    reached = {v}
    frontier = {v}
    for _ in range(t):
        nxt = {a * Q + u // q for u in frontier for a in range(q)}
        reached.update(nxt)
        frontier = nxt
    return reached


def check(q, t):
    n = 2 * t - 1
    N = q ** n
    codes = [selected(u, q, t) for u in range(N)]
    size = sum(codes)
    target = q ** (n - 1) * (q - 1)
    assert size == target, (q, t, size, target)
    # The lower bound follows from each (n-1)-digit prefix class.
    for prefix in range(q ** (n - 1)):
        assert sum(codes[q * prefix + a] for a in range(q)) == q - 1

    signatures = {}
    digest = sha256()
    for v in range(N):
        neighborhood = from_prefixes(v, q, n, t)
        reverse = from_reverse_paths(v, q, n, t)
        assert neighborhood == reverse, ('neighborhood_mismatch', q, t, v)
        sig = tuple(sorted(u for u in neighborhood if codes[u]))
        assert sig, ('empty_identification', q, t, v)
        assert sig not in signatures, ('collision', q, t, v, signatures.get(sig))
        signatures[sig] = v
        # Canonical, length-framed encoding of each signature and its vertex.
        digest.update(v.to_bytes(4, 'big'))
        digest.update(len(sig).to_bytes(4, 'big'))
        for u in sig:
            digest.update(u.to_bytes(4, 'big'))
    assert len(signatures) == N
    print(f'q={q} t={t} n={n} vertices={N} sensors={size} signatures={len(signatures)} sha256={digest.hexdigest()}')


if __name__ == '__main__':
    for q, t in CASES:
        check(q, t)
    print('VERIFY_OK cases=4')
