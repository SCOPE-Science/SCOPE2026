#!/usr/bin/env python3
"""Exact rational checks for graph tree edge-band least-squares variation sensitivity.
No external dependencies. Tests block averaging vs cut formula and topology thresholds.
"""
from fractions import Fraction as Q
from itertools import product
from collections import deque

def components(n, edges):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    out=[];seen=set()
    for a in range(n):
        if a in seen: continue
        q=[a];seen.add(a)
        for v in q:
            for w in adj[v]:
                if w not in seen:seen.add(w);q.append(w)
        out.append(set(q))
    return out

def side(n,edges,e):
    a,b=e
    adj=[[] for _ in range(n)]
    for x,y in edges:
        if (x,y)==e:continue
        adj[x].append(y);adj[y].append(x)
    S={a}; q=[a]
    for v in q:
        for w in adj[v]:
            if w not in S:S.add(w);q.append(w)
    assert b not in S
    return S

def project(n, all_edges, active, masses, z):
    r=[Q(0)]*n
    for B in components(n,active):
        value=sum(masses[v]*z[v] for v in B)/sum(masses[v] for v in B)
        for v in B:r[v]=value
    return r

def var(edges,z):return sum((abs(z[b]-z[a]) for a,b in edges), Q(0))

def cut_formula(n,edges,active,masses,e):
    S=side(n,edges,e)
    B=next(B for B in components(n,active) if e[0] in B)
    if e[1] not in B:return Q(1)
    AA=B&S;CC=B-S
    x=sum(masses[v] for v in AA);y=sum(masses[v] for v in CC)
    bA=sum(1 for a,b in edges if ((a in AA and b not in B) or (b in AA and a not in B)))
    bC=sum(1 for a,b in edges if ((a in CC and b not in B) or (b in CC and a not in B)))
    return (bA*y+bC*x)/(x+y)

def full_check(n,edges,masses):
    k=Q(0)
    for mask in range(1<<len(edges)):
        active=[e for i,e in enumerate(edges) if mask>>i & 1]
        for e in edges:
            S=side(n,edges,e)
            z=[Q(int(v in S)) for v in range(n)]
            p=project(n,edges,active,masses,z)
            v=var(edges,p)
            f=cut_formula(n,edges,active,masses,e)
            assert v == f,(n,edges,active,e,masses,v,f)
            k=max(k,v)
    return k

def prufer(n, seq):
    deg=[1]*n
    for v in seq:deg[v]+=1
    edges=[]
    for v in seq:
        u=min(i for i in range(n) if deg[i]==1)
        edges.append(tuple(sorted((u,v))));deg[u]-=1;deg[v]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    edges.append(tuple(sorted((a,b))))
    return tuple(sorted(edges))

def is_path(n,edges):
    deg=[0]*n
    for a,b in edges:deg[a]+=1;deg[b]+=1
    return max(deg,default=0)<=2

def is_claw(n,edges):
    deg=[0]*n
    for a,b in edges:deg[a]+=1;deg[b]+=1
    return n==4 and sorted(deg)==[1,1,1,3]


