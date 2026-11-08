#!/usr/bin/env python3
"""Exact finite face-poset orbit checks for the 3-by-4 chessboard surface."""
from itertools import combinations, permutations
from collections import defaultdict, deque, Counter

P = list(permutations(range(4)))
ident = tuple(range(4))

def mul(p, q): return tuple(p[q[i]] for i in range(4))
def inv(p): return tuple(p.index(i) for i in range(4))
def parity(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def group(gens):
    out = {ident};todo=deque([ident]);steps=list(gens)+[inv(x) for x in gens]
    while todo:
        x=todo.popleft()
        for y in steps:
            z=mul(x,y)
            if z not in out:out.add(z);todo.append(z)
    return frozenset(out)

V=tuple((i,j) for i in range(3) for j in range(4))
faces=[tuple(sorted(combo)) for size in range(1,4) for combo in combinations(V,size)
       if len({v[0] for v in combo})==size and len({v[1] for v in combo})==size]
S={s:frozenset(f for f in faces if len(f)==s) for s in (1,2,3)}
E=frozenset((x,y) for a,b in ((1,2),(1,3),(2,3)) for x in S[a] for y in S[b] if set(x)<set(y))
T=frozenset((x,y,z) for x in S[1] for y in S[2] for z in S[3] if set(x)<set(y)<set(z))
assert (tuple(map(len,(S[1],S[2],S[3]))),len(E),len(T))==((12,36,24),216,144)

def af(g,f):return tuple(sorted((r,g[c]) for r,c in f))
def ax(g,c):return tuple(af(g,f) for f in c)

def orbit_cells(cells,H):
    remain=set(cells);orbits=[];which={}
    while remain:
        x=min(remain);orbit={ax(g,x) for g in H}
        assert orbit<=remain
        i=len(orbits)
        for v in orbit:which[v]=i
        orbits.append(orbit);remain-=orbit
    return orbits,which

def quotient(H):
    b=[(f,) for f in faces]
    c1=sorted(E);c2=sorted(T)
    obs=[];wis=[]
    for c in (b,c1,c2):
        o,w=orbit_cells(c,H);obs.append(o);wis.append(w)
    verts,edges,tri=obs;vid,eid,tid=wis
    eends={}
    for x,orb in enumerate(edges):
        a,b=next(iter(orb));eends[x]=(vid[(a,)],vid[(b,)])
    deg=Counter()
    for orb in tri:
        a,b,c=next(iter(orb))
        inds=[eid[(a,b)],eid[(a,c)],eid[(b,c)]]
        assert len(set(inds))==3
        for i in inds:deg[i]+=1
    assert set(deg)==set(range(len(edges)))
    assert set(deg.values())<= {1,2},(len(H),Counter(deg.values()))
    bedges={e for e,v in deg.items() if v==1}
    bg=defaultdict(set)
    for e in bedges:
        a,b=eends[e];assert a!=b
        bg[a].add((b,e));bg[b].add((a,e))
    assert all(len(nbr)==2 for nbr in bg.values()),(len(H),bg)
    seen=set();bc=0
    for v in bg:
        if v in seen:continue
        bc+=1;st=[v];seen.add(v)
        while st:
            for w,_ in bg[st.pop()]:
                if w not in seen:seen.add(w);st.append(w)
    # Independently check every quotient vertex link is a single path or circle.
    # This rules out vertex pinches that Euler/boundary counts alone could miss.
    for v in range(len(verts)):
        incident={e for e,(a,b) in eends.items() if v in (a,b)}
        lk=defaultdict(set)
        for orbit in tri:
            a,b,c=next(iter(orbit))
            triangle_verts={vid[(a,)],vid[(b,)],vid[(c,)]}
            if v not in triangle_verts:continue
            pair=sorted(e for e in (eid[(a,b)],eid[(a,c)],eid[(b,c)]) if e in incident)
            assert len(pair)==2,(v,pair)
            x,y=pair;lk[x].add(y);lk[y].add(x)
        assert set(lk)==incident
        assert all(len(nbr) in (1,2) for nbr in lk.values())
        st=[next(iter(incident))];seen_link={st[0]}
        while st:
            for w in lk[st.pop()]:
                if w not in seen_link:seen_link.add(w);st.append(w)
        assert seen_link==incident
        num_end=sum(len(nbr)==1 for nbr in lk.values())
        assert num_end in (0,2),(len(H),v,num_end)
        assert (num_end==2)==any(e in bedges for e in incident)
    assert len(verts)-len(edges)+len(tri)==sum((-1)**i*len(obs[i]) for i in range(3))
    return len(verts),len(edges),len(tri),len(bedges),bc

def ctype(g):
    seen=set();ls=[]
    for i in range(4):
        if i in seen:continue
        j=i;n=0
        while j not in seen: seen.add(j);n+=1;j=g[j]
        ls.append(n)
    return tuple(sorted(ls,reverse=True))

all_groups={group(())};change=True
while change:
    change=False
    for h in list(all_groups):
        for x in P:
            if x in h: continue
            u=group(tuple(h)+(x,))
            if u not in all_groups:all_groups.add(u);change=True
assert len(all_groups)==30,len(all_groups)
remaining=set(all_groups); classes=[]
while remaining:
    H=min(remaining,key=lambda x:(len(x),sorted(x)))
    conjugates={frozenset(mul(mul(g,h),inv(g)) for h in H) for g in P}
    assert conjugates<=remaining
    classes.append((H,len(conjugates)));remaining-=conjugates

out=[]
for H,nconj in classes:
    types=Counter(ctype(g) for g in H)
    q=quotient(H);chi=q[0]-q[1]+q[2]
    is_even=all(parity(g)>0 for g in H)
    # A quotient of an oriented compact connected surface by a finite group
    # is a connected compact surface, possibly with boundary.
    if q[-1]==0:
        if is_even:
            assert chi in (0,2)
            name='torus' if chi==0 else 'sphere'
        else:
            assert chi==0
            name='Klein bottle'
    elif q[-1]==1:
        assert chi in (0,1)
        name='Moebius band' if chi==0 else 'disk'
    else:
        assert q[-1]==2 and chi==0
        name='annulus'
    out.append((len(H),nconj,dict(sorted(types.items())),q,chi,name))

for tup in out:print('SUBGROUP',repr(tup))
assert len(out)==11
want={'torus':3,'sphere':2,'Moebius band':2,'disk':2,'annulus':1,'Klein bottle':1}
assert Counter(row[-1] for row in out)==Counter(want)
# action on integral H2 via explicitly oriented sum of all top faces
z={}
for t in S[3]:
    ordered=tuple(c for row,c in sorted(t))
    omitted=next(c for c in range(4) if c not in ordered)
    z[t]=parity(ordered+(omitted,))
for e in S[2]:
    j=sum(((-1)**omit)*z[t] for t in S[3] for omit in range(3) if tuple(x for k,x in enumerate(t) if k!=omit)==e)
    assert j==0,(e,j)
for g in P:
    for t in S[3]:
        assert z[af(g,t)]==parity(g)*z[t]

print('ALL_VERIFY_OK: face_vector=(12,36,24); barycentric=(72,216,144); subgroups=30; conjugacy_classes=11; full_orbit_surface_classification=True; oriented_fundamental_cycle=True')
