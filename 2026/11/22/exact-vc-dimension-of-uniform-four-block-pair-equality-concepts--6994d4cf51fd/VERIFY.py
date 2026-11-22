#!/usr/bin/env python3
"""Independent finite checks of the uniform-four-block shattering theorem.
Run: python3 VERIFY_uniform4.py
"""
from itertools import combinations


def queries(m):
    return [(4*i, 4*i+k) for i in range(m) for k in range(1, 4 if i < m-2 else 3)]


def partition_for_labels(m, bits):
    """Construct a four-block partition for a prescribed query trace."""
    Q = queries(m)
    values = dict(zip(Q, bits))
    core, neg, frees = [], [], []
    for i in range(m):
        positive = [4*i]
        negative = []
        for k in range(1, 4 if i < m-2 else 3):
            v = 4*i+k
            (positive if values[(4*i, v)] else negative).append(v)
        core.append(positive)
        neg.append(negative)
        if i >= m-2:
            frees.append(4*i+3)
    caps = [4-len(x) for x in core]
    tokens = [(x, i) for i in range(m) for x in neg[i]] + [(x, -1) for x in frees]
    assert sum(caps) == len(tokens)
    # bipartite assignment, each unit vacancy is a slot
    slots = [i for i, c in enumerate(caps) for _ in range(c)]
    owner = [-1] * len(slots)
    def augment(t, seen):
        x, forbidden = tokens[t]
        for k, b in enumerate(slots):
            if b == forbidden or k in seen:
                continue
            seen.add(k)
            if owner[k] == -1 or augment(owner[k], seen):
                owner[k] = t
                return True
        return False
    ok = all(augment(t, set()) for t in range(len(tokens)))
    if ok:
        blocks = [set(g) for g in core]
        for k, t in enumerate(owner):
            blocks[slots[k]].add(tokens[t][0])
    else:
        failures = [i for i in range(m) if 2*caps[i] > sum(caps)+(1 if i >= m-2 else 0)]
        assert len(failures) == 1, (m, caps, failures)
        i = failures[0]
        blocks = [set(core[j]) for j in range(m) if j != i and j < m-2]
        if i < m-2:
            assert len(neg[i]) == 3 and all(caps[j]==0 for j in range(m-2) if j!=i)
            assert caps[-2:]==[1,1]
            blocks += [set(core[m-2])|{4*i}, set(core[m-1])|{neg[i][0]},
                       {neg[i][1],neg[i][2],frees[0],frees[1]}]
        else:
            j = m-2 if i == m-1 else m-1
            assert len(neg[i]) == 2 and all(caps[k]==0 for k in range(m-2))
            assert caps[j]==1
            blocks += [set(core[j])|{4*i}, {neg[i][0],neg[i][1],frees[0],frees[1]}]
    assert len(blocks) == m and all(len(B)==4 for B in blocks)
    assert set.union(*blocks) == set(range(4*m))
    assert sum(len(B) for B in blocks)==4*m
    location={x:i for i,B in enumerate(blocks) for x in B}
    assert all((location[u]==location[v])==bool(answer) for (u,v),answer in zip(Q,bits))
    return tuple(tuple(sorted(B)) for B in blocks)


def partitions(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    u=vertices[0]
    for rest in combinations(vertices[1:],3):
        rem = tuple(x for x in vertices[1:] if x not in rest)
        for tail in partitions(rem):
            yield ((u,)+rest,)+tail


def trace(partition, Q):
    which={x:i for i,B in enumerate(partition) for x in B}
    return tuple(int(which[u]==which[v]) for u,v in Q)


def main():
    for m in range(2,6):
        Q=queries(m)
        encountered=set()
        for label in range(1<<len(Q)):
            bits=tuple((label>>j)&1 for j in range(len(Q)))
            p=partition_for_labels(m,bits)
            encountered.add(trace(p,Q))
        assert len(encountered)==1<<len(Q)
        print('CONSTRUCTIVE_ALL_LABELINGS_PASS',m,len(Q),len(encountered))
    for m in (2,3):
        Q=queries(m)
        actual={trace(p,Q) for p in partitions(range(4*m))}
        assert len(actual)==1<<len(Q)
        print('INDEPENDENT_PARTITION_ENUMERATION_PASS',m,len(actual))
    # For two four-blocks, every candidate >4 queries in a common positive
    # hypothesis fails some alternative trace. This is exhaustive for size 5.
    m=2
    all_pairs=list(combinations(range(8),2))
    family=list(partitions(range(8)))
    masks=[]
    for P in family:
        loc={x:i for i,B in enumerate(P) for x in B}
        masks.append(sum(1<<j for j,(u,v) in enumerate(all_pairs) if loc[u]==loc[v]))
    candidates=set()
    for mask in masks:
        indices=[j for j in range(len(all_pairs)) if mask>>j&1]
        for S in combinations(indices,5):
            candidates.add(sum(1<<j for j in S))
    for S in candidates:
        observed={m0&S for m0 in masks}
        assert len(observed)<32
    print('EXHAUSTIVE_FIVE_QUERY_UPPER_OBSTRUCTION_PASS',len(candidates))
    print('UNIFORM_FOUR_PARTITION_SHATTERING_PASS')


if __name__ == '__main__':
    main()
