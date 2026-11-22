#!/usr/bin/env python3
"""Reconstruct half-spin generators and independently check small Boolean trace data."""
from itertools import combinations
from functools import lru_cache
from math import comb

def test(n):
    m=2*n; lim=1<<m; mask=(1<<n)-1
    def q(v): return ((v&mask)&(v>>n)).bit_count()%2
    def b(v,w): return (((v&mask)&(w>>n))^((w&mask)&(v>>n))).bit_count()%2
    points=[v for v in range(1,lim) if q(v)==0]
    sub=[{(0,)}]
    for k in range(1,n+1):
        new=set()
        for s in sub[-1]:
            for v in points:
                if v not in s and all(b(v,u)==0 for u in s):
                    new.add(tuple(sorted(set(s)|{u^v for u in s})))
        sub.append(new)
    E={v for v in range(1<<n)}
    # Correct intersection dimension: len=2^dimension, so dim=bit_length-1
    half=[s for s in sub[n] if (n-((len(set(s)&E)).bit_length()-1))%2==0]
    assert len(half)*2==len(sub[n])
    genmasks=[sum(1<<points.index(v) for v in s if v) for s in half]
    def shattered(I):
        need=1<<len(I); traces=set()
        for mask0 in genmasks:
            t=sum(((mask0>>i)&1)<<j for j,i in enumerate(I));traces.add(t)
            if len(traces)==need:return True
        return False
    print('n',n,'singular points',len(points),'all generator count',len(sub[n]),'one ruling',len(half),'subspace_counts',[len(s) for s in sub])
    if n==3:
        poly=[1]
        for k in range(1,4):
            poly.append(sum(shattered(s) for s in combinations(range(len(points)),k)))
        assert poly==[1,35,315,0],poly
        # Ldim recurrence
        @lru_cache(None)
        def depth(M):
            res=0
            for i in range(len(points)):
                a=tuple(m for m in M if (m>>i)&1);c=tuple(m for m in M if not((m>>i)&1))
                if a and c:
                    res=max(res,1+min(depth(a),depth(c)))
            return res
        assert depth(tuple(genmasks))==2
        print('  polynomial',poly,'littlestone',depth(tuple(genmasks)),'beta1',poly[2]-poly[1]+1)
    if n==4:
        faces=set()
        for s in half:
            pts=[points.index(v) for v in s if v]
            for triple in combinations(pts,3):
                if (points[triple[0]]^points[triple[1]])!=points[triple[2]]:faces.add(triple)
        assert len(faces)==56700,len(faces)
        assert len(set(tuple(sorted((i,j))) for s in faces for i,j in combinations(s,2)))==4725
        # all 135 singleton and 4725 orthogonal pairs; sample 1000 independent triples
        for j,s in enumerate(sorted(faces)):
            if j%57==0:assert shattered(s),s
        print('  predicted polynomial [1,135,4725,56700], checked triple sample and exact facets')
for n in (2,3,4):test(n)
