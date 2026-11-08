"""Exact census for repeated PageRank pair-ranking reversals on small trees.

Requirements: Python >=3.10 and networkx >=2.8. All arithmetic and
root-count certificates below use the Python standard library.
Run: python check.py
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb
import networkx as nx

EDGES = ((0,7),(1,0),(1,2),(1,6),(2,3),(2,4),(2,5),(7,8),(7,10),(8,9))
EXPECTED_TREE_COUNTS = {2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47,10:106,11:235}
EXPECTED_PAIR_COUNTS = {2:1,3:3,4:12,5:30,6:90,7:231,8:644,9:1692,10:4770,11:12925}


def norm(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def evalpoly(p,x):
    return sum((a*x**i for i,a in enumerate(p)),F(0))


def var(signs):
    signs=[1 if a>0 else -1 for a in signs if a]
    return sum(x!=y for x,y in zip(signs, signs[1:]))


def interval_descartes(p):
    p=norm(p)
    d=len(p)-1
    transformed=[sum((p[i]*comb(d-i,k-i) for i in range(k+1)),F(0)) for k in range(d+1)]
    return var(transformed)


def divrem(a,b):
    a=norm(a);b=norm(b)
    assert b[-1]
    while len(a)>=len(b) and a!=[0]:
        c=a[-1]/b[-1]
        off=len(a)-len(b)
        for j,v in enumerate(b):a[off+j]-=c*v
        a=norm(a)
    return a


def derivative(p):
    return norm([k*p[k] for k in range(1,len(p))] or [F(0)])


def strip_endpoints(p):
    p=norm(p)
    while len(p)>1 and p[0]==0:
        p=p[1:]
    while len(p)>1 and sum(p)==0:
        d=len(p)-1
        q=[F(0)]*d
        q[d-1]=p[d]
        for k in range(d-1,0,-1):q[k-1]=p[k]+q[k]
        assert p[0]==-q[0]
        p=norm(q)
    return p


def side_sign(p,endpoint):
    # Sign of p at 0+ or 1- without arbitrary floating-point tolerance.
    if endpoint==0:
        for c in p:
            if c:return 1 if c>0 else -1
    else:
        for k in range(len(p)):
            t=sum((p[j]*comb(j,k) for j in range(k,len(p))),F(0))
            if t:return 1 if (-1)**k*t>0 else -1
    raise ValueError('identically zero Sturm polynomial')


def sturm_count_01(p):
    p=strip_endpoints(p)
    if len(p)==1:return 0
    seq=[p,derivative(p)]
    while len(seq[-1])>1:
        r=divrem(seq[-2],seq[-1])
        if r==[0]:break
        seq.append([-v for v in r])
    return var(side_sign(q,0) for q in seq)-var(side_sign(q,1) for q in seq)


def matching_determinant(T):
    n=len(T);deg=dict(T.degree());ed=list(T.edges());h=[F(0)]*(n+1);h[0]=F(1)
    for k in range(1,n//2+1):
        s=F(0)
        for sub in combinations(ed,k):
            ends=[u for e in sub for u in e]
            if len(set(ends))!=2*k:continue
            w=F(1)
            for u,v in sub:w/=deg[u]*deg[v]
            s+=w
        h[2*k]=(-1)**k*s
    return h


def numerators(T):
    n=len(T); d=dict(T.degree()); h=matching_determinant(T)
    y=[[F(0)]*n for _ in range(n)]
    for u in T:y[u][0]=F(1)
    for k in range(1,n):
        for u in T:y[u][k]=sum((y[v][k-1]/d[v] for v in T[u]),F(0))
    nums=[[sum((h[j]*y[u][k-j] for j in range(k+1)),F(0)) for k in range(n)] for u in range(n)]
    # Check the exact polynomial linear-system identity through degree n.
    for u in T:
        for k in range(n+1):
            lhs=(nums[u][k] if k<n else F(0))
            if k:lhs-=sum((nums[v][k-1]/d[v] for v in T[u]),F(0))
            assert lhs==h[k],('resolvent identity',n,u,k)
    return nums,h


def pair_poly(nums,u,v):
    return norm([x-y for x,y in zip(nums[u],nums[v])])


def canonical_tree(T):
    return nx.to_graph6_bytes(T,header=False).decode().strip()


def run():
    found=[]
    for n in range(2,12):
        trees=list(nx.generators.nonisomorphic_trees(n))
        assert len(trees)==EXPECTED_TREE_COUNTS[n],(n,len(trees))
        pairs=0; d2=0; actual2=[]
        for ti,T in enumerate(trees):
            nums,h=numerators(T)
            for u,v in combinations(range(n),2):
                pairs+=1
                p=pair_poly(nums,u,v)
                variation=interval_descartes(p)
                if n<=10:
                    assert variation<=1,(n,ti,u,v,p)
                    continue
                if variation>=2:
                    d2+=1
                    k=sturm_count_01(p)
                    assert 0<=k<=variation
                    if k>=2:
                        actual2.append((ti,u,v))
                        found.append((T,u,v,p,h))
                elif variation==1:
                    # Exactly one or zero crossings; cannot produce two.
                    pass
        assert pairs==EXPECTED_PAIR_COUNTS[n]
        if n==11:
            assert d2==30 and len(actual2)==3
            assert actual2==[(74,3,10),(74,4,10),(74,5,10)],actual2
        print(f'n={n}: trees={len(trees)}, vertex_pairs={pairs}, '
              f'Descartes_candidates_for_2={d2}, actual_2_crossing_pairs={len(actual2)}')
    assert len(found)==3
    for T,u,v,p,h in found:
        assert set(map(frozenset,T.edges()))==set(map(frozenset,EDGES))
        assert u in (3,4,5) and v==10
        # Exact numerator factored as a*(1-a)*F(a)/144.
        Fpoly=[-F(12),F(12),F(26),-F(16),-F(18),F(4),F(3)]
        fact=[F(0)]+[Fpoly[k-1]-(Fpoly[k-2] if k>=2 else F(0)) for k in range(1,8)]+[-Fpoly[-1]]
        fact=[z/F(144) for z in fact]
        assert p==norm(fact),(p,norm(fact))
        assert h==matching_determinant(T)
    f=[F(-12),F(12),F(26),F(-16),F(-18),F(4),F(3)]
    for alpha,positive in [(F(1,2),False),(F(2,3),True),
                           (F(9,10),True),(F(19,20),False)]:
        assert (evalpoly(f,alpha)>0)==positive
    assert interval_descartes(f)==2
    assert sturm_count_01(f)==2
    print('WITNESS: one 11-vertex tree and one leaf-pair orbit (three labelled representatives).')
    print('The difference is proportional to a(1-a)F(a),')
    print(' F(a)=3a^6+4a^5-18a^4-16a^3+26a^2+12a-12.')
    print('CHECK PASS')

if __name__=='__main__':run()
