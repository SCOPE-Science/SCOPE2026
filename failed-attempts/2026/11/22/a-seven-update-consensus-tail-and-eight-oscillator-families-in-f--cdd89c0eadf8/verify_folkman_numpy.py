"""Independent bit-sliced complete verifier for 20-vertex Folkman majority dynamics."""
import itertools
import json
import numpy as np

N=20
pairs=list(itertools.combinations(range(5),2))
assert len(pairs)==10
neighbors=[[] for _ in range(N)]
for k,(i,j) in enumerate(pairs):
    w=10+k
    for twin in (2*i,2*i+1,2*j,2*j+1):
        neighbors[w].append(twin)
        neighbors[twin].append(w)
assert sorted(map(len,neighbors))==[4]*20
assert sum(len(v) for v in neighbors)//2==40
# Check structural twin property and bipartition by direct adjacency.
assert all(set(neighbors[2*i])==set(neighbors[2*i+1]) for i in range(5))

def F(A):
    y=np.zeros(A.shape,dtype=np.uint32)
    for v,ns in enumerate(neighbors):
        count=sum((A>>np.uint32(u))&np.uint32(1) for u in ns)
        new=(count>2)|((count==2)&(((A>>np.uint32(v))&np.uint32(1))!=0))
        y |= (new.astype(np.uint32)<<np.uint32(v))
    return y

S=1<<N
initial=np.arange(S,dtype=np.uint32)
steps=[initial]
for k in range(9):
    steps.append(F(steps[-1]))
assert len(steps)==10
entry=np.full(S,-1,dtype=np.int16)
period=np.zeros(S,dtype=np.int8)
for t in range(8):
    isperiodic=steps[t+2]==steps[t]
    fresh=isperiodic & (entry<0)
    entry[fresh]=t
    period[fresh]=np.where(steps[t][fresh]==steps[t+1][fresh],1,2)
assert (entry>=0).all()
counts={f"{t}:{p}":int(np.sum((entry==t)&(period==p))) for t in range(8) for p in (1,2) if np.any((entry==t)&(period==p))}
assert sum(counts.values())==S
witness=int(np.flatnonzero(entry==7)[0])
result={"method":"direct iterate-comparison, independent bit-sliced implementation", "vertex_count":N,
"state_count":S,"degree_sequence":sorted(map(len,neighbors)),"edge_count":40,
"primitive_periods":sorted(set(period.tolist())),"first_entry_shells":counts,
"max_entry":int(entry.max()),"max_entry_witness_decimal":witness,
"witness_trajectory":[format(int(arr[witness]),'020b') for arr in steps],
"max_entry_periods":sorted(set(period[entry==7].tolist())),
"late_period_two_count":int(np.sum((entry>=4)&(period==2))),
"max_entry_consensus_counts":{"zeros":int(np.sum((entry==7)&(steps[7]==0))),"ones":int(np.sum((entry==7)&(steps[7]==S-1))),"nonconsensus":int(np.sum((entry==7)&(steps[7]!=0)&(steps[7]!=S-1)))},
"penultimate_entry_consensus_counts":{"zeros":int(np.sum((entry==6)&(steps[6]==0))),"ones":int(np.sum((entry==6)&(steps[6]==S-1))),"nonconsensus":int(np.sum((entry==6)&(steps[6]!=0)&(steps[6]!=S-1)))}}
assert result["max_entry_consensus_counts"]=={"zeros":480,"ones":480,"nonconsensus":0}
assert result["late_period_two_count"]==0
print(json.dumps(result,indent=2))
