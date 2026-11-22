"""Independent graph-based calculation of the supersymmetric Witten index.

No external packages needed. Uses signed deletion--closed-neighborhood recurrence
on the actual 2n-vertex graph, independent of transfer matrices.
Execute: python verify_graph.py
"""
from functools import lru_cache

expected = {7:1,8:3,9:-11,10:4,11:1,12:6,13:-12,14:13}

def graph(n):
    assert n>=7
    adj = [0]*(2*n)
    def edge(a,b):
        assert a!=b
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    for i in range(n):
        edge(i,(i+1)%n)
        edge(i,n+i)
        edge(n+i,n+((i+3)%n))
    assert all(a.bit_count()==3 for a in adj)
    return tuple(adj)

def signed_sum(n):
    adjacency=graph(n)
    @lru_cache(None)
    def visit(remaining):
        if not remaining: return 1
        # Recurrence W(G)=W(G-v)-W(G-N[v]).
        vertex=(remaining&-remaining).bit_length()-1
        without=remaining&~(1<<vertex)
        closed=without&~adjacency[vertex]
        return visit(without)-visit(closed)
    result=visit((1<<(2*n))-1)
    return result, visit.cache_info()

if __name__=='__main__':
    for n,truth in expected.items():
        got,cache=signed_sum(n)
        assert got == truth,(n,got,truth)
        print(f'n={n}, signed independent sets={got}, visited subgraphs={cache.currsize}')
    print('PASS: independent graph-based signed sums on eight graph orders')
