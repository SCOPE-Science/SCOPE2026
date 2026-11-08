"""Finite corroboration for q-Kneser two-extension and pencil obstruction.
No external dependencies; exhaustive cases are labelled in the output.
"""
from itertools import combinations, product
from collections import Counter


def rank(rows, q):
    if not rows:
        return 0
    a = [list(v) for v in rows]
    m, n = len(a), len(a[0])
    p = 0
    for c in range(n):
        t = next((i for i in range(p, m) if a[i][c] % q), None)
        if t is None:
            continue
        a[p], a[t] = a[t], a[p]
        inv = pow(a[p][c] % q, -1, q)
        a[p] = [(v * inv) % q for v in a[p]]
        for i in range(m):
            if i != p and a[i][c]:
                z = a[i][c]
                a[i] = [(x - z*y) % q for x, y in zip(a[i], a[p])]
        p += 1
        if p == m:
            break
    return p


def all_subspaces(n, k, q):
    assert q in (2, 3), 'Finite checker supports prime fields two and three only.'
    all_vectors = list(product(range(q), repeat=n))
    zero = (0,)*n
    out = set()
    for basis in combinations([v for v in all_vectors if v != zero], k):
        if rank(basis, q) != k:
            continue
        span = frozenset(tuple(sum(c*v[j] for c,v in zip(cs,basis)) % q
                               for j in range(n))
                         for cs in product(range(q), repeat=k))
        out.add(span)
    return list(out)


def all_pair_profiles(S, q, limit_pairs=None):
    N = len(S)
    # adjacency means trivial intersection; pairwise distinct handled below.
    adj = [0]*N
    for i in range(N):
        for j in range(i):
            if len(S[i] & S[j]) == 1:
                adj[i] |= 1<<j
                adj[j] |= 1<<i
    full = (1<<N)-1
    cases = list(combinations(range(N), 2))
    if limit_pairs is not None:
        # Deterministic, distributed sample; not reported as exhaustive.
        cases = cases[::max(1, len(cases)//limit_pairs)][:limit_pairs]
    for a,b in cases:
        omit = full ^ ((1<<a)|(1<<b))
        for s in range(4):
            good = omit
            good &= adj[a] if s&1 else (full ^ adj[a])
            good &= adj[b] if s&2 else (full ^ adj[b])
            assert good, (N, a, b, s)
    return adj, len(cases)


def find_pencil_obstruction(S,q,adj):
    # Search a common (k-1)-subspace pencil, with k=2 for the exhaustive cases.
    for a in range(len(S)):
        for b in range(len(S)):
            if b == a: continue
            line = S[a]&S[b]
            if len(line)!=q: continue
            for c in range(len(S)):
                if c in (a,b):continue
                if S[a]&S[c] != line or S[b]&S[c] != line: continue
                union_rank = rank(tuple(S[a] | S[b] | S[c]), q)
                if union_rank != 3:continue
                exists = any((adj[a]>>d)&1 and not (adj[b]>>d)&1 and not (adj[c]>>d)&1
                             for d in range(len(S)) if d not in (a,b,c))
                assert not exists, (a,b,c)
                return (a,b,c)
    raise AssertionError('No pencil obstruction found')


def main():
    for n,k,q,cut in [(4,2,2,None),(5,2,2,None),(4,2,3,None),(6,3,2,40)]:
        S=all_subspaces(n,k,q)
        adj, checked = all_pair_profiles(S,q,cut)
        if k==2:
            pencil=find_pencil_obstruction(S,q,adj)
        else:
            # k=3, q=2: three 3-spaces over a common 2-space in a 4-space.
            B=[]
            for z in (2,3,2+3):
                basis=[tuple(int(i==v) for i in range(n)) for v in (0,1)]
                third=[0]*n
                if z==5:third[2]=third[3]=1
                else:third[z]=1
                B.append(frozenset(tuple(sum(c*v[j] for c,v in zip(cs,basis+[tuple(third)]))%2
                                         for j in range(n)) for cs in product(range(2),repeat=3)))
            pencil=tuple(S.index(z) for z in B)
            a,b,c=pencil
            assert not any((adj[a]>>d)&1 and not (adj[b]>>d)&1 and not (adj[c]>>d)&1
                           for d in range(len(S)) if d not in pencil)
        assert all(not (adj[x]>>y)&1 for x,y in combinations(pencil,2))
        print('CASE',n,k,q,'subspaces',len(S),'pairs',checked,
              'exhaustive',cut is None, 'pencil_checked',True)
    print('Q_KNESER_FINITE_CHECKS_OK')

if __name__ == '__main__':
    main()
