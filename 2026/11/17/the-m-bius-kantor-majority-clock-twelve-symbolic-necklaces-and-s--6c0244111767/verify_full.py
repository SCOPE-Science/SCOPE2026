"""Independent exhaustive 16-vertex majority functional-graph census.
Adjacency is constructed from the [5,-5]^8 LCF graph, with no dependence
on the shore-map program. Python 3 standard library only.
"""
from collections import Counter, defaultdict
N=16
adj=[set() for _ in range(N)]
def edge(u,v):
    assert u!=v
    adj[u].add(v);adj[v].add(u)
for j in range(N):edge(j,(j+1)%N)
for j in range(0,N,2):edge(j,(j+5)%N)
assert all(len(vs)==3 for vs in adj)
assert all(all((v^u)&1 for v in vs) for u,vs in enumerate(adj))

# Bitwise majority is computed here as a count, not Boolean polynomial.
def step(s):
    out=0
    for j,neighbors in enumerate(adj):
        if sum((s>>v)&1 for v in neighbors)>=2:out|=1<<j
    return out
succ=[step(s) for s in range(1<<N)]
# Four applications suffice for first periodic entry of every possible input.
entry=Counter(); periods=Counter(); basins=Counter();
fixed_states=set(); periodic_2=set()
witness_3=None
for s in range(1<<N):
    z=s; t=0
    while succ[succ[z]]!=z:
        z=succ[z];t+=1
        assert t<=3,(s,t)
    if t==3 and witness_3 is None:witness_3=s
    length=1 if succ[z]==z else 2
    orbit_id=min(z,succ[z])
    entry[(t,length)]+=1;periods[length]+=1;basins[(orbit_id,length)]+=1
    if t==0:
        if length==1:fixed_states.add(s)
        else:periodic_2.add(orbit_id)
assert len(fixed_states)==72
assert len(periodic_2)==2556
assert periods=={1:9736,2:55800}
expected_entry={(0,1):72,(0,2):5112,(1,1):480,(1,2):15072,
                (2,1):3712,(2,2):18816,(3,1):5472,(3,2):16800}
assert entry==expected_entry
assert Counter(n for (orbit,length),n in basins.items() if length==1)=={1:22,4:48,4761:2}
assert Counter(n for (orbit,length),n in basins.items() if length==2)=={2:231,4:1056,8:1128,138:44,276:96,9522:1}
assert all(succ[succ[succ[succ[succ[s]]]]]==succ[succ[succ[s]]] for s in range(1<<N))
print('FULL_65536_STATE_CENSUS_OK')
print('graph LCF [5,-5]^8, vertices',N,'edges',sum(map(len,adj))//2)
print('periodic fixed',len(fixed_states),'primitive_2cycles',len(periodic_2))
print('eventual period populations',sorted(periods.items()))
print('entry_period_table', sorted(entry.items()))
print('basin_count',len(basins))
print('basins_fixed',sorted(Counter(n for (orbit,length),n in basins.items() if length==1).items()))
print('basins_2cycle',sorted(Counter(n for (orbit,length),n in basins.items() if length==2).items()))
print('max_entry_time',max(t for t,_ in entry),'witness',witness_3)
print('identity F^5=F^3 YES')
