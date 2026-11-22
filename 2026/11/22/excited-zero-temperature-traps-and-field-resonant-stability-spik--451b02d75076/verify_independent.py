"""Independent exhaustive certificate: adjacency from an icosahedral chord embedding,
using down-spin subsets and edge-cut counts rather than spin-flip energies.
"""
from itertools import combinations
from collections import Counter

# Two pentagons, each with an apex, and oppositely staggered rim links.
V=tuple(range(12))
E=set()
for a in range(5):
    E.add(frozenset((0, 1+a)))
    E.add(frozenset((11, 6+a)))
    E.add(frozenset((1+a, 1+(a+1)%5)))
    E.add(frozenset((6+a, 6+(a+1)%5)))
    E.add(frozenset((1+a, 6+a)))
    E.add(frozenset((1+a, 6+(a+4)%5)))
assert len(E)==30
adj={v:set() for v in V}
for uv in E:
    u,v=tuple(uv)
    adj[u].add(v);adj[v].add(u)

# Each down subset D has magnetization M=12-2|D| and bond sum B=30-2|cut(D)|.
# A plus spin is stable iff h>=5-2|N(v) cap D|;
# a minus spin is stable iff h<=5-2|N(v) cap D|.
expected={0:(92,72),1:(407,222),2:(45,30),3:(191,50),4:(26,20),5:(69,69),6:(1,1)}
for h,(want,ground_want) in expected.items():
    c=Counter(); energy_list=[]
    for k in range(13):
        for Dtuple in combinations(V,k):
            D=set(Dtuple)
            cut=sum((u in D)!=(v in D) for uv in E for u,v in [tuple(uv)])
            M=12-2*k; B=30-2*cut
            energy_list.append(B-h*M)
            if all((h <= 5-2*len(adj[v]&D) if v in D else h >= 5-2*len(adj[v]&D)) for v in V):
                c[M,B]+=1
    assert sum(c.values())==want
    emin=min(energy_list)
    assert sum(x==emin for x in energy_list)==ground_want
    if h in (0,2,4):
        print('open_field',h,'stable_decomposition',sorted(c.items()))
    else:
        print('critical_field',h,'stable_decomposition',sorted(c.items()))
print('INDEPENDENT_ICO_VERTEX_SUBSET_CERTIFICATE_PASSED', 'all=4096', 'fields=7')
