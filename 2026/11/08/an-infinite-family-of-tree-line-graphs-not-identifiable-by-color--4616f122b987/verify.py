#!/usr/bin/env python3
"""Standalone finite verification for an infinite line-tree-switch construction.
The mathematical proof, not these finite samples, establishes all m >= 2.
"""
from collections import Counter
from itertools import combinations
from math import comb

def construct(m):
    assert m >= 2
    edges = {'b': ('A', 'B')}
    for c in ('A', 'B'):
        for i in range(1, m + 1):
            u, v, z = f'u{c}{i}', f'v{c}{i}', f'z{c}{i}'
            edges[u] = (c, f'UL{c}{i}')
            edges[v] = (c, f'VI{c}{i}')
            edges[z] = (f'VI{c}{i}', f'ZO{c}{i}')
    vertices = sorted(edges)
    G = {a:set() for a in vertices}
    for a, b in combinations(vertices, 2):
        if set(edges[a]).intersection(edges[b]):
            G[a].add(b);G[b].add(a)
    H={a:set(neighbors) for a,neighbors in G.items()}
    deleted=(('uA1','vA1'),('uB1','vB1'))
    added=(('uA1','vB1'),('uB1','vA1'))
    for a,b in deleted:
        assert b in H[a]
        H[a].remove(b);H[b].remove(a)
    for a,b in added:
        assert b not in H[a]
        H[a].add(b);H[b].add(a)
    return edges,G,H

def colors_partition(X):
    return lambda v:'b' if v=='b' else v[0]

def quotients(X):
    cells={c:sorted(v for v in X if colors_partition(X)(v)==c) for c in 'buvz'}
    ans={}
    for c,verts in cells.items():
        entries=set(tuple(sum(y in X[x] for y in cells[d]) for d in 'buvz') for x in verts)
        assert len(entries)==1, (c,entries)
        ans[c]=next(iter(entries))
    return ans,{c:len(verts) for c,verts in cells.items()}

def triangles(X):
    return sum(b in X[a] and c in X[a] and c in X[b]
               for a,b,c in combinations(sorted(X),3))

def joint_color_refinement(G,H):
    gkeys=sorted(G);hkeys=sorted(H)
    vertices=[(0,v) for v in gkeys]+[(1,v) for v in hkeys]
    adj={(0,v):{(0,w) for w in G[v]} for v in gkeys}
    adj.update({(1,v):{(1,w) for w in H[v]} for v in hkeys})
    colors={v:0 for v in vertices}
    for step in range(len(vertices)+2):
        signatures={v:(colors[v],tuple(sorted(Counter(colors[w] for w in adj[v]).items()))) for v in vertices}
        alphabet={signature:i for i,signature in enumerate(sorted(set(signatures.values())))}
        new={v:alphabet[signatures[v]] for v in vertices}
        assert Counter(new[(0,v)] for v in gkeys)==Counter(new[(1,v)] for v in hkeys),step
        if all(new[v]==colors[v] for v in vertices): return step
        colors=new
    raise AssertionError('color refinement did not stabilize')

def main():
    for m in range(2,7):
        edges,G,H=construct(m)
        assert len(edges)==6*m+1
        endpoints=set(sum((list(x) for x in edges.values()),[]))
        assert len(endpoints)==6*m+2
        deg={c:set(len(G[v]) for v in G if colors_partition(G)(v)==c) for c in 'buvz'}
        assert deg == {'b':{4*m},'u':{2*m},'v':{2*m+1},'z':{1}},deg
        expected={'b':(0,2*m,2*m,0),'u':(1,m-1,m,0),'v':(1,m,m-1,1),'z':(0,0,1,0)}
        gquot,gsizes=quotients(G);hquot,hsizes=quotients(H)
        assert gquot==hquot==expected,(m,gquot,hquot)
        assert gsizes==hsizes=={'b':1,'u':2*m,'v':2*m,'z':2*m}
        rounds=joint_color_refinement(G,H)
        tg,th=triangles(G),triangles(H)
        assert tg==2*comb(2*m+1,3)
        assert th==tg-4*m+4
        assert tg!=th
        print('m',m,'tree_vertices',len(endpoints),'line_vertices',len(G),
              'triangles_G',tg,'triangles_H',th,'refinement_rounds',rounds)
    print('PASS: exact quotients, color-refinement equivalence and triangle deficit for m=2..6')

if __name__=='__main__':main()
