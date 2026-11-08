"""Independent finite checks for line-graph radius-two Rips hexagon theorem.
Dependency-free Python 3. No external downloads and no data files needed.
"""
from itertools import combinations
from collections import defaultdict

def edge(a,b):
    return tuple(sorted((a,b)))

def cycles(n):
    return [edge(i,(i+1)%n) for i in range(n)]

def wedge(*lengths):
    out=[]; nxt=1
    for n in lengths:
        v=[0]+list(range(nxt,nxt+n-1));nxt+=n-1
        out += [edge(v[i],v[(i+1)%n]) for i in range(n)]
    return out

def theta(*lengths):
    out=[]; nxt=2
    for length in lengths:
        v=[0]+list(range(nxt,nxt+length-1))+[1];nxt+=length-1
        out += [edge(v[i],v[i+1]) for i in range(length)]
    return out

def example_cases():
    g=cycles(6)+[edge(0,i) for i in range(6,10)]
    cases=[('hexagon',cycles(6)),('heptagon',cycles(7)),('octagon',cycles(8)),
           ('two-hexagon bouquet',wedge(6,6)),('hexagon-octagon bouquet',wedge(6,8)),
           ('theta 3,3,4',theta(3,3,4)),('theta 3,3,7',theta(3,3,7)),('theta 3,3,8',theta(3,3,8)),
           ('theta 3,4,6',theta(3,4,6)),('hexagon with four pendant leaves',g),
           ('tree with arms',theta(3,3,7)[:-1])]
    # The final case is a connected graph with one long path deleted; still has a hexagon.
    return cases

def graph_data(edgelist):
    ed=sorted(set(edge(*e) for e in edgelist))
    assert len(ed)==len(edgelist)
    verts=sorted(set(x for e in ed for x in e))
    N={v:set() for v in verts}
    for a,b in ed:N[a].add(b);N[b].add(a)
    # Graph connectedness
    seen={verts[0]};stack=[verts[0]]
    while stack:
        for w in N[stack.pop()]:
            if w not in seen:seen.add(w);stack.append(w)
    assert seen==set(verts)
    return ed,verts,N

def small_cycles(N):
    found={}
    for start in N:
        def walk(path):
            if len(path)>=4 and path[-1] in N[start] and len(path)<=6:
                cyc=frozenset(edge(a,b) for a,b in zip(path,path[1:]+[start]))
                found[cyc]=len(path)
            if len(path)==6:return
            for w in N[path[-1]]:
                if w not in path:walk(path+[w])
        walk([start])
    return found

def faces_from_generators(gens):
    faces={0}
    for c in gens:
        bits=sum(1<<i for i in c)
        sub=bits
        while sub:
            faces.add(sub);sub=(sub-1)&bits
    return faces

def cliques(adj):
    # Every clique appears once by increasing vertex extension.
    out={0}; m=len(adj)
    def extend(face, candidates):
        for j in range(len(candidates)):
            x=candidates[j];f=face | (1<<x);out.add(f)
            extend(f,[z for z in candidates[j+1:] if z in adj[x]])
    extend(0,list(range(m)))
    return out

def ranks(faces):
    by=defaultdict(list)
    for mask in faces:
        if mask:by[mask.bit_count()-1].append(mask)
    ranks={}; maxdim=max(by)
    for dim in range(1,maxdim+1):
        idx={mask:i for i,mask in enumerate(by[dim-1])}
        pivots={}; rank=0
        for mask in by[dim]:
            v=mask; col=0
            while v:
                bit=v&-v;v-=bit;col^=1<<idx[mask^bit]
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:pivots[p]=col;rank+=1;break
        ranks[dim]=rank
    betti={k:len(arr)-ranks.get(k,0)-ranks.get(k+1,0) for k,arr in by.items()}
    betti[0]-=1
    return {k:v for k,v in betti.items() if v}, tuple(len(by[k]) for k in range(maxdim+1))

