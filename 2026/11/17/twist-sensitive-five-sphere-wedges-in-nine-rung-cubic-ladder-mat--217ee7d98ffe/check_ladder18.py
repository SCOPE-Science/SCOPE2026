#!/usr/bin/env python3
"""Exact check of ordinary matching complexes of the two 18-vertex cubic ladders.
No outside packages are required. All arithmetic in Morse boundaries uses integers.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import json, sys

def ladder(kind, n=9):
    v=2*n
    if kind=='twisted':
        edges={tuple(sorted((i,(i+1)%v))) for i in range(v)}
        edges.update((i,i+n) for i in range(n))
    elif kind=='untwisted':
        edges={tuple(sorted((i,(i+1)%n))) for i in range(n)}
        edges.update(tuple(sorted((i+n,(i+1)%n+n))) for i in range(n))
        edges.update((i,i+n) for i in range(n))
    else:raise ValueError(kind)
    edges=sorted(edges)
    m=len(edges)
    conflict=[]
    for i,(a,b) in enumerate(edges):
        conflict.append(sum(1<<j for j,(c,d) in enumerate(edges) if i!=j and (a==c or a==d or b==c or b==d)))
    faces=[]
    def dfs(available,selected):
        if not available:
            faces.append(selected);return
        bit=available&-available
        i=bit.bit_length()-1
        dfs(available^bit,selected)
        dfs(available&~(bit|conflict[i]),selected|bit)
    dfs((1<<m)-1,0)
    faces=sorted(set(faces))
    assert len(faces)==len(set(faces)) and 0 in faces
    proper=set(faces);proper.remove(0)
    alive=set(proper)
    matched={}
    # Lexicographic pivot matching on surviving faces, highest pivot first.
    for i in range(m-1,-1,-1):
        bit=1<<i
        pairs=[(x,x|bit) for x in alive if not x&bit and x|bit in alive]
        for low,high in pairs:
            assert low in alive and high in alive
            alive.remove(low);alive.remove(high)
            matched[low]=high
    assert 2*len(matched)+len(alive)==len(proper)
    critical=sorted(alive)
    cc=Counter(x.bit_count()-1 for x in critical)
    assert cc[0]==1 and all(x in (0,5,6) for x in cc)
    # Complete directed face-poset Hasse graph: gradient pairs go up,
    # all other covers go down. Kahn's algorithm certifies acyclicity.
    ix={v:i for i,v in enumerate(faces)}
    indeg=[0]*len(faces)
    arcs=[[] for _ in faces]
    covers=0
    for hi in faces:
        if not hi:continue
        for b in bits(hi):
            lo=hi^b
            if not lo:continue
            if matched.get(lo)==hi:src,dst=lo,hi
            else:src,dst=hi,lo
            arcs[ix[src]].append(ix[dst]);indeg[ix[dst]]+=1;covers+=1
    dq=deque(i for i,x in enumerate(indeg) if x==0)
    visited=0
    while dq:
        i=dq.popleft();visited+=1
        for j in arcs[i]:
            indeg[j]-=1
            if indeg[j]==0:dq.append(j)
    assert visited==len(faces),('cycle',visited,len(faces))
    # Reduced Morse integer differential from each critical 6-cell to
    # critical 5-cells: signed cancellation along upward (5,6) pairs.
    C5=sorted(x for x in critical if x.bit_count()==6)
    C6=sorted(x for x in critical if x.bit_count()==7)
    up56={x:y for x,y in matched.items() if x.bit_count()==6}
    def boundary(x):
        return [(x^b,(-1)**p) for p,b in enumerate(bits(x))]
    @lru_cache(None)
    def project(face):
        if face in alive:
            return {face:1} if face.bit_count()==6 else {}
        upper=up56.get(face)
        if upper is None:return {}
        df=dict(boundary(upper))[face]
        assert df in (-1,1)
        out=defaultdict(int)
        for other,sgn in boundary(upper):
            if other==face:continue
            for target,coef in project(other).items():out[target]-=sgn*coef*df
        return {k:v for k,v in out.items() if v}
    D=[]
    for six in C6:
        row=defaultdict(int)
        for f,sgn in boundary(six):
            for c,coef in project(f).items():row[c]+=sgn*coef
        D.append([row[c] for c in C5])
    # Full matrix is at most 2 by 26. A +/-1 rank minor gives
    # a primitive cancellable block over Z and hence sphere wedge.
    minor=None
    if len(D)==1:
        for i,z in enumerate(D[0]):
            if abs(z)==1:minor={'columns_1_based':[i+1], 'determinant':z};break
    elif len(D)==2:
        for i in range(len(C5)):
            for j in range(i+1,len(C5)):
                det=D[0][i]*D[1][j]-D[0][j]*D[1][i]
                if abs(det)==1:
                    minor={'columns_1_based':[i+1,j+1], 'determinant':det};break
            if minor:break
    unimod=bool(minor)
    assert unimod,('no unimodular minor',D)
    assert sum(len(x) for x in D)>0
    # No critical 1..4 cells; after integral unit cancellations,
    # only 0-cell and (len(C5)-len(C6)) 5-cells remain.
    assert len(C5)-len(C6)==(22 if kind=='twisted' else 24)
    # Independent simplicial mod-two boundary-rank computation, with NO
    # use of the gradient matching; this tests the homology conclusion.
    by_card={k:sorted(x for x in proper if x.bit_count()==k) for k in range(1,10)}
    def rank2(k):
        if k==1:return 0
        rowindex={x:i for i,x in enumerate(by_card[k-1])}
        basis={}
        for simplex in by_card[k]:
            col=0
            for bit in bits(simplex):col^=1<<rowindex[simplex^bit]
            while col:
                pivot=col.bit_length()-1
                if pivot in basis:col^=basis[pivot]
                else:basis[pivot]=col;break
        return len(basis)
    ranks={k:rank2(k) for k in range(1,10)}
    betti={d:len(by_card[d+1])-ranks[d+1]-ranks.get(d+2,0) for d in range(0,9)}
    assert betti[0]==1 and betti[5]==len(C5)-len(C6) and all(v==0 for d,v in betti.items() if d not in (0,5))
    # Re-enumerated alternating Euler characteristic check.
    chi=sum((-1)**(x.bit_count()-1) for x in proper)
    assert chi==1-(len(C5)-len(C6))
    return dict(kind=kind,vertices=v,edges=m,total_faces_including_empty=len(faces),nonempty_faces=len(proper),f_vector={str(k):v for k,v in sorted(Counter(x.bit_count()-1 for x in proper).items())},matching_pairs=len(matched),critical_cells={str(k):v for k,v in sorted(cc.items())},directed_hasse_covers=covers,topologically_sorted_faces=visited,morse_boundary_6_to_5=D,unimodular_minor=minor,mod2_boundary_ranks=ranks,mod2_betti=betti,reduced_euler=chi-1,homotopy=f'wedge of {len(C5)-len(C6)} five-spheres')

def bits(x):
    while x:
        b=x&-x;yield b;x^=b

if __name__=='__main__':
    r=[ladder(k) for k in ('twisted','untwisted')]
    print(json.dumps(r,sort_keys=True,indent=2))
