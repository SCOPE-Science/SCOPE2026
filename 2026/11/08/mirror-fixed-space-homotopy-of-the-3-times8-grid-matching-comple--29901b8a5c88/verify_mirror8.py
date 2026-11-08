"""Reproducible exact checks for a reflected rectangular-grid matching complex.
Python 3 standard library only. All integer Morse coefficients use oriented simplicial boundaries.
"""
from collections import Counter, deque
from functools import lru_cache


def graph_edges(n):
    edges=[]
    for r in range(3):
        for c in range(n):
            if r+1<3:
                edges.append(tuple(sorted(((r,c),(r+1,c)))))
            if c+1<n:
                edges.append(tuple(sorted(((r,c),(r,c+1)))))
    return edges


def orbit_complex(n, axis):
    E=graph_edges(n)
    index={frozenset(e):i for i,e in enumerate(E)}
    t=(lambda v:(v[0],n-1-v[1])) if axis=='column' else (lambda v:(2-v[0],v[1]))
    seen=set();orbit=[]
    for i,e in enumerate(E):
        if i in seen:continue
        j=index[frozenset(t(v) for v in e)]; inds=tuple(sorted({i,j}));seen.update(inds)
        support=[v for h in inds for v in E[h]]
        if len(support)!=len(set(support)):continue
        orbit.append((inds, frozenset(support)))
    faces=[0]
    def extend(start,mask,occupied):
        for i in range(start,len(orbit)):
            if orbit[i][1].isdisjoint(occupied):
                s=mask|(1<<i);faces.append(s)
                extend(i+1,s,occupied|orbit[i][1])
    extend(0,0,frozenset())
    return E,orbit,set(faces)


def morse(faces,number_of_vertices):
    unpaired=set(faces);pairs=[]
    for j in range(number_of_vertices):
        bit=1<<j
        for a in list(unpaired):
            if a&bit:continue
            b=a|bit
            if b in unpaired:
                unpaired.remove(a);unpaired.remove(b);pairs.append((a,b))
    return unpaired,pairs


def boundary(simplex):
    k=0; rest=simplex
    while rest:
        bit=rest&-rest;rest^=bit
        yield simplex^bit, (-1 if k&1 else 1)
        k+=1


def check_acyclic(faces,pairs):
    pairs=set(pairs); outgoing={v:[] for v in faces};indeg=Counter()
    incidences=0
    for top in faces:
        for small,s in boundary(top):
            incidences+=1
            a,b=(small,top) if (small,top) in pairs else (top,small)
            outgoing[a].append(b);indeg[b]+=1
    q=deque(v for v in faces if indeg[v]==0);removed=0
    while q:
        v=q.popleft();removed+=1
        for w in outgoing[v]:
            indeg[w]-=1
            if indeg[w]==0:q.append(w)
    assert removed==len(faces), 'cyclic matching'
    return incidences


def morse_matrix(critical,pairs,hi,lo):
    top=sorted(s for s in critical if s.bit_count()==hi+1)
    bottom=sorted(s for s in critical if s.bit_count()==lo+1)
    up=dict(pairs);down={b for a,b in pairs};bottom_set=set(bottom)
    @lru_cache(maxsize=None)
    def resolve(s):
        if s in bottom_set:return {s:1}
        if s in down:return {}
        assert s in up
        b=up[s]; bd=dict(boundary(b));pivot=bd.pop(s)
        out=Counter()
        for ss,sgn in bd.items():
            for z,v in resolve(ss).items():out[z]-=pivot*sgn*v
        return {z:v for z,v in out.items() if v}
    mat=[]
    for t in top:
        out=Counter()
        for s,sign in boundary(t):
            for z,v in resolve(s).items():out[z]+=sign*v
        mat.append([out[z] for z in bottom])
    return top,bottom,mat


def rank_mod2(faces):
    bydim={}
    for s in faces:bydim.setdefault(s.bit_count()-1,[]).append(s)
    rank={}
    for k in sorted(d for d in bydim if d>=1):
        lower={s:i for i,s in enumerate(bydim[k-1])}
        pivots={}
        for s in bydim[k]:
            col=0
            for sm,_ in boundary(s):col^=1<<lower[sm]
            while col:
                j=col.bit_length()-1
                if j in pivots:col^=pivots[j]
                else:pivots[j]=col;break
        rank[k]=len(pivots)
    betti={}
    for k in sorted(d for d in bydim if d>=0):
        b=len(bydim[k])-rank.get(k,0)-rank.get(k+1,0)
        if k==0:b-=1
        if b:betti[k]=b
    return betti


def run():
    for n in (2,4,6,8):
        E,orbits,faces=orbit_complex(n,'column');critical,pairs=morse(faces,len(orbits))
        incidences=check_acyclic(faces,pairs)
        dims=Counter(s.bit_count()-1 for s in critical)
        print('COL',n,'grid_edges',len(E),'valid_orbits',len(orbits),'faces',len(faces),'incidences',incidences,'pairs',len(pairs),'critical',dict(sorted(dims.items())))
        if n>=4:
            hi=n//2;lo=hi-1
            tops,bots,mat=morse_matrix(critical,pairs,hi,lo)
            assert len(tops)==dims[hi] and len(bots)==dims[lo]
            if n==4: assert len(bots)==1 and any(x in (1,-1) for row in mat for x in row)
            if n==6: assert len(bots)==1 and any(x in (1,-1) for row in mat for x in row)
            if n==8:
                assert len(tops)==6 and len(bots)==2
                # Two chosen columns of the transpose form an integral unimodular pivot block.
                witnesses=[(i,j,mat[i][0]*mat[j][1]-mat[j][0]*mat[i][1]) for i in range(6) for j in range(i+1,6)]
                unit=next((w for w in witnesses if abs(w[2])==1),None)
                assert unit is not None
                print('MORSE_MATRIX_8',mat)
                print('UNIT_2x2_WITNESS',unit)
                betti=rank_mod2(faces)
                assert betti=={4:4},betti
                print('INDEPENDENT_MOD2_BETTI_8',betti)
    E,orbits,faces=orbit_complex(8,'row');critical,pairs=morse(faces,len(orbits));incidences=check_acyclic(faces,pairs)
    assert not critical
    print('ROW',8,'valid_orbits',len(orbits),'faces',len(faces),'incidences',incidences,'pairs',len(pairs),'critical',len(critical),'contractible_from_reduced_matching')
    print('ALL_VERIFY_OK')
if __name__=='__main__':run()
