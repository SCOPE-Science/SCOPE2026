import itertools

def graph_from_facets(facets, n):
    adj = [set() for _ in range(n)]
    for F in facets:
        for a, b in itertools.combinations(sorted(F), 2):
            adj[a].add(b); adj[b].add(a)
    return adj

def linear_strand(adj):
    n = len(adj)
    beta = [0]*(n+1)
    nbr = [0]*n
    for i in range(n):
        m = 0
        for j in adj[i]:
            m |= (1 << j)
        nbr[i] = m
    for mask in range(1, 1 << n):
        # count components of induced subgraph via bit ops
        rem = mask; comp = 0
        while rem:
            comp += 1
            v = (rem & (-rem)).bit_length() - 1
            stack = (1 << v); seen = 0
            while stack:
                u = (stack & (-stack)).bit_length() - 1
                stack ^= (1 << u)
                if (seen >> u) & 1: continue
                seen |= (1 << u)
                stack |= (nbr[u] & mask & ~seen)
            rem &= ~seen
        if comp > 1:
            beta[bin(mask).count('1') - 1] += (comp - 1)
    return beta

def gamma_facets(d=4):
    # two cross-polytope boundaries glued along all-+ facet
    # A verts: (c,0/1); B verts: (c,0/1); identify B(c,0)=A(c,0)
    def idxA(c, s): return c*2+s
    nA = 2*d
    facetsA = [frozenset(idxA(c, s[c]) for c in range(d)) for s in itertools.product([0,1], repeat=d)]
    FA = frozenset(idxA(c, 0) for c in range(d))
    facetsA = [F for F in facetsA if F != FA]
    # B: new ids for s-side only; 0-side identified with A
    base = 2*d
    bmap = {}
    for c in range(d):
        bmap[(c,0)] = idxA(c,0)
    nb = {}
    for c in range(d):
        nb[(c,1)] = base; base += 1
        bmap[(c,1)] = base-1
    n = base
    FB = frozenset(bmap[(c,0)] for c in range(d))
    facetsB = []
    for s in itertools.product([0,1], repeat=d):
        F = frozenset(bmap[(c, s[c])] for c in range(d))
        if F != FB: facetsB.append(F)
    return facetsA + facetsB, n

def check_pseudo(facets, d):
    from collections import Counter
    c = Counter()
    for F in facets:
        for v in F:
            c[F - {v}] += 1
    return all(v == 2 for v in c.values()), len(c)

def formula(d, k, i):
    from math import comb
    def C(n, r):
        if r < 0 or r > n: return 0
        return comb(n, r)
    return (k-2)*C(d*(k-1), i+1) - (k-1)*C(d*(k-2), i+1) + d*(k-1)*C(d*(k-2), i-1)

if __name__ == '__main__':
    facets, n = gamma_facets(4)
    print('n =', n, 'nfacets =', len(facets))
    ok, nridge = check_pseudo(facets, 4)
    print('pseudomanifold (all ridges x2):', ok, 'nridges:', nridge)
    adj = graph_from_facets(facets, n)
    ne = sum(len(a) for a in adj)//2
    print('f1 =', ne, 'missing =', n*(n-1)//2 - ne)
    beta = linear_strand(adj)
    print('Gamma strand:', beta)
    print('formula     :', [formula(4, 3, i) for i in range(n+1)])
