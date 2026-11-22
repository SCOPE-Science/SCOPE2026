from itertools import combinations
from math import floor, comb
from collections import Counter

def B_patterns(edges):
    inc={}
    for i,(u,v) in enumerate(edges):
        inc[u]=inc.get(u,0)|(1<<i)
        inc[v]=inc.get(v,0)|(1<<i)
    return {v for v in inc.values() if v!=0}

def expected_components(edges):
    adj={}
    for u,v in edges:
        adj.setdefault(u,set()).add(v)
        adj.setdefault(v,set()).add(u)
    visited=set();types=[]
    for v in adj:
        if v in visited:continue
        stack=[v];verts=set()
        while stack:
            w=stack.pop()
            if w in visited:continue
            visited.add(w);verts.add(w)
            stack+=list(adj[w]-visited)
        deg=sorted(len(adj[w]) for w in verts)
        if deg==[1,1]:typ='K2'
        elif deg==[1,1,2]:typ='P3'
        elif deg==[1,1,1,3]:typ='K13'
        elif deg==[1,1,2,2] and len(verts)==4:typ='P4'
        else:typ='other:'+str(deg)
        types.append(typ)
    return Counter(types)

def is_extremal_type(edges):
    b=len(edges); t=expected_components(edges); k=b//2
    if b%2==0:
        return t==Counter({'P3':k})
    return t in [Counter({'P3':k,'K2':1}), Counter({'P3':k-1,'K13':1}), Counter({'P3':k-1,'P4':1})]

cases=0;extreme=0
for n in range(2,8):
    all_edges=list(combinations(range(n),2))
    for b in range(1,min(6,len(all_edges))+1):
        for edges in combinations(all_edges,b):
            cases+=1
            pats=B_patterns(edges)
            upper=(3*b)//2
            assert len(pats)<=upper,(n,b,edges,pats)
            if len(pats)==upper:
                extreme+=1
                assert is_extremal_type(edges),(n,b,edges,expected_components(edges))
            else:
                assert not is_extremal_type(edges),(n,b,edges)
print('EXHAUSTIVE_EDGE_SKELETON_CHECK_OK',cases,'cases; extremal',extreme)

# Independently construct the three families and check their extremal star profiles.
for b in range(1,35):
  k=b//2
  for family in ('cherries','isolated','three_star','four_path'):
    edges=[];current=0
    if b%2==0 and family!='cherries':continue
    if b%2==1 and family=='cherries':continue
    nc=k if family in ('cherries','isolated') else k-1
    if nc<0:continue
    for _ in range(nc):
      edges += [(current,current+1),(current,current+2)];current+=3
    if family=='isolated':edges.append((current,current+1))
    if family=='three_star':edges += [(current,current+1),(current,current+2),(current,current+3)]
    if family=='four_path':edges += [(current,current+1),(current+1,current+2),(current+2,current+3)]
    assert len(edges)==b
    assert len(B_patterns(edges))==(3*b)//2,(b,family)
print('CONSTRUCTIVE_B_SPECTRA_CHECK_OK')

# Build incidence hosts, from the two independent gadgets:
# mark a original vertices (a clique), b selected subdivision-edge vertices;
# include separate components for B and extra edges to realize singles/pairs/empty.
construction_count=0
for a in range(0,11):
 for b in range(0,11):
  if a+b==0:continue
  construction_count+=1
  edges=[]; next_v=a
  for i,j in combinations(range(a),2):edges.append((i,j))
  if a:
   helper=next_v;next_v+=1
   for i in range(a):edges.append((i,helper))
  # marked-edge skeleton uses cherries + possible isolated K2
  B=[]
  k=b//2
  for _ in range(k):
   u=next_v;v=u+1;w=u+2;next_v+=3
   B += [(u,v),(u,w)]
  if b%2:
   B.append((next_v,next_v+1));next_v+=2
  edges+=B
  # if a=0, all subdivision vertices have empty traces;
  # if b=0, original vertices have empty traces;
  # if a,b>0, A-marked originals are B-disjoint, so empty.
  orig=set(range(next_v)); marked_orig=set(range(a)); marked_edges=B
  patterns=[]
  for u in orig:
   patterns.append(frozenset(('e',i) for i,edge in enumerate(B) if u in edge))
  for edge in edges:
   patterns.append(frozenset(('v',i) for i in marked_orig if i in edge))
  observed=len(set(patterns))
  goal=1+a+comb(a,2)+(3*b)//2
  assert observed==goal,(a,b,goal,observed)
