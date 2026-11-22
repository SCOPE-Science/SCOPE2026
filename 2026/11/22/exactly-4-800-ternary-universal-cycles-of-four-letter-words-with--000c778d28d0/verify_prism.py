"""Independent spanning-tree/BEST check, using only Python's standard library."""
from itertools import permutations, combinations
from math import factorial
P = list(permutations(range(3)))
assert len(P)==6
# Every permutation abc leads to bca, cab and cba after suppressing forced states.
A = {(u, (u[1],u[2],u[0])) for u in P}
A |= {(u,(u[2],u[0],u[1])) for u in P}
A |= {(u,(u[2],u[1],u[0])) for u in P}
assert len(A)==18
assert all((v,u) in A for u,v in A)
E = {frozenset((u,v)) for u,v in A}
assert len(E)==9
# The graph is a triangular prism: two triangles joined by a matching.
def parity(t):return sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))%2
assert sum(parity(v)==0 for v in P)==3
for v in P:
    nbrs=[w for w in P if frozenset((v,w)) in E]
    assert len(nbrs)==3
    assert sum(parity(w)==parity(v) for w in nbrs)==2
    assert sum(parity(w)!=parity(v) for w in nbrs)==1

def connected(edge_set):
    seen={P[0]};changed=True
    while changed:
        old=len(seen)
        for e in edge_set:
            if any(v in seen for v in e):seen.update(e)
        changed=len(seen)>old
    return len(seen)==len(P)
tree_count=sum(connected(choice) for choice in combinations(E,5))
assert tree_count==75
# A bidirected graph has directed arborescences in bijection with its spanning trees.
# In a three-outregular digraph BEST gives 2! at each of six vertices.
cycle_count=tree_count*(factorial(2)**6)
assert cycle_count==4800
print('prism edges:',len(E),'spanning trees:',tree_count,'Euler tours mod rotation:',cycle_count)
