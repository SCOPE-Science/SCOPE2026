"""Standalone exact enumeration of the ternary short-repeat-free Hamming graph.

Requires only Python 3 standard library. Tests every admissible word at each
length 4..16, builds every Hamming-one edge by changing coordinates, and
computes components without using the structural proof's core partition.
"""
from collections import Counter, deque


def admissible(w):
    return (all(a != b for a, b in zip(w, w[1:]))
            and all(not (w[i] == w[i+2] and w[i+1] == w[i+3])
                    for i in range(len(w)-3)))


def all_words(n):
    def extend(w):
        if len(w) == n:
            yield w
            return
        for a in range(3):
            w2 = w + (a,)
            if admissible(w2):
                yield from extend(w2)
    return list(extend(()))


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a+b
    return a


def expected(n):
    if n == 4:
        return Counter({'P3': 6})
    if n == 5:
        return Counter({'K1': 6, 'C4': 6})
    return Counter({'K1': 6*fib(n-6),
                    'K2': 12*fib(n-5),
                    'C4': 6*fib(n-4)})


def verify(n):
    vertex_list = all_words(n)
    vertices = set(vertex_list)
    assert len(vertex_list) == len(vertices)
    adj = {}
    for w in vertices:
        neighbors = set()
        for i in range(n):
            for replacement in range(3):
                if replacement == w[i]:
                    continue
                y = w[:i] + (replacement,) + w[i+1:]
                if y in vertices:
                    neighbors.add(y)
        adj[w] = neighbors
    assert all(v in adj[u] for v, neis in adj.items() for u in neis)
    unseen = set(vertices)
    counts = Counter()
    maximal_code_count_exp = 0
    independent_number = 0
    while unseen:
        v = unseen.pop()
        group = {v}
        queue = deque([v])
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if b not in group:
                    group.add(b)
                    unseen.remove(b)
                    queue.append(b)
        es = sum(len(adj[w]) for w in group)//2
        degree_seq = sorted(len(adj[w]) for w in group)
        shape = (len(group), es, tuple(degree_seq))
        family = {(1,0,(0,)):'K1', (2,1,(1,1)):'K2',
                  (4,4,(2,2,2,2)):'C4'}
        family[(3,2,(1,1,2))]='P3'
        assert shape in family, (n,shape)
        ty = family[shape]
        counts[ty] += 1
        if ty=='K1': independent_number += 1
        elif ty=='K2':
            independent_number += 1
            maximal_code_count_exp += 1
        elif ty=='C4':
            independent_number += 2
            maximal_code_count_exp += 1
        elif ty=='P3': independent_number += 2
    assert counts == expected(n),(n,counts,expected(n))
    if n >= 6:
        pred_alpha = 6*fib(n-6)+12*fib(n-5)+12*fib(n-4)
        pred_exp = 12*fib(n-5)+6*fib(n-4)
    elif n == 5:
        pred_alpha,pred_exp=18,6
    else:
        pred_alpha,pred_exp=12,0
    assert independent_number == pred_alpha
    assert maximal_code_count_exp == pred_exp
    print(f"n={n:2d} vertices={len(vertices):5d} "+
          f"components={dict(sorted(counts.items()))} "+
          f"alpha={independent_number} max_codes=2^{maximal_code_count_exp}")


if __name__ == '__main__':
    for length in range(4,17):
        verify(length)
    print('PASS: all admissible source words and all Hamming-one edges at n=4..16')
