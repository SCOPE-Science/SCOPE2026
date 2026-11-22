"""Independent enumeration of contiguous one- and two-factor observation fibers.

Usage: python3 check_direct.py
No optional dependencies. All alphabet symbols are labeled.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import comb, factorial


def predicted(r, s):
    buckets = Counter()
    for k in range(min(s, r-1) + 1):
        fiber_size = factorial(r-1) // factorial(r-1-k)
        number_of_profiles = factorial(s) * comb(s+1, k+1) // factorial(k)
        buckets[fiber_size] += number_of_profiles
    return buckets


def profile(word):
    return (tuple(sorted(Counter(word).items())),
            tuple(sorted(Counter(zip(word, word[1:])).items())))


def internal_chains(word):
    positions = [i for i, x in enumerate(word) if x == 0]
    return sum(positions[j+1] > positions[j] + 1
               for j in range(len(positions)-1))


def check(r, s):
    fibers = defaultdict(list)
    for word in set(permutations([0]*r + list(range(1, s+1)))):
        fibers[profile(word)].append(word)
    observed = Counter()
    for words in fibers.values():
        ks = {internal_chains(w) for w in words}
        assert len(ks) == 1, (r, s, 'inconsistent chain count', ks)
        k = next(iter(ks))
        expected_size = factorial(r-1) // factorial(r-1-k)
        assert len(words) == expected_size, (r, s, k, len(words), expected_size)
        observed[len(words)] += 1
    assert observed == predicted(r, s), (r, s, observed, predicted(r,s))
    assert sum(size*num for size,num in observed.items()) == factorial(r+s)//factorial(r)
    return len(fibers)


if __name__ == '__main__':
    cases = 0
    total = 0
    for r in range(1, 8):
        for s in range(0, 7):
            if r+s > 10:
                continue
            total += check(r,s)
            cases += 1
    print('Direct one/two-factor fiber enumeration: PASS')
    print('Parameter cases:', cases)
    print('Total counted observation classes across cases:', total)
