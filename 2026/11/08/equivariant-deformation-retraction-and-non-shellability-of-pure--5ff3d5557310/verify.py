"""Exhaustive tests of pure strong discrete-Morse complexes of complete multipartite graphs.
The graph is its unfilled one-dimensional simplicial complex. No external packages.
Finite checks supplement, rather than replace, the uniform proof.
"""
from itertools import permutations, combinations
from collections import Counter
from math import comb, factorial


def build_parts(sizes):
    assert len(sizes)>=2 and all(s>0 for s in sizes)
    who=[]
    for i,s in enumerate(sizes):who += [i]*s
    return who


def all_gradients(sizes):
    owner=build_parts(sizes); L=len(owner); records=set()
    for order in permutations(range(L)):
        earlier=[]; pairs=[]
        for v in order:
            neighbors=[u for u in earlier if owner[u]!=owner[v]]
            if len(neighbors)==1:
                pairs.append((v,neighbors[0]))
            earlier.append(v)
        records.add(frozenset(pairs))
    return records


def formula_facets(sizes):
    owner=build_parts(sizes); n=max(sizes); part=sizes.index(n)
    C=[i for i,v in enumerate(owner) if v==part]
    R=[i for i,v in enumerate(owner) if v!=part]
    facets=set()
    for r in R:
        facets.add(frozenset((c,r) for c in C))
        for c in C:
            facets.add(frozenset([(r,c)]+[(d,r) for d in C if d!=c]))
    return facets,R,C


def face_set(facets):
    faces={frozenset()}
    for F in facets:
        for k in range(1,len(F)+1):
            faces.update(frozenset(s) for s in combinations(F,k))
    return faces


def gf2_ranks(faces,n):
    chains=[[frozenset()]]+[[f for f in faces if len(f)==k] for k in range(1,n+1)]
    ranks=[]
    for k in range(1,n+1):
        index={F:i for i,F in enumerate(chains[k-1])}
        pivots={}
        for F in chains[k]:
            v=0
            for e in F:v ^= 1<<index[F.difference((e,))]
            while v:
                j=v.bit_length()-1
                if j in pivots:v^=pivots[j]
                else:pivots[j]=v;break
        ranks.append(len(pivots))
    b=[len(chains[k])-ranks[k-1]-(ranks[k] if k<n else 0) for k in range(1,n+1)]
    return b


def check(sizes):
    assert sizes[-1]>max(sizes[:-1]) and sizes[-1]>=2
    n=sizes[-1]; M=sum(sizes[:-1]); N=sum(sizes)
    seen=all_gradients(sizes)
    top=max(map(len,seen)); actual={F for F in seen if len(F)==top}
    expected,R,C=formula_facets(sizes)
    assert top==n
    assert actual==expected,(sizes,'facets disagree',len(actual),len(expected),actual^expected)
    assert len(actual)==M*(n+1)
    faces=face_set(actual); counts=Counter(map(len,faces))
    assert all(counts[k]==M*(comb(n,k)+n*comb(n-1,k-1)) for k in range(1,n+1))
    # Every nonempty face has exactly one distinguished outside-part target/source.
    for f in faces:
        if not f:continue
        pivots={v if v in R else w for v,w in f}
        assert len(pivots)==1 and next(iter(pivots)) in R
    # Verify facet invariance under generators of the entire graph automorphism group:
    # transpositions within each part and exchanges of any equal-sized parts.
    groups=[];st=0
    for s in sizes:groups.append(list(range(st,st+s)));st+=s
    maps=[]
    for g in groups:
        for u,v in zip(g,g[1:]):
            sigma=list(range(N));sigma[u],sigma[v]=sigma[v],sigma[u];maps.append(sigma)
    for i in range(len(groups)):
        for j in range(i+1,len(groups)):
            if len(groups[i])==len(groups[j]):
                sigma=list(range(N))
                for u,v in zip(groups[i],groups[j]):sigma[u],sigma[v]=v,u
                maps.append(sigma)
    for sigma in maps:
        moved={frozenset((sigma[v],sigma[w]) for v,w in F) for F in actual}
        assert moved==actual
    betti=gf2_ranks(faces,n)
    assert betti==[M-1]+[0]*(n-1),(sizes,betti)
    print('PASS parts='+repr(sizes)+' orders='+str(factorial(N))+' distinct_gradients='+str(len(seen))+
          ' facets='+str(len(actual))+' f='+repr(tuple(counts[k] for k in range(1,n+1)))+
          ' reduced_F2_betti='+repr(tuple(betti)))


if __name__=='__main__':
    cases=[(1,2),(2,3),(2,4),(2,5),(3,4),
           (1,1,2),(1,1,3),(1,2,3),(1,2,4),
           (2,2,3),(2,2,4),(2,3,4),
           (1,1,1,2),(1,1,1,3),(1,1,2,3),(1,2,2,3)]
    for case in cases:check(case)
    print('ALL_VERIFY_OK')
