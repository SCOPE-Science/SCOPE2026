"""Finite checks for nonparallel two-line incidence concept classes.

Run with Python 3.10 or later; no third-party dependencies.
"""
from functools import lru_cache
from itertools import combinations, product
from math import comb


def plus(q,a,b):
    return a ^ b if q == 4 else (a+b)%q


def times(q,a,b):
    if q != 4:
        return a*b%q
    # GF(4) = GF(2)[t]/(t*t+t+1), low-bit polynomial encoding.
    c=0
    for j in range(2):
        if (b>>j)&1: c ^= a<<j
    if (c>>2)&1: c ^= 7
    return c


def family(q):
    points=list(product(range(q),repeat=2))
    lines=[]
    directions=[]
    for x in range(q):
        lines.append(frozenset(i for i,p in enumerate(points) if p[0]==x))
        directions.append(q)
    for slope in range(q):
        for intercept in range(q):
            lines.append(frozenset(i for i,p in enumerate(points)
                                   if p[1]==plus(q,times(q,slope,p[0]),intercept)))
            directions.append(slope)
    assert len(lines)==q*(q+1) and len(set(lines))==len(lines)
    assert all(len(line)==q for line in lines)
    concepts=[]
    for i in range(len(lines)):
        for j in range(i):
            if directions[i]!=directions[j]:
                assert len(lines[i]&lines[j])==1
                concepts.append(lines[i]|lines[j])
    assert len(concepts)==q*q*comb(q+1,2)
    concepts=sorted(set(concepts), key=lambda s: tuple(sorted(s)))
    queries=[]
    for p in range(q*q):
        mask=0
        for i,c in enumerate(concepts):
            if p in c: mask|=1<<i
        queries.append(mask)
    return points,concepts,queries


def rank(query,n):
    @lru_cache(None)
    def compute(mask):
        ans=0
        for col in query:
            yes=mask&col
            no=mask^yes
            if not yes or not no:continue
            if min(yes.bit_count(),no.bit_count()) < 1<<ans:
                continue  # Can't improve the current lower bound.
            candidate=1+min(compute(yes),compute(no))
            ans=max(ans,candidate)
        return ans
    return compute((1<<n)-1),compute.cache_info().currsize


def all_traces(query,n,support):
    return {sum(1<<j for j,p in enumerate(support)
                if query[p]>>i&1) for i in range(n)}


def run():
    expected={2:(4,1),3:(54,4),4:(160,5),5:(375,5)}
    for q in (2,3,4,5):
        points,concepts,queries=family(q)
        n=len(concepts)
        assert n==expected[q][0]
        result,states=rank(queries,n)
        assert result==expected[q][1],(q,result)
        if q==3:
            witness=[(0,0),(0,1),(1,0),(1,1)]
        elif q in (4,5):
            witness=[(0,0),(0,1),(0,2),(1,0),(2,0)]
        else:
            witness=[(0,0)]
        ids=[points.index(p) for p in witness]
        assert len(all_traces(queries,n,ids))==1<<len(ids)
        print('order',q,'distinct_concepts',n,'Ldim',result,'memoized_states',states,
              'witness_size',len(ids),flush=True)
    print('TWO_LINE_AFFINE_ONLINE_PASS',flush=True)

if __name__=='__main__':run()
