#!/usr/bin/env python3
"""Exact, self-contained finite certificate for Möbius--Kantor hexagon convolution.

Usage: python3 verify.py
Uses only the standard library. All arithmetic is integral.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations


def graph_gp():
    e = set()
    for i in range(8):
        e.add(tuple(sorted((i, (i+1) % 8))))
        e.add(tuple(sorted((i, 8+i))))
        e.add(tuple(sorted((8+i, 8+(i+3) % 8))))
    return sorted(e)


def graph_configuration():
    """Independent realization: 8 nonzero F_3^2 points, 8 affine lines avoiding 0."""
    points = sorted((x, y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
    directions = ((1,0),(0,1),(1,1),(1,2))
    lines = set()
    for dx,dy in directions:
        for x,y in points:
            line = frozenset(((x+t*dx)%3, (y+t*dy)%3) for t in range(3))
            if (0,0) not in line: lines.add(line)
    lines = sorted(lines, key=lambda s: sorted(s))
    assert len(points) == len(lines) == 8
    return sorted((points.index(p), 8+j) for j,L in enumerate(lines) for p in L)


def hexagons_dfs(edges):
    idx={e:i for i,e in enumerate(edges)}
    adj=[set() for _ in range(16)]
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    cycles=set()
    def walk(path):
        if len(path)==6:
            if path[0] in adj[path[-1]]:
                z=0
                for j in range(6):
                    e=tuple(sorted((path[j],path[(j+1)%6])))
                    z|=1<<idx[e]
                cycles.add(z)
            return
        for v in adj[path[-1]]:
            if v not in path:walk(path+[v])
    for v in range(16):walk([v])
    return cycles


def hexagons_six_subsets(edges):
    # Characterization of length-6 cycles in a bipartite simple graph:
    # a six-edge support having only degrees 0 or 2.
    out=set()
    for subset in combinations(range(len(edges)),6):
        deg=[0]*16
        for j in subset:
            a,b=edges[j];deg[a]+=1;deg[b]+=1
        if all(d in (0,2) for d in deg):
            out.add(sum(1<<j for j in subset))
    return out


def fwt(v):
    a=list(v)
    h=1
    while h<len(a):
        for base in range(0,len(a),2*h):
            for i in range(base,base+h):
                x,y=a[i],a[i+h]
                a[i],a[i+h]=x+y,x-y
        h*=2
    return a


def cycle_spectrum(edges,cycles):
    adj=[[] for _ in range(16)]
    for j,(a,b) in enumerate(edges):
        adj[a].append((b,j));adj[b].append((a,j))
    seen={0}; queue=deque([0]); tree=set()
    while queue:
        u=queue.popleft()
        for v,j in sorted(adj[u]):
            if v not in seen:
                seen.add(v);queue.append(v);tree.add(j)
    assert len(seen)==16 and len(tree)==15
    chords=[j for j in range(24) if j not in tree]
    assert len(chords)==9
    code=[]
    for c in cycles:
        code.append(sum(1<<k for k,j in enumerate(chords) if (c>>j)&1))
    assert len(set(code))==24
    pivots={}
    for z in code:
        x=z
        for p in sorted(pivots,reverse=True):
            if (x>>p)&1:x^=pivots[p]
        if x:pivots[x.bit_length()-1]=x
    assert len(pivots)==9
    # First method: 512 direct signed sums, no transform.
    direct=[sum(-1 if (z&s).bit_count()%2 else 1 for z in code)
            for s in range(512)]
    # Independent method: Walsh transform of sparse 0/1 support.
    source=[int(j in code) for j in range(512)]
    assert direct==fwt(source)
    histogram=Counter(direct)
    assert histogram=={-8:33,-4:168,0:160,4:96,8:30,12:24,24:1},histogram
    indicator=[int(a!=0) for a in direct]
    p_num=fwt(indicator)
    assert Counter(p_num)=={-24:30,-16:12,-8:100,0:216,8:102,16:24,24:24,32:3,352:1},Counter(p_num)
    assert sum(p_num)==512 and p_num[0]==352
    assert sum(abs(x) for x in p_num)==3936
    return histogram,Counter(p_num),Fraction(sum(abs(x) for x in p_num),512)


def main():
    gp=graph_gp();gc=graph_configuration()
    assert len(gp)==len(gc)==24
    # Explicit isomorphism GP vertex index -> configuration vertex index,
    # established by checking all 24 adjacency relations.
    phi={0:0,8:8,11:2,13:7,1:9,9:3,2:6,7:10,
         6:4,15:5,3:11,4:1,12:12,5:13,14:14,10:15}
    assert set(phi)==set(phi.values())==set(range(16))
    assert {tuple(sorted((phi[a],phi[b]))) for a,b in gp}==set(gc)
    c1=hexagons_dfs(gp)
    c2=hexagons_six_subsets(gp)
    assert c1==c2 and len(c1)==24
    counts=Counter(sum((c>>j)&1 for c in c1) for j in range(24))
    assert counts=={6:24}
    # Transport cycles through the independent F_3^2 incidence model.
    gc_idx={e:i for i,e in enumerate(gc)}
    transported=set()
    for c in c1:
        z=0
        for j,(a,b) in enumerate(gp):
            if (c>>j)&1:z|=1<<gc_idx[tuple(sorted((phi[a],phi[b])))]
        transported.add(z)
    assert transported==hexagons_dfs(gc)==hexagons_six_subsets(gc)
    h1,k1,p1=cycle_spectrum(gp,c1)
    h2,k2,p2=cycle_spectrum(gc,transported)
    assert h1==h2 and k1==k2 and p1==p2==Fraction(123,16)
    N=1<<24;quotient_multiplicity=1<<15
    assert sum(h1.values())==512
    rank=(512-h1[0])*quotient_multiplicity
    assert rank==11534336 and N-rank==5242880
    assert min(abs(v) for v in h1 if v)!=0
    assert min(abs(v) for v in h1 if v!=0)==4
    assert max(abs(v) for v in h1)==24
    print('independent graphs: GP(8,3) and affine F_3^2 configuration')
    print('DFS and exhaustive six-subset cycles: 24; each edge in 6')
    print('cycle-space dimension: 9; direct and FWT signed spectra match')
    print('reduced spectrum:',sorted(h1.items()))
    print('scaled spectrum:',sorted((lam,c*quotient_multiplicity) for lam,c in h1.items()))
    print('full Fourier rank, nullity:',rank,N-rank)
    print('projection kernel numerators:',sorted(k1.items()))
    print('optimal endpoint norm:',p1)
    print('PASS')

if __name__=='__main__':main()
