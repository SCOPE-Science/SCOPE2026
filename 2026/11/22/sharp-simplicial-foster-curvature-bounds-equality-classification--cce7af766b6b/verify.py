"""Exact finite checks for local Foster-curvature inequalities.

This script uses only the Python standard library. It independently enumerates
spanning trees instead of computing electrical-network potentials.
"""
from fractions import Fraction
from itertools import combinations


def edges_of(n,mask):
    pairs=list(combinations(range(n),2))
    return [e for i,e in enumerate(pairs) if (mask>>i)&1]


def tree_edge_counts(n,edges):
    counts=[0]*len(edges)
    count=0
    for inds in combinations(range(len(edges)), n-1):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        valid=True
        for j in inds:
            a,b=edges[j]; a=find(a); b=find(b)
            if a==b:
                valid=False; break
            parent[a]=b
        if valid and len({find(v) for v in range(n)})==1:
            count+=1
            for j in inds:counts[j]+=1
    return count,counts


def profile(n,edges):
    nt, tc=tree_edge_counts(n,edges)
    if not nt:return None
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    probs=[Fraction(c,nt) for c in tc]
    curvature=[Fraction(1) for _ in range(n)]
    for (a,b),p in zip(edges,probs):
        curvature[a]-=p/2
        curvature[b]-=p/2
    assert sum(curvature)==1
    return adj,curvature,probs


def equality_graph_condition(n,adj,v):
    # Outside components may attach to at most one member of the clique N(v).
    outside=set(range(n))-adj[v]-{v}
    while outside:
        w=next(iter(outside))
        comp={w}; frontier=[w];outside.remove(w)
        while frontier:
            z=frontier.pop()
            for a in adj[z]&outside:
                outside.remove(a);comp.add(a);frontier.append(a)
        attachments=set().union(*(adj[a]&adj[v] for a in comp))
        if len(attachments)>1:
            return False
    return True


def check(n,edges):
    p=profile(n,edges)
    if p is None:return False
    adj,curvature,probs=p
    for v in range(n):
        budget=sum((Fraction(1,2+len(adj[v]&adj[u])) for u in adj[v]),Fraction(0))
        assert curvature[v]>=1-budget,(n,edges,v,curvature[v],budget)
        d=len(adj[v]);simplicial=all(b in adj[a] for a,b in combinations(adj[v],2))
        if simplicial:
            assert curvature[v]>=Fraction(1,d+1)
            assert (curvature[v]==Fraction(1,d+1)) == equality_graph_condition(n,adj,v), (n,edges,v,curvature[v])
            if d<n-1:
                assert curvature[v]>Fraction(1,n)
    if all(curvature[v]==Fraction(1,n) for v in range(n)) and any(
        all(b in adj[a] for a,b in combinations(adj[v],2)) for v in range(n)
    ):
        assert len(edges)==n*(n-1)//2
    return True


def main():
    for n in range(2,6):
        checked=0
        for mask in range(1<<(n*(n-1)//2)):
            checked+=check(n,edges_of(n,mask))
        print('ALL_CONNECTED_GRAPHS_VERTEX_CURVATURE_AND_SIMPLICIAL_TEST_PASS',n,checked)
    for n in range(3,8):
        for d in range(1,n-1):
            # Clique on vertices 0..d; the remaining path attaches to vertex 0.
            edges=list(combinations(range(d+1),2))
            for w in range(d+1,n):
                edges.append((w-1 if w>d+1 else 0,w))
            adj,curv,probs=profile(n,edges)
            assert curv[1]==Fraction(1,d+1), (n,d,curv[1])
        print('SHARP_ALL_CLIQUE_DEGREES_WITH_PENDANT_PATH_PASS',n)
    # At least one biconnected noncomplete chordal graph cannot have constant local curvature.
    diamond=[(0,1),(0,2),(1,2),(0,3),(1,3)]
    adj,curv,probs=profile(4,diamond)
    assert curv[2]>Fraction(1,4) and curv[3]>Fraction(1,4)
    print('NONCOMPLETE_2_CONNECTED_CHORDAL_WITNESS_PASS',list(map(str,curv)))
    print('VERIFY_OK')

if __name__=='__main__':main()
