#!/usr/bin/env python3
"""Reproduce finite tree-restriction incidence and verify the claimed threshold.
No nonstandard Python packages are used.
"""
from collections import defaultdict,Counter
from itertools import combinations
from pathlib import Path
import json, subprocess, sys

ROOT = Path(__file__).resolve().parent

def normalize_edges(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))

def canonical_splits(edges, leaves):
    adj=defaultdict(list)
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    L=set(leaves); parts=[]
    for u,v in edges:
        seen={u}; q=[u]
        for a in q:
            for b in adj[a]:
                if (a==u and b==v) or (a==v and b==u):continue
                if b not in seen:seen.add(b);q.append(b)
        A=tuple(sorted(seen & L)); B=tuple(sorted(L-set(A)))
        if len(A)>=2 and len(B)>=2:parts.append(min(A,B))
    return tuple(sorted(parts))

def tree_list(n):
    cur=[normalize_edges([(-1,0),(-1,1),(-1,2)])]
    for m in range(3,n):
        nxt={}
        for tree in cur:
            for u,v in tree:
                ed=[e for e in tree if e!=(u,v)] + [(u,-m),(v,-m),(-m,m)]
                ed=normalize_edges(ed)
                nxt[canonical_splits(ed,range(m+1))]=ed
        cur=[nxt[k] for k in sorted(nxt)]
    return cur

def restrict_by_splits(tree, n, deleted):
    full=canonical_splits(tree,range(n))
    remain=set(range(n))-{deleted}
    out=[]
    for A in full:
        B=remain-set(A)
        AA=set(A)&remain
        if len(AA)>=2 and len(B)>=2:
            out.append(min(tuple(sorted(AA)),tuple(sorted(B))))
    return tuple(sorted(set(out)))

def restrict_by_pruning(tree,n,deleted):
    adj=defaultdict(set)
    for u,v in tree:adj[u].add(v);adj[v].add(u)
    neigh=next(iter(adj[deleted]));adj[neigh].remove(deleted);del adj[deleted]
    if len(adj[neigh])==2:
        a,b=tuple(adj[neigh]);adj[a].remove(neigh);adj[b].remove(neigh)
        adj[a].add(b);adj[b].add(a);del adj[neigh]
    edges=normalize_edges((u,v) for u in adj for v in adj[u] if u<v)
    return canonical_splits(edges,[i for i in range(n) if i!=deleted])

def shadow_matrix(n):
    trees=tree_list(n)
    keys=[]
    for T in trees:
        r=[]
        for deleted in range(n):
            a=restrict_by_splits(T,n,deleted)
            b=restrict_by_pruning(T,n,deleted)
            assert a==b,(n,T,deleted,a,b)
            r.append((deleted,a))
        keys.append(r)
    allcols=sorted(set(x for row in keys for x in row))
    ids={c:i for i,c in enumerate(allcols)}
    rows=[tuple(ids[x] for x in row) for row in keys]
    degree=Counter(c for row in rows for c in row)
    assert len(trees)=={4:3,5:15,6:105,7:945}[n]
    assert len(allcols)==n*{4:1,5:3,6:15,7:105}[n]
    assert set(degree.values())=={2*n-5}
    return trees,rows,allcols

def valid_code(rows, indices, ncols):
    covered=[]
    for i in indices: covered.extend(rows[i])
    return len(covered)==len(set(covered)) and len(covered)==ncols

assert len(tree_list(3))==1
witness={}
for n in (4,5,6,7):
    trees,rows,cols=shadow_matrix(n)
    if n==4: picks=[0]
    elif n==5:
        picks=next((list(c) for c in combinations(range(15),3) if valid_code(rows,c,15)),None)
        assert picks is not None
    elif n==6:
        def cherries(tree):
            adj=defaultdict(set)
            for u,v in tree:adj[u].add(v);adj[v].add(u)
            return sum(sum(x>=0 for x in adj[next(iter(adj[i]))])==2 for i in range(n))//2
        picks=[i for i,t in enumerate(trees) if cherries(t)==3]
        assert len(picks)==15
    if n<=6:
        assert valid_code(rows,picks,len(cols))
        witness[str(n)]={'indices':picks,'split_signatures':[canonical_splits(trees[i],range(n)) for i in picks]}
    if n==7:
        data=f'{len(rows)} {len(cols)}\n' + ''.join(' '.join(map(str,row))+'\n' for row in rows)
        assert (ROOT/'incidence7.txt').read_text(encoding='utf-8')==data, 'Incidence file mismatch'
    print('TREE_AND_SHADOW_OK',n,len(trees),len(cols),2*n-5,flush=True)
assert json.loads((ROOT/'witnesses.json').read_text(encoding='utf-8'))==json.loads(json.dumps(witness)), 'Witness file mismatch'
print('CONSTRUCTION_OK',[(n,len(witness[str(n)]['indices'])) for n in (4,5,6)],flush=True)
