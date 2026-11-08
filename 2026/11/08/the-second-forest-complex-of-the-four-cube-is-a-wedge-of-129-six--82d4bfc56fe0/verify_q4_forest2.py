#!/usr/bin/env python3
"""Self-contained exact finite verification of the four-cube linear-forest complex."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=16
EDGES=[(a,b) for a in range(N) for b in range(a+1,N) if (a^b).bit_count()==1]
ADJ=[sum(1<<j for i,j in EDGES if i==k)+sum(1<<i for i,j in EDGES if j==k) for k in range(N)]

def valid_by_union_find(s):
    for v in range(N):
        if (s>>v)&1 and (ADJ[v]&s).bit_count()>2:
            return False
    parent=list(range(N))
    def root(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for u,v in EDGES:
        if (s>>u)&1 and (s>>v)&1:
            a,b=root(u),root(v)
            if a==b: return False
            parent[a]=b
    return True

def valid_by_components(s):
    verts=[v for v in range(N) if (s>>v)&1]
    seen=set()
    for v in verts:
        if v in seen: continue
        queue=[v];seen.add(v);size=0;twice_edges=0
        while queue:
            x=queue.pop();size+=1
            neighbors=[y for y in verts if (x^y).bit_count()==1]
            if len(neighbors)>2:return False
            twice_edges+=len(neighbors)
            for y in neighbors:
                if y not in seen:seen.add(y);queue.append(y)
        if twice_edges!=2*(size-1):return False
    return True

def faces():
    out=set()
    for s in range(1<<N):
        a=valid_by_union_find(s)
        b=valid_by_components(s)
        assert a==b, ('predicates disagree',s)
        if a:out.add(s)
    return out

def face_boundary(s):
    r=s;position=0
    while r:
        b=r&-r;r^=b
        yield (s^b,1 if position%2==0 else -1)
        position+=1

def staged_match(remaining,order):
    remaining=set(remaining)
    lo={};hi={};pivot_counts=[]
    for v in order:
        b=1<<v
        lows=[s for s in remaining if not s&b and (s|b) in remaining]
        for s in lows:
            lo[s]=s|b;hi[s|b]=s
        remaining.difference_update(lows)
        remaining.difference_update([s|b for s in lows])
        pivot_counts.append(len(lows))
    return remaining,lo,hi,pivot_counts

def check_acyclic(all_faces,lo):
    indeg={s:0 for s in all_faces}
    forward=defaultdict(list)
    covers=0
    for high in all_faces:
        for low,e in face_boundary(high):
            if low==0:continue
            covers+=1
            if lo.get(low)==high:
                u,v=low,high
            else:
                u,v=high,low
            forward[u].append(v);indeg[v]+=1
    queue=deque(s for s in indeg if indeg[s]==0)
    cleared=0
    while queue:
        s=queue.popleft();cleared+=1
        for t in forward[s]:
            indeg[t]-=1
            if indeg[t]==0:queue.append(t)
    assert cleared==len(all_faces),(cleared,len(all_faces))
    return covers

def morse_boundary(crit,lo,hi):
    top=sorted(s for s in crit if s.bit_count()==7)
    bottom=sorted(s for s in crit if s.bit_count()==6)
    assert len(top)==136 and len(bottom)==7
    target=set(bottom)
    @lru_cache(None)
    def project(x):
        if x in target:return {x:1}
        if x in hi:return {}
        assert x in lo,(x,'neither matched nor critical')
        t=lo[x]
        incidence=dict(face_boundary(t))
        assert incidence[x] in (-1,1)
        acc=defaultdict(int)
        for u,e in incidence.items():
            if u==x:continue
            for z,a in project(u).items():acc[z]-=incidence[x]*e*a
        return {z:a for z,a in acc.items() if a}
    mat=[]
    for s in top:
        acc=defaultdict(int)
        for u,e in face_boundary(s):
            for z,a in project(u).items():acc[z]+=e*a
        mat.append([acc.get(z,0) for z in bottom])
    return top,bottom,mat

def determinant(rows):
    # Exact Bareiss fraction-free determinant. Integer division is checked.
    a=[list(map(int,row)) for row in rows]
    n=len(a);assert n and all(len(r)==n for r in a)
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=p*a[i][j]-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def rank_mod_two(boundary_vectors):
    pivot={}
    for x in boundary_vectors:
        while x:
            k=x.bit_length()-1
            if k in pivot:x^=pivot[k]
            else:pivot[k]=x;break
    return len(pivot)

def run():
    assert len(EDGES)==32
    F=faces();assert len(F)==14911
    vec=[sum(s.bit_count()==k for s in F) for k in range(9)]
    assert vec==[1,16,120,560,1732,3552,4616,3392,922],vec
    facets=Counter(s.bit_count()-1 for s in F if all((s|(1<<i)) not in F for i in range(N) if not (s>>i)&1))
    assert facets=={6:192,7:922},facets
    assert sum((-1)**(s.bit_count()-1) for s in F)==129
    print('graph_vertices=16 edges=32 subsets=65536 faces_including_empty=14911')
    print('face_vector_by_cardinality='+repr(vec))
    print('facets_dimensions_6_7=192,922 reduced_euler=129')
    for name,order,row_masks in [
        ('forward',list(range(N)),[6872,7112,7352,7592,11384,28778,34228]),
        ('reverse',list(reversed(range(N))),[1964,1994,2908,3386,5548,7777,12590])]:
        crit,lo,hi,stage=staged_match(F-{0},order)
        profile=dict(sorted(Counter(s.bit_count()-1 for s in crit).items()))
        assert profile=={0:1,5:7,6:136},profile
        assert len(lo)==7383 and len(hi)==7383 and len(crit)==144
        assert all(t in F and (t^s).bit_count()==1 for s,t in lo.items())
        covers=check_acyclic(F-{0},lo)
        top,bottom,mat=morse_boundary(crit,lo,hi)
        selected=[mat[top.index(t)] for t in row_masks]
        det=determinant(selected)
        assert abs(det)==1,(name,det)
        nonzeros=sum(bool(x) for row in mat for x in row)
        assert nonzeros==105,nonzeros
        assert len(top)==136 and len(bottom)==7
        print(name+': pairs='+str(len(lo))+' critical=1x0+7x5+136x6 covers='+str(covers)+' acyclic=YES')
        print(name+': boundary_shape=7x136 nonzeros=105 unimodular_minor_det='+str(det))
        print(name+': minor_rows='+repr(row_masks)+' critical5_masks='+repr(bottom))
    groups={k:sorted(s for s in F if s.bit_count()==k+1) for k in range(8)}
    ranks=[]
    for d in range(1,8):
        lowindex={s:i for i,s in enumerate(groups[d-1])}
        cols=[]
        for t in groups[d]:
            v=0
            for s,_ in face_boundary(t):v^=1<<lowindex[s]
            cols.append(v)
        ranks.append(rank_mod_two(cols))
    assert ranks==[15,105,455,1277,2275,2341,922],ranks
    print('full_simplicial_mod2_boundary_ranks='+repr(ranks))
    print('VERIFY_Q4_SECOND_FOREST_WEDGE129_S6_OK')
if __name__=='__main__':run()
