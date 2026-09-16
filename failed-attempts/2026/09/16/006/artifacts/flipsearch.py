import itertools, random

def stacked_chain(d, t):
    # chain of t cross-polytope boundaries; returns facets(list of frozenset), colors(list), n
    # summand 0: verts (0,c,s). glue facet F={(c,0)} to next summand's {(c,0)} etc.
    colors = {}
    facets = []
    def v(s, c, sd):
        return (s, c, sd)
    # assign ids
    ids = {}
    n = [0]
    def get(key):
        if key not in ids:
            ids[key] = n[0]; n[0] += 1
        return ids[key]
    # summand s uses side-keys: left facet shared with s-1 (except s=0), right facet shared with s+1 (except last)
    # left facet of summand s (s>=1): reuse right facet ids of summand s-1
    right_ids = None
    for s in range(t):
        if s == 0:
            left = {c: get(('L', 0, c)) for c in range(d)}  # fresh left (all-0 side)
            # all-1 side fresh for now
            side1 = {c: get(('M', 0, c, 1)) for c in range(d)}
        else:
            left = right_ids
            side1 = {c: get(('M', s, c, 1)) for c in range(d)}
        # all 2^d transversals except the actual glue facets
        skip = set()
        if s >= 1:
            skip.add(frozenset(left[c] for c in range(d)))
        if s < t - 1:
            skip.add(frozenset(side1[c] for c in range(d)))
        for choice in itertools.product([0, 1], repeat=d):
            F = frozenset((left[c] if choice[c] == 0 else side1[c]) for c in range(d))
            if F in skip:
                continue
            facets.append(F)
        right_ids = side1
    N = n[0]
    colors = [None]*N
    # color by original color c: recover from key
    for key, i in ids.items():
        if key[0] == 'L':
            colors[i] = key[2]
        else:  # 'M'
            colors[i] = key[2]
    return facets, colors, N

def faceset_of(facets):
    S = set()
    for F in facets:
        F = list(F)
        for r in range(len(F)+1):
            for sub in itertools.combinations(F, r):
                S.add(frozenset(sub))
    return S

def link_of(facets, face):
    return [F - face for F in facets if face <= F]

def graph_edges(facets):
    E = set()
    for F in facets:
        for a, b in itertools.combinations(sorted(F), 2):
            E.add((a, b))
    return E

def linear_strand_nbr(nbr, n):
    beta = [0]*(n+1)
    for mask in range(1, 1 << n):
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

def strand_of_facets(facets, n):
    nbr = [0]*n
    for F in facets:
        for a, b in itertools.combinations(sorted(F), 2):
            nbr[a] |= (1 << b); nbr[b] |= (1 << a)
    return linear_strand_nbr(nbr, n)

def find_moves(facets, faces):
    fwd = []  # (A, B): remove edge A, add triangle B
    rev = []  # (B, A): add edge A={a1,a2}, remove triangle B
    # forward: edges with triangle link
    E = graph_edges(facets)
    for (x, y) in E:
        A = frozenset((x, y))
        L = link_of(facets, A)
        if len(L) == 3 and all(len(l) == 2 for l in L):
            U = set().union(*L)
            if len(U) == 3:
                B = frozenset(U)
                if B not in faces:
                    fwd.append((A, B))
    # reverse: triangles with 2-apex link
    tris = set()
    for F in facets:
        for t in itertools.combinations(sorted(F), 3):
            tris.add(frozenset(t))
    for B in tris:
        L = link_of(facets, B)
        if len(L) == 2 and all(len(l) == 1 for l in L):
            a = next(iter(L[0])); b = next(iter(L[1]))
            A = frozenset((a, b))
            if A not in faces:
                rev.append((B, A))
    return fwd, rev

def apply_fwd(facets, A, B):
    a1, a2 = sorted(A); b = sorted(B)
    out = []
    for F in facets:
        if A <= F:
            continue
        out.append(F)
    out.append(frozenset((a1,)) | B)
    out.append(frozenset((a2,)) | B)
    return out

def apply_rev(facets, B, A):
    a1, a2 = sorted(A); b = sorted(B)
    e1, e2, e3 = [frozenset(p) for p in itertools.combinations(b, 2)]
    out = []
    for F in facets:
        if B <= F:
            continue
        out.append(F)
    out.append(A | e1); out.append(A | e2); out.append(A | e3)
    return out

def check_valid(facets, d, colors):
    from collections import Counter
    c = Counter()
    for F in facets:
        if len(F) != d: return False, 'facet size'
        for v in F:
            c[F - frozenset((v,))] += 1
    if not all(v == 2 for v in c.values()):
        return False, 'ridge counts'
    # balanced
    for F in facets:
        if sorted(colors[v] for v in F) != list(range(d)):
            return False, 'balanced'
    return True, 'ok'

if __name__ == '__main__':
    random.seed(0)
    d = 4
    facets, colors, n = stacked_chain(d, 2)
    print('n =', n, 'nfacets =', len(facets))
    print('valid:', check_valid(facets, d, colors))
    faces = faceset_of(facets)
    fwd, rev = find_moves(facets, faces)
    print('fwd moves (should be 0 by LBT):', len(fwd))
    print('rev moves:', len(rev))
    beta0 = strand_of_facets(facets, n)
    print('Gamma strand:', beta0)
