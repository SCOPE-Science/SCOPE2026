"""Independent vertex-wise time updates for reversible waves on J(n,2).
Uses only the standard Python library.  Deterministic finite checks, not a proof for all n.
"""
from itertools import combinations, product
from collections import Counter
from random import Random

def edges_and_neighbors(n):
    vertices=list(combinations(range(n),2))
    neighbors=[[j for j,w in enumerate(vertices) if i!=j and len(set(v)&set(w))==1] for i,v in enumerate(vertices)]
    return vertices,neighbors

def evolve(state,neighbors):
    u,v=state
    next_u=tuple((sum(u[j] for j in nbrs)-v[i])%3 for i,nbrs in enumerate(neighbors))
    return next_u,u

def primitive_period(state,neighbors,cap):
    old=state
    for t in range(1,cap+1):
        state=evolve(state,neighbors)
        if state==old:return t
    raise AssertionError(('orbit not found',cap))

def expected(n,t):
    N=n*(n-1)//2
    h=t;g=1
    while h%3==0:
        g*=3;h//=3
    if n%3==0:
        return min(4,g)+(n-2)*min(2,g)+(N-n)*min(2,g)*(t%2==0)
    if n%3==1:
        return 2*(n-1)*(t%4==0)+(t%2==0)*(min(4,g)+(N-n-1)*min(2,g))
    return 2*(t%4==0)+(t%2==0)*((n-1)*min(4,g)+(N-2*n+1)*min(2,g))

if __name__=='__main__':
    _,adj=edges_and_neighbors(3)
    hist=Counter(primitive_period((tuple(u),tuple(v)),adj,9) for u in product(range(3),repeat=3) for v in product(range(3),repeat=3))
    assert dict(hist)=={1:9,3:234,9:486},hist
    print('n=3, all 729 two-time-level states, primitive periods:',dict(sorted(hist.items())))
    rng=Random(271828)
    for n in (4,5,6,7,8):
        vertices,adj=edges_and_neighbors(n)
        N=len(vertices);L=18 if n%3==0 else 36
        for k in range(120):
            init=(tuple(rng.randrange(3) for _ in vertices),tuple(rng.randrange(3) for _ in vertices))
            per=primitive_period(init,adj,L)
            assert L%per==0
        print(f'n={n}, vertices={N}, randomized direct trajectories=120, all closed within {L}')
    print('PASS: independent direct-update checks')
