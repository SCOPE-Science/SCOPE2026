"""Exact simplex-level tests for triangular-fiber pendant reduction.

Run: python verify_leaf_collapse.py
No external dependencies.
"""
from itertools import combinations
from random import Random


def full_complex(edges, n, colors=3):
    neighbors = [set() for _ in range(n * colors)]
    for v in range(n):
        for i in range(colors):
            for j in range(colors):
                if i != j:
                    neighbors[colors*v+i].add(colors*v+j)
    for u, v in edges:
        for i in range(colors):
            a, b = colors*u+i, colors*v+i
            neighbors[a].add(b); neighbors[b].add(a)
    faces = {frozenset()}
    for neigh in neighbors:
        for size in range(1, len(neigh)+1):
            for ss in combinations(sorted(neigh), size):
                faces.add(frozenset(ss))
    return faces


def validate_pair(faces, small, big):
    assert len(big) == len(small)+1
    assert small in faces and big in faces
    cofaces = [f for f in faces if small <= f]
    assert cofaces == [small, big] or set(cofaces) == {small,big}, (small,big,cofaces)
    faces.remove(small); faces.remove(big)


def check_one(edges, n, w):
    assert n >= 2
    edges = {tuple(sorted(e)) for e in edges}
    neigh = {j for e in edges for j in e if w in e and j!=w}
    assert len(neigh) == 1
    v = next(iter(neigh))
    old_edges = {e for e in edges if w not in e}
    faces = full_complex(edges, n)
    target = full_complex(old_edges, n)
    # The deleted color-fiber vertices have no neighborhoods in the target.
    target = {f for f in target if not any(x//3==w for x in f)}
    original_count = len(faces)
    pairs = 0
    X = [3*w+i for i in range(3)]
    Y = [3*v+i for i in range(3)]
    for i in range(3):
        other=[j for j in range(3) if j!=i]
        edge=frozenset([X[j] for j in other])
        triangle=edge | {Y[i]}
        validate_pair(faces,edge,triangle)
        pairs+=1
    other_neighbors = sorted(u for e in old_edges for u in e if v in e and u!=v)
    for i in range(3):
        distinguished=Y[(i+1)%3]
        base=[Y[j] for j in range(3) if j!=i and Y[j]!=distinguished]
        base += [3*u+i for u in other_neighbors]
        for size in range(len(base),-1,-1):
            for S in combinations(base,size):
                small=frozenset((X[i],)+S)
                big=small|{distinguished}
                validate_pair(faces,small,big)
                pairs+=1
    assert faces==target, (len(faces-target),len(target-faces))
    assert original_count-len(target)==2*pairs
    assert pairs==3+3*2**(len(other_neighbors)+1)
    return pairs,original_count


def homology_mod2(faces):
    by_degree={d:sorted((tuple(sorted(s)) for s in faces if len(s)==d+1)) for d in range(0, max(map(len,faces)))}
    dims={d:len(rows) for d,rows in by_degree.items()}
    ranks={0:0}
    for d in range(1,len(by_degree)):
        ix={f:i for i,f in enumerate(by_degree[d-1])}
        basis={}
        for s in by_degree[d]:
            z=0
            for t in combinations(s,d):z^=1<<ix[t]
            while z:
                bit=z.bit_length()-1
                if bit not in basis: basis[bit]=z;break
                z^=basis[bit]
        ranks[d]=len(basis)
    return {d:dims[d]-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in dims}


def main():
    rng=Random(164213)
    cases=0;total_pairs=0; max_faces=0
    # Arbitrary cores: paths, cycles, cliques, and random graphs, all with leaf attached.
    for n0 in range(1,9):
        for trial in range(40):
            E=set()
            if trial%4==0:
                E={(i,i+1) for i in range(n0-1)}
            elif trial%4==1:
                E={(i,(i+1)%n0) for i in range(n0) if i!=(i+1)%n0}
            elif trial%4==2:
                E={(i,j) for i in range(n0) for j in range(i+1,n0)}
            else:
                E={(i,j) for i in range(n0) for j in range(i+1,n0) if rng.random()<.45}
            E={tuple(sorted(e)) for e in E}
            v=rng.randrange(n0)
            E.add((v,n0))
            count,fc=check_one(E,n0+1,n0)
            cases+=1;total_pairs+=count;max_faces=max(max_faces,fc)
    print('leaf-collapse instances',cases)
    print('verified elementary pairs',total_pairs)
    print('largest entire complex face count',max_faces)
    # Identical complexes for multiple leaf removals on trees.
    for n in range(1,12):
        E={(i,i+1) for i in range(n-1)}
        h=homology_mod2(full_complex(E,n))
        assert h.get(1,0)==1 and all(v==0 for d,v in h.items() if d!=1), (n,h)
    print('path homology checks',11)
    # Four colors are genuinely different: simple path base already changes homology.
    v0=homology_mod2(full_complex(set(),1,colors=4))
    v1=homology_mod2(full_complex({(0,1)},2,colors=4))
    print('four-color base singleton Betti',v0)
    print('four-color base one edge Betti',v1)
    assert v0!=v1
    print('ALL CHECKS PASSED')
if __name__=='__main__':main()