def check_case(name,edgelist):
    ed,V,N=graph_data(edgelist); m=len(ed);b=m-len(V)+1
    short=small_cycles(N)
    assert all(L>=6 for L in short.values()),(name,'short cycle')
    six=[x for x,L in short.items() if L==6]
    assert all(x.isdisjoint(y) for x,y in combinations(six,2)),(name,'sixcycles overlap')
    # Vertices of the line graph are the original graph edges.
    L=[{j for j,f in enumerate(ed) if i!=j and bool(set(e)&set(f))} for i,e in enumerate(ed)]
    Nclosed=[{i}|L[i] for i in range(m)]
    R=[set(L[i])|set().union(*(L[j] for j in L[i]))-{i} for i in range(m)]
    R=[v-{i} for i,v in enumerate(R)]
    rips=cliques(R)
    centered=faces_from_generators(Nclosed)
    stars=[{i for i,e in enumerate(ed) if v in e} for v in V]
    Y=faces_from_generators(stars)
    assert Y<=centered<=rips
    alternate=set()
    for c in six:
        cycgraph={v:[] for e in c for v in e}
        for a,z in c:cycgraph[a].append(z);cycgraph[z].append(a)
        s=min(cycgraph);first=min(cycgraph[s]);walk=[s,first]
        while len(walk)<6:
            cur=walk[-1];walk.append(next(x for x in cycgraph[cur] if x!=walk[-2]))
        cyc_ed=[edge(walk[i],walk[(i+1)%6]) for i in range(6)]
        for parity in (0,1):
            alternate.add(sum(1<<ed.index(cyc_ed[j]) for j in range(parity,6,2)))
    assert rips-centered==alternate,(name,'noncentered mismatch',len(rips-centered),len(alternate))
    centers={}
    for mask in centered-Y:
        choices=[i for i,Nc in enumerate(Nclosed) if mask&~sum(1<<v for v in Nc)==0]
        assert len(choices)==1,(name,'center ambiguity',mask,choices)
        centers[mask]=choices[0]
    pending=set(centered-Y)
    pairs=[]
    for mask in pending:
        c=centers[mask]
        if not(mask>>c&1):
            upper=mask|(1<<c)
            assert upper in pending and centers[upper]==c
            pairs.append((mask,upper))
    assert set(x for p in pairs for x in p)==pending
    for lower,upper in sorted(pairs,key=lambda p:-p[0].bit_count()):
        assert lower in pending and upper in pending
        cofaces=[f for f in pending if f!=lower and f&lower==lower]
        assert cofaces==[upper],(name,'nonfree collapse',lower,cofaces)
        pending.remove(lower);pending.remove(upper)
    assert not pending
    hom,fvector=ranks(rips)
    expect={}
    if b-len(six):expect[1]=b-len(six)
    if six:expect[2]=len(six)
    assert hom==expect,(name,'homology',hom,expect)
    print(f'{name}: V={len(V)} E={m} b={b} q={len(six)} faces={len(rips)} f={fvector} '+
          f'centered_collapses={len(pairs)} exceptional_triangles={len(alternate)} reduced_mod2={hom} OK')

if __name__=='__main__':
    for title,edges in example_cases():check_case(title,edges)
    # Boundary check: three overlapping hexagons violate the hypothesis.
    ed,V,N=graph_data(theta(3,3,3))
    short=small_cycles(N)
    six=[c for c,l in short.items() if l==6]
    assert len(six)==3 and any(not a.isdisjoint(b) for a,b in combinations(six,2))
    L=[{j for j,f in enumerate(ed) if i!=j and bool(set(e)&set(f))} for i,e in enumerate(ed)]
    R=[(set(L[i])|set().union(*(L[j] for j in L[i])))-{i} for i in range(len(ed))]
    hom,_=ranks(cliques(R))
    assert hom=={2:4},hom
    print('theta 3,3,3: OUT OF SCOPE, overlapping hexagons, reduced_mod2={2:4} OK')
    print('LINE_GRAPH_GIRTH6_RIPS2_ALL_FINITE_CHECKS_OK')
