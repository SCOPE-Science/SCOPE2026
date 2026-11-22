"""Independent full-state numerical check with 680 Markov states (120 pairs+560 triples).
Requires scipy and numpy. Symmetry and exact rational code are not used.
"""
from itertools import combinations
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
import numpy as np

def neighbors(which):
    z=[]
    for i in range(16):
        x,y=divmod(i,4); row=[]
        for j in range(16):
            a,b=divmod(j,4)
            if which=='rook': edge=(x==a or y==b) and j!=i
            else: edge=((a-x)%4,(b-y)%4) in [(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)]
            if edge:row.append(j)
        assert len(row)==6
        z.append(row)
    return z

for name in ['rook','shrikhande']:
    adj=neighbors(name)
    states=list(combinations(range(16),2))+list(combinations(range(16),3))
    ix={x:k for k,x in enumerate(states)}
    L=lil_matrix((len(states),len(states)),dtype=float)
    rhs=np.ones(len(states))
    for k,s in enumerate(states):
        L[k,k]=len(s)
        for a in s:
            for b in adj[a]:
                dest=tuple(sorted((set(s)-{a})|{b}))
                if len(dest)>1:L[k,ix[dest]]-=1/6
    t=spsolve(L.tocsr(),rhs)
    triangles=[tuple(sorted(q)) for q in combinations(range(16),3) if all(a in adj[b] for a,b in combinations(q,2))]
    assert len(triangles)==32
    v=np.mean([t[ix[x]] for x in triangles]);avg=np.mean([t[ix[x]] for x in combinations(range(16),3)])
    print(name, 'triangle',repr(v),'uniform',repr(avg))
    exact=143/14 if name=='rook' else 1145/112
    assert abs(v-exact)<1e-10
    assert abs(avg-2203/196)<1e-10
print('PASS full 680-state sparse computation')
