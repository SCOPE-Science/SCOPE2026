#!/usr/bin/env python3
"""Exact finite checks for the Euclidean inball of interpolated equal multipartite metrics.

Uses independently enumerated spanning-tree potential vertices for the six-point case;
no external data, no floating point, and no assumptions of the claimed radius in that enumeration.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict, deque
from math import comb

def prufer_trees(n):
    for code in product(range(n), repeat=n-2):
        deg=[1]*n
        for x in code: deg[x]+=1
        edges=[]
        for x in code:
            leaf=next(i for i in range(n) if deg[i]==1)
            edges.append((leaf,x));deg[leaf]-=1;deg[x]-=1
        a,b=[i for i in range(n) if deg[i]==1]
        yield edges+[(a,b)]

def all_exact_potentials(nparts,m,p,q):
    n=nparts*m
    dist=[[0 if i==j else (p if i//m==j//m else q) for j in range(n)]for i in range(n)]
    seen=set()
    for edges in prufer_trees(n):
        adj=[[] for _ in range(n)]
        for idx,(i,j) in enumerate(edges):
            adj[i].append((j,idx,dist[i][j]));adj[j].append((i,idx,dist[i][j]))
        for signs in product((-1,1), repeat=n-1):
            vals=[None]*n;vals[0]=0
            que=deque([0])
            while que:
                u=que.popleft()
                for v,idx,d in adj[u]:
                    if vals[v] is None:
                        vals[v]=vals[u]+(signs[idx]*d if u==edges[idx][0] else -signs[idx]*d)
                        que.append(v)
            vec=tuple(vals)
            if vec in seen:continue
            if all(abs(vec[i]-vec[j])<=dist[i][j] for i in range(n) for j in range(i)):
                seen.add(vec)
    return seen

def var(vec,scale=1):
    n=len(vec)
    return (F(sum(x*x for x in vec),1)-F(sum(vec)**2,n))/scale**2

def max_formula(k,m,t):
    n=k*m
    return max(F(n,4),F(m,4)*(t*t+(k-1)*(2-t)*(2-t)))

def predicted_contacts(k,m,t):
    N=k*m
    base=comb(N,N//2)
    if k>=4 or t<F(5,3):return base
    total=0
    if t==F(5,3): total+=base
    for q in range(1,m):
        for s in range(0,2*m+1):
            if t*(q-F(m,2))+(t-2)*(s-m)==0:
                total+=3*comb(m,q)*comb(2*m,s)
    return total

def contact_rank(vectors):
    # row rank on Q, exact rational Gauss elimination
    rows=[[F(z) for z in v] for v in vectors]
    n=len(rows[0]);piv=0
    for c in range(n):
        idx=next((r for r in range(piv,len(rows)) if rows[r][c]),None)
        if idx is None:continue
        rows[piv],rows[idx]=rows[idx],rows[piv]
        x=rows[piv][c]
        rows[piv]=[z/x for z in rows[piv]]
        for r in range(piv+1,len(rows)):
            if rows[r][c]:
                x=rows[r][c]
                rows[r]=[rows[r][j]-x*rows[piv][j] for j in range(n)]
        piv+=1
        if piv==len(rows):break
    return piv

def active_span_witnesses(k,m,t):
    n=k*m;out=[]
    for i in (0,1):
        part=list(range(i*m,(i+1)*m))
        outside=[j for j in range(n) if j//m!=i]
        highs=set(part[:m//2]);lows=set(outside[:len(outside)//2])
        choices=[(highs,lows)]
        for old in part[:m//2]:
            for new in part[m//2:]:
                choices.append(((highs-{old})|{new},lows))
        for old in outside[:len(outside)//2]:
            for new in outside[len(outside)//2:]:
                choices.append((highs,(lows-{old})|{new}))
        for h,s in choices:
            a=[t if j in h else F(0) if j//m==i else t-1 if j in s else F(1) for j in range(n)]
            out.append(tuple(v-t/2 for v in a))
    return out

def balanced_binary_span_witnesses(n):
    h=n//2;ones=set(range(h));out=[]
    choices=[ones]
    for old in range(h):
        for new in range(h,n):choices.append((ones-{old})|{new})
    for os in choices:
        out.append(tuple(F(1,2) if j in os else F(-1,2) for j in range(n)))
    return out

def run():
    tests=[F(6,5),F(7,5),F(3,2),F(8,5),F(5,3),F(9,5),F(19,10)]
    n=6
    for t in tests:
        p,q=t.numerator,t.denominator
        vs=all_exact_potentials(3,2,p,q)
        v_max=max(var(v,q) for v in vs)
        contacts=[v for v in vs if var(v,q)==v_max]
        expected=max_formula(3,2,t)
        assert v_max==expected,(t,v_max,expected)
        assert len(contacts)==predicted_contacts(3,2,t),(t,len(contacts),predicted_contacts(3,2,t))
        for x in contacts:
            assert all(F(z,q) - F(sum(x),q*len(x)) for z in x)
        centered=[tuple(F(z,q)-F(sum(x),q*len(x)) for z in x) for x in contacts]
        assert contact_rank(centered)==n-1
        print('EXACT_FULL_TIGHT_TREE_VERTEX_PASS',str(t),'vertices',len(vs),'maxvariance',str(v_max),'contacts',len(contacts),'rank',contact_rank(centered))
    # Larger examples: independent direct enumeration of all endpoint patterns (not every polar vertex)
    # for the two competing classes, plus a separate rank calculation.
    for k,m,t in [(3,4,F(3,2)),(3,4,F(5,3)),(3,4,F(9,5)),(3,6,F(5,3)),(3,6,F(12,7)),(4,2,F(19,10)),(4,4,F(19,10)),(5,2,F(19,10))]:
        n=k*m
        vmax=max_formula(k,m,t)
        baseline=F(n,4)
        # exact maximization over all binary configurations, enumerated by cardinality
        vbin=max(F(s*(n-s),n) for s in range(n+1))
        assert vbin==baseline
        # active outside endpoint count -> compute exact scores by integer counts
        score=F(-1)
        for q in range(1,m):
            for s in range((k-1)*m+1):
                L=(k-1)*m;S=q*t+s*(t-2)+L
                V=q*t*t+s*(t-1)**2+(L-s)-S*S/n
                score=max(score,V)
        assert max(score,vbin)==vmax,(k,m,t,score,vbin,vmax)
        expected=F(m,4)*(t*t+(k-1)*(2-t)**2)
        assert score==expected
        if k==3:
            b,a=balanced_binary_span_witnesses(n),active_span_witnesses(k,m,t)
            if t<=F(5,3):assert contact_rank(b)==n-1
            if t>=F(5,3):assert contact_rank(a)==n-1
            print('ENDPOINT_EXTREMAL_ENUMERATION_PASS',k,m,str(t),'max',str(vmax),'contacts',predicted_contacts(k,m,t))
        else:
            print('ENDPOINT_EXTREMAL_ENUMERATION_PASS',k,m,str(t),'max',str(vmax),'balanced_binary_contacts',comb(n,n//2))
    assert predicted_contacts(3,6,F(12,7))==3*comb(6,3)*comb(12,6)+90
    assert predicted_contacts(3,6,F(5,3))==comb(18,9)+3*comb(6,3)*comb(12,6)+1080
    print('TRIPARTITE_INBALL_TRANSITION_AND_RESONANCE_ALL_CHECKS_PASS')

if __name__=='__main__':run()
