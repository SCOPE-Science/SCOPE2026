#!/usr/bin/env python3
"""Exhaustive literal graph checks for mutual visibility in 3 by n rook graphs.

No third-party packages are needed. All vertices/columns are labeled.
"""
from collections import Counter
from math import comb, factorial


def falling(n,j):
    p=1
    for k in range(j): p*=n-k
    return p


def expected_visibility(n):
    a=Counter()
    for j in range(4):
        if j>n: continue
        factor=comb(3,j)*falling(n,j)
        for t in range(n-j+1):
            a[2*j+t]+=factor*comb(n-j,t)*3**t
    for t in range(n):
        a[3+t]+=n*comb(n-1,t)*3**t
    return a


def expected_facets(n):
    a=Counter({n+2:n*3**(n-1)+3*falling(n,2)})
    if n>=3: a[n+3]=falling(n,3)*3**(n-3)
    return a


def structural_type(supports):
    n=len(supports)
    if 0 in supports: return None
    triples=[i for i,x in enumerate(supports) if x.bit_count()==3]
    if len(triples)==1 and all(x.bit_count()==1 for i,x in enumerate(supports) if i!=triples[0]):
        return 'triple_with_singletons'
    if triples: return None
    pairs=[x for x in supports if x.bit_count()==2]
    if len(pairs)==2 and len(set(pairs))==2:
        common=pairs[0]&pairs[1]
        if all(x==common for x in supports if x.bit_count()==1):return 'two_pairs_with_singletons'
    if len(pairs)==3 and len(set(pairs))==3:
        if all(x.bit_count()==1 for x in supports if x not in pairs):return 'three_pairs_with_singletons'
    return None


def verify(n):
    v=3*n
    # Adjacency of K_3 square K_n, built independently of the C4 correspondence.
    adj=[]
    for p in range(v):
        row,col=divmod(p,n)
        adj.append(sum(1<<q for q in range(v) if q!=p and (q//n==row or q%n==col)))
    common={(p,q):adj[p]&adj[q] for p in range(v) for q in range(p+1,v) if not (adj[p]>>q)&1}
    observed=Counter();facets=Counter();types=Counter()
    # Literal visibility test: for each nonadjacent selected pair, one common
    # neighbor must be outside the selected set. Diameter is exactly 2.
    def visible(S):
        for (p,q),mid in common.items():
            if ((S>>p)&1) and ((S>>q)&1) and not (mid&~S): return False
        return True
    for S in range(1<<v):
        if not visible(S): continue
        observed[S.bit_count()]+=1
        maximal=True
        for p in range(v):
            if not ((S>>p)&1) and visible(S|(1<<p)):
                maximal=False; break
        if maximal:
            facets[S.bit_count()]+=1
            supports=[sum((1<<r) for r in range(3) if ((S>>(r*n+c))&1)) for c in range(n)]
            kind=structural_type(supports)
            assert kind is not None,(n,S,supports)
            types[kind]+=1
    assert observed==expected_visibility(n),(n,observed,expected_visibility(n))
    assert facets==expected_facets(n),(n,facets,expected_facets(n))
    print('PROFILE_OK',n,'subsets',1<<v,'visibility_sets',sum(observed.values()),
          'maximal_counts',dict(sorted(facets.items())),'types',dict(sorted(types.items())))
    return 1<<v


def main():
    total=0
    for n in range(2,7): total+=verify(n)
    # Arithmetic evaluations beyond the exhaustive range.
    for n in range(2,91):
        v=expected_visibility(n)
        f=expected_facets(n)
        assert max(v)==(n+3 if n>=3 else n+2)
        assert min(f)==n+2
        assert sum(v.values())==sum(v[k] for k in v)
    print('VERIFY_OK','literal_graph_profiles=5','all_initial_subsets='+str(total),
          'visibility_polynomial=PASS','all_maximal_sets=PASS','nonpure_facet_profile=PASS',
          'arithmetic_profiles=89')


if __name__=='__main__':main()
