#!/usr/bin/env python3
"""Reproducible finite checks for marked-vertex leaf-neighbor fluctuations."""
from fractions import Fraction
from collections import defaultdict
from math import isclose

def transitions(n,d,l):
    T = 2*(n-1)
    assert 0 <= l <= d and d >= 1, (n,d,l)
    z = [(Fraction(d,T),(d+1,l+1)), (Fraction(l,T),(d,l-1)), (Fraction(T-d-l,T),(d,l))]
    assert all(p>=0 for p,_ in z) and sum((p for p,_ in z), Fraction())==1
    return [(p,s) for p,s in z if p] 

def check_conditional(n,d,l):
    a=Fraction(2*l-d,2); T=2*(n-1)
    z=transitions(n,d,l)
    da=sum((p*(Fraction(2*ll-dd,2)-a) for p,(dd,ll) in z),Fraction())
    dz2=sum((p*(Fraction(2*ll-dd,2)-a)**2 for p,(dd,ll) in z),Fraction())
    assert da==-a/T
    assert dz2==Fraction(d,4*T)+Fraction(l,T)

counts=0
states={(1,1):Fraction(1)}
# vertex 1 at size 2
for n in range(2,23):
    assert sum(states.values(),Fraction())==1
    for (d,l),p in states.items():
        check_conditional(n,d,l); counts+=2
    if n==22: break
    nxt=defaultdict(Fraction)
    for (d,l),p in states.items():
        for w,s in transitions(n,d,l):
            nxt[s]+=p*w
    states=dict(nxt)
# independently enumerate all labeled tree histories through size 8
histories={(0,):Fraction(1)} # parent of vertex 2 is 1; parent indices zero-based
for n in range(2,9):
    agg=defaultdict(Fraction)
    for pa,prob in histories.items():
        deg=[0]*n
        for j,p in enumerate(pa,start=1): deg[j]+=1; deg[p]+=1
        leaf=[0]*n
        for j,p in enumerate(pa,start=1):
            if deg[j]==1: leaf[p]+=1
            if deg[p]==1: leaf[j]+=1
        a=Fraction(2*leaf[0]-deg[0],2)
        agg[(deg[0],leaf[0])]+=prob
        check_conditional(n,deg[0],leaf[0]); counts+=2
    if n==8: break
    # save actual PA marginal DP comparison at n for root 1
    if n==2: ref={(1,1):Fraction(1)}
    assert dict(agg)==ref, (n,'distribution mismatch')
    new=defaultdict(Fraction)
    for pa,prob in histories.items():
        deg=[0]*n
        for j,p in enumerate(pa,start=1): deg[j]+=1; deg[p]+=1
        for k,d in enumerate(deg):
            new[pa+(k,)]+=prob*Fraction(d,2*(n-1))
    histories=dict(new)
    update=defaultdict(Fraction)
    for (d,l),prob in ref.items():
        for w,s in transitions(n,d,l): update[s]+=prob*w
    ref=dict(update)
print('PASS exact marked-root transition and independent tree-history census; assertions:', counts)
# For two marked vertices of degree at least two, one new attachment
# cannot change both marked centered leaf-neighbor statistics.
checked_pairs=0
for pa,prob in histories.items():
    n=len(pa)+1
    deg=[0]*n
    adj=[set() for _ in range(n)]
    for j,p in enumerate(pa,1):
        deg[j]+=1;deg[p]+=1
        adj[j].add(p);adj[p].add(j)
    leaves=[sum(deg[w]==1 for w in adj[v]) for v in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if min(deg[u],deg[v])<2: continue
            au=leaves[u]-deg[u]/2; av=leaves[v]-deg[v]/2
            for parent in range(n):
                dd=deg.copy();dd[parent]+=1
                l2=[]
                for x in [u,v]:
                    l2.append(sum(dd[w]==1 for w in adj[x]) + int(parent==x))
                du=l2[0]-dd[u]/2-au
                dv=l2[1]-dd[v]/2-av
                assert du*dv==0,(pa,u,v,parent,du,dv)
                checked_pairs+=1
print('PASS non-simultaneous increment test for two nonleaf hubs:',checked_pairs,'cases')

# A finite-n check of the asymptotic coefficient; this is diagnostic only.
st={(1,1):1.0}
for n in range(2,351):
    if n in (50,150,350):
        d=sum(p*k for (k,l),p in st.items())
        a2=sum(p*(l-k/2)**2 for (k,l),p in st.items())
        assert abs(a2/d-0.25)< 0.012, (n,a2/d)
        print('finite coefficient diagnostic', n, 'E[A^2]/E[D]=',round(a2/d,9))
    if n==350:break
    nxt=defaultdict(float); T=2*(n-1)
    for (d,l),p in st.items():
        nxt[d+1,l+1]+=p*d/T
        if l: nxt[d,l-1]+=p*l/T
        if T-d-l: nxt[d,l]+=p*(T-d-l)/T
    st=nxt
print('ALL MARKED-VERTEX CHECKS PASSED')
# Independently check the actual transition for every marked birth label.
all_mark_transition_checks=0
for pa,prob in histories.items():
    n=len(pa)+1
    degree=[0]*n; neighborhood=[set() for _ in range(n)]
    for j,parent in enumerate(pa,1):
        degree[j]+=1; degree[parent]+=1
        neighborhood[j].add(parent); neighborhood[parent].add(j)
    leafcount=[sum(degree[w]==1 for w in neighborhood[v]) for v in range(n)]
    for parent in range(n):
        next_degree=degree.copy(); next_degree[parent]+=1
        for mark in range(n):
            newleaf=sum(next_degree[w]==1 for w in neighborhood[mark])+int(parent==mark)
            increment=(newleaf-next_degree[mark]/2)-(leafcount[mark]-degree[mark]/2)
            expected=.5 if parent==mark else (-1 if parent in neighborhood[mark] and degree[parent]==1 else 0)
            assert increment==expected,(pa,mark,parent,increment,expected)
            all_mark_transition_checks+=1
print('PASS actual transitions of every marked label and attachment:',all_mark_transition_checks,'cases')
