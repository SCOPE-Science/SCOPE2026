"""Exact certificate replay for three-terminal habitat corridor reliability.

Usage: python3 verify.py
Requires only Python's standard library and bundled atlas.tsv.
Graph atlas completeness is an external catalog fact, not proved by code.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path

ATLAS = Path(__file__).with_name('atlas.tsv')
WITNESS_EDGES = {(0,4),(0,5),(1,5),(1,6),(2,3),(2,4),(2,7),(3,6),(5,7)}


def pairs(n):
    return list(combinations(range(n), 2))


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen={0}; stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v);stack.append(v)
    return len(seen)==n


def components(n, edges, alive):
    parent = list(range(n))
    def root(u):
        while parent[u]!=u:
            parent[u] = parent[parent[u]]
            u=parent[u]
        return u
    for u,v in edges:
        if (alive>>u)&1 and (alive>>v)&1:
            ru,rv=root(u),root(v)
            if ru!=rv:parent[ru]=rv
    return [root(u) for u in range(n)]


def gain_vectors(n, edges, terminals):
    nonterm=[v for v in range(n) if v not in terminals]
    absent=[e for e in pairs(n) if e not in edges]
    gains={e:[0]*(len(nonterm)+1) for e in absent}
    for subset in range(1<<len(nonterm)):
        alive=sum(1<<t for t in terminals)
        for i,v in enumerate(nonterm):
            if (subset>>i)&1:alive |= 1<<v
        rep=components(n,edges,alive)
        roots={rep[t] for t in terminals}
        if len(roots)!=2:
            continue  # one edge cannot fix three separated terminal components
        for u,v in absent:
            if (alive>>u)&1 and (alive>>v)&1 and {rep[u],rep[v]}==roots:
                gains[(u,v)][subset.bit_count()] += 1
    return gains


def inspect_atlas():
    number=0; by_n=Counter(); checked=0; by_order=Counter(); order_counts=Counter()
    for raw in ATLAS.read_text(encoding='utf8').splitlines():
        if not raw or raw.startswith('#'):continue
        index,nn,mm=(int(v) for v in raw.split('\t'))
        assert index==number
        number+=1
        n=nn
        order_counts[n]+=1
        e=pairs(n)
        assert mm>=0 and mm < 1<<len(e)
        edges={edge for i,edge in enumerate(e) if mm>>i&1}
        if n<3 or not connected(n,edges):continue
        for terminals in combinations(range(n),3):
            gains=gain_vectors(n,edges,terminals)
            if len(gains)<=1:continue
            checked+=1;by_order[n]+=1
            options=list(gains.values())
            assert any(all(all(a>=b for a,b in zip(g,h)) for h in options) for g in options), (index,n,terminals)
    assert number==1253,number
    assert tuple(order_counts[i] for i in range(8))==(1,1,2,4,11,34,156,1044), order_counts
    assert checked==32191,(checked,by_order)
    print('ATLAS PASS; 1253 graphs covering orders 0..7; 32191 nontrivial rooted cases; exact coefficientwise domination in all')
    print('Counts by n:',dict(sorted(by_order.items())))


def check_witness():
    n=8; ts=(0,1,2)
    assert connected(n,WITNESS_EDGES)
    gain=gain_vectors(n,WITNESS_EDGES,ts)
    a=gain[(0,1)]; b=gain[(1,2)]
    assert a==[0,1,4,3,0,0],a
    assert b==[0,2,5,2,0,0],b
    assert len(gain)==19
    assert all(c==a or c==b or
               (all(x<=y for x,y in zip(c,a)) and c!=a) or
               (all(x<=y for x,y in zip(c,b)) and c!=b)
               for c in gain.values())
    # Independent brute-force connectivity comparison (no gain formula) for 32 survival sets.
    for edge,g in (((0,1),a),((1,2),b)):
        for k in range(6):
            baseline=augmented=0
            for s in combinations(range(3,8),k):
                alive=set(ts)|set(s)
                for E,mode in ((WITNESS_EDGES,'base'),(WITNESS_EDGES|{edge},'aug')):
                    H={e for e in E if e[0] in alive and e[1] in alive}
                    # direct BFS from terminal 0
                    reached={0};frontier=[0]
                    while frontier:
                        u=frontier.pop()
                        for v,w in H:
                            neighbor=w if v==u else (v if w==u else None)
                            if neighbor is not None and neighbor not in reached:
                                reached.add(neighbor); frontier.append(neighbor)
                    yes=set(ts)<=reached
                    if mode=='base':baseline+=yes
                    else:augmented+=yes
            assert augmented-baseline==g[k], (edge,k,augmented-baseline,g[k])
    # Exact identity: (A-B)(p)=p(1-p)^2(p^2+p-1).
    # The two winner gain differences are [0,-1,-1,+1,0,0],
    # hence -p(1-p)^4-p^2(1-p)^3+p^3(1-p)^2.
    assert [v-u for u,v in zip(b,a)]==[0,-1,-1,1,0,0]
    print('WITNESS PASS; n=8, m=9, 19 eligible links; winning gains',a,b)
    print('Gain difference A-B = p*(1-p)^2*(p^2+p-1); threshold (sqrt(5)-1)/2')


if __name__=='__main__':
    inspect_atlas()
    check_witness()
