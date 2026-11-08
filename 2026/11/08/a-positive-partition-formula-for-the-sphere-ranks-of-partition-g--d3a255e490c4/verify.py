"""Independent finite checks of a positive partition formula for partition-graph sphere ranks.
Standard library only. All dates and research provenance are omitted.
Run: python3 verify.py
"""
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def partitions(n, ceiling=None):
    if n == 0:
        return ((),)
    if ceiling is None:
        ceiling = n
    return tuple((a,) + p for a in range(min(n, ceiling), 0, -1)
                 for p in partitions(n-a, a))

def conjugate(p):
    return tuple(sum(part >= j for part in p) for j in range(1,max(p)+1))

def sphere_weight(p):
    h = sorted(set(conjugate(p)), reverse=True)
    s = len(h)
    if s < 3:
        return 0
    return (comb(s-2, 2) if s >= 4 else 0) + sum(
        h[i] - h[i+1] >= 2 for i in range(1, s-1))

def graph_neighbors(p):
    """Independently enumerate one-cell transfers among rows, with a new row allowed."""
    vals = list(p) + [0]
    ans = set()
    for i in range(len(p)):
        for j in range(len(vals)):
            if i == j:
                continue
            b = vals.copy()
            b[i] -= 1
            b[j] += 1
            out = tuple(sorted((x for x in b if x > 0), reverse=True))
            if out != p:
                ans.add(out)
    return ans

def lower_link_contribution(p):
    low = [x for x in graph_neighbors(p) if conjugate(x) < conjugate(p)]
    e = {i:set() for i in range(len(low))}
    for i,j in combinations(range(len(low)), 2):
        if low[j] in graph_neighbors(low[i]):
            e[i].add(j)
            e[j].add(i)
    # Independent exhaustive clique count for the lower link.
    clique_euler = 0
    for mask in range(1, 1 << len(low)):
        ix = [i for i in range(len(low)) if (mask >> i) & 1]
        if all(j in e[i] for i,j in combinations(ix, 2)):
            clique_euler += (-1)**(len(ix)-1)
    return 1-clique_euler

def addpoly(dst, src, weight):
    """Add src times q^(a)+q^(2a)+... where weight is a."""
    N = len(dst)-1
    for i,v in enumerate(src):
        if v:
            for k in range(weight,N-i+1,weight):
                dst[i+k] += v

def addmarked(dst, src, weight):
    """Add src times q^(2a)+q^(3a)+..., gap >= 2."""
    N=len(dst)-1
    for i,v in enumerate(src):
        if v:
            for k in range(2*weight,N-i+1,weight):
                dst[i+k] += v

def q_series(N):
    # The first state computes the elementary-symmetric polynomial in
    # f_a=q^a/(1-q^a), i.e. partitions with a fixed number of distinct heights.
    E=[[0]*(N+1) for _ in range(N+1)]
    E[0][0]=1
    for a in range(1,N+1):
        for s in range(N,0,-1):
            addpoly(E[s], E[s-1], a)
    base=[sum(comb(s-2,2)*E[s][n] for s in range(4,N+1)) for n in range(N+1)]
    # State machine for one *internal* gap of size >= 2:
    # no selection; a prior selection; a marked gap with no later selection;
    # a marked gap with at least one later selection.
    states=[[0]*(N+1) for _ in range(4)]
    states[0][0]=1
    for a in range(1,N+1):
        new=[row.copy() for row in states] # skip value a
        addpoly(new[1],states[0],a)
        addpoly(new[1],states[1],a)
        addmarked(new[2],states[1],a)
        addpoly(new[3],states[2],a)
        addpoly(new[3],states[3],a)
        states=new
    return [base[n]+states[3][n] for n in range(N+1)]

if __name__ == '__main__':
    # This check uses a different graph construction from the positive formula.
    local_checks=0
    for n in range(1,18):
        total=0
        for p in partitions(n):
            c=lower_link_contribution(p)
            target=sphere_weight(p)+(1 if p==(n,) else 0)
            assert c==target, (n,p,c,target)
            total+=c
            local_checks+=1
        assert total-1==sum(map(sphere_weight,partitions(n)))
    print('EXHAUSTIVE_LOCAL_LINK_CHECKS',local_checks,'PASS')

    coeff=q_series(50)
    partition_checks=0
    for n in range(1,36):
        expected=sum(sphere_weight(p) for p in partitions(n))
        assert coeff[n]==expected,(n,coeff[n],expected)
        partition_checks+=len(partitions(n))
    print('INDEPENDENT_Q_SERIES_CHECKS',partition_checks,'PASS')

    published = (0,0,0,0,0,0,0,1,2,5,10,19,32,55,87,137,207,310,
                 451,652,921,1293,1787,2453,3324)
    assert coeff[1:26] == list(published)
    print('PUBLISHED_RANKS_1_TO_25 PASS')
    print('EXACT_RANKS_26_TO_50',','.join(map(str,coeff[26:51])))
    print('ALL_VERIFY_OK')
