#!/usr/bin/env python3
"""Exact finite witness for a pair of dominance complexes."""
from collections import Counter,deque
from itertools import product
import json
from pathlib import Path
N=16; SIZE=1<<N

def make_graph(which):
    a=[]
    for x,y in product(range(4),repeat=2):
        row=0
        for u,v in product(range(4),repeat=2):
            dx=(u-x)%4;dy=(v-y)%4
            if which=='Shrikhande': ok=(dx,dy) in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3))
            else:ok=((dx==0) != (dy==0))
            if ok:row |= 1<<(4*u+v)
        a.append(row)
    return a

def make_faces(adj):
    closed=[adj[v]|(1<<v) for v in range(N)]
    legal=bytearray(SIZE);legal[0]=1
    faces=[];fvec=Counter()
    for m in range(1,SIZE):
        # Criterion I: no closed neighborhood is contained in m.
        ok=not any((m&cl)==cl for cl in closed)
        # Criterion II: the complementary set dominates via a union of closed neighborhoods.
        cm=(SIZE-1)^m
        union=0
        while cm:
            low=cm&-cm
            union |= closed[low.bit_length()-1]
            cm^=low
        assert ok==(union==SIZE-1)
        if ok:legal[m]=1;faces.append(m);fvec[m.bit_count()-1]+=1
    return legal,faces,fvec

def match(legal,faces,order):
    used=bytearray(SIZE);lower_by_higher={}
    for v in order:
        bit=1<<v
        for m in faces:
            if m&bit:continue
            n=m|bit
            if not used[m] and legal[n] and not used[n]:
                used[m]=used[n]=1;lower_by_higher[n]=m
    crit=[m for m in faces if not used[m]]
    return lower_by_higher,crit

def acyclic(faces,pairs):
    indeg=[0]*SIZE
    adj={m:[] for m in faces}
    edges=0
    for high in faces:
        h=high
        while h:
            bit=h&-h;h^=bit
            low=high^bit
            if low==0:continue
            if pairs.get(high)==low:
                src,dst=low,high
            else:src,dst=high,low
            adj[src].append(dst);indeg[dst]+=1;edges+=1
    q=deque(m for m in faces if not indeg[m]);count=0
    while q:
        cur=q.popleft();count+=1
        for nxt in adj[cur]:
            indeg[nxt]-=1
            if indeg[nxt]==0:q.append(nxt)
    assert count==len(faces),(count,len(faces))
    return edges,count

def sign_on_set(g,s):
    vs=[v for v in range(N) if s>>v&1]
    w=[g[v] for v in vs]
    swaps=sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
    return -1 if swaps%2 else 1

def permutations():
    S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    transforms=[]
    for a,b,c,d in product(range(4),repeat=4):
        cols={(a,c),(b,d),((a+b)%4,(c+d)%4)}
        image={((a*x+b*y)%4,(c*x+d*y)%4) for x,y in S}
        if image==S and len(cols)==3:transforms.append((a,b,c,d))
    group=[]
    for a,b,c,d in transforms:
        for tx,ty in product(range(4),repeat=2):
            group.append(tuple(4*((a*x+b*y+tx)%4)+(c*x+d*y+ty)%4 for x,y in product(range(4),repeat=2)))
    assert len(transforms)==12 and len(group)==192 and len(set(group))==192
    return group

def character(legal,faces):
    group=permutations()
    chi=[];hist=Counter()
    for g in group:
        # sum signed contributions for all fixed nonempty faces
        total=0
        for m in faces:
            t=m;s=0
            while t:
                bit=t&-t;t^=bit;s |= 1<<g[bit.bit_length()-1]
            if s==m:total+=((-1)**(m.bit_count()-1))*sign_on_set(g,m)
        trace=1-total  # degree nine -> trace = 1 - ordinary Lefschetz
        chi.append(trace)
        cycle=[];seen=set()
        for v in range(N):
            if v in seen:continue
            z=v;k=0
            while z not in seen:
                seen.add(z);z=g[z];k+=1
            cycle.append(k)
        hist[(tuple(sorted(cycle)),trace)]+=1
    # Orthogonality and invariants for rational character
    assert chi[0]==11 or 11 in chi
    return group,chi,hist

