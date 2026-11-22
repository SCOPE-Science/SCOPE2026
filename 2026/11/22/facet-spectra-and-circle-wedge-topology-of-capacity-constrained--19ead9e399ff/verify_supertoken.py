#!/usr/bin/env python3
"""Standalone finite checks of capacity-constrained labelled-token clique facets.
This is finite corroboration; the general theorem is established separately."""
import itertools,math
from collections import Counter
import networkx as nx
from fractions import Fraction

def coeff_power(lim,n,d):
    if d<0:return Fraction(0)
    p=[Fraction(1)]+[Fraction(0)]*d
    for _ in range(n):
        q=[Fraction(0)]*(d+1)
        for j,c in enumerate(p):
            if c:
                for a in range(min(lim,d-j)+1):q[j+a]+=c/Fraction(math.factorial(a))
        p=q
    return p[d]

def coefficient_prediction(n,s,k):
    V=math.factorial(k)*coeff_power(s,n,k)
    facets=Counter()
    for f in range(n-1):
        m=math.comb(n,f)*math.factorial(k-1)*coeff_power(s-1,n-f,k-1-s*f)/math.factorial(s)**f
        assert m.denominator==1
        if m:facets[n-f]=int(k*m)
    return int(V),facets,int(1-V+sum((t-1)*v for t,v in facets.items()))


def admissible(n,s,k):
    for tup in itertools.product(range(n),repeat=k):
        if max(Counter(tup).values())<=s:
            yield tup

def predicted(n,s,k):
    V=sum(1 for a in itertools.product(range(n),repeat=k) if max(Counter(a).values())<=s)
    if k>=n*s: return V,Counter({1:V}),None
    # Count partial assignments independently, without building graph or facets.
    partial=Counter()
    for z in itertools.product(range(n),repeat=k-1):
        if max(Counter(z).values(),default=0)>s: continue
        full=sum(Counter(z).get(v,0)==s for v in range(n))
        if n-full>=2: partial[n-full]+=1
    faces=Counter({size:k*num for size,num in partial.items()})
    beta=1-V+sum((t-1)*c for t,c in faces.items())
    return V,faces,beta

def test(n,s,k):
    vertices=list(admissible(n,s,k))
    if len(vertices)>420:return 0
    H=nx.Graph(); H.add_nodes_from(vertices)
    for v in vertices:
        for i in range(k):
            for w in range(n):
                if w==v[i]:continue
                u=v[:i]+(w,)+v[i+1:]
                if u in H: H.add_edge(v,u)
    cliques=list(nx.find_cliques(H))
    hist=Counter(len(c) for c in cliques)
    V,F,B=predicted(n,s,k)
    if k<n*s:
        CV,CF,CB=coefficient_prediction(n,s,k)
        assert (V,F,B)==(CV,CF,CB),(n,s,k,"COEFFICIENT",(V,F,B),(CV,CF,CB))
    assert len(vertices)==V,(n,s,k,'V',V,len(vertices))
    assert hist==F,(n,s,k,'FACETS',hist,F)
    if k<n*s:
        assert nx.is_connected(H),(n,s,k,'DISCONNECTED')
        f=[V]+[sum(math.comb(t,j)*cnt for t,cnt in F.items()) for j in range(2,n+1)]
        # Euler characteristic from clique counts (including vertices).
        chi=V+sum((-1)**(j-1)*num for j,num in enumerate(f[1:],start=2))
        assert B==1-chi,(n,s,k,'BETTI',B,1-chi)
        if n>=3:
            expected_pure = (k<=s or k==n*s-1)
            assert (len(F)==1)==expected_pure,(n,s,k,'PURITY',F)
    else:
        assert len(H.edges())==0,(n,s,k,'FULL')
    print('CHECK',n,s,k,'vertices',V,'facets',dict(sorted(F.items())),'beta1',B)
    return 1

if __name__=='__main__':
    count=0
    for n in range(2,5):
        for s in range(2,5):
            for k in range(1,min(n*s,7)+1):
                count+=test(n,s,k)
    print('TESTED_INSTANCES',count,'VERIFY_OK')
