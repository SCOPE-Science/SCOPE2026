"""Exact joint arm/label symmetry character for Conf_3(Y_3).

The first model is the graph spine of ordered particle distributions on a
three-arm star, with a moving innermost particle giving each oriented edge.
The second is an independent subdivided cubical (Abrams) model, with signed
fixed-cell traces. No external libraries are required.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product
from math import factorial

S3 = list(permutations(range(3)))
identity = (0,1,2)
transposition = (1,0,2)
threecycle = (1,2,0)
reps = [identity,transposition,threecycle]
classes = {identity:1,transposition:3,threecycle:2}
characters = {"trivial":[1,1,1],"sign":[1,-1,1],"standard":[2,0,-1]}

def arm_lists(labels):
    found=set()
    for assn in product(range(3),repeat=len(labels)):
        for order in permutations(labels):
            arr=tuple(tuple(z for z in order if assn[labels.index(z)]==a) for a in range(3))
            found.add(arr)
    return sorted(found)

def make_spine():
    vertices=set()
    for arr in arm_lists((0,1,2)):
        vertices.add((3,arr)) # 3 signals no label at center
    for j in range(3):
        for arr in arm_lists(tuple(z for z in range(3) if z!=j)):
            vertices.add((j,arr))
    edges=set()
    for moving in range(3):
        for a in range(3):
            for arr in arm_lists(tuple(z for z in range(3) if z!=moving)):
                center=(moving,arr)
                extra=tuple((moving,)+arr[b] if a==b else arr[b] for b in range(3))
                exterior=(3,extra)
                assert center in vertices and exterior in vertices
                edges.add((center,exterior)) # orientation: center to arm
    return vertices,edges

def map_vertex(v,s,p):
    c,arms=v
    ret=[None]*3
    for a in range(3):ret[s[a]]=tuple(p[j] for j in arms[a])
    return (3 if c==3 else p[c],tuple(ret))

def get_spine_character():
    vs,es=make_spine()
    assert (len(vs),len(es))==(96,108),(len(vs),len(es))
    adj={v:[] for v in vs}
    for v,w in es:adj[v].append(w);adj[w].append(v)
    seen={next(iter(vs))};q=deque(seen)
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in seen: seen.add(w);q.append(w)
    assert len(seen)==96
    tab={}
    for s in S3:
        for p in S3:
            vt=sum(map_vertex(v,s,p)==v for v in vs)
            et=sum(map_vertex(v,s,p)==v and map_vertex(w,s,p)==w for v,w in es)
            assert set(map_vertex(v,s,p) for v in vs)==vs
            assert set((map_vertex(v,s,p),map_vertex(w,s,p)) for v,w in es)==es
            tab[s,p]=1-vt+et
    reduced=[[tab[s,p] for p in reps] for s in reps]
    assert reduced==[[13,1,1],[-5,-1,1],[1,1,-2]],reduced
    irreps={}
    for ia,(an,ac) in enumerate(characters.items()):
        for ip,(pn,pc) in enumerate(characters.items()):
            val=sum(classes[s]*classes[p]*reduced[is_][ip_]*ac[is_]*pc[ip_]
                    for is_,s in enumerate(reps) for ip_,p in enumerate(reps))
            assert val%36==0,(an,pn,val)
            irreps[an+' x '+pn]=val//36
    expected={'sign x trivial':1,'sign x standard':2,
              'standard x trivial':1,'standard x sign':1,
              'standard x standard':1}
    assert {k:v for k,v in irreps.items() if v}==expected,irreps
    assert 1+sum(len(adj[v]) for v in vs)//2-len(vs)==13
    print('SPINE 96 vertices 108 oriented edges 1 connected component H1_Z_rank 13')
    print('REP_TABLE arm(e,swap,cycle) x particle(e,swap,cycle):',reduced)
    print('RATIONAL_DECOMPOSITION',sorted((k,v) for k,v in irreps.items() if v))
    print('ARM_INVARIANT_DIM 0 PARTICLE_INVARIANT_DIM 3 FULL_INVARIANT_DIM 0')
    return reduced

def cubical_character(L):
    # Independent model with particles on closed-disjoint vertices or edges.
    v=[('v',-1,0)]+[('v',a,k) for a in range(3) for k in range(1,L+1)]
    e=[('e',a,k) for a in range(3) for k in range(1,L+1)]
    items=v+e
    def supp(x):
        typ,a,k=x
        if typ=='v':return frozenset([x])
        return frozenset([('v',a,k-1) if k>1 else ('v',-1,0),('v',a,k)])
    su={x:supp(x) for x in items}
    cells=[c for c in product(items,repeat=3)
           if all(su[c[i]].isdisjoint(su[c[j]]) for i,j in combinations(range(3),2))]
    tab={}
    for s in reps:
        for p in reps:
            ch=0
            for c in cells:
                img=tuple((x[0],s[x[1]],x[2]) if x[1]>=0 else x
                          for x in (c[p.index(i)] for i in range(3)))
                if img!=c:continue
                active=[i for i in range(3) if c[i][0]=='e']
                perm=[p[i] for i in active]
                inv=sum(perm[i]>perm[j] for i,j in combinations(range(len(perm)),2))
                ch+=(-1)**(len(active)+inv)
            tab[s,p]=1-ch
    return [[tab[s,p] for p in reps] for s in reps],len(cells),Counter(sum(x[0]=='e' for x in c) for c in cells)

if __name__=='__main__':
    expected=get_spine_character()
    for L in [2,3,4]:
        ch,n,bydim=cubical_character(L)
        assert ch==expected,(L,ch)
        print('SUBDIVIDED_CUBICAL_MODEL L',L,'cells',n,'counts_by_dimension',sorted(bydim.items()),'joint_traces_match')
    print('Y3_THREE_PARTICLE_JOINT_S3_X_S3_CHARACTER_PASS')

def verify_uniform_three_particles(m):
    """Independent all-group-element check for the uniform arm-count theorem."""
    perms=list(permutations(range(m)))
    def arm_lists_m(labels):
        found=set()
        for assn in product(range(m),repeat=len(labels)):
            for order in permutations(labels):
                found.add(tuple(tuple(z for z in order if assn[labels.index(z)]==a)
                                for a in range(m)))
        return found
    vs=set()
    for arms in arm_lists_m((0,1,2)):vs.add((3,arms))
    for center in range(3):
        for arms in arm_lists_m(tuple(x for x in range(3) if x!=center)):
            vs.add((center,arms))
    es=set()
    for moving in range(3):
        for arm in range(m):
            for arms in arm_lists_m(tuple(x for x in range(3) if x!=moving)):
                v=(moving,arms)
                w=(3,tuple(((moving,)+arms[j]) if j==arm else arms[j] for j in range(m)))
                assert v in vs and w in vs
                es.add((v,w))
    assert len(vs)==m*(m+1)*(m+5)
    assert len(es)==3*m*m*(m+1)
    graph={v:set() for v in vs}
    for a,b in es: graph[a].add(b);graph[b].add(a)
    todo=[next(iter(vs))];seen=set(todo)
    for z in todo:
        for w in graph[z]:
            if w not in seen:seen.add(w);todo.append(w)
    assert len(seen)==len(vs)
    def act(x,s,p):
        cent,arms=x
        arr=[() for _ in range(m)]
        for a in range(m):arr[s[a]]=tuple(p[z] for z in arms[a])
        return (p[cent] if cent!=3 else 3,tuple(arr))
    labels_reps=[identity,transposition,threecycle]
    checked=0
    for s in perms:
        f=sum(s[i]==i for i in range(m))
        t=sum(s[i]!=i and s[s[i]]==i for i in range(m))//2
        q=sum(s[i]!=i and s[s[i]]!=i and s[s[s[i]]]==i for i in range(m))//3
        for p in S3:
            if p==identity:pred=1+f*(f+1)*(2*f-5)
            elif p in [(1,0,2),(2,1,0),(0,2,1)]:pred=1-2*t
            else:pred=1-3*q
            vf=sum(act(v,s,p)==v for v in vs)
            ef=sum(act(v,s,p)==v and act(w,s,p)==w for v,w in es)
            assert 1-vf+ef==pred,(m,s,p,vf,ef,pred)
            checked+=1
    assert 1+len(es)-len(vs)==1+m*(m+1)*(2*m-5)
    print('UNIFORM m',m,'vertices',len(vs),'edges',len(es),'group_actions',checked,'PASS')

if __name__=='__main__':
    for arms in [3,4,5,6]:verify_uniform_three_particles(arms)
    print('THREE_PARTICLE_STAR_UNIFORM_COMPLETE_JOINT_CHARACTER_PASS')
