"""Independent inverse-interval search, Bellman certificate, and witnesses.

The block alphabet is A=ab (weight 2), B=aab (weight 3).
After the mandatory first b, the active state domain is 0,...,n-2.
Use full set-theoretic inverse images. No external packages are required.
Run: python verify_interval.py
"""
import heapq


def g(w, r):
    return (3 * r + 1) // 2 + int(r % 2 == 0 and w % 2 == 0 and 2 <= w <= r)


def formula(n):
    return (3 * n * n - 8 * n + 6) // 2


def interval(s, w, N):
    return {(s + j) % N for j in range(w)}


def inverse_edges(z, N):
    s, w = z
    target = interval(s, w, N)
    old_a = {i for i in range(N) if (i + 1) % N in target}
    old_b = {i for i in range(N) if (0 if i >= N - 2 else i + 2) in target}
    result = []
    for old, weight, kind in [(old_a, 2, 'A'), (old_b, 3, 'B')]:
        if old:
            representations = [(t, len(old)) for t in range(N) if interval(t, len(old), N) == old]
            assert representations, (N, z, kind, old)
            # In a non-full interval, the starting point is unique.
            t = representations[0]
            result.append((t, weight, kind))
    return result


def shortest_inverse(n):
    N = n - 1
    start = (0, 1)
    distances = {start: 0}
    pq = [(0, start)]
    while pq:
        cost, z = heapq.heappop(pq)
        if cost != distances[z]:
            continue
        if z[1] == N:
            return cost + 1
        for next_z, weight, _ in inverse_edges(z, N):
            new = cost + weight
            if new < distances.get(next_z, 10**100):
                distances[next_z] = new
                heapq.heappush(pq, (new, next_z))
    raise AssertionError('No reverse path')


def potential(w, r, N):
    if w == N:
        return 0
    H = 0
    for k in range(N - 1, w, -1):
        H += 3 + g(k, N - 1)
    return g(w, r) + 3 + H


def certificate_check(N):
    for w in range(1, N + 1):
        for s in range(N):
            # right endpoint r = start+w-1 mod N
            z = (s, w)
            r = (s + w - 1) % N
            F = potential(w, r, N)
            for next_z, cost, _ in inverse_edges(z, N):
                t, v = next_z
                rr = (t + v - 1) % N
                assert F <= cost + potential(v, rr, N), (N, z, next_z, cost)


def construct(n):
    N = n - 1
    w = 1
    r = 0
    inverse_actions = []
    while w < N:
        while r:
            if r >= 2 and r != w and g(w, r) == 3 + g(w, r - 2):
                inverse_actions.append('B')
                r -= 2
            else:
                assert g(w, r) == 2 + g(w, r - 1)
                inverse_actions.append('A')
                r -= 1
        inverse_actions.append('B')
        w += 1
        r = N - 1
    return 'b' + ''.join('ab' if action == 'A' else 'aab' for action in reversed(inverse_actions))


def simulate(n, word):
    image = set(range(n))
    for letter in word:
        if letter == 'a':
            image = {(x + 1) % n for x in image}
        else:
            image = {0 if x == n - 1 else x for x in image}
    return image


if __name__ == '__main__':
    for n in range(3, 36):
        got = shortest_inverse(n)
        expected = formula(n)
        assert got == expected, (n, got, expected)
    print('PASS: full inverse-interval Dijkstra, all n=3..35')
    for n in range(3, 81):
        certificate_check(n - 1)
    print('PASS: every Bellman inequality, all n=3..80')
    for n in range(3, 151):
        word = construct(n)
        assert 'aaa' not in word
        assert len(word) == formula(n), (n, len(word), formula(n))
        assert len(simulate(n, word)) == 1
    print('PASS: explicit reset words, all n=3..150')
