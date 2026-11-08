"""Finite cross-checks for a uniform prism-neighborhood simplicial collapse.

Run with Python 3.9+: python verify.py
Only standard-library packages are used. The theorem has a separate symbolic proof.
"""
from itertools import combinations
from collections import Counter


def c4_free(n, edges):
    adj = [set() for _ in range(n)]
    for x, y in edges:
        assert x != y and 0 <= x < n and 0 <= y < n
        adj[x].add(y)
        adj[y].add(x)
    return all(len(adj[x] & adj[y]) <= 1
               for x in range(n) for y in range(x + 1, n))


def all_faces_of_neighborhood(n, edges):
    """Vertices (v,a) use integer code 2*v+a."""
    adj = [set() for _ in range(n)]
    for x,y in edges:
        adj[x].add(y); adj[y].add(x)
    facets = []
    for v in range(n):
        for a in range(2):
            facets.append(frozenset([2*v+1-a] + [2*w+a for w in adj[v]]))
    faces = {frozenset()}
    for N in facets:
        seq = sorted(N)
        for k in range(1, len(seq)+1):
            faces.update(frozenset(S) for S in combinations(seq,k))
    return adj,faces


def target_graph_faces(n, edges):
    f={frozenset()}
    for v in range(n):
        for a in range(2):
            f.add(frozenset((2*v+a,)))
    for x,y in edges:
        for a in range(2):
            f.add(frozenset((2*x+a,2*y+1-a)))
    return f


def check_collapse(n, edges):
    assert c4_free(n,edges), "the theorem assumes no four-cycles"
    adj, faces = all_faces_of_neighborhood(n,edges)
    start_count = len(faces)
    pairs=[]
    for v in range(n):
        for a in range(2):
            neighbors=sorted(2*w+a for w in adj[v])
            apex=2*v+1-a
            for s in range(2,len(neighbors)+1):
                for raw in combinations(neighbors,s):
                    low=frozenset(raw)
                    high=low | {apex}
                    pairs.append((low,high))
    pairs.sort(key=lambda pq:(-len(pq[0]),tuple(sorted(pq[0])),tuple(sorted(pq[1]))))
    assert len(pairs)==len(set(pairs))
    for lower,upper in pairs:
        assert lower in faces and upper in faces
        cofaces=[lower | {j} for j in range(2*n) if j not in lower and (lower | {j}) in faces]
        assert cofaces == [upper], (n,edges,lower,cofaces,upper)
        assert not any(upper | {j} in faces for j in range(2*n) if j not in upper)
        faces.remove(lower);faces.remove(upper)
    target=target_graph_faces(n,edges)
    assert faces==target, (n,edges,len(faces),len(target))
    expected_pairs=2*sum((2**len(adj[v])-len(adj[v])-1) for v in range(n))
    assert len(pairs)==expected_pairs
    assert start_count==len(target)+2*expected_pairs
    return start_count,len(pairs),len(target)


def check_negative_square():
    e=[(0,1),(1,2),(2,3),(0,3)]
    assert not c4_free(4,e)
    adj,faces=all_faces_of_neighborhood(4,e)
    target=target_graph_faces(4,e)
    assert len(faces)>len(target)
    # Cube graph has open-neighborhood complex equal to two tetrahedral boundaries.
    assert Counter(len(f) for f in faces if f)=={1:8,2:12,3:8}
    assert Counter(len(f) for f in target if f)=={1:8,2:8}
    return len(faces)-1,len(target)-1


def edges_cycle(n):
    return sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)})

def edges_complete(n):
    return list(combinations(range(n),2))

def edges_star(n):
    return [(0,i) for i in range(1,n)]

def edges_petersen():
    # Vertices 0..4 and 5..9; outer 5-cycle, inner pentagram, spokes.
    return sorted({tuple(sorted(e)) for i in range(5)
                   for e in ((i,(i+1)%5),(i,5+i),(5+i,5+(i+2)%5))})


def main():
    checked=0
    by_n=Counter()
    max_f=0
    for n in range(1,6):
        possible=list(combinations(range(n),2))
        for bits in range(1<<len(possible)):
            edges=[e for j,e in enumerate(possible) if bits & (1<<j)]
            if c4_free(n,edges):
                a,b,c=check_collapse(n,edges)
                checked+=1;by_n[n]+=1;max_f=max(max_f,a)
    # Nontrivial natural examples at higher degrees and larger order.
    specials={"triangle":(3,edges_complete(3)),
              "five_cycle":(5,edges_cycle(5)),
              "seven_cycle":(7,edges_cycle(7)),
              "star_six":(6,edges_star(6)),
              "petersen":(10,edges_petersen())}
    special_results={}
    for name,(n,edges) in specials.items():
        special_results[name]=check_collapse(n,edges)
    print("C4_FREE_EXHAUSTIVE_UP_TO_5", checked, dict(sorted(by_n.items())))
    print("MAX_ORIGINAL_FACE_COUNT",max_f)
    for name,v in special_results.items():
        print("EXAMPLE",name,"faces_including_empty",v[0],"collapse_pairs",v[1],"residual_faces_including_empty",v[2])
    print("SQUARE_NEGATIVE_CONTROL",check_negative_square())
    print("ALL_PRISM_NEIGHBORHOOD_CHECKS_PASS")

if __name__ == "__main__":
    main()
