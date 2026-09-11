import itertools

# Fano plane canonical: 7 points 0..6, 7 lines
FANO = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
# Automorphism group order 168; distinct copies on a labeled 7-set = 30.
# Precompute the 30 patterns as frozensets of triple-index positions? Instead brute force per 7-set via permutations with dedup.

def all_triples(n):
    return list(itertools.combinations(range(n),3))

def fano_copies_on_set(S):
    """Yield frozensets of triples (as sorted tuples) forming a Fano plane on vertex set S (tuple of 7)."""
    # All bijections from {0..6} to S modulo Aut: just iterate over all 5040 perms and dedup via set
    seen=set()
    S=list(S)
    for p in itertools.permutations(range(7)):
        edges=frozenset(tuple(sorted((S[p[a]],S[p[b]],S[p[c]]))) for (a,b,c) in FANO)
        if edges not in seen:
            seen.add(edges)
            yield edges

# Precompute canonical 30 patterns on (0..6) once
CANON30=set()
for p in itertools.permutations(range(7)):
    e=frozenset(tuple(sorted((p[a],p[b],p[c]))) for (a,b,c) in FANO)
    CANON30.add(e)
CANON30=list(CANON30)
print(f"canon patterns: {len(CANON30)}")

def is_fano_free(n, eset):
    eset=set(eset)
    if len(eset)<7:
        return True, None
    # map triple->present for quick count per 7-set? brute force
    for S in itertools.combinations(range(n),7):
        Sset=set(S)
        # quick prune: count edges inside S
        c=sum(1 for e in eset if e[0] in Sset and e[1] in Sset and e[2] in Sset)
        if c<7:
            continue
        inside=set(e for e in eset if e[0] in Sset and e[1] in Sset and e[2] in Sset)
        # check each canon pattern relabeled: need mapping S->0..6. Build index map
        idx={v:i for i,v in enumerate(S)}
        rel=set(tuple(sorted((idx[a],idx[b],idx[c]))) for (a,b,c) in inside)
        for pat in CANON30:
            if pat.issubset(rel):
                return False, S
    return True, None

def bipartite_edge_set(n, U):
    U=set(U)
    es=set()
    for e in itertools.combinations(range(n),3):
        a=sum(1 for v in e if v in U)
        if a in (1,2):  # meets both U and complement
            es.add(e)
    return es

def b_n(n):
    best=0
    for k in range(n+1):
        U=set(range(k))
        best=max(best,len(bipartite_edge_set(n,U)))
    return best

def min_edit_distance(n, H):
    H=set(H)
    h=len(H)
    best=None; bestU=None
    # fix 0 in U
    for mask in range(1<<(n-1)):
        U={0}|{i+1 for i in range(n-1) if (mask>>i)&1}
        B=bipartite_edge_set(n,U)
        d=len(H.symmetric_difference(B))
        if best is None or d<best:
            best=d; bestU=set(U)
    return best, bestU

def H_unbalanced_internal(n, nx, nx1, internal='bip'):
    # X = 0..nx-1, Y = rest; X1 = 0..nx1-1, X2 = rest of X
    X=set(range(nx)); X1=set(range(nx1)) if nx1 is not None else set(); X2=X-X1
    Y=set(range(nx,n))
    H=set()
    for e in itertools.combinations(range(n),3):
        sX=sum(1 for v in e if v in X)
        if sX in (1,2):
            H.add(e)
        elif sX==3:
            if internal=='bip':
                a=sum(1 for v in e if v in X1)
                if a in (1,2):
                    H.add(e)
            elif internal=='clique':
                H.add(e)
            elif internal=='empty':
                pass
            elif internal=='star':
                # all triples in X containing vertex 0
                if 0 in e:
                    H.add(e)
    return H

if __name__=="__main__":
    for n in [7,8,9]:
        print("b",n,b_n(n))
