"""Exact verification of oriented-square dependence identities.

Requires Python 3.9+; all arithmetic integral.
"""
from itertools import combinations
from fractions import Fraction


def c4_edge_masks(n, edges):
    index = {e:i for i,e in enumerate(edges)}
    ans = set()
    for a,b,c,d in combinations(range(n),4):
        for path in ((a,b,c,d),(a,b,d,c),(a,c,b,d)):
            pairs = [tuple(sorted((path[i],path[(i+1)%4]))) for i in range(4)]
            if all(p in index for p in pairs):
                ans.add(sum(1<<index[p] for p in pairs))
    return sorted(ans)


def is_directed_cycle(cmask, orientation, n, edges):
    indeg = [0]*n
    vertices = set()
    for i,(a,b) in enumerate(edges):
        if (cmask>>i)&1:
            if (orientation>>i)&1:
                a,b=b,a
            indeg[b]+=1
            vertices.update((a,b))
    return all(indeg[v]==1 for v in vertices)


def copy_count(n, edges, shape):
    # Count distinct image edge-sets of labelled subgraphs, not induced copies.
    m=len(edges); e=set(edges)
    from itertools import permutations
    found=set()
    if shape=='K4':
        for v in combinations(range(n),4):
            f=frozenset(tuple(sorted(z)) for z in combinations(v,2))
            if f<=e:found.add(f)
    elif shape=='K23':
        for v in combinations(range(n),2):
            for w in combinations(sorted(set(range(n))-set(v)),3):
                f=frozenset(tuple(sorted((a,b))) for a in v for b in w)
                if f<=e:found.add(f)
    else:raise ValueError(shape)
    return len(found)


def check_graph(n, edges, triple=False):
    cycles=c4_edge_masks(n,edges)
    k=len(cycles)
    if not k: return 0
    totals=[0]*k
    joints=[[0]*k for _ in range(k)]
    second=0
    for orient in range(1<<len(edges)):
        active=[i for i,c in enumerate(cycles) if is_directed_cycle(c,orient,n,edges)]
        for i in active:totals[i]+=1
        second+=len(active)**2
        for i in active:
            for j in active:
                joints[i][j]+=1
    scale=1<<len(edges)
    assert all(8*t==scale for t in totals)
    for i,j in combinations(range(k),2):
        shared=(cycles[i]&cycles[j]).bit_count()
        joint=Fraction(joints[i][j],scale)
        if shared==0 or shared==1:expected=Fraction(1,64)
        elif shared==2:
            # An overlapping pair on 4 vertices (K4) is incompatible;
            # a shared length-two path on five vertices (K2,3) is compatible.
            verts={v for h,(u,v) in enumerate(edges) if (cycles[i]|cycles[j])>>h&1 for v in (u,v)}
            expected=Fraction(0) if len(verts)==4 else Fraction(1,32)
        else:raise AssertionError((n,edges,shared))
        assert joint==expected,(n,edges,cycles[i],cycles[j],joint,expected)
    variance=Fraction(second,scale)-Fraction(k*k,64)
    predicted=Fraction(7*k+6*(copy_count(n,edges,'K23')-copy_count(n,edges,'K4')),64)
    assert variance==predicted,(n,edges,k,variance,predicted)
    return 1


def verify_small():
    total=0
    for n in range(4,6):
        universe=list(combinations(range(n),2))
        for graph in range(1<<len(universe)):
            edges=[x for i,x in enumerate(universe) if graph>>i&1]
            total+=check_graph(n,edges)
    # Dense six-vertex graph checks overlapping copies of both motifs.
    check_graph(6, list(combinations(range(6),2)))
    # Both graphs have exactly three squares and no other four-cycles.
    k4=list(combinations(range(4),2))
    biclique=[(a,b) for a in (0,1) for b in (2,3,4)]
    assert len(c4_edge_masks(4,k4))==len(c4_edge_masks(5,biclique))==3
    assert copy_count(4,k4,'K4')==1
    assert copy_count(5,biclique,'K23')==1
    # Cube: all six squares are pairwise independent, but three at
    # a common vertex cannot be directed simultaneously.
    cube_edges=[(x,y) for x in range(8) for y in range(x+1,8) if (x^y).bit_count()==1]
    faces=c4_edge_masks(8,cube_edges)
    assert len(faces)==6
    assert copy_count(8,cube_edges,'K4')==0
    assert copy_count(8,cube_edges,'K23')==0
    common=[c for c in faces if any(((c>>i)&1) and (0 in cube_edges[i]) for i in range(len(cube_edges)))]
    assert len(common)==3
    counts=[0]*3; joint2=[0]*3; joint3=0
    for orient in range(1<<12):
        b=[is_directed_cycle(c,orient,8,cube_edges) for c in common]
        for i in range(3):counts[i]+=b[i]
        for i,(a,b_) in enumerate(((0,1),(0,2),(1,2))):joint2[i]+=int(b[a] and b[b_])
        joint3+=int(all(b))
    assert counts==[512]*3
    assert joint2==[64]*3
    assert joint3==0
    return total,counts,joint2,joint3

if __name__=='__main__':
    t=verify_small()
    print('PASS: exactly checked',t[0],'graphs with four and five vertices containing squares')
    print('Cube three faces through a vertex: singleton counts, pair counts, triple count over 4096 orientations =',t[1:])