def strict_face_witness(n, edges, active, masses, e):
    """Exact KKT witness at boxes [-1,1] for a nontrivial active forest."""
    # Construct a feasible vertex potential: active edges saturate the upper bound;
    # inactive edges have zero differences. A tree has no compatibility obstructions.
    adj=[[] for _ in range(n)]
    for a,b in edges:
        t=Q(1) if (a,b) in active else Q(0)
        adj[a].append((b,t));adj[b].append((a,-t))
    u=[None]*n;u[0]=Q(0);q=[0]
    for v in q:
        for w,t in adj[v]:
            if u[w] is None:u[w]=u[v]+t;q.append(w)
    def incidence_transpose(lam):
        r=[Q(0)]*n
        for (a,b),v in lam.items():r[a]-=v;r[b]+=v
        return r
    r0=incidence_transpose({ed:Q(1) for ed in active})
    y=[u[i]+r0[i]/masses[i] for i in range(n)]
    S=side(n,edges,e)
    h=[Q(int(i in S)) for i in range(n)]
    ph=project(n,edges,active,masses,h)
    t=Q(1,10000)
    un=[u[i]+t*ph[i] for i in range(n)]
    yn=[y[i]+t*h[i] for i in range(n)]
    # Solve the KKT edge multipliers on the active forest by exact leaf elimination.
    rhs=[masses[i]*(yn[i]-un[i]) for i in range(n)]
    pending=set(active);ans={}
    while pending:
        deg=[0]*n
        for a,b in pending:deg[a]+=1;deg[b]+=1
        v=next(i for i in range(n) if deg[i]==1)
        edge=next(ed for ed in pending if v in ed)
        a,b=edge; sigma=Q(1) if b==v else Q(-1)
        val=rhs[v]/sigma
        assert val>0, (edge,val)
        ans[edge]=val
        rhs[a if v==b else b]+=rhs[v]
        rhs[v]=Q(0)
        pending.remove(edge)
    assert all(x==0 for x in rhs)
    for a,b in edges:
        d=un[b]-un[a]
        if (a,b) in active: assert d==1
        else: assert -1<d<1
    return var(edges,[un[i]-u[i] for i in range(n)])/var(edges,[yn[i]-y[i] for i in range(n)])

def main():
    counts=0
    for n in range(2,6):
        for seq in product(range(n),repeat=n-2):
            E=prufer(n,seq)
            m=[Q(1)]*n
            v=full_check(n,E,m)
            assert (v==1)==(is_path(n,E) or is_claw(n,E)),(n,E,v)
            counts+=1
    print('ALL_LABELED_TREES_THROUGH_FIVE_EXACT_UNWEIGHTED_RIGIDITY_PASS',counts)
    E=((0,1),(0,2),(0,3))
    assert full_check(4,E,[Q(1),Q(1),Q(1),Q(1)])==1
    assert full_check(4,E,[Q(1),Q(10),Q(1),Q(1)])==Q(20,11)
    assert full_check(4,E,[Q(10),Q(1),Q(1),Q(1)])==1
    print('THREE_LEAF_STAR_WEIGHTED_PHASE_CHECK_PASS')
    E=((0,1),(1,2),(2,3),(3,4),(4,5))
    assert full_check(6,E,[Q(1),Q(4),Q(3),Q(2),Q(5),Q(1)])==1
    print('PATH_MASS_INDEPENDENT_CONTRACTION_PASS')
    E=((0,1),(1,2),(1,3),(3,4))
    v=full_check(5,E,[Q(1)]*5)
    assert v>=Q(3,2)
    print('BRANCHING_TREE_UNIFORM_MASS_INSTABILITY_PASS',str(v))
    E=((0,1),(0,2),(0,3),(0,4))
    assert full_check(5,E,[Q(1)]*5)==Q(3,2)
    print('FOUR_LEAF_STAR_UNIFORM_MASS_SHARP_GAIN_PASS')
    assert strict_face_witness(4,((0,1),(0,2),(0,3)),[(0,1)],[Q(1),Q(10),Q(1),Q(1)],(0,1))==Q(20,11)
    print('EXACT_STRICT_FACE_KKT_FINITE_PERTURBATION_WITNESS_PASS')
    E=((0,1),(0,3),(0,4),(1,2),(2,5))
    assert full_check(6,E,[Q(1)]*6)==Q(5,3)
    assert cut_formula(6,E,[(0,1),(1,2)],[Q(1)]*6,(0,1))==Q(5,3)
    print('SIX_VERTEX_NONLOCAL_FIVE_THIRDS_GAIN_PASS')
    for m in range(2,9):
        k=2*m
        cat=[(i,i+1) for i in range(k-1)]+[(i,k+i-1) for i in range(1,k-1)]
        assert cut_formula(2*k-2,cat,[(i,i+1) for i in range(k-1)],
                           [Q(1)]*(2*k-2),(m-1,m))==m-1
    print('SUBCUBIC_CATERPILLAR_LINEAR_AMPLIFICATION_PASS')
    print('ALL_TREE_EDGE_BAND_VARIATION_CERTIFICATES_PASS')
if __name__=='__main__':main()
