"""Reproduce exact 2-dynamic four-colouring and recolouring of KG(5,2).

All vertex labels are the lexicographically ordered two-subsets of {0,...,4}.
Only Python's standard library is required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

PAIRS = tuple(combinations(range(5), 2))
INDEX = {p: i for i, p in enumerate(PAIRS)}
NBR = tuple(tuple(j for j, q in enumerate(PAIRS) if set(p).isdisjoint(q))
            for p in PAIRS)
assert all(len(a) == 3 for a in NBR)


def partitions(k):
    """Generate partitions into exactly k labelled-by-first-appearance blocks."""
    labels = [0] * 10

    def extend(i, high):
        if i == 10:
            if high + 1 == k:
                yield tuple(labels)
            return
        for t in range(min(high + 1, k - 1) + 1):
            if any(t == labels[j] for j in NBR[i] if j < i):
                continue
            labels[i] = t
            yield from extend(i + 1, max(high, t))

    yield from extend(1, 0)


def dynamic(a):
    return all(len({a[j] for j in NBR[i]}) >= 2 for i in range(10))


P3 = list(partitions(3))
P4 = list(partitions(4))
D3 = [a for a in P3 if dynamic(a)]
D4 = [a for a in P4 if dynamic(a)]
assert (len(P3), len(P4), len(D3), len(D4)) == (20, 520, 0, 240)

STATES = sorted({tuple(c[t] for t in a) for a in D4
                 for c in permutations(range(4))})
assert len(STATES) == 5760
LOOKUP = {s: i for i, s in enumerate(STATES)}


def prof(s):
    return tuple(sorted(Counter(s).values()))


BYPROFILE = defaultdict(list)
for i, s in enumerate(STATES):
    BYPROFILE[prof(s)].append(i)
expected = {(1, 2, 3, 4): 1440, (1, 3, 3, 3): 480,
            (2, 2, 2, 4): 960, (2, 2, 3, 3): 2880}
assert {p: len(v) for p, v in BYPROFILE.items()} == expected


# Check that permutations of the five underlying labels and of the four
# colours act transitively on each of the four profile classes.
REPS = {}
for p, indices in sorted(BYPROFILE.items()):
    s = STATES[indices[0]]
    orbit = set()
    for perm in permutations(range(5)):
        induced = [INDEX[tuple(sorted((perm[a], perm[b])))]
                   for a, b in PAIRS]
        pulled = [0] * 10
        for i, c in enumerate(s):
            pulled[induced[i]] = c
        for cperm in permutations(range(4)):
            orbit.add(tuple(cperm[t] for t in pulled))
    assert orbit == {STATES[i] for i in indices}
    REPS[p] = s

GRAPH = []
for s in STATES:
    next_states = set()
    for i in range(10):
        for new in range(4):
            if new != s[i]:
                t = s[:i] + (new,) + s[i + 1:]
                if t in LOOKUP:
                    next_states.add(LOOKUP[t])
    GRAPH.append(tuple(sorted(next_states)))
assert all(i in GRAPH[j] for i, ns in enumerate(GRAPH) for j in ns)
assert sum(map(len, GRAPH)) == 40320


def shells(start):
    distances = [-1] * len(STATES)
    distances[start] = 0
    pending = deque([start])
    while pending:
        u = pending.popleft()
        for v in GRAPH[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                pending.append(v)
    assert min(distances) == 0  # Connectivity
    return Counter(distances)


COUNTS = Counter()
for p, s in sorted(REPS.items()):
    rep = LOOKUP[s]
    shell = shells(rep)
    ecc = max(shell)
    degree = len(GRAPH[rep])
    for d, ct in shell.items():
        COUNTS[d] += expected[p] * ct
    print('orbit=%s count=%s degree=%s eccentricity=%s representative=%s' %
          (''.join(map(str, p)), expected[p], degree, ecc,
           ''.join(map(str, s))))

assert sum(COUNTS.values()) == 5760 ** 2
assert all(COUNTS[d] % 2 == 0 for d in range(1, 17))
print('proper3=%d dynamic3=%d proper4=%d dynamic4=%d' %
      (len(P3)*6, len(D3)*6, len(P4)*24 + len(P3)*24, len(STATES)))
print('edges=%d radius=%d diameter=%d' %
      (sum(map(len, GRAPH)) // 2, 15, max(COUNTS)))
print('unordered_distance_histogram=' + ' '.join(
    '%d:%d' % (d, COUNTS[d] // 2) for d in range(1, 17)))
