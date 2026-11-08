"""Independent finite checks for the cyclic defect-one rank-frontier theorem.
Run: python verify.py. All dependencies are from the Python standard library.
"""
from collections import deque
from itertools import product


def act(n, r, s, letter):
    if letter == 'a':
        mask = (1 << n) - 1
        return ((s << 1) & mask) | (s >> (n - 1))
    return (s & ~1) | ((s & 1) << r)


def bfs_rank_shortest_counts(n, r):
    full = (1 << n) - 1
    dist, count = {full: 0}, {full: 1}
    queue = deque([full])
    while queue:
        s = queue.popleft()
        for letter in 'ab':
            t = act(n, r, s, letter)
            if t not in dist:
                dist[t] = dist[s] + 1
                count[t] = count[s]
                queue.append(t)
            elif dist[t] == dist[s] + 1:
                count[t] += count[s]
    return dist, count


def formula_words(r):
    for choices in product((0, 1), repeat=r - 1):
        times = sorted([0, 2 * r] + [i + bit*r for i, bit in enumerate(choices, 1)])
        w = 'b'
        for u, v in zip(times, times[1:]):
            w += 'a' * (v - u) + 'b'
        yield w


def compute(n, r, w):
    s = (1 << n) - 1
    for letter in w:
        s = act(n, r, s, letter)
    return s.bit_count()


def test():
    bfs_cases = 0
    for n in range(5, 15):
        for r in range(2, (n - 1) // 2 + 1):
            dist, count = bfs_rank_shortest_counts(n, r)
            for j in range(1, r + 2):
                candidates = [s for s in dist if s.bit_count() <= n-j]
                assert candidates, (n, r, j, 'unreachable')
                depth = min(dist[s] for s in candidates)
                multiplicity = sum(count[s] for s in candidates if dist[s] == depth)
                expected_depth = 2*j-1 if j <= r else 3*r+1
                expected_count = 1 if j <= r else 2 ** (r-1)
                assert (depth, multiplicity) == (expected_depth, expected_count), (n,r,j,depth,multiplicity)
                bfs_cases += 1
    witness_cases = 0
    for r in range(2, 12):
        allw = list(formula_words(r))
        assert len(allw) == len(set(allw)) == 2 ** (r-1)
        for n in (2*r+1, 3*r+2, 5*r+5):
            for w in allw:
                assert len(w) == 3*r+1 and w.count('b') == r+1
                assert compute(n, r, w) == n-r-1, (n,r,w)
                witness_cases += 1
    print('VERIFIED', 'bfs_threshold_cases=', bfs_cases, 'constructed_word_cases=', witness_cases)

if __name__ == '__main__':
    test()
