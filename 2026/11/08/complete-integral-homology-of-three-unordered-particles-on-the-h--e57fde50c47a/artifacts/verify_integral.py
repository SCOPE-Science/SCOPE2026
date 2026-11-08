#!/usr/bin/env python3
"""Exact integral top-boundary certificate for the Heawood three-point configuration space.
Standard-library-only reconstruction from the Fano incidence presentation.
"""
from collections import defaultdict
from itertools import combinations,product,combinations_with_replacement
from heapq import heappush,heappop
import hashlib


def graph():
    edges=tuple((i,7+j) for i in range(7) for j in range(7) if (i-j)%7 in (0,1,3))
    inc=[[] for _ in range(14)]
    adj=[set() for _ in range(14)]
    for e,(a,b) in enumerate(edges):
        inc[a].append(e);inc[b].append(e)
        adj[a].add(b);adj[b].add(a)
    assert len(edges)==21 and all(len(q)==3 for q in inc)
    # Enumerate every deletion set with fewer than three vertices.
    for n in range(3):
        for cut in combinations(range(14),n):
            active=set(range(14))-set(cut)
            seen={min(active)}
            frontier=list(seen)
            while frontier:
                x=frontier.pop()
                for y in adj[x]&active-seen:
                    seen.add(y);frontier.append(y)
            assert seen==active
    # Any two distinct points of the Fano plane share one line: cycles have length >=6.
    assert all(len(adj[i]&adj[j])==1 for i in range(7) for j in range(i+1,7))
    # Bipartite planar girth-six bound: e<=3/2(v-2)=18; here e=21.
    assert len(edges)>3*(14-2)//2
    return edges,inc


def boundary(verts,bits,monomial,inc):
    """Differential of an ordered product of local differences and edge variables."""
    d=defaultdict(int)
    for k,v in enumerate(verts):
        restv=verts[:k]+verts[k+1:]
        restb=bits[:k]+bits[k+1:]
        sig=1 if k%2==0 else -1
        for edge,coeff in ((inc[v][bits[k]+1],sig),(inc[v][0],-sig)):
            m=tuple(sorted(monomial+(edge,)))
            d[(restv,restb,m)]+=coeff
    return {key:x for key,x in d.items() if x}


def matrices():
    edges,inc=graph()
    column=[]
    all_d2=set()
    all_d1=set()
    for verts in combinations(range(14),3):
        for bits in product((0,1),repeat=3):
            col=boundary(verts,bits,(),inc)
            column.append(col)
            all_d2.update(col)
            # direct integer boundary^2 check, not a mod-p approximation
            d2=defaultdict(int)
            for (v,b,m),c in col.items():
                for term,x in boundary(v,b,m,inc).items():
                    d2[term]+=c*x
            assert not any(d2.values())
    # Full dimensions, INCLUDING unused rows; weight 3.
    sizes=(1771,6468,7644,2912)
    assert len(column)==sizes[3] and len(all_d2)==7560
    assert len(all_d1)==0  # intentionally unused accumulator
    print('graph_vertices_edges=14,21')
    print('fano_graph_3_vertex_connected=yes;nonplanar_by_girth=yes')
    print('chain_dimensions='+','.join(map(str,sizes)))
    print('d3_nonzero_rows='+str(len(all_d2)))
    print('d2_d3_zero_integer=yes')
    return column


