"""Finite certificates for homopolymer-free two-read deletion reconstruction.
Uses only the Python standard library. Run: python verify_direct.py
"""
from itertools import product, combinations
from collections import defaultdict, deque
from math import comb

WITNESS19 = '''01020 01021 01210 02021 02101 02102 02121 10102 10201 10202 10212 12101 12102 20210 20212 21010 21020 21021 21210'''.split()
# An exact rational fractional cover of the 42 ternary length-five
# vertices using edges (independent-set cap 1) and seven-cycles (cap 3).
# All weights are doubled integers, to avoid floating arithmetic.
CERT = [
 ('E',2,'01020 01202'),('E',1,'01210 02120'),
 ('E',2,'01212 02121'),('E',2,'02010 02101'),
 ('E',2,'10121 10212'),('E',1,'10201 12021'),
 ('E',2,'10202 12020'),('E',2,'12010 12101'),
 ('E',2,'20101 21010'),('E',1,'20102 21012'),
 ('E',2,'20121 20212'),('E',2,'21020 21202'),
 ('C',1,'01012 01021 01201 01210 10102 10120 10210'),
 ('C',1,'01012 01021 01201 10102 10120 10201 10210'),
 ('C',1,'02012 02021 02102 02120 20120 20201 20210'),
 ('C',1,'02012 02021 02102 20102 20120 20201 20210'),
 ('C',1,'12012 12021 12102 12120 21021 21201 21210'),
 ('C',1,'12012 12102 12120 21012 21021 21201 21210'),
]
ODD7 = '01012 01021 01201 01210 10210 10120 10102'.split()

def make_graph(q,n):
    words=[''.join(map(str,v)) for v in product(range(q),repeat=n)
           if all(v[i]!=v[i+1] for i in range(n-1))]
    byread=defaultdict(set)
    for word in words:
        for k in range(n):byread[word[:k]+word[k+1:]].add(word)
    hits=defaultdict(int)
    for source in byread.values():
        for a,b in combinations(sorted(source),2):hits[a,b]+=1
    adj={v:set() for v in words}
    for (a,b),m in hits.items():
        if m>=2:adj[a].add(b);adj[b].add(a)
    return adj

def is_bipartite_and_perfect(adj):
    # Breadth-first two-colouring and augmenting-path matching.
    color={}
    for root in adj:
        if root in color:continue
        color[root]=0;Q=deque([root])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if v in color:assert color[v]!=color[u]
                else:color[v]=1-color[u];Q.append(v)
    left=[v for v in adj if color[v]==0]
    right=[v for v in adj if color[v]==1]
    assert len(left)==len(right)==len(adj)//2
    mate={}
    def augment(u,seen):
        for v in sorted(adj[u]):
            if v in seen:continue
            seen.add(v)
            if v not in mate or augment(mate[v],seen):mate[v]=u;return True
        return False
    assert all(augment(u,set()) for u in sorted(left))
    assert len(mate)==len(right)

def test():
    for n in (2,3,4):
        for s in range(2,n+1):
            g=make_graph(s,n)
            h={w:{v for v in vs if len(set(v))==s}
               for w,vs in g.items() if len(set(w))==s}
            is_bipartite_and_perfect(h)
    for s in (2,4,5):
        g=make_graph(s,5)
        h={w:{v for v in vs if len(set(v))==s}
           for w,vs in g.items() if len(set(w))==s}
        is_bipartite_and_perfect(h)
    adj=make_graph(3,5)
    H={w:{v for v in vs if len(set(v))==3}
       for w,vs in adj.items() if len(set(w))==3}
    assert len(H)==42 and sum(map(len,H.values()))//2==57
    assert len(WITNESS19)==19 and len(set(WITNESS19))==19
    assert all(x in H for x in WITNESS19)
    assert all(y not in H[x] for x,y in combinations(WITNESS19,2))
    cover={w:0 for w in H};cost=0
    for kind,twice_weight,vertex_string in CERT:
        V=vertex_string.split()
        assert len(set(V))==len(V) and set(V)<=set(H)
        if kind=='E':
            assert len(V)==2 and V[1] in H[V[0]]
            cost+=twice_weight
        else:
            assert kind=='C' and len(V)==7
            # Each vertex has degree two in a connected induced 7-cycle.
            assert all(len(H[u]&set(V))==2 for u in V)
            reach={V[0]};Q=[V[0]]
            for u in Q:
                for v in H[u]&set(V):
                    if v not in reach:reach.add(v);Q.append(v)
            assert len(reach)==7
            cost+=3*twice_weight
        for v in V:cover[v]+=twice_weight
    assert all(wt>=2 for wt in cover.values())
    assert cost==39  # 2*|I| <= 39, so any integer independent set <=19
    assert len(ODD7)==7
    assert all(ODD7[(k+1)%7] in adj[ODD7[k]] for k in range(7))
    assert all(len(adj[u]&set(ODD7))==2 for u in ODD7)
    for q in range(2,6):
        for n in range(2,6):
            g=make_graph(q,n)
            edges=sum(map(len,g.values()))//2
            expected=comb(q,2)*(q-1)**(n-3)*((n-1)*(q-2)+1)
            assert edges==expected,(q,n,edges,expected)
    print('VERIFY_DIRECT_OK')
if __name__=='__main__':test()
