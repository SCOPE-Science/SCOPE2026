"""Reproduce an exact factor-trigram fiber census for two nonzero letters.

Run with Python 3.8 or later: python verify.py
All computations use exact integers. No third-party packages.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb


def trigram_nonzero_signature(gaps, a, b):
    left, middle, right = gaps
    word = (0,) * left + (a,) + (0,) * middle + (b,) + (0,) * right
    return tuple(sorted((pattern, count) for pattern, count in
                        Counter(tuple(word[j:j+3]) for j in range(len(word)-2)).items()
                        if pattern != (0, 0, 0)))


def lift_count(gaps, n):
    number_large = gaps.count(2)
    assert number_large >= 1
    extra = n - 2 - sum(gaps)
    assert extra >= 0
    return comb(extra + number_large - 1, number_large - 1)


def template_fibers(pairs, n):
    buckets = defaultdict(int)
    for a, b in pairs:
        for triple in product(range(3), repeat=3):
            if 2 not in triple:
                continue
            buckets[trigram_nonzero_signature(triple, a, b)] += lift_count(triple, n)
    return Counter(buckets.values())


def expected_same(n):
    return Counter([1]*10 + [2] + [n-6]*3 + [n-5]*3 + [comb(n-6, 2)])


def expected_distinct(n):
    return Counter([1]*24 + [n-6]*6 + [n-5]*6 + [(n-6)*(n-7)])


def direct_fibers(n, q):
    buckets = defaultdict(int)
    for i, j in combinations(range(n), 2):
        for a, b in product(range(1, q), repeat=2):
            word = [0]*n
            word[i], word[j] = a, b
            sig = tuple(sorted(Counter(tuple(word[t:t+3])
                                       for t in range(n-2)).items()))
            buckets[sig] += 1
    return Counter(buckets.values())


def predicted_fibers(n, q):
    r = q-1
    ans = Counter()
    for size, multiplicity in expected_same(n).items():
        ans[size] += r*multiplicity
    for size, multiplicity in expected_distinct(n).items():
        ans[size] += comb(r,2)*multiplicity
    return ans


def check():
    # Every possible nonzero trigram signature is represented by a template
    # of three zero gaps, each capped at two. The spectrum classes consist
    # of 19 possible templates for equal letters and 38 for different letters.
    for n in (8, 9, 10):
        assert template_fibers([(1,1)],n) == expected_same(n), n
        assert template_fibers([(1,2),(2,1)],n) == expected_distinct(n), n
    # Each class has a fiber-size polynomial of degree <= 2 in n. Equality
    # at three integer n proves each polynomial identity for every n >= 8;
    # the template signature partition itself does not depend on n.
    for n in range(8, 31):
        assert template_fibers([(1,1)],n) == expected_same(n), n
        assert template_fibers([(1,2),(2,1)],n) == expected_distinct(n), n
        for q in range(2,7):
            r = q-1
            groups = predicted_fibers(n,q)
            assert sum(groups.values()) == 18*r + 37*comb(r,2)
            assert sum(k*v for k,v in groups.items()) == comb(n,2)*r*r
    # Sharpness: at length seven the all-two gap template is unavailable.
    # Exactly 17 repeated-marker and 36 distinct-marker signatures remain.
    for q in range(2,7):
        r=q-1
        assert sum(direct_fibers(7,q).values()) == 17*r + 36*comb(r,2)
    words_checked=0
    for q in range(2,6):
        for n in range(8,16):
            assert direct_fibers(n,q) == predicted_fibers(n,q), (n,q)
            words_checked += comb(n,2)*(q-1)**2
    assert len({trigram_nonzero_signature(t,1,1)
                for t in product(range(3),repeat=3) if 2 in t}) == 18
    assert len({trigram_nonzero_signature(t,a,b)
                for a,b in ((1,2),(2,1))
                for t in product(range(3),repeat=3) if 2 in t}) == 37
    print('VERIFY_OK templates=57 direct_words=%d alphabet_sizes=4 n=8..15' % words_checked)


if __name__ == '__main__':
    check()
