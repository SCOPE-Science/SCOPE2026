"""Direct graph-theoretic check of TOI-coalition partition counts.

Requires Python 3 standard library.  It checks every set partition for
all complete multipartite graphs whose sorted positive part-size profile
has at least three parts and at most nine vertices.
"""
from collections import Counter
from itertools import combinations_with_replacement


def set_partitions(n):
    blocks = []
    def rec(v):
        if v == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(v)
            yield from rec(v + 1)
            b.pop()
        blocks.append([v])
        yield from rec(v + 1)
        blocks.pop()
    yield from rec(0)


def expected(parts):
    r, n = len(parts), sum(parts)
    c2 = (1 << (n-1)) - 1 - sum((1 << v) - 1 for v in parts)
    c3 = sum(((1 << parts[i])-1) * ((1 << parts[j])-1)
             for i in range(r) for j in range(i+1,r)) - 2 * (r == 3)
    return {2:c2,3:c3}


def directly_test(parts):
    group = [i for i,s in enumerate(parts) for _ in range(s)]
    n = len(group)
    full = (1 << n)-1
    neighbors = [sum(1 << j for j in range(n) if group[j] != group[i]) for i in range(n)]
    def is_toids(mask):
        complement = full ^ mask
        # Independently test *all* total domination and outer-independence conditions.
        for vertex in range(n):
            if not neighbors[vertex] & mask:
                return False
            if complement & (1 << vertex) and neighbors[vertex] & complement:
                return False
        return True
    good = [is_toids(s) for s in range(1 << n)]
    result = Counter()
    for partition in set_partitions(n):
        if len(partition) == 1:
            continue
        masks = [sum(1 << v for v in block) for block in partition]
        if any(good[s] for s in masks):
            continue
        partnerships = [0] * len(masks)
        for i in range(len(masks)):
            for j in range(i+1,len(masks)):
                if good[masks[i] | masks[j]]:
                    partnerships[i] += 1
                    partnerships[j] += 1
        if not all(partnerships):
            continue
        result[len(masks)] += 1
        assert len(masks) <= 3
        if len(masks) == 3:
            contained = []
            for mask in masks:
                profile = {group[v] for v in range(n) if (mask >> v) & 1}
                contained.append(next(iter(profile)) if len(profile)==1 else None)
            pure = [p for p in contained if p is not None]
            assert len(set(pure)) >= 2
            if all(p is not None for p in contained):
                assert len(parts)==3 and sorted(contained)==[0,1,2]
                assert partnerships == [2,2,2]
            else:
                assert sorted(partnerships)==[1,1,2]
    assert dict(result) == {k:v for k,v in expected(parts).items() if v}
    return sum(result.values()),result[2],result[3]


def main():
    profiles=[]
    for r in range(3,10):
        for sizes in combinations_with_replacement(range(1,8),r):
            if sum(sizes) <= 9:
                profiles.append(sizes)
    all_counts = [0,0,0]
    for p in profiles:
        counts = directly_test(p)
        all_counts = [a+b for a,b in zip(all_counts, counts)]
    print('EXHAUSTIVE_MULTIPARTITE_PROFILES_OK',len(profiles),
          'partitions_accepted',all_counts[0], 'two_blocks',all_counts[1],
          'three_blocks',all_counts[2])
    # A large labelled unbalanced instance shows distinct families of partitions.
    p = (2,4,7,10)
    a,b = expected(p)[2],expected(p)[3]
    assert a == 2**(sum(p)-1)-1-sum(2**x-1 for x in p)
    assert b == sum((2**p[i]-1)*(2**p[j]-1)
                    for i in range(len(p)) for j in range(i+1,len(p)))
    print('LARGE_PROFILE_FORMULAS_OK',p,a,b)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
