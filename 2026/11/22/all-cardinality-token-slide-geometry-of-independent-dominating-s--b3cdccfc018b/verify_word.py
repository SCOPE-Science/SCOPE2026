from itertools import combinations
from math import comb

def word(n, k, sign, gaps):
    cells = [None] * n
    col = 0
    for j in range(k):
        cells[col] = (sign + j) % 2
        col += 1
        if j in gaps:
            col += 1
    assert col == n
    return tuple(cells)

def is_independent_dominating(cells):
    n = len(cells)
    for j in range(n):
        if j and cells[j] is not None and cells[j-1] == cells[j]:
            return False
        if cells[j] is None:
            if j in (0, n-1):
                return False
            if set((cells[j-1],cells[j+1])) != {0,1}:
                return False
    return True

def slides(cells):
    n = len(cells)
    results = set()
    for j, value in enumerate(cells):
        if value is None:
            continue
        candidates = [(j, 1-value)] + [(q, value) for q in (j-1,j+1) if 0<=q<n]
        for loc, newval in candidates:
            if cells[loc] is not None:
                continue
            other = list(cells)
            other[j] = None
            other[loc] = newval
            if is_independent_dominating(other):
                results.add(tuple(other))
    return results

for n in range(2,19):
    total=0
    for k in range((n+2)//2,n+1):
        z=n-k
        expected=2*comb(k-1,z)
        configurations={word(n,k,s,g) for s in range(2) for g in combinations(range(k-1),z)}
        assert len(configurations)==expected
        assert all(is_independent_dominating(c) for c in configurations)
        total+=len(configurations)
        edges=set()
        for config in configurations:
            for new in slides(config):
                assert new in configurations
                edges.add(tuple(sorted((config,new), key=lambda a:repr(a))))
        expected_edges=2*(k-2)*comb(k-3,z-1) if 1<=z<=k-2 else 0
        assert len(edges)==expected_edges,(n,k,len(edges),expected_edges)
        # Exhaustive adjacency equivalence with swapping adjacent gap bits.
        for sign in range(2):
            for gaps in combinations(range(k-1),z):
                a=word(n,k,sign,gaps)
                predicted=set()
                bits=[int(j in gaps) for j in range(k-1)]
                for j in range(k-2):
                    if bits[j]!=bits[j+1]:
                        nxt=bits.copy();nxt[j],nxt[j+1]=nxt[j+1],nxt[j]
                        predicted.add(word(n,k,sign,tuple(i for i,x in enumerate(nxt) if x)))
                assert predicted==slides(a),(n,k,sign,gaps)
    print('n=%d configurations=%d expected_Fibonacci_covered' % (n,total))
print('WORD_BIJECTION_AND_MOVES_PASS')
