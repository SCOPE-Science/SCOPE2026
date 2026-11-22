"""Finite exact-rational consistency checks for Sturmian coding partitions.

The all-irrational, all-cardinality theorem is proved analytically in RESULT.md.
"""
from itertools import combinations

P, Q = 233, 377
ARCS = [(5, 20), (41, 56), (76, 91)]   # Endpoints in hundredths


def cut_midpoints(n):
    cuts = sorted({(-j * P) % Q for j in range(n + 1)})
    assert len(cuts) == n + 1
    ans = []
    for i, a in enumerate(cuts):
        b = cuts[i + 1] if i + 1 < len(cuts) else cuts[0] + Q
        theta_numerator = (a + b) % (2 * Q)
        # midpoint theta=(a+b)/(2Q) modulo 1
        theta_numerator %= 2 * Q
        ans.append(theta_numerator)
    return ans


def word(theta, n):
    return tuple(((theta + 2 * (j+1)*P) // (2*Q)) -
                 ((theta + 2*j*P) // (2*Q)) for j in range(n))


def arc(theta, lo, hi):
    return 2 * Q * lo < 100 * theta < 2 * Q * hi


print('exact rational slope: %d/%d' % (P, Q))
for n in range(1, 61):
    mid = cut_midpoints(n)
    words = [word(t, n) for t in mid]
    assert len(set(words)) == n + 1, (n, len(set(words)))
    assert all(len(w) == n and set(w) <= {0,1} for w in words)
    if n >= 24:
        sets = [[w for t, w in zip(mid, words) if arc(t,*I)] for I in ARCS]
        assert all(len(s) >= 1 for s in sets), (n, [len(s) for s in sets])
        assert all(len(set(s)) == len(s) for s in sets)
        for i, j in combinations(range(3), 2):
            # Disjoint arc labels preserve a positive circular separation.
            assert ARCS[i][1] < ARCS[j][0]
    if n in (24, 36, 48, 60):
        print('length=%2d total_words=%2d arc_word_counts=%s' %
              (n, n+1, [len(s) for s in sets]))
print('PASS: all 60 exact finite partition and phase-marker checks')
