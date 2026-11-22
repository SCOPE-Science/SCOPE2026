#!/usr/bin/env python3
"""Independent direct trace enumeration for valley-permutation assignment queries."""
from itertools import combinations, permutations


def valley_hypotheses(n):
    words = []
    for bits in range(1 << (n-1)):
        left = [v for v in range(n, 1, -1) if bits & (1 << (v-2))]
        right = [v for v in range(2, n+1) if not bits & (1 << (v-2))]
        words.append(tuple(left + [1] + right))
    assert len(set(words)) == 1 << (n-1)
    return words


def direct_face_counts(n):
    words = valley_hypotheses(n)
    qs = [(i, v) for i in range(n) for v in range(1, n+1)
          if any(w[i] == v for w in words) and any(w[i] != v for w in words)]
    bitsets = []
    for i, v in qs:
        hit = sum(1 << j for j, w in enumerate(words) if w[i] == v)
        bitsets.append(hit)
    full = (1 << len(words)) - 1
    levels = [((), (full,))]
    counts = [1]
    for d in range(1, n+1):
        following = []
        for support, atoms in levels:
            for j in range(support[-1]+1 if support else 0, len(qs)):
                m = bitsets[j]
                newatoms = []
                for atom in atoms:
                    yes = atom & m
                    no = atom & (full ^ m)
                    if not yes or not no:
                        break
                    newatoms.extend((yes, no))
                else:
                    following.append((support+(j,), tuple(newatoms)))
        if not following:
            break
        counts.append(len(following))
        levels = following
    return counts, qs


def verify(nmax=8):
    expected = {
        1:[1],2:[1,4],3:[1,8,4],4:[1,14,22],
        5:[1,21,68,16],6:[1,30,150,116],
        7:[1,40,294,440,64],8:[1,52,510,1238,560]
    }
    for n in range(1, nmax+1):
        words = valley_hypotheses(n)
        if n <= 7:
            # Independent generation: brute-force all permutations and test pattern avoidance.
            brute = []
            for w in permutations(range(1,n+1)):
                if all(not (w[j] > w[i] and w[j] > w[k])
                       for i in range(n) for j in range(i+1,n) for k in range(j+1,n)):
                    brute.append(w)
            assert set(words) == set(brute), (n,len(words),len(brute))
        counts, queries = direct_face_counts(n)
        assert counts == expected[n], (n, counts, expected[n])
        print(f'n={n} hypotheses={len(words)} candidate_queries={len(queries)} shattering={counts}')
    print('VALLEY_ASSIGNMENT_TRACE_ENUMERATION_PASS')


if __name__ == '__main__':
    verify()
