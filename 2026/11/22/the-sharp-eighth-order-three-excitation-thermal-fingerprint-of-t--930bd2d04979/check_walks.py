"""Exact elementary-walk count for the three-excitation XY Hamiltonian.
No third-party dependencies.  Prints its complete short spectral-moment certificate.
"""
from itertools import combinations
V = tuple((a,b) for a in range(4) for b in range(4))
TRIPLES = tuple(combinations(range(16),3))
INDEX = {p:i for i,p in enumerate(TRIPLES)}

def graph_edges(kind):
    e=set()
    offsets = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    for i,(x,y) in enumerate(V):
        for j,(u,v) in enumerate(V):
            if j <= i: continue
            on = (x==u or y==v) if kind=='rook' else ((u-x)%4,(v-y)%4) in offsets
            if on: e.add((i,j))
    return e

def exchange_graph(edges):
    nbr=[set() for _ in range(16)]
    for u,v in edges:
        nbr[u].add(v); nbr[v].add(u)
    ans=[]
    for triple in TRIPLES:
        moves=set()
        for x in triple:
            for y in nbr[x]:
                if y not in triple:
                    nxt=tuple(sorted((set(triple)-{x})|{y}))
                    moves.add(INDEX[nxt])
        ans.append(tuple(sorted(moves)))
    assert all(i not in a for i,a in enumerate(ans))
    assert all(i in ans[j] for i,a in enumerate(ans) for j in a)
    return ans

def moments(adj, stop=8):
    ans=[len(adj)]
    for k in range(1,stop+1): ans.append(0)
    for root in range(len(adj)):
        walk=[0]*len(adj)
        walk[root]=1
        for k in range(1,stop+1):
            nextwalk=[0]*len(adj)
            for u,number in enumerate(walk):
                if number:
                    for v in adj[u]: nextwalk[v]+=number
            walk=nextwalk
            ans[k]+=walk[root]
    return ans

if __name__=='__main__':
    values={}
    for graph in ('rook','shrikhande'):
        edges=graph_edges('rook' if graph=='rook' else 'shrikhande')
        adj=exchange_graph(edges)
        assert len(edges)==48 and len(adj)==560 and sum(map(len,adj))==8736
        values[graph]=moments(adj)
        print(graph,values[graph])
    assert values['rook'][:8]==values['shrikhande'][:8]
    assert values['rook'][8]-values['shrikhande'][8]==2193408
    print('PASS: first distinct spectral moment is order 8; difference 2193408')
