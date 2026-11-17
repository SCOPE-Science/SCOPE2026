"""Direct exhaustive checks for exact binary weight-three non-overlapping codes.

Run: python verify.py
No third-party libraries required.
"""
from itertools import combinations
from math import comb


def weight_three_words(n):
    for p in combinations(range(n), 3):
        w = ['0'] * n
        for i in p:
            w[i] = '1'
        yield ''.join(w)


def compatible(u, v):
    n = len(u)
    return all(u[:k] != v[-k:] and v[:k] != u[-k:]
               for k in range(1, n))


def internal_pair(w):
    p = [i for i, c in enumerate(w) if c == '1']
    assert p[0] == 0 and p[-1] < len(w)-1 and len(p) == 3
    return (p[1], p[2])


def rectangular_family(n, t):
    return [''.join('1' if x in (0, i, j) else '0' for x in range(n))
            for i in range(1,t+1)
            for j in range(i+1,n-t)]


def upper(n):
    return ((2*n-3)**2)//24


def optimum_indices(n):
    cand = list(range(1, (n-2)//2+1))
    vals = [(t, t*(2*n-3-3*t)//2) for t in cand]
    v = max(x for _,x in vals)
    return [t for t,x in vals if x==v]


def maximum_clique(adj):
    # Compatible graph; exact branch & bound on bitsets.
    N = len(adj)
    best = 0
    def rec(candidates, size):
        nonlocal best
        if candidates == 0:
            best = max(best, size)
            return
        if size + candidates.bit_count() <= best:
            return
        while candidates and size + candidates.bit_count() > best:
            b = candidates & -candidates
            v = b.bit_length()-1
            candidates ^= b
            rec(candidates & adj[v], size+1)
    rec((1<<N)-1,0)
    return best


def count_cliques_of_size(adj, target):
    count = 0
    def rec(candidates, size):
        nonlocal count
        if size == target:
            count += 1
            return
        if size + candidates.bit_count() < target:
            return
        while candidates and size + candidates.bit_count() >= target:
            bit = candidates & -candidates
            v = bit.bit_length()-1
            candidates ^= bit
            rec(candidates & adj[v], size+1)
    rec((1<<len(adj))-1, 0)
    return count


def check():
    # Directly check the universal pair criterion, including self-overlaps.
    comparisons = 0
    for n in range(4, 19):
        words = [''.join('1' if x in (0,i,j) else '0' for x in range(n))
                 for i,j in combinations(range(1,n-1),2)
                 if i+j<n]
        pairs = [internal_pair(w) for w in words]
        for a,u in enumerate(words):
            i,j = pairs[a]
            for b,v in enumerate(words):
                k,l = pairs[b]
                expected = max(i,k)+max(j,l) < n
                actual = compatible(u,v)
                assert actual == expected, (n,u,v,expected,actual)
                comparisons += 1
        assert max(t*(2*n-3-3*t)//2 for t in optimum_indices(n)) == upper(n)
        for t in optimum_indices(n):
            C=rectangular_family(n,t)
            assert len(C)==upper(n)
            assert all(compatible(u,v) for u in C for v in C)

    # Separate exact clique search for whole non-overlapping universe
    # at small n; self-bordered words are excluded.
    exact = []
    for n in range(4, 10):
        W = list(weight_three_words(n))
        W = [w for w in W if compatible(w,w)]
        adj = []
        for i,w in enumerate(W):
            bits = 0
            for j,v in enumerate(W):
                if j != i and compatible(w,v):
                    bits |= 1 << j
            adj.append(bits)
        m = maximum_clique(adj)
        assert m == upper(n), (n,m,upper(n))
        num_max = count_cliques_of_size(adj, m)
        expected_max = 4 if n%3==0 else 2
        assert num_max == expected_max, (n,num_max,expected_max)
        exact.append((n,m,len(W),num_max))

    # Directly compare whole-word self-bifix-free test with symbol-boundary lemma.
    for n in range(4,13):
        for w in weight_three_words(n):
            if compatible(w,w):
                assert w[0]!=w[-1]

    print('VERIFY_OK')
    print('ordered_cross_checks=',comparisons)
    print('maximum_clique_checks=',exact)
    print('capacity_n4_through18=',[upper(n) for n in range(4,19)])
    print('n_mod3_equal0_tie_check=', [(n,optimum_indices(n)) for n in (6,9,12,15,18)])


if __name__=='__main__':
    check()
