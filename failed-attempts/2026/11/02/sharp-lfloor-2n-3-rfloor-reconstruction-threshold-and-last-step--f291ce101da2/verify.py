"""Reproducibility tests for three-marker circular substring spectra.

No external packages are needed. Run with Python 3.8 or newer.
"""
from collections import Counter, defaultdict
from itertools import combinations


def canonical_gaps(gaps):
    a, b, c = gaps
    return min((a, b, c), (b, c, a), (c, a, b))


def gap_necklaces(n):
    return sorted({canonical_gaps((a, b, n-a-b))
                   for a in range(1, n-1) for b in range(1, n-a)})


def encode_cyclic_kmers(bits, k):
    n = len(bits)
    return tuple(sorted(Counter(tuple(bits[(i+j) % n] for j in range(k))
                                for i in range(n)).items()))


def gap_profile(gaps, k):
    n = sum(gaps)
    a, b, _ = gaps
    bits = [0] * n
    bits[0] = bits[a] = bits[a+b] = 1
    return encode_cyclic_kmers(bits, k)


def predicted_ambiguous_gaps(n):
    m, r = divmod(n, 3)
    if r == 0:
        return [(m-1, m, m+1)]
    if r == 1:
        ans = [(m-1, m, m+2)]
        if m >= 3:
            ans.append((m-2, m+1, m+2))
        return ans
    return [(m-1, m+1, m+2)]


def test_gap_necklaces():
    for n in range(6, 81):
        k = 2*n//3
        groups_before = defaultdict(list)
        groups_at = defaultdict(list)
        for t in gap_necklaces(n):
            groups_before[gap_profile(t, k-1)].append(t)
            groups_at[gap_profile(t, k)].append(t)
        assert all(len(v) == 1 for v in groups_at.values()), n
        ambiguous = [v for v in groups_before.values() if len(v) > 1]
        assert all(len(v) == 2 for v in ambiguous), n
        # Every predicted ambiguity consists of the two different orders
        # of three distinct circular gaps, with identical multiset spectra.
        actual = sorted({tuple(sorted(v[0])) for v in ambiguous})
        expected = sorted(predicted_ambiguous_gaps(n))
        assert actual == expected, (n, actual, expected)
        for pair in ambiguous:
            assert pair[0] != pair[1]
            assert sorted(pair[0]) == sorted(pair[1])
    print('gap necklaces n=6..80: all thresholds and boundary fiber classes agree')


def test_independent_marked_words():
    # Independent enumeration: choose all positions of the three ones,
    # then canonicalize all n rotations of the marked binary word.
    for n in range(6, 18):
        k = 2*n//3
        distinct = {}
        for positions in combinations(range(n), 3):
            word = [int(j in positions) for j in range(n)]
            key = min(tuple(word[i:] + word[:i]) for i in range(n))
            distinct[key] = word
        for read_len, expected_largest in ((k-1, 2), (k, 1)):
            seen = defaultdict(set)
            for word in distinct.values():
                key = min(tuple(word[i:] + word[:i]) for i in range(n))
                seen[encode_cyclic_kmers(word, read_len)].add(key)
            assert max(map(len, seen.values())) == expected_largest, (n, read_len)
            if read_len == k-1:
                expected = len(predicted_ambiguous_gaps(n))
                assert sum(len(v)==2 for v in seen.values()) == expected
            else:
                assert len(seen) == len(distinct)
    print('independent marked-word census n=6..17: all boundary cases agree')


def test_no_three_read_formula():
    # Independently verify no-three classification and the factor counts.
    for n in range(6, 38):
        for t in gap_necklaces(n):
            a, b, c = t
            for k in range(2, min(n, 2*n//3+1)):
                p = Counter(dict(gap_profile(t, k)))
                three = sum(freq for word, freq in p.items() if sum(word)==3)
                assert (three==0) == (max(t)<=n-k), (n,t,k,three)
                if three:
                    continue
                for d in range(1,k):
                    word = tuple([1]+[0]*(d-1)+[1]+[0]*(k-d-1))
                    assert p[word] == t.count(d), (n,t,k,d,p[word])
                for j in range(k):
                    word = tuple([0]*j+[1]+[0]*(k-j-1))
                    expected = 3-sum(g<=j for g in t)-sum(g<=k-j-1 for g in t)
                    assert p[word] == expected, (n,t,k,j,p[word],expected)
                assert p[(0,)*k] == sum(max(g-k,0) for g in t)
    print('independent word-frequency identities n=6..37: agree')


if __name__ == '__main__':
    test_gap_necklaces()
    test_independent_marked_words()
    test_no_three_read_formula()
    print('ALL TESTS PASSED')
