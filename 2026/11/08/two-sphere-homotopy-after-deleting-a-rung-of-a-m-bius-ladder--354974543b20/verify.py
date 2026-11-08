"""Independent graph and fold checks for one-rung-deficient Möbius ladders.

No external packages are required. A fold (witness, removed) is valid when
N(witness) is a subset of N(removed) in the current simple graph.
"""
from collections import defaultdict


def ladder(n):
    v = set(range(2*n))
    edges = set()
    for i in v:
        for j in ((i+1) % (2*n), (i+n) % (2*n)):
            if {i, j} != {0, n}:
                edges.add(frozenset((i, j)))
    return v, edges


def remove(v, edges, deleted):
    v.difference_update(deleted)
    edges.difference_update(e for e in list(edges) if not e <= v)


def neighborhood(v, edges, x):
    return {next(iter(e-{x})) for e in edges if x in e}


def fold(v, edges, witness, removed):
    assert witness in v and removed in v and witness != removed
    assert neighborhood(v,edges,witness) <= neighborhood(v,edges,removed), (witness, removed, len(v))
    remove(v,edges,{removed})


def l0_certificate(k):
    n=4*k+1
    v,e=ladder(n)
    remove(v,e,{0,1,2*n-1})
    pairs=[(2*n-2,n-3)]
    for j in range(k-1):
        pairs.extend(((4*j+2,n+4*j+3),(n+4*j+4,4*j+5)))
    for w,d in pairs:fold(v,e,w,d)
    assert len(v)==6*k and len(e)==6*k
    assert all(len(neighborhood(v,e,x))==2 for x in v)
    # Connectivity verifies the residue graph is a single cycle.
    seen={next(iter(v))}; todo=list(seen)
    while todo:
        for t in neighborhood(v,e,todo.pop()):
            if t not in seen:seen.add(t);todo.append(t)
    assert seen==v
    return len(pairs)


def d1_certificate(k):
    n=4*k+2;v,e=ladder(n);remove(v,e,{1})
    pairs=[(0,n-1),(n,n+2)]
    for j in range(k-1):
        pairs.extend(((4*j+2,4*j+4),(4*j+2,n+4*j+3),
                      (n+4*j+4,4*j+5),(n+4*j+4,n+4*j+6)))
    pairs.extend(((4*k-2,4*k),(4*k-2,n+4*k-1),(2*n-2,0)))
    for w,d in pairs:fold(v,e,w,d)
    expected={x for j in range(n//2) for x in (4*j+2,4*j+3)}
    expectede={frozenset((4*j+2,4*j+3)) for j in range(n//2)}
    assert v==expected and e==expectede,(n,v^expected)
    return len(pairs)


def l1_certificate(k):
    n=4*k+2;v,e=ladder(n)
    remove(v,e,{1,*neighborhood(v,e,1)})
    pairs=[(n+2,3),(n+2,n+4)]
    for j in range(k-1):
        pairs.extend(((4*j+4,4*j+6),(4*j+4,n+4*j+5),
                      (n+4*j+6,4*j+7),(n+4*j+6,n+4*j+8)))
    pairs.extend(((4*k,4*k+2),(4*k,n+4*k+1)))
    for w,d in pairs:fold(v,e,w,d)
    expected={x for j in range(1,n//2) for x in (4*j,4*j+1)}
    expectede={frozenset((4*j,4*j+1)) for j in range(1,n//2)}
    assert v==expected and e==expectede,(n,v^expected)
    return len(pairs)


def d0_check(k):
    n=4*k+1;v,e=ladder(n);remove(v,e,{0})
    folds=0
    while not any(not neighborhood(v,e,x) for x in v):
        options=[(w,t) for w in sorted(v) for t in sorted(v)
                 if w!=t and neighborhood(v,e,w)<=neighborhood(v,e,t)]
        assert options, n
        w,t=options[0];fold(v,e,w,t);folds+=1
    return folds


def homology_mod2(n):
    vertices,edges=ladder(n)
    adj=[set() for _ in vertices]
    for e in edges:
        a,b=tuple(e);adj[a].add(b);adj[b].add(a)
    F=defaultdict(list)
    def search(mask,chosen):
        F[chosen.bit_count()-1].append(chosen)
        while mask:
            bit=mask & -mask;mask-=bit
            u=bit.bit_length()-1
            search(mask & ~sum(1<<t for t in adj[u]),chosen|bit)
    search((1<<(2*n))-1,0)
    rank={}
    for d in sorted(F):
        if d<1:continue
        rows={mask:i for i,mask in enumerate(F[d-1])}
        pivot={}
        for f in F[d]:
            vec=0; s=f
            while s:
                bit=s&-s;s-=bit
                vec^=1<<rows[f^bit]
            while vec:
                p=vec.bit_length()-1
                if p in pivot:vec^=pivot[p]
                else:pivot[p]=vec;break
        rank[d]=len(pivot)
    hom={d:len(F[d])-rank.get(d,0)-rank.get(d+1,0)-(d==0) for d in F if d>=0}
    return {d:r for d,r in hom.items() if r},sum(map(len,F.values()))


def main():
    total_folds=0;tests=0
    for k in range(1,21):
        total_folds+=l0_certificate(k)+d1_certificate(k)+l1_certificate(k)
        tests+=3
    for k in range(1,11):
        total_folds+=d0_check(k);tests+=1
    total_faces=0
    for n in (5,6,9,10):
        got,faces=homology_mod2(n)
        expected={2*((n-1)//4):2}
        assert got==expected,(n,got,expected)
        total_faces+=faces
    print('ALL_VERIFY_OK symbolic_fold_cases=%d valid_folds=%d homology_cases=4 face_instances=%d' % (tests,total_folds,total_faces))

if __name__=='__main__':main()
