"""Exhaustive all-shortest quaternary cyclic-palindrome-cover enumeration."""
import csv
import itertools
from collections import Counter
from functools import lru_cache
from pathlib import Path

ALPHABET = '0123'
WORDS = tuple(a+b+b+a for a in ALPHABET for b in ALPHABET)
N = len(WORDS)
FULL = (1 << N) - 1

def overlap_cost(a, b):
    return next(4-k for k in range(3, -1, -1)
                if k == 0 or WORDS[a][4-k:] == WORDS[b][:k])

C = tuple(tuple(overlap_cost(i, j) for j in range(N)) for i in range(N))

@lru_cache(None)
def remainder(mask, last):
    if mask == FULL:
        return C[last][0]
    return min(C[last][j] + remainder(mask | 1 << j, j)
               for j in range(1, N) if not mask >> j & 1)

def rotate_to_constant(word):
    k = word.index('0000')
    return word[k:] + word[:k]

minimum = remainder(1, 0)
assert minimum == 44
all_covers = set()
number_of_minimum_tours = 0

def enumerate_tours(mask, last, path):
    global number_of_minimum_tours
    if mask == FULL:
        number_of_minimum_tours += 1
        circle = ''.join(WORDS[path[(i + 1) % N]][-C[path[i]][path[(i + 1) % N]]:]
                         for i in range(N))
        assert len(circle) == minimum
        circle = rotate_to_constant(circle)
        factors = Counter(''.join(circle[(k+j) % minimum] for j in range(4))
                          for k in range(minimum))
        assert all(factors[w] == 1 for w in WORDS), 'A selected palindrome repeated'
        all_covers.add(circle)
        return
    need = remainder(mask, last)
    for nxt in range(1, N):
        if not mask >> nxt & 1 and C[last][nxt] + remainder(mask | 1 << nxt, nxt) == need:
            enumerate_tours(mask | 1 << nxt, nxt, path + (nxt,))

enumerate_tours(1, 0, (0,))
assert number_of_minimum_tours == len(all_covers) == 5472
perms = tuple(str.maketrans(ALPHABET, ''.join(t))
              for t in itertools.permutations(ALPHABET))
unvisited = set(all_covers)
classes = []
while unvisited:
    representative = min(unvisited)
    images = {rotate_to_constant(representative.translate(t)) for t in perms}
    images |= {rotate_to_constant(s[::-1]) for s in tuple(images)}
    assert images <= all_covers
    unvisited.difference_update(images)
    classes.append((representative, len(images)))
assert len(classes) == 124
assert Counter(size for _, size in classes) == {48:105, 24:17, 12:2}
expected = set()
with (Path(__file__).parent / 'representatives.csv').open(newline='', encoding='utf-8') as file:
    for row in csv.DictReader(file):
        expected.add((row['canonical_word'], int(row['orbit_size'])))
assert set(classes) == expected
print('ENUMERATION_OK', minimum, number_of_minimum_tours, len(all_covers),
      len(classes), dict(Counter(s for _, s in classes)))
