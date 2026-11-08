"""Reproduce finite instances of the Hermitian two-projector convolution theorem."""
from collections import Counter


def gf_mul(a, b, degree, irreducible):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= irreducible
    return out


def gf_pow(a, power, degree, irreducible):
    out = 1
    while power:
        if power & 1:
            out = gf_mul(out, a, degree, irreducible)
        a = gf_mul(a, a, degree, irreducible)
        power >>= 1
    return out


def check(m, irreducible):
    degree = 2 * m
    q = 1 << m
    size = 1 << degree
    mul = lambda x, y: gf_mul(x, y, degree, irreducible)
    frob = lambda x: gf_pow(x, q, degree, irreducible)
    norm = lambda x: mul(x, frob(x))
    # Also verify these polynomial models are fields, not quotient rings.
    for x in range(1, size):
        assert mul(x, gf_pow(x, size - 2, degree, irreducible)) == 1
    base = [x for x in range(size) if frob(x) == x]
    assert len(base) == q and 0 in base and 1 in base
    # Each (a,z) is the uniquely represented projector
    # [[a,z],[z^q,1+a]] with norm(z)=a*(a+1).
    projectors = [(a, z) for a in base for z in range(size)
                  if norm(z) == mul(a, a ^ 1)]
    assert len(projectors) == q * (q - 1)
    observed = Counter((a ^ b, z ^ w) for a, z in projectors
                       for b, w in projectors)
    predicted = {}
    for s in base:
        for w in range(size):
            h = norm(w)
            if w == 0:
                predicted[(s, w)] = q * (q - 1) if s in (0, 1) else 0
            else:
                predicted[(s, w)] = (0 if h in (mul(s, s), mul(s ^ 1, s ^ 1))
                                     else q)
    assert len(predicted) == q ** 3
    assert all(observed[target] == count for target, count in predicted.items())
    assert set(observed) <= set(predicted)
    assert len(observed) == 2 + (q - 2) * (q * q - 1)
    assert sum(observed.values()) == len(projectors) ** 2
    assert sum(value ** 2 for value in observed.values()) == q*q*(q**3 - 5*q + 4)
    assert Counter(observed.values()) == (Counter({q * (q - 1): 2})
                                              if q == 2 else
                                              Counter({q * (q - 1): 2,
                                                       q: (q - 2) * (q * q - 1)}))
    print(f"q={q}: projectors={len(projectors)}, support={len(observed)}, "
          f"energy={sum(v*v for v in observed.values())}: PASS")


if __name__ == '__main__':
    for m, polynomial in ((1, 0b111), (2, 0b10011),
                          (3, 0b1000011), (4, 0b100011101)):
        check(m, polynomial)
    print('HERMITIAN_BINARY_PROJECTOR_PAIR_PASS')
