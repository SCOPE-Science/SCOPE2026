#!/usr/bin/env python3
"""Reproduce the first forest complex of the generalized Petersen graph G(8,3).

Standard Python 3 only. All enumerations are complete, and the Morse boundary
is computed by signed integral gradient-path elimination. No external files.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import json

N = 16

def graph():
    edges = set()
    for i in range(8):
        for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
            edges.add(tuple(sorted((a,b))))
    adj = [0]*N
    for a,b in edges:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    assert len(edges) == 24 and all(a.bit_count()==3 for a in adj)
    return sorted(edges),adj

EDGES,ADJ=graph()

def admissible(mask,level):
    if level==0:
        return all(not (mask & (1<<v) and mask&ADJ[v]) for v in range(N))
    return all((mask&ADJ[v]).bit_count()<=1 for v in range(N) if mask&(1<<v))

def admissible_second(mask,level):
    degrees=[0]*N
    for u,v in EDGES:
        if mask&(1<<u) and mask&(1<<v):
            degrees[u]+=1;degrees[v]+=1
    return max(degrees)<=level

def enumerate_faces(level):
    F=[]
    for mask in range(1<<N):
        a=admissible(mask,level)
        b=admissible_second(mask,level)
        assert a==b,('disagree',mask,level)
        if a:F.append(mask)
    return F

def boundary(face):
    # Signed simplicial boundary of an ordered vertex subset.
    b=face;position=0
    while b:
        bit=b&-b
        yield face^bit, (-1 if position%2 else 1)
        position+=1;b^=bit

def pairing(F,order):
    remaining=set(F);lo={};hi={}
    for v in order:
        bit=1<<v
        for face in F:
            if face&bit or face not in remaining:continue
            larger=face|bit
            if larger in remaining:
                lo[face]=larger;hi[larger]=face
                remaining.remove(face);remaining.remove(larger)
    return lo,hi,remaining

def acyclic(F,lo):
    matched={(a,b) for a,b in lo.items()}
    indeg={x:0 for x in F}
    successors=defaultdict(list)
    arrows=0
    for upper in F:
        for lower,_ in boundary(upper):
            if (lower,upper) in matched:
                a,b=lower,upper
            else:
                a,b=upper,lower
            successors[a].append(b);indeg[b]+=1;arrows+=1
    queue=deque(x for x in F if indeg[x]==0)
    visited=0
    while queue:
        x=queue.popleft();visited+=1
        for y in successors[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert visited==len(F),(visited,len(F))
    return arrows

def morse_complex(F,order):
    lo,hi,crit=pairing(F,order)
    arrows=acyclic(F,lo)
    bydim={d:sorted(x for x in crit if x.bit_count()-1==d) for d in sorted({x.bit_count()-1 for x in crit})}
    @lru_cache(None)
    def project(x):
        if x in crit:return {x:1}
        if x in hi:return {}
        upper=lo[x]
        inc=next(sign for y,sign in boundary(upper) if y==x)
        out=defaultdict(int)
        for y,sgn in boundary(upper):
            if y==x:continue
            for z,value in project(y).items():out[z]-=inc*sgn*value
        return {k:v for k,v in out.items() if v}
    matrices={}
    for d in bydim:
        if d-1 not in bydim:continue
        rows={x:i for i,x in enumerate(bydim[d-1])}
        A=[[0]*len(bydim[d]) for _ in rows]
        for j,c in enumerate(bydim[d]):
            for face,sgn in boundary(c):
                for target,value in project(face).items():
                    A[rows[target]][j]+=sgn*value
        matrices[d]=A
    return {'pairs':len(lo),'critical':{str(d):len(xs) for d,xs in bydim.items()},
            'arrows':arrows,'differentials':matrices,'projection_states':project.cache_info().currsize}

def determinant(M):
    # Only used for small, explicitly chosen 3x3 integer minors.
    if len(M)==1:return M[0][0]
    return sum((-1 if k%2 else 1)*a*determinant([row[:k]+row[k+1:] for row in M[1:]]) for k,a in enumerate(M[0]))

def mod2_boundary_rank(cells_lo,cells_hi):
    ind={f:j for j,f in enumerate(cells_lo)}
    pivots={}
    for x in cells_hi:
        vec=0
        for y,_ in boundary(x):vec|=1<<ind[y]
        while vec:
            lead=vec.bit_length()-1
            if lead not in pivots:
                pivots[lead]=vec;break
            vec^=pivots[lead]
    return len(pivots)

def simplicial_homology_mod2(F):
    bysize=defaultdict(list)
    for x in F:bysize[x.bit_count()].append(x)
    sizes=sorted(bysize)
    ranks={d-1:mod2_boundary_rank(bysize[d-1],bysize[d]) for d in sizes if d>=1}
    # augmented boundary for singletons -> empty face has rank one
    betti={d-1:len(bysize[d])-ranks.get(d-1,0)-ranks.get(d,0) for d in sizes if d>=1}
    return {str(k):v for k,v in betti.items() if v},ranks

def check(level):
    F=enumerate_faces(level)
    count=dict(sorted(Counter(str(x.bit_count()-1) for x in F).items(),key=lambda t:int(t[0])))
    up=morse_complex(F,range(N))
    down=morse_complex(F,range(N-1,-1,-1))
    betti,ranks=simplicial_homology_mod2(F)
    assert up['arrows']==down['arrows']
    return {'face_count_including_empty':len(F),'face_numbers':count,'ascending':up,'descending':down,
            'mod2_betti_reduced':betti,'simplicial_mod2_boundary_ranks':{str(k):v for k,v in ranks.items()}}

def main():
    v0=check(0);v1=check(1)
    assert v0['face_count_including_empty']==1091
    assert v1['face_count_including_empty']==6813
    assert v0['mod2_betti_reduced']=={'3':4,'4':1}
    assert v1['mod2_betti_reduced']=={'6':3}
    for report in (v1,):
        for name in ('ascending','descending'):
            M=report[name]
            assert M['critical']=={'4':1,'5':4,'6':6},M['critical']
            B5=M['differentials'][5]
            B6=M['differentials'][6]
            assert len(B5)==1 and len(B5[0])==4
            assert len(B6)==4 and len(B6[0])==6
            assert any(abs(t)==1 for t in B5[0])
            for col in range(6):assert sum(B5[0][r]*B6[r][col] for r in range(4))==0
            # Eliminate a unit incidence between the only degree-4 cell and one degree-5 cell.
            pivot=next(i for i,x in enumerate(B5[0]) if abs(x)==1)
            remaining=[i for i in range(4) if i!=pivot]
            assert any(abs(determinant([[B6[r][c] for c in cols] for r in remaining]))==1
                       for cols in combinations(range(6),3))
    # Count reduced Euler characteristic directly, independent of Morse matrices.
    assert sum((-1)**(int(d)) * x for d,x in v1['face_numbers'].items()) == 3
    print(json.dumps({'graph':'generalized Petersen graph GP(8,3)',
          'level_zero':v0,'level_one':v1,'verified':'MOBIUS_KANTOR_FIRST_FOREST_THREE_SIX_SPHERES_VERIFIED'},
          sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
