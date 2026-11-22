#!/usr/bin/env python3
"""Independent finite checks of scale-two Rips complexes of honeycomb subgraphs."""
import collections
import itertools
import random


def honeycomb(m, n):
    # A finite rectangular coordinate window in the infinite hexagonal lattice.
    vertices = [('B',i,j) for i in range(m+1) for j in range(n+1)] + [('W',i,j) for i in range(m+1) for j in range(n+1)]
    idx = {v:k for k,v in enumerate(vertices)}
    edges = set()
    for i in range(m+1):
        for j in range(n+1):
            u = idx[('B',i,j)]
            for x,y in ((i,j),(i-1,j),(i,j-1)):
                if ('W',x,y) in idx:
                    v=idx[('W',x,y)]
                    edges.add(tuple(sorted((u,v))))
    return len(vertices), edges


def connected_component(num, edges):
    adj=[set() for _ in range(num)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    seen=set(); groups=[]
    for a in range(num):
        if a in seen:continue
        todo=[a];seen.add(a); group={a}
        while todo:
            v=todo.pop()
            for w in adj[v]-seen:
                seen.add(w);group.add(w);todo.append(w)
        groups.append(group)
    keep=max(groups,key=lambda g:(len(g),-min(g)))
    remap={v:i for i,v in enumerate(sorted(keep))}
    return len(keep),{tuple(sorted((remap[u],remap[v]))) for u,v in edges if u in keep and v in keep}


def bfs_distance(num,edges):
    adj=[set() for _ in range(num)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    dd=[]
    for x in range(num):
        d={x:0};q=collections.deque([x])
        while q:
            y=q.popleft()
            for z in adj[y]:
                if z not in d:d[z]=d[y]+1;q.append(z)
        dd.append(d)
    return adj,dd


def hexagons(adj):
    n=len(adj)
    cycles=set()
    for s in range(n):
        stack=[(s,(s,))]
        while stack:
            v,path=stack.pop()
            if len(path)==6:
                if s in adj[v]:
                    cyc=path
                    if s==min(cyc):
                        a=cyc; b=(cyc[0],)+tuple(reversed(cyc[1:]))
                        cycles.add(min(a,b))
                continue
            for z in adj[v]:
                if z not in path and z>s:stack.append((z,path+(z,)))
    return sorted(cycles)


def rips_faces(num,dist):
    neighbors=[{j for j in dist[i] if j!=i and dist[i][j]<=2} for i in range(num)]
    sets={1:{(i,) for i in range(num)}}
    layer=sets[1]
    while True:
        new=set()
        for face in layer:
            for x in range(face[-1]+1,num):
                if all(x in neighbors[y] for y in face):new.add(face+(x,))
        if not new:break
        sets[len(next(iter(new)))]=new
        layer=new
    return sets


def gf2_rank(vectors):
    piv={}
    for v in vectors:
        while v:
            j=v.bit_length()-1
            if j not in piv:piv[j]=v;break
            v^=piv[j]
    return len(piv)


def betti_mod2(faces):
    dims=sorted(faces)
    ranks={}
    for k in dims[1:]:
        lower={f:i for i,f in enumerate(sorted(faces[k-1]))}
        cols=[]
        for f in faces[k]:
            bit=0
            for j in range(k):
                smaller=f[:j]+f[j+1:]
                bit^=1<<lower[smaller]
            cols.append(bit)
        ranks[k]=gf2_rank(cols)
    b={k-1:len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in dims}
    return b


def check(n,edges,homology=True):
    adj,dist=bfs_distance(n,edges)
    assert len(dist[0])==n
    six=hexagons(adj)
    fs=rips_faces(n,dist)
    assert max(fs)<=4,('unexpected dimension',max(fs))
    # All centered triangles, larger faces, plus exceptional alternating triples.
    centered=set()
    center_tetra=set()
    for v in range(n):
        N=sorted({v}|adj[v])
        for k in range(1,len(N)+1):
            centered.update(itertools.combinations(N,k))
        if len(N)==4:center_tetra.add(tuple(N))
    exceptional=set()
    for cyc in six:
        exceptional.add(tuple(sorted(cyc[0::2])))
        exceptional.add(tuple(sorted(cyc[1::2])))
    actual_exceptions=fs.get(3,set())-centered
    assert actual_exceptions==exceptional,('triangle discrepancy',n,len(actual_exceptions),len(exceptional))
    assert fs.get(4,set())==center_tetra,('tetrahedron discrepancy',n)
    assert all(len(fs.get(k,set()))==0 for k in range(5,max(fs)+1))
    b=len(edges)-n+1
    h=len(six)
    assert h<=b
    expected={0:1,1:b-h,2:h,3:0}
    if homology:
        got=betti_mod2(fs)
        assert all(got.get(i,0)==expected[i] for i in expected),(n,b,h,got,expected)
    return n,len(edges),h,b-h,tuple(len(fs.get(k,set())) for k in range(1,5))


def main():
    count=0
    examples=[]
    for m in range(1,5):
        for n in range(1,5):
            v,e=honeycomb(m,n)
            v,e=connected_component(v,e)
            ex=check(v,e)
            examples.append((m,n,ex))
            count+=1
    # A missing interior bond merges two hexagonal cells into a decagonal hole.
    N,E=honeycomb(3,3)
    N,E=connected_component(N,E)
    base_adj,_=bfs_distance(N,E)
    cycles=hexagons(base_adj)
    edge_count=collections.Counter(tuple(sorted((c[i],c[(i+1)%6]))) for c in cycles for i in range(6))
    shared=sorted(e for e,k in edge_count.items() if k==2)
    assert shared
    defect=check(N,E-{shared[0]})
    assert defect[2]==7 and defect[3]==1,defect
    print('INTERIOR_BOND_DEFECT',f'hexagons={defect[2]}',f'circles={defect[3]}')
    rnd=random.Random(20261116)
    checks=0
    for m,n in ((2,2),(3,3),(4,3)):
        N,E=honeycomb(m,n)
        for k in range(45):
            # First delete vertices, then delete edges, then take largest component.
            present={v for v in range(N) if rnd.random()>=.18}
            ee={(u,v) for u,v in E if u in present and v in present and rnd.random()>=.14}
            nn,ee=connected_component(N,ee)
            if nn>=2 and len(ee)>=nn-1:
                check(nn,ee)
                checks+=1
    print('RECTANGULAR_WINDOWS',count)
    print('RANDOM_DELETED_SUBGRAPHS',checks)
    for m,n,x in examples:
        print(f'WINDOW_{m}x{n}',f'vertices={x[0]}',f'edges={x[1]}',f'hexagons={x[2]}',f'circles={x[3]}',f'f_vector={x[4]}')
    print('HEXAGON_RIPS_CHECKS_OK')

if __name__=='__main__':main()
