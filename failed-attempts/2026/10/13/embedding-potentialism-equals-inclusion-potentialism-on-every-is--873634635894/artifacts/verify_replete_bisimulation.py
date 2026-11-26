from itertools import combinations, permutations

# Exact finite replay of the two local back/forth constructions for simple graphs.
# A graph is (n, edges) on domain range(n); edges are 2-subsets.

def all_graphs(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        yield frozenset(pairs[i] for i in range(len(pairs)) if (mask>>i)&1)

def edge(E,a,b):
    if a==b: return False
    return tuple(sorted((a,b))) in E

def is_embedding(EA,nA, EB,nB, f):
    # f tuple length nA with distinct target vertices.
    if len(set(f)) != nA: return False
    for a in range(nA):
        for b in range(nA):
            if edge(EA,a,b) != edge(EB,f[a],f[b]):
                return False
    return True

def permute_graph(E,p):
    return frozenset(tuple(sorted((p[a],p[b]))) for a,b in E)

def pullback_extension(M_edges, n, Np_edges, m, h, rho):
    # h: M -> N isomorphism on range(n); rho: N -> N' embedding into range(m).
    # Build M'' on D = old M-points 0..n-1 plus tagged complement as n..m-1,
    # with bijection j:D -> N' extending rho∘h.
    image=[rho[h[a]] for a in range(n)]
    rest=[y for y in range(m) if y not in image]
    assert len(rest)==m-n
    j=tuple(image+rest)
    inv={j[d]:d for d in range(m)}
    Mpp=frozenset(tuple(sorted((inv[a],inv[b]))) for a,b in Np_edges)
    return Mpp,j

checks=0

# Back direction: embedding on the right can be mirrored by inclusion on the left
# after replacing the target by an isomorphic copy containing the old left world.
for n in range(1,4):
    for M in all_graphs(n):
        for p in permutations(range(n)):
            N=permute_graph(M,p)
            h=p
            assert is_embedding(M,n,N,n,h); checks+=1
            for m in range(n,5):
                for Np in all_graphs(m):
                    for rho in permutations(range(m),n):
                        if not is_embedding(N,n,Np,m,rho):
                            continue
                        Mpp,j=pullback_extension(M,n,Np,m,h,rho)
                        # M is literally the induced subgraph of M'' on first n points.
                        for a in range(n):
                            for b in range(n):
                                assert edge(M,a,b)==edge(Mpp,a,b); checks+=1
                        # j is an isomorphism M'' -> N'.
                        assert is_embedding(Mpp,m,Np,m,j); checks+=1
                        assert len(set(j))==m; checks+=1
                        # Commutation on the old world: j(a)=rho(h(a)).
                        for a in range(n):
                            assert j[a]==rho[h[a]]; checks+=1

# Forth direction: an inclusion M⊆M' can be mirrored by the embedding i∘h^{-1}.
for n in range(1,4):
    for m in range(n,5):
        for Mp in all_graphs(m):
            M=frozenset(e for e in Mp if e[0]<n and e[1]<n)
            for p in permutations(range(n)):
                N=permute_graph(M,p)
                h=p
                # h=p maps M to N; rho = inclusion ∘ h^{-1} maps N to M'.
                hinv=[None]*n
                for a,b in enumerate(p):
                    hinv[b]=a
                rho=tuple(hinv)
                assert is_embedding(N,n,Mp,m,rho); checks+=1
                for a in range(n):
                    assert rho[h[a]]==a; checks+=1

print(f"VERIFY_OK {checks} exact assertions")
