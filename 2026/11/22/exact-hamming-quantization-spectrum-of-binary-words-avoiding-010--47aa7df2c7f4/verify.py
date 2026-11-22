"""Exact finite checks for the no-010 Hamming quantization theorem.

Only the Python standard library is required. Run: python3 verify.py
"""
from collections import Counter
from itertools import product


def greedy_nonoverlap(word):
    i = hits = 0
    while i + 2 < len(word):
        if word[i:i + 3] == (0, 1, 0):
            hits += 1
            i += 3
        else:
            i += 1
    return hits


def nearest_avoider_distance(word):
    # Independent shortest-path dynamic program over output suffixes.
    dp = {(): 0}
    for bit in word:
        new = {}
        for suffix, cost in dp.items():
            for b in (0, 1):
                if suffix == (0, 1) and b == 0:
                    continue
                end = (suffix + (b,))[-2:]
                value = cost + (b != bit)
                if end not in new or value < new[end]:
                    new[end] = value
        dp = new
    return min(dp.values())


def constructive_quantizer(word):
    n = len(word)
    starts = [i for i in range(n - 2) if word[i:i+3] == (0, 1, 0)]
    flip = []
    j = 0
    while j < len(starts):
        k = j + 1
        while k < len(starts) and starts[k] == starts[k - 1] + 2:
            k += 1
        # Each step-two chain has ceiling(length/2) disjoint occurrences.
        for t in range(j, k - 1, 2):
            flip.append(starts[t] + 2)
        if (k - j) & 1:
            flip.append(starts[k - 1] + 1)
        j = k
    out = list(word)
    for i in flip:
        out[i] ^= 1
    return tuple(out), len(flip)


def poly_add(*terms):
    size = max(len(x) for _, x in terms)
    a = [0] * size
    for scale, p in terms:
        for i, c in enumerate(p):
            a[i] += scale*c
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def distance_polynomials(N):
    # (1+z^2)/(1-2z+z^2-(1+u)z^3).
    P = [[1], [2], [4]]
    for n in range(3, N + 1):
        P.append(poly_add((2,P[-1]), (-1,P[-2]),
                          (1,P[-3]), (1,[0] + P[-3])))
    return P[:N+1]


def expected_deep_holes(n):
    k,r=divmod(n,3)
    return [1, 2*(k+1), 2*k*k+5*k+4][r]


def verify():
    P = distance_polynomials(180)
    checked = 0
    for n in range(16):
        histogram = Counter()
        for word in product((0, 1), repeat=n):
            d = nearest_avoider_distance(word)
            g = greedy_nonoverlap(word)
            quantized, edits = constructive_quantizer(word)
            assert d == g == edits, (n, word, d, g, edits)
            assert (0,1,0) not in tuple(quantized[i:i+3] for i in range(n-2))
            assert sum(a!=b for a,b in zip(word,quantized)) == edits
            histogram[d] += 1
            checked += 1
        assert histogram == Counter({d:c for d,c in enumerate(P[n]) if c}), (n,histogram,P[n])
    for n in range(181):
        p = P[n]
        assert sum(p) == 1 << n
        assert len(p) - 1 == n//3
        assert p[-1] == expected_deep_holes(n), (n,p[-1],expected_deep_holes(n))
    for n in (80,120,180):
        p=P[n]; q=1<<n
        mean=sum(j*c for j,c in enumerate(p))/q
        var=sum(j*j*c for j,c in enumerate(p))/q-mean*mean
        assert abs(mean-n/10+4/25) < 0.001
        assert abs(var - 29*n/500) < 0.3
    print(f'VERIFY_OK: {checked} input words checked for n=0..15; polynomial identities through n=180')

if __name__ == '__main__':
    verify()
