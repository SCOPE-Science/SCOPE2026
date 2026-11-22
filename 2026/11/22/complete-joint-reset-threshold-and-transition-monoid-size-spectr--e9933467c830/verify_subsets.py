"""Independent subset-search and transformation-closure census, Python 3 stdlib."""
from collections import Counter, defaultdict, deque
from itertools import permutations
from pathlib import Path
import csv

N = 4
MAPS = [tuple((code >> (2*i)) & 3 for i in range(N)) for code in range(256)]
ENCODE = lambda f: sum(value << (2*i) for i, value in enumerate(f))
IDENTITY = ENCODE(tuple(range(N)))

# Different presentation from the transformation-depth checker: materialize tuples.
PRODUCT = [[ENCODE(tuple(g[f[i]] for i in range(N))) for g in MAPS]
           for f in MAPS]
IMAGES = [[sum({1 << f[i] for i in range(N) if (mask >> i) & 1})
           for mask in range(16)] for f in MAPS]


def monoid_size(a, b):
    seen = {IDENTITY}
    queue = [IDENTITY]
    for f in queue:
        for g in (a, b):
            h = PRODUCT[f][g]
            if h not in seen:
                seen.add(h)
                queue.append(h)
    return len(queue)


def shortest_reset(a, b):
    queue = deque([(15, 0)])
    seen = {15}
    while queue:
        mask, distance = queue.popleft()
        if mask.bit_count() == 1:
            return distance
        for g in (a, b):
            following = IMAGES[g][mask]
            if following not in seen:
                seen.add(following)
                queue.append((following, distance+1))
    return -1


def permute_map(code, permutation):
    inverse = [permutation.index(i) for i in range(N)]
    f = MAPS[code]
    return ENCODE(tuple(permutation[f[inverse[i]]] for i in range(N)))


def orbit(a, b):
    pairs = set()
    for p in permutations(range(N)):
        x, y = permute_map(a, p), permute_map(b, p)
        pairs.add((x, y))
        pairs.add((y, x))
    return pairs


def main():
    spectrum = Counter()
    slow_pairs = defaultdict(set)
    for a in range(256):
        for b in range(256):
            size = monoid_size(a, b)
            distance = shortest_reset(a, b)
            spectrum[(distance, size)] += 1
            if distance == 9:
                slow_pairs[size].add((a, b))
    with Path("joint_spectrum.csv").open(newline="") as fd:
        reader = csv.DictReader(fd)
        expected = {}
        for row in reader:
            key = (int(row["reset_length"]), int(row["monoid_size"]))
            assert key not in expected
            expected[key] = int(row["count"])
    assert spectrum == expected
    assert sum(spectrum.values()) == 65536 and len(spectrum) == 179
    assert {size:len(pairs) for size,pairs in slow_pairs.items()} == {128:48,145:48}
    assert slow_pairs[128] == orbit(30,36)
    assert slow_pairs[145] == orbit(6,156)
    # Check a 176-element monoid at reset threshold eight.
    assert spectrum[(8,176)] == 96
    assert shortest_reset(6,147) == 8 and monoid_size(6,147) == 176
    print("VERIFY_SUBSETS_OK: independent histogram and two 48-element extreme orbits")


if __name__ == "__main__":
    main()
