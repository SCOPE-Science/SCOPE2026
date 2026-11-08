"""Certificate checker for pair-equality queries on 3-versus-6 partitions.

Python 3 standard library only. Run: python verify_three_block_cut.py depth6_tree.json
"""
from itertools import combinations, product
from math import comb
from pathlib import Path
import json, sys

certificate=Path(sys.argv[1] if len(sys.argv)>1 else 'depth6_tree.json')
a=json.loads(certificate.read_text(encoding='utf-8'))
n=a['n']; b=a['block_size']; d=a['depth']
assert (n,b,d)==(9,3,6)
assert max(comb(m,3) for m in range(4,9))==56 < 2**d
assert 2**d<=comb(9,3)<2**(d+1)
leaves=[];queries=[]

def walk(node,trace,level):
    if level==d:
        assert set(node)=={'witness'}
        A=tuple(node['witness'])
        assert len(A)==3 and len(set(A))==3 and all(0<=x<9 for x in A)
        assert all(int((u in A)==(v in A))==answer for u,v,answer in trace)
        leaves.append(A)
        return
    assert set(node)=={'query','yes','no'}
    u,v=node['query']
    assert 0<=u<v<n
    queries.append((u,v))
    walk(node['no'],trace+[(u,v,0)],level+1)
    walk(node['yes'],trace+[(u,v,1)],level+1)

walk(a['root'],[],0)
assert len(leaves)==64 and len(queries)==63 and len(set(leaves))==64

# Five independent pair queries admit all 32 traces.  The remaining
# three vertices are unconstrained by the query support.
star=[(0,i) for i in range(1,6)]
all_A=list(combinations(range(9),3))
traces={tuple(int((u in A)==(v in A)) for u,v in star) for A in all_A}
assert len(traces)==32

# The seven possible component size profiles of a six-edge forest
# on nine vertices.  For each one choose a vertex bipartition (c,t-c)
# in every component whose componentwise orientation choices cannot
# yield exactly three selected vertices.
obstructions={
    (1,1,7):(0,0,0),
    (1,2,6):(0,1,0),
    (1,3,5):(0,0,1),
    (1,4,4):(0,0,0),
    (2,2,5):(0,0,0),
    (2,3,4):(0,0,2),
    (3,3,3):(0,0,1)
}
possible_profiles={}
for u in range(1,10):
    for v in range(u,10):
        w=9-u-v
        if w>=v:possible_profiles[(u,v,w)]=1
assert set(obstructions)==set(possible_profiles)
for t,c in obstructions.items():
    assert all(0<=v<=s for s,v in zip(t,c))
    sums={sum(choices) for choices in product(*[(v,s-v) for s,v in zip(t,c)])}
    assert 3 not in sums,(t,c,sums)

print('THREE_BLOCK_PARTITION_CHECKS_PASS', 'depth='+str(d),
      'leaves='+str(len(leaves)), 'queries='+str(len(queries)),
      'distinct_queries='+str(len(set(queries))),
      'VC_lower_traces='+str(len(traces)),
      'VC_upper_profiles='+str(len(obstructions)))