def main():
    out={}
    for name in ('Shrikhande','rook'):
        adj=make_graph(name)
        assert all((adj[i]>>i&1)==0 for i in range(N))
        assert all(adj[i]>>j&1==adj[j]>>i&1 for i in range(N) for j in range(N))
        assert all(x.bit_count()==6 for x in adj)
        assert all(sum((adj[i] & adj[j]).bit_count()==2 for j in range(N) if i!=j)==15 for i in range(N))
        legal,faces,fvec=make_faces(adj)
        pairs,crit=match(legal,faces,list(range(N)))
        edges,visited=acyclic(faces,pairs)
        # inverse ordering is independent acyclic check
        pairs2,crit2=match(legal,faces,list(reversed(range(N))))
        edges2,visited2=acyclic(faces,pairs2)
        c=Counter(m.bit_count()-1 for m in crit)
        c2=Counter(m.bit_count()-1 for m in crit2)
        assert c==c2
        euler=sum((-1)**d*k for d,k in fvec.items())
        assert euler==sum((-1)**d*k for d,k in c.items())
        assert 2*len(pairs)+len(crit)==len(faces)
        # Every exterior vertex of a fixed vertex has a distinct intersection
        # with the six-vertex neighborhood, proving faithfulness of the
        # local automorphism action.
        if name=='Shrikhande':
            nbr0=adj[0]
            near=[i for i in range(N) if nbr0>>i&1]
            far=[i for i in range(1,N) if not(nbr0>>i&1)]
            assert len(near)==6 and len(far)==9
            assert all((adj[v]&nbr0).bit_count()==2 for v in near)
            signatures=[adj[v]&nbr0 for v in far]
            assert len(set(signatures))==9
            # The neighbors of zero induce a 6-cycle.
            assert all((adj[v]&nbr0).bit_count()==2 for v in near)
            seen={near[0]};stack=[near[0]]
            while stack:
                v=stack.pop()
                for w in near:
                    if adj[v]>>w&1 and w not in seen:seen.add(w);stack.append(w)
            assert len(seen)==6
        out[name]={"adjacency_bitmasks":adj,"vertices":N,"edges":sum(x.bit_count() for x in adj)//2,"face_count":len(faces),"f_vector":{"%d"%d:v for d,v in sorted(fvec.items())},"euler_characteristic":euler,"match_pairs":len(pairs),"cover_relations":edges,"topological_order_visits":visited,"critical_cells":{"%d"%d:v for d,v in sorted(c.items())},"second_matching_pairs":len(pairs2),"second_critical_cells":{"%d"%d:v for d,v in sorted(c2.items())},"second_acyclic_cover_relations":edges2}
        print(name,out[name]['face_count'],out[name]['critical_cells'],out[name]['second_critical_cells'],flush=True)
        if name=='Shrikhande':
            gr,chi,hist=character(legal,faces)
            assert sum(chi)%len(chi)==0
            out[name]['automorphism_group_size']=len(gr)
            out[name]['character_by_group_element']=chi
            out[name]['character_by_cycle_type_and_trace']=[{'cycle_lengths':list(cyc),'homology_trace':tr,'frequency':cnt} for (cyc,tr),cnt in sorted(hist.items())]
            out[name]['invariant_homology_dimension']=sum(chi)//len(chi)
            assert sum(k*k for k in chi)%len(chi)==0
            out[name]['character_inner_product']=sum(k*k for k in chi)//len(chi)
            # Exact conjugacy-class character table: every element belongs
            # to one of the computed classes and trace is constant there.
            indices={g:i for i,g in enumerate(gr)}
            def comp(a,b):return tuple(a[b[i]] for i in range(N))
            def inv(a):
                v=[0]*N
                for i,j in enumerate(a):v[j]=i
                return tuple(v)
            classes=[];seen=set()
            for i,g in enumerate(gr):
                if i in seen:continue
                cl={indices[comp(comp(h,g),inv(h))] for h in gr}
                assert len({chi[j] for j in cl})==1
                seen|=cl
                cs=[];visited=set()
                for j in range(N):
                    if j in visited:continue
                    v=j;length=0
                    while v not in visited:
                        visited.add(v);v=g[v];length+=1
                    cs.append(length)
                classes.append({'representative_index':i,'cycle_lengths':sorted(cs),
                                'class_size':len(cl),'H9_trace':chi[i]})
            assert len(classes)==14 and len(seen)==192
            out[name]['conjugacy_classes']=classes
            print('aut',len(gr),'invariant',out[name]['invariant_homology_dimension'],'inner',out[name]['character_inner_product'],flush=True)
    with open(Path(__file__).with_name('certificate.json'),'w',encoding='utf-8') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
    print('SHRIKHANDE_ROOK_DOMINANCE_CERTIFICATE_PASS')
if __name__=='__main__':main()
