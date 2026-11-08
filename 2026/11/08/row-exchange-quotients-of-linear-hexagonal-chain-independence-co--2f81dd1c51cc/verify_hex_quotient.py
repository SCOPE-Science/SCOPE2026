#!/usr/bin/env python3
"""Finite independent checks for row-exchange quotients of hexagonal-chain independence complexes.
Run: python3 verify_hex_quotient.py. Standard library only."""
from collections import defaultdict


def graph(n):
    assert n >= 1
    vertices = [(r, j) for r in (0, 1) for j in range(1, 2*n+2)]
    labels = {v: i for i,v in enumerate(vertices)}
    edges = set()
    for r in (0, 1):
        for j in range(1, 2*n+1):
            edges.add(frozenset((labels[r,j], labels[r,j+1])))
    for j in range(1, 2*n+2, 2):
        edges.add(frozenset((labels[0,j], labels[1,j])))
    exchange = tuple(labels[1-r,j] for r,j in vertices)
    return vertices, edges, exchange


def all_faces(n):
    vertices, edges, exchange = graph(n)
    adj = [0]*len(vertices)
    for e in edges:
        a,b = tuple(e)
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    fs=[0]
    for i in range(len(vertices)):
        fs += [x|(1<<i) for x in fs if not (x & adj[i])]
    return vertices, edges, exchange, fs


def image_face(f, exchange):
    return sum(1<<exchange[i] for i in range(len(exchange)) if (f>>i)&1)


def chains_of_faces(fs):
    fs = sorted((f for f in fs if f), key=lambda f:(f.bit_count(),f))
    bysize=defaultdict(list)
    for f in fs:
        bysize[f.bit_count()].append(f)
    chain_by_last={}
    for f in fs:
        arr=[(f,)]
        for k in range(1, f.bit_count()):
            for g in bysize[k]:
                if g&f == g:
                    arr.extend(c+(f,) for c in chain_by_last[g])
        chain_by_last[f] = arr
    return [c for arr in chain_by_last.values() for c in arr]


def orbit_cells(fs, exchange):
    chains=chains_of_faces(fs)
    bydim=defaultdict(set)
    for c in chains:
        t=tuple(image_face(f,exchange) for f in c)
        bydim[len(c)-1].add(min(c,t))
    return [sorted(bydim[d]) for d in range(max(bydim)+1)]


def verify_base_circle(fs,exchange):
    cells=orbit_cells(fs,exchange)
    v,e,t=map(set,cells)
    canon=lambda c:min(c,tuple(image_face(f,exchange) for f in c))
    collapsed=0
    while t:
        count=defaultdict(int)
        for tri in t:
            for k in range(3):count[canon(tri[:k]+tri[k+1:])]+=1
        eligible=sorted((tri,canon(tri[:k]+tri[k+1:])) for tri in t for k in range(3) if count[canon(tri[:k]+tri[k+1:])]==1)
        assert eligible, "no free edge in quotient triangulation"
        tri,edge=eligible[0]
        t.remove(tri);e.remove(edge);collapsed+=1
    adjacency=defaultdict(set)
    for a,b in e:
        a=canon((a,));b=canon((b,))
        adjacency[a].add(b);adjacency[b].add(a)
    seen={min(v)}
    while True:
        nxt=seen | {b for a in seen for b in adjacency[a]}
        if nxt==seen:break
        seen=nxt
    assert seen==v and len(e)==len(v), "remaining graph not a single circle up to homotopy"
    print(f"BASE_COLLAPSE n=1 pairs={collapsed} remaining_vertices={len(v)} remaining_edges={len(e)} connected=True")

def quotient_chain_betti(fs, exchange):
    cells=orbit_cells(fs,exchange)
    ranks=[0]
    for d in range(1,len(cells)):
        low={c:j for j,c in enumerate(cells[d-1])}
        echelon={}
        for c in cells[d]:
            v=0
            for k in range(len(c)):
                sub=c[:k]+c[k+1:]
                img=tuple(image_face(f,exchange) for f in sub)
                v ^= 1<<low[min(sub,img)]
            while v:
                pivot=v.bit_length()-1
                if pivot in echelon: v ^= echelon[pivot]
                else:
                    echelon[pivot]=v;break
        ranks.append(len(echelon))
    ranks.append(0)
    b=[len(cells[d])-ranks[d]-ranks[d+1] for d in range(len(cells))]
    return [len(v) for v in cells], ranks[1:-1],b


def main():
    stats=[]
    for n in range(1,7):
        vertices, edges, exchange, fs = all_faces(n)
        fixed = {f for f in fs if image_face(f, exchange)==f}
        even_orbit_masks = [(1 << i) | (1 << exchange[i]) for i,(r,j) in enumerate(vertices) if r==0 and j%2==0]
        target={sum(mask for k,mask in enumerate(even_orbit_masks) if (v>>k)&1) for v in range(1<<n)}
        assert fixed == target, (n, 'incorrect fixed subcomplex')
        chi = sum((-1)**(f.bit_count()-1) for f in fs if f)
        assert chi == 1+2*(-1)**n, (n,chi)
        chi_fix = sum((-1)**(f.bit_count()//2-1) for f in fixed if f)
        assert chi_fix==1, (n,chi_fix)
        chi_quot = (chi+chi_fix)//2
        assert chi_quot==1+(-1)**n
        stats.append((n,len(fs)-1,len(fixed)-1,chi_quot))
    for n in (1,2):
        _,_,exchange,fs=all_faces(n)
        if n==1:verify_base_circle(fs,exchange)
        fvector,ranks,betti=quotient_chain_betti(fs,exchange)
        assert all(x == (1 if d in (0,n) else 0) for d,x in enumerate(betti)), (n,betti)
        print(f'QUOTIENT n={n} barycentric_orbit_cells={fvector} boundary_ranks_F2={ranks} betti_F2={betti}')
    print('FACE_CHECKS n,number_nonempty_faces,nonempty_fixed_faces,quotient_euler:')
    for row in stats:print(*row)
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
