#!/usr/bin/env python3
"""Finite independent checks of two-endpoint pendant deletion in matching complexes."""
import json, itertools, random
from collections import defaultdict, deque

def matching_count(vertices, edges):
    vertices=tuple(vertices)
    if not vertices: return 1
    u=vertices[0]; rest=vertices[1:]; adj={tuple(sorted(e)) for e in edges}
    return sum(matching_count(tuple(x for x in rest if x!=v), edges) for v in rest if tuple(sorted((u,v))) in adj)

def make(n, base):
    base=sorted({tuple(sorted(e)) for e in base})
    assert (0,1) in base
    es=[('b',a,b) for a,b in base]+[('w',i,n+i) for i in range(2,n)]
    masks=[]; labels=[]
    for tag,u,v in es:
        masks.append((1<<u)|(1<<v)); labels.append(f'{tag}{u}_{v}')
    faces=[0]
    for i,bitmask in enumerate(masks):
        for s in list(faces):
            occupied=0
            for j in range(i):
                if s>>j&1:occupied|=masks[j]
            if not occupied & bitmask: faces.append(s | (1<<i))
    return base,es,masks,labels,set(faces)

def morse(n,base,es,masks,faces):
    edge_index={e:i for i,e in enumerate(es)}; e0=1<<edge_index[('b',0,1)]
    matched={}; unpaired=[]
    for face in faces:
        B=[(i,x) for i,x in enumerate(es) if face>>i&1 and x[0]=='b']
        phi=any((x[1] in (0,1) or x[2] in (0,1)) and x!=('b',0,1) for i,x in B)
        if not phi:
            target=face^e0
        else:
            cov={v for i,x in B for v in x[1:]}
            free=[v for v in range(2,n) if v not in cov]
            if not free:
                unpaired.append(face);continue
            j=edge_index[('w',free[0],n+free[0])]
            target=face^(1<<j)
        assert target in faces,('illegal',n,face,target)
        assert target!=face
        matched[face]=target
    assert all(matched[matched[x]]==x for x in matched)
    assert matched[0]==e0
    critical=set(unpaired)|{e0}
    assert len(critical)==len(unpaired)+1
    # Explicit gradient digraph: unmatched face inclusions down, matched covers up.
    indeg={f:0 for f in faces}; adj=defaultdict(list)
    for upper in faces:
        t=upper
        while t:
            bit=t&-t;lower=upper^bit;t-=bit
            if upper==e0 and lower==0: # removed augmented pair, no empty face in ordinary poset
                continue
            if lower==0:continue
            if matched.get(lower)==upper and lower!=0:
                a,b=lower,upper
            else:
                a,b=upper,lower
            adj[a].append(b);indeg[b]+=1
    queue=deque(f for f in indeg if not indeg[f]); count=0
    while queue:
        f=queue.popleft();count+=1
        for g in adj[f]:
            indeg[g]-=1
            if not indeg[g]:queue.append(g)
    assert count==len(faces),('morse cyclic',n,len(faces),count)
    # Actual critical faces (except one zero-cell) are just original edge matchings.
    assert all(all(es[j][0]=='b' for j in range(len(es)) if c>>j&1) for c in unpaired)
    return critical,unpaired,len(adj),sum(map(len,adj.values()))

def homology_mod2(faces):
    groups=defaultdict(list)
    for f in faces:
        groups[f.bit_count()-1].append(f)
    rank={}; dims=sorted(k for k in groups if k>=0)
    for k in dims:
        if k==0:rank[k]=0;continue
        row_index={x:i for i,x in enumerate(groups[k-1])}
        basis={}
        for f in groups[k]:
            t=f;v=0
            while t:
                bit=t&-t;t-=bit;v ^=1<<row_index[f^bit]
            while v:
                pivot=v.bit_length()-1
                if pivot in basis:v^=basis[pivot]
                else:basis[pivot]=v;break
        rank[k]=len(basis)
    betti={k:len(groups[k])-rank.get(k,0)-rank.get(k+1,0) for k in dims}
    betti[0]-=1
    return {k:v for k,v in betti.items() if v}

