"""Independent finite checks for the descent spectrum of <n,n+1>.

Uses reachability and ordered-pair convolution, not the proof's Apéry-coordinate formula.
Python 3, standard library only. Finite tests supplement, not replace, the proof.
"""
from collections import Counter


def verify(n):
    conductor = n * (n - 1)
    limit = 2 * conductor + n + 2
    reachable = bytearray(limit + 1)
    reachable[0] = 1
    for s in range(limit + 1):
        if reachable[s]:
            if s + n <= limit:
                reachable[s + n] = 1
            if s + n + 1 <= limit:
                reachable[s + n + 1] = 1
    elements = [s for s in range(limit + 1) if reachable[s]]
    counts = [0] * (limit + 1)
    for x in elements:
        for y in elements:
            if x + y > limit:
                break
            counts[x + y] += 1
    for s in elements:
        t, r = divmod(s, n)
        a = t - r
        predicted_count = (a + 1) * (r + 1) + (n - 1 - r) * max(a - n, 0)
        assert counts[s] == predicted_count, (n, s, counts[s], predicted_count)
    observed = {x: counts[x] - counts[y]
                for x, y in zip(elements, elements[1:])
                if counts[x] > counts[y]}
    predicted = {n*t + r: 2*r + 1 - t
                 for r in range(1, n - 1)
                 for t in range(r + 1, 2*r + 1)}
    assert observed == predicted, (n, observed, predicted)
    freq = Counter(observed.values())
    assert freq == Counter({d: n - 1 - d for d in range(1, n - 1)})
    assert sum(observed.values()) == n*(n-1)*(n-2)//6
    return len(observed)


def main():
    checks = [verify(n) for n in range(2, 49)]
    print('PASS: every semigroup parameter n = 2,...,48')
    print('PASS: all adjacent counts through 2*n*(n-1)+n+2, with complete descent locations')
    print('PASS: complete Apéry-coordinate formula at all tested nongaps')
    print('PASS: every descent magnitude frequency and summed descent sizes')
    print('Number of verified pairs (n, predicted descent) =', sum(checks))


if __name__ == '__main__':
    main()