print('MIXED_CONSTRUCTION_CHECK_OK',construction_count,'cases')

# Equality characterization, checked against literal incidence graph traces.
from random import Random
rng=Random(20261121)
def test_case(n,E,A,B):
    atypes=set();btypes=set()
    for v in range(n):
        btypes.add(frozenset(e for e in B if v in E[e]))
    for edge in E:
        atypes.add(frozenset(v for v in A if v in edge))
    types=set(('b',t) for t in btypes if t)|set(('a',t) for t in atypes if t)
    types.add(('zero',)) if frozenset() in btypes or frozenset() in atypes else None
    observed=len(types)
    a=len(A);b=len(B)
    # Euler characteristic identity for the marked-edge skeleton.
    sk=[E[i] for i in B]
    nodes=set(t for e in sk for t in e)
    adj={v:set() for v in nodes}
    for x,y in sk:
        adj[x].add(y);adj[y].add(x)
    visited=set();components=[]
    for v in nodes:
        if v in visited:continue
        stk=[v];comp=set()
        while stk:
            w=stk.pop()
            if w in visited:continue
            visited.add(w);comp.add(w)
            stk+=list(adj[w]-visited)
        components.append(comp)
    c=len(components)
    p=sum(1 for comp in components if sum(len(adj[w]) for w in comp)//2>=2)
    beta=b-len(nodes)+c
    eA=sum(1 for u,v in E if u in A and v in A)
    external=sum(1 for u in A if any(u in e and not(e[0] in A and e[1] in A) for e in E))
    eta=int(frozenset() in btypes or frozenset() in atypes)
    assert observed==eta+eA+external+b+p-beta,(n,E,A,B,observed,eta,eA,external,b,p,beta)
    assert len({t for t in btypes if t})==b+p-beta

    goal=1+a+comb(a,2)+(3*b)//2
    joint_empty=frozenset() in btypes or frozenset() in atypes
    a_ok=all(tuple(sorted((u,v))) in E for u,v in combinations(A,2)) and all(any(u in e and (e[0] not in A or e[1] not in A) for e in E) for u in A)
    b_ok=b==0 or is_extremal_type([E[i] for i in B])
    assert (observed==goal)==(joint_empty and a_ok and b_ok),(n,E,A,B,observed,goal,joint_empty,a_ok,b_ok)
    return observed

count=0
for n in range(1,5):
    ps=list(combinations(range(n),2))
    for mask in range(1<<len(ps)):
        E=[ps[i] for i in range(len(ps)) if mask>>i&1]
        for amask in range(1,1<<n):
            A={v for v in range(n) if amask>>v&1}
            for bmask in range(1<<len(E)):
                B={i for i in range(len(E)) if bmask>>i&1}
                test_case(n,E,A,B);count+=1
        for bmask in range(1,1<<len(E)):
            B={i for i in range(len(E)) if bmask>>i&1}
            test_case(n,E,set(),B);count+=1
for _ in range(40000):
    n=rng.randint(2,9); ps=list(combinations(range(n),2))
    E=[e for e in ps if rng.random()<rng.uniform(0.1,0.8)]
    A={v for v in range(n) if rng.random()<0.5}
    B={i for i in range(len(E)) if rng.random()<0.35}
    if A or B:
        test_case(n,E,A,B);count+=1
print('MIXED_EQUALITY_CHARACTERIZATION_OK',count,'cases')
