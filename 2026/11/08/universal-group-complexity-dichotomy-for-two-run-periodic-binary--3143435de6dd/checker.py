"""Independent finite checks for a two-run periodic-word group-complexity theorem.

This code tests finite cases; the infinite quantifiers follow from the proof.
Python 3.10+ standard library only.
"""
from itertools import permutations


def factors(a, b, n):
    p = '0' * a + '1' * b
    return set((p * ((n + len(p) - 1) // len(p) + 2))[i:i+n]
               for i in range(len(p)))


def suffix_orbits(F, m):
    # Two binary strings are equivalent under S_{m+1,...,n} iff
    # their fixed prefixes coincide and their suffixes have equal Parikh vectors.
    return len({(s[:m], s[m:].count('1')) for s in F})


def group_complexity(F, G):
    # Canonicalize the whole permutation orbit of each factor, not only F.
    return len({min(''.join(s[g[i]] for i in range(len(s))) for g in G)
                for s in F})


def all_s3_subgroups():
    P = tuple(permutations(range(3)))
    identity = (0, 1, 2)
    groups = set()
    for mask in range(1 << len(P)):
        H = frozenset(P[i] for i in range(len(P)) if mask & (1 << i))
        if identity not in H:
            continue
        if all(tuple(g[h[i]] for i in range(3)) in H for g in H for h in H):
            groups.add(H)
    assert len(groups) == 6
    return groups


def positive_branch():
    cases = 0
    for r in range(2, 31):
        for a, b in ((1, r-1), (r-1, 1)):
            for n in range(1, 4*r + 1):
                F = factors(a, b, n)
                expected_factor = n+1 if n < r else r
                expected_abelian = 2 if n < r or n % r else 1
                assert len(F) == expected_factor, (a,b,n,'factor')
                assert len({s.count('1') for s in F}) == expected_abelian, (a,b,n,'abelian')
                seen = set()
                for m in range(n+1):
                    if n < r:
                        expected = m + 2 if m < n else n + 1
                    elif m < r:
                        expected = m + 1 + int(m < n % r)
                    else:
                        expected = r
                    actual = suffix_orbits(F, m)
                    assert actual == expected, (a,b,n,m,actual,expected)
                    seen.add(actual)
                    cases += 1
                assert seen == set(range(expected_abelian, expected_factor+1)), (a,b,n)
    return cases


def negative_branch():
    groups = all_s3_subgroups()
    cases = 0
    for a in range(2, 20):
        for b in range(2, 20):
            F = factors(a,b,3)
            expected_F = {'001','011','110','100'}
            if a >= 3:
                expected_F.add('000')
            if b >= 3:
                expected_F.add('111')
            assert F == expected_F, (a,b,F)
            vals = {group_complexity(F,G) for G in groups}
            assert vals == {len(F)-2, len(F)}, (a,b,vals)
            assert len({s.count('1') for s in F}) == len(F)-2
            cases += 1
    return cases, len(groups)


if __name__ == '__main__':
    a=positive_branch()
    b,g=negative_branch()
    print(f'PASS {a} direct suffix-orbit comparisons; {b} full S3 subgroup spectra; {g} subgroups')