def primitive_cycles(n, base, es, faces):
    """Integer chain-level test of explicit cycles and coefficient pairing."""
    if n % 2: return 0
    ix={e:i for i,e in enumerate(es)}
    P=[]
    def rec(rest, chosen):
        if not rest:
            P.append(tuple(chosen));return
        u=rest[0]
        for v in rest[1:]:
            f=tuple(sorted((u,v)))
            if f != (0,1) and f in base:
                rec(tuple(x for x in rest[1:] if x!=v),chosen+[f])
    rec(tuple(range(n)),[])
    chosen_base={}
    for Q in P:
        factors=[]
        for f in Q:
            w=next(x for x in f if x not in (0,1))
            factors.append((ix[('b',*f)],ix[('w',w,n+w)]))
        chain={}
        for b in itertools.product((0,1),repeat=len(factors)):
            t=tuple(factors[i][b[i]] for i in range(len(factors)))
            assert sum(1<<i for i in t) in faces
            chain[t]=(-1)**sum(b)
        bd=defaultdict(int)
        for t,c in chain.items():
            for j in range(len(t)):
                bd[t[:j]+t[j+1:]]+=c*((-1)**j)
        assert not any(bd.values()),('chain boundary',n,Q)
        chosen_base[Q]={t:c for t,c in chain.items() if all(es[i][0]=='b' for i in t)}
        assert len(chosen_base[Q])==1 and list(chosen_base[Q].values())==[1]
    for Q in P:
        for R in P:
            target=tuple(ix[('b',*f)] for f in R)
            assert chosen_base[Q].get(target,0)==int(Q==R)
    return len(P)

def check(n,base,do_homology=True):
    base,es,masks,labels,faces=make(n,base)
    critical,more,nn,arcs=morse(n,base,es,masks,faces)
    primitive=primitive_cycles(n,base,es,faces)
    if n%2==0:
        expected=matching_count(range(n),[e for e in base if e!=(0,1)])
    else:
        expected=matching_count([v for v in range(n) if v!=0],base)+matching_count([v for v in range(n) if v!=1],base)
    assert len(more)==expected, (n,base,len(more),expected)
    if n%2==0: assert primitive==expected
    assert all(f.bit_count()==n//2 for f in more)
    if do_homology:
        actual=homology_mod2(faces)
        target=({n//2-1:expected} if expected else {})
        assert actual==target,(n,base,actual,target)
    return len(faces),arcs,expected

def main():
    cases=[]
    for n in (2,3,4):
        others=[x for x in itertools.combinations(range(n),2) if x!=(0,1)]
        for mask in range(1<<len(others)):
            base=[(0,1)]+[e for i,e in enumerate(others) if mask>>i&1]
            cases.append((n,base,True))
    rng=random.Random(13579)
    for n,samples in ((5,64),(6,55)):
        other=[x for x in itertools.combinations(range(n),2) if x!=(0,1)]
        for t in range(samples):
            if t==0:base=[(0,1)]+other
            elif t==1:base=[(0,1)]+[(i,(i+1)%n) for i in range(1,n)]
            else:base=[(0,1)]+[x for x in other if rng.random()<(0.25+0.5*rng.random())]
            cases.append((n,base,True))
    totals=defaultdict(lambda:{'cases':0,'faces':0,'cover_arcs':0,'critical_top_cells':0})
    for n,base,h in cases:
        faces,arcs,crit=check(n,base,h)
        t=totals[n];t['cases']+=1;t['faces']+=faces;t['cover_arcs']+=arcs;t['critical_top_cells']+=crit
    print(json.dumps({'status':'PASS','model':'ordinary matching complexes of two-endpoint unwhiskered graphs','checks':'augmented Morse pairing, full nonempty gradient acyclicity, perfect/near-perfect critical-cell counts, exact mod-two simplicial homology, integer primitive cycle boundaries and unit coefficient pairings','per_order':dict(sorted(totals.items()))},sort_keys=True,indent=2))
if __name__=='__main__':main()