def smith_unit_reduction(columns,order=0,return_residual=False):
    """Exact invertible integer row/column operations; pivots must be +/-1.
    Operations implement a unimodular Schur complement, and stop only after
    exhausting all eligible pivots; the final matrix is returned implicitly.
    """
    columns={c:dict(vec) for c,vec in enumerate(columns)}
    rows=defaultdict(dict)
    for c,vec in columns.items():
        for r,v in vec.items(): rows[r][c]=v
    # Reencode row keys into small integers for reproducible tie order.
    labels={r:j for j,r in enumerate(sorted(rows))}
    cols={c:{labels[r]:a for r,a in d.items()} for c,d in columns.items()}
    row={labels[r]:dict(d) for r,d in rows.items()}
    def priority(r,c):
        a=len(row[r])-1; b=len(cols[c])-1
        if order==0:return (a*b,a+b,r,c)
        return (a*b,a+b,-c,-r)
    heap=[]
    for r,cs in row.items():
        for c,a in cs.items():
            if abs(a)==1:heappush(heap,(priority(r,c),r,c))
    pivots=0;max_pivot_fill=0
    while heap:
        priority_stored,r,c=heappop(heap)
        if r not in row or c not in cols or abs(row[r].get(c,0))!=1:continue
        p=priority(r,c)
        if p>priority_stored:
            heappush(heap,(p,r,c));continue
        col=cols[c]; rr=row[r]; sign=rr[c]
        fill=(len(rr)-1)*(len(col)-1)
        max_pivot_fill=max(fill,max_pivot_fill)
        for other,b in list(rr.items()):
            if other==c:continue
            mult=b*sign
            q=cols[other]
            for target,value in col.items():
                if target==r:continue
                new=q.get(target,0)-mult*value
                if new:
                    q[target]=new;row[target][other]=new
                else:
                    q.pop(target,None)
                    row[target].pop(other,None)
                    if not row[target]:row.pop(target)
            q.pop(r,None)
        for target in col:
            if target==r:continue
            row[target].pop(c,None)
            if not row[target]:row.pop(target)
        cols.pop(c);row.pop(r,None);pivots+=1
        for other in rr:
            if other not in cols:continue
            for target,a in cols[other].items():
                if abs(a)==1:
                    heappush(heap,(priority(target,other),target,other))
    nonzero=sum(bool(q) for q in cols.values())
    nnz=sum(map(len,cols.values()))
    if return_residual: return pivots,len(cols),len(row),nonzero,nnz,max_pivot_fill,cols
    return pivots,len(cols),len(row),nonzero,nnz,max_pivot_fill


def rank_one_invariant(residual):
    """For rank-one integer matrix, gcd(entries) is its Smith invariant."""
    from math import gcd
    nz=[q for q in residual.values() if q]
    assert nz
    reference=nz[0]
    pivot=next(iter(reference))
    lead=reference[pivot]
    factor=0
    for col in nz:
        for row in set(reference)|set(col):
            assert reference.get(row,0)*col.get(pivot,0) == col.get(row,0)*lead
        for x in col.values():factor=gcd(factor,abs(x))
    return factor


def main():
    cols3=matrices()
    _,inc=graph()
    # Generate the complete lower-dimensional boundary matrices, not just
    # submatrices reached by the degree-three boundary.
    cols2=[]
    for vv in combinations(range(14),2):
        for bits in product((0,1),repeat=2):
            for e in range(21):
                q=boundary(vv,bits,(e,),inc)
                cols2.append(q)
                composition=defaultdict(int)
                for (v,b,m),coef in q.items():
                    for r,x in boundary(v,b,m,inc).items():
                        composition[r]+=coef*x
                assert not any(composition.values())
    cols1=[]
    for v in range(14):
        for bit in (0,1):
            for m in combinations_with_replacement(range(21),2):
                cols1.append(boundary((v,),(bit,),m,inc))
    assert [len(cols1),len(cols2),len(cols3)]==[6468,7644,2912]
    print('d1_d2_zero_integer=yes')

    r1=smith_unit_reduction(cols1)
    assert r1[:2]==(1770,4698) and r1[3:5]==(0,0)
    print('smith_d1=unit^1770,zero')
    r2=smith_unit_reduction(cols2,return_residual=True)
    assert r2[:2]==(4689,2955)
    invariant=rank_one_invariant(r2[-1])
    assert invariant==2
    print('smith_d2=unit^4689,2,zero')
    print('d2_remaining_nonzero_rows=%d;nonzero_columns=%d'%(r2[2],r2[3]))
    for order in (0,1):
        r3=smith_unit_reduction(cols3,order=order)
        assert r3[:2]==(2911,1) and r3[3:5]==(0,0)
        print('smith_d3_order_%d=unit^2911,zero;maximum_fill=%d'%(order,r3[5]))
    chi=1771-6468+7644-2912
    assert chi==35
    betti=(1771-1770,6468-1770-4690,7644-4690-2911,2912-2911)
    assert betti==(1,8,43,1)
    print('euler_characteristic='+str(chi))
    print('integral_H0=Z;H1=Z^8+Z/2;H2=Z^43;H3=Z')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
