#!/usr/bin/env python3
"""Exact combinatorial checks for the four-color multipath orbit complexes.
The symbolic orbit model is valid for every n by the partition argument in RESULT.md.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

COLORS=tuple(range(4))
ALLOWED_PAIRS={frozenset((0,3)),frozenset((1,2))}

def partitionings(S):
    if not S:
        yield ()
        return
    v,*rest=S
    for blocks in partitionings(rest):
        yield (frozenset((v,)),)+blocks
        for i,b in enumerate(blocks):
            yield blocks[:i]+(b|{v},)+blocks[i+1:]

def canon(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))

def valid(blocks):
    return all(len(b)==1 or b in ALLOWED_PAIRS for b in blocks) and not (
        len(blocks)==2 and all(len(b)==2 for b in blocks))

def allcells(n):
    out={d:[] for d in range(4)}
    for r in range(1,5):
        for S in combinations(COLORS,r):
            partitions={canon(p) for p in partitionings(S) if valid(p) and len(p)<=n}
            for p in sorted(partitions):
                out[r-1].append((S,p))
    return out

def restrict(cell,removed):
    S,p=cell
    return (tuple(x for x in S if x!=removed),canon([set(b)-{removed} for b in p if set(b)-{removed}]))

def model(n):
    cells=allcells(n)
    ids={d:{c:i for i,c in enumerate(cells[d])} for d in cells}
    boundary={}
    for d in (1,2,3):
        for i,cell in enumerate(cells[d]):
            boundary[d,i]={ (d-1,ids[d-1][restrict(cell,x)]) for x in cell[0] }
            assert len(boundary[d,i])==d+1
    return cells,boundary

def collapse(n,certificate):
    cells,boundary=model(n)
    alive={(d,i) for d in cells for i in range(len(cells[d]))}
    ids={d:{c:i for i,c in enumerate(cells[d])} for d in cells}
    for k,(f,p) in enumerate(certificate):
        low=(len(f[0])-1,ids[len(f[0])-1][f]); high=(len(p[0])-1,ids[len(p[0])-1][p])
        assert low in alive and high in alive and low in boundary[high],(k,low,high)
        # A free face cannot belong to any other surviving cell.
        supers=[q for q in alive if q[0]>low[0] and contains_face(low,q,cells)]
        assert supers==[high],(k,low,high,supers)
        alive.remove(low);alive.remove(high)
    return cells,alive

def contains_face(low,high,cells):
    d,i=low; D,j=high
    S,p=cells[d][i];T,q=cells[D][j]
    if not set(S).issubset(T):return False
    return (S,p)==(S,canon([set(b)&set(S) for b in q if set(b)&set(S)]))

def c(S,*blocks):
    return (tuple(int(v) for v in S),canon([tuple(int(t) for t in b) for b in blocks]))

CERT4=[
    (c('012','0','12'),c('0123','0','12','3')),
    (c('013','0','1','3'),c('0123','0','1','2','3')),
    (c('012','0','1','2'),c('0123','03','1','2')),
    (c('01','0','1'),c('013','03','1')),
    (c('03','0','3'),c('023','0','2','3')),
    (c('02','0','2'),c('023','03','2')),
    (c('12','1','2'),c('123','1','2','3')),
    (c('12','12'),c('123','12','3')),
    (c('0','0'),c('03','03')),
    (c('1','1'),c('13','1','3')),
    (c('2','2'),c('23','2','3')),
]
CERT3=[
    (c('012','0','1','2'),c('0123','03','1','2')),
    (c('012','0','12'),c('0123','0','12','3')),
    (c('12','1','2'),c('123','1','2','3')),
    (c('12','12'),c('123','12','3')),
]

def closed_sphere_surface(cells,alive):
    assert [sum((d,i) in alive for i in range(len(cells[d]))) for d in range(4)]==[4,6,4,0]
    vertices=[i for d,i in alive if d==0]
    edges=[(d,i) for d,i in alive if d==1]
    faces=[(d,i) for d,i in alive if d==2]
    # Closed surface: every edge in two 2-faces; vertex-link graph connected, degree 2.
    for e in edges:
        assert sum(contains_face(e,t,cells) for t in faces)==2
    for vi in vertices:
        incid_edges=[e for e in edges if vi in cells[e[0]][e[1]][0]]
        incidence_faces=[t for t in faces if vi in cells[t[0]][t[1]][0]]
        assert len(incid_edges)==len(incidence_faces)
        graph=defaultdict(set)
        for t in incidence_faces:
            incident=[e for e in incid_edges if contains_face(e,t,cells)]
            assert len(incident)==2
            a,b=incident;graph[a].add(b);graph[b].add(a)
        assert all(len(graph[e])==2 for e in incid_edges) if len(incid_edges)>2 else all(len(graph[e])==1 for e in incid_edges)
        reached={incid_edges[0]}
        while True:
            expanded=reached|set().union(*(graph[t] for t in reached))
            if expanded==reached:break
            reached=expanded
        assert reached==set(incid_edges)

def explicit_orbits(n):
    """Independent direct arcs enumeration and comparison to partition signatures."""
    arcs=[(u,v) for j in range(n) for u,v in [(0,j+2),(j+2,0),(1,j+2),(j+2,1)]]
    signatures=set()
    face_count=0
    for k in range(1,5):
        for inds in combinations(range(4*n),k):
            ed=[arcs[i] for i in inds]
            if len({a for a,b in ed})!=k or len({b for a,b in ed})!=k:continue
            nxt={a:b for a,b in ed}
            good=True
            for x in nxt:
                y=x
                for _ in range(k):
                    y=nxt.get(y,None)
                    if y is None:break
                    if y==x:good=False;break
                if not good:break
            if not good:continue
            face_count+=1
            colors={i%4:i//4 for i in inds}
            groups=defaultdict(list)
            for color,j in colors.items():groups[j].append(color)
            sig=(tuple(sorted(colors)),canon(groups.values()))
            signatures.add(sig)
    cells,_=model(n)
    expected={cell for d in cells for cell in cells[d]}
    assert signatures==expected,(n,len(signatures),len(expected),expected-signatures)
    return face_count

def main():
    for n,expected in [(1,(4,2,0,0)),(2,(4,8,4,0)),(3,(4,8,8,2)),(4,(4,8,8,3)),(5,(4,8,8,3))]:
        cells,_=model(n)
        assert tuple(len(cells[d]) for d in range(4))==expected
        print('CELL_VECTOR',n,expected,'DIRECT_FACES',explicit_orbits(n))
    cells,alive=collapse(4,CERT4)
    assert len(alive)==1 and cells[next(iter(alive))[0]][next(iter(alive))[1]]==c('3','3')
    print('N_GE_4_CERTIFIED_COLLAPSES',len(CERT4))
    cells,alive=collapse(3,CERT3)
    closed_sphere_surface(cells,alive)
    print('N_3_SPHERE_COLLAPSES',len(CERT3),'SPHERE_SURFACE_OK')
    cells,bd=model(2)
    triangles=[(2,i) for i in range(len(cells[2]))]
    edges=[(1,i) for i in range(len(cells[1]))]
    used=[e for e in edges if any(contains_face(e,t,cells) for t in triangles)]
    assert len(used)==6 and len(edges)==8
    assert all(sum(contains_face(e,t,cells) for t in triangles)==2 for e in used)
    assert len({frozenset(cells[e[0]][e[1]][0]) for e in used})==6
    assert len({frozenset(cells[t[0]][t[1]][0]) for t in triangles})==4
    print('N_2_TETRAHEDRAL_SPHERE_PLUS_TWO_CHORDS_OK')
    cells,_=model(1)
    assert tuple(map(len,cells.values()))==(4,2,0,0)
    print('N_1_TWO_INTERVALS_OK')
    print('ALL_VERIFY_OK')
if __name__=='__main__': main()
