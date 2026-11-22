#!/usr/bin/env python3
"""Exact integral certificate for the Pappus three-particle product-torus lattice.

No third-party libraries required. Run: python3 verify.py
The fully reduced Swiatkowski model computes unordered graph configurations.
"""
from collections import defaultdict, Counter
from itertools import combinations, product
from heapq import heappush, heappop


def graph():
    jumps=(5,7,-7,7,-7,-5)*3
    edges={tuple(sorted((i,(i+1)%18))) for i in range(18)}
    for i,delta in enumerate(jumps):
        edges.add(tuple(sorted((i,(i+delta)%18))))
    edges=sorted(edges)
    assert len(edges)==27
    assert all(sum(v in e for e in edges)==3 for v in range(18))
    inc={v:tuple(i for i,e in enumerate(edges) if v in e) for v in range(18)}
    return edges,inc


def simple_cycles(edges):
    """Start each undirected cycle at its least vertex and take one direction."""
    nbr={v:[] for v in range(18)}
    for u,v in edges:
        nbr[u].append(v);nbr[v].append(u)
    for n in nbr.values():n.sort()
    cycles=[]
    for root in range(18):
        def dfs(path,seen):
            v=path[-1]
            for w in nbr[v]:
                if w==root:
                    if len(path)>=3 and path[1]<path[-1]:
                        cycles.append(tuple(path))
                elif w>root and w not in seen:
                    dfs(path+[w],seen|{w})
        for v in nbr[root]:
            if v>root:
                dfs([root,v],{root,v})
    return sorted(cycles,key=lambda c:(len(c),c))


def three_complex(edges,inc):
    c3=[]
    for vs in combinations(range(18),3):
        for aa in product((1,2),repeat=3):c3.append((vs,aa))
    c2=[(vs,aa,e) for vs in combinations(range(18),2)
        for aa in product((1,2),repeat=2) for e in range(27)]
    c3_index={x:i for i,x in enumerate(c3)}
    c2_index={x:i for i,x in enumerate(c2)}
    cols=[]
    for vs,aa in c3:
        d={}
        for k in range(3):
            rem=tuple(v for j,v in enumerate(vs) if j!=k)
            rb=tuple(a for j,a in enumerate(aa) if j!=k)
            for sgn,e in ((1,inc[vs[k]][aa[k]]),(-1,inc[vs[k]][0])):
                row=c2_index[(rem,rb,e)]
                d[row]=d.get(row,0)+(-1 if k&1 else 1)*sgn
        cols.append(d)
    assert len(c3)==6528 and len(c2)==16524
    assert sum(map(len,cols))==39168
    return c3_index,cols


def torus_chains(cycles,edges,inc,c3_index,cols):
    eid={e:i for i,e in enumerate(edges)}
    six=[c for c in cycles if len(c)==6]
    covers=[tr for tr in combinations(six,3)
            if not (set(tr[0])&set(tr[1]) or set(tr[0])&set(tr[2])
                    or set(tr[1])&set(tr[2]))]
    assert Counter(map(len,cycles))=={6:18,8:54,10:54,12:243,14:162,16:216,18:36}
    assert len(covers)==6
    def one_cycle(c):
        f=defaultdict(int)
        for i,v in enumerate(c):
            prev=c[i-1]; nex=c[(i+1)%len(c)]
            ep=eid[tuple(sorted((v,prev)))];en=eid[tuple(sorted((v,nex)))]
            for s,e in ((1,ep),(-1,en)):
                j=inc[v].index(e)
                if j:f[(v,j)]+=s
        return [(x,a) for x,a in f.items() if a]
    tori=[]
    for tr in covers:
        factors=[one_cycle(c) for c in tr]
        chain=defaultdict(int)
        for t in product(*factors):
            s=sorted(t,key=lambda x:x[0][0])
            v=tuple(x[0][0] for x in s);a=tuple(x[0][1] for x in s)
            sign=(-1)**sum(t[i][0][0]>t[j][0][0] for i in range(3) for j in range(i+1,3))
            coeff=sign
            for _,b in t:coeff*=b
            chain[c3_index[(v,a)]]+=coeff
        chain={r:b for r,b in chain.items() if b}
        boundary=defaultdict(int)
        for j,b in chain.items():
            for i,a in cols[j].items():boundary[i]+=a*b
        assert all(x==0 for x in boundary.values())
        tori.append(chain)
    # Six selected coordinate functionals, in the c3 basis defined above.
    witness_rows=[8,32,140,176,285,600]
    coefficient_matrix=[[t.get(r,0) for t in tori] for r in witness_rows]
    assert coefficient_matrix==[
        [0,0,0,0,0,-1], [0,0,0,0,-1,0], [0,0,0,1,0,0],
        [0,0,1,0,0,0], [0,1,0,0,0,0], [1,0,0,0,0,0]]
    return covers,tori,witness_rows


def mod_rank(vectors,p=101):
    basis={}
    for v in vectors:
        d={i:a%p for i,a in v.items() if a%p}
        while d:
            k=min(d)
            if k not in basis:
                inv=pow(d[k],-1,p)
                basis[k]={i:a*inv%p for i,a in d.items() if a*inv%p}
                break
            a=d[k]
            for r,b in basis[k].items():
                w=(d.get(r,0)-a*b)%p
                if w:d[r]=w
                else:d.pop(r,None)
    return len(basis)


def integer_unit_reduction(raw_cols):
    """Reversible matrix elimination by signed unit pivots.

    Eliminating row r/column j with coefficient +1 or -1 is a
    unimodular change of bases; the remaining block has the same kernel
    and cokernel ranks as the old block minus one. The function returns
    its terminal columns and the number of exact unit cancellations.
    """
    cols=[dict(x) for x in raw_cols]
    rowcols=defaultdict(set)
    for j,d in enumerate(cols):
        for r in d:rowcols[r].add(j)
    h=[(len(s),r) for r,s in rowcols.items() if s]
    from heapq import heapify
    heapify(h)
    active=set(range(len(cols)))
    zero_columns=0
    for j,c in enumerate(cols):
        if not c:active.remove(j);zero_columns+=1
    pivots=0
    while h:
        degree,r=heappop(h)
        if not rowcols[r] or len(rowcols[r])!=degree:continue
        js=rowcols[r]
        candidates=[j for j in js if abs(cols[j][r])==1]
        if not candidates:continue
        j=min(candidates,key=lambda k:len(cols[k]))
        piv=cols[j][r]
        pivotcol=cols[j]
        for k in tuple(js):
            if k==j:continue
            mul=cols[k][r]*piv
            d=cols[k]
            for rr,aa in pivotcol.items():
                val=d.get(rr,0)-mul*aa
                if val:
                    if rr not in d:rowcols[rr].add(k)
                    d[rr]=val
                elif rr in d:
                    del d[rr];rowcols[rr].discard(k)
                if rr!=r and rowcols[rr]:heappush(h,(len(rowcols[rr]),rr))
            if not d:
                active.remove(k)
                zero_columns+=1
        for rr in pivotcol:
            rowcols[rr].discard(j)
            if rowcols[rr]:heappush(h,(len(rowcols[rr]),rr))
        active.remove(j)
        cols[j]={}
        pivots+=1
    return pivots,zero_columns,[cols[j] for j in sorted(active)]


def verify():
    edges,inc=graph()
    cy=simple_cycles(edges)
    c3index,cols=three_complex(edges,inc)
    covers,tori,rows=torus_chains(cy,edges,inc,c3index,cols)
    assert mod_rank(tori,101)==6
    pivots,zeros,residual=integer_unit_reduction(cols)
    assert (pivots,zeros,len(residual))==(6515,4,9), (pivots,zeros,len(residual))
    # Exact integral relations, relative to the final nine residual columns.
    relations=[(-1,1,0,0,0,0,0,0,0),
               (-1,0,-2,1,1,0,0,1,0),
               (1,0,2,-1,0,-1,1,0,1)]
    for rel in relations:
        rowsums=defaultdict(int)
        for i,a in enumerate(rel):
            if a:
                for r,v in residual[i].items():rowsums[r]+=a*v
        assert all(v==0 for v in rowsums.values())
    assert mod_rank(residual,101)==6
    # 3 independent residual kernel relations imply rank <=6 over Q.
    # F_101 rank 6 implies rank >=6 over Q: hence equality.
    assert [[r[1],r[4],r[5]] for r in relations] == [
        [1,0,0], [0,1,0], [0,0,-1]]
    # Complete differential has rank 6515+6=6521 and 6528 columns,
    # so its integral kernel is free of rank 7 (no degree-four chains).
    # Product three-tori are six independent elements and are primitive:
    # their 6x6 integral coordinate minor is a signed permutation matrix.
    # Since ker(d3) is saturated in C3, quotient by these tori is Z.
    print('VERIFY_OK_PAPPUS_THREE_PRODUCT_TORI_PRIMITIVE_RANK_SIX')
    print('cycles',len(cy),'disjoint_hexagon_triples',len(covers))
    print('chain_ranks',6528,16524,'unit_pivots',pivots,
          'residual_rank',6,'H3_rank',6528-pivots-6,
          'product_rank',len(tori),'product_quotient_free_rank',1)

if __name__=='__main__':verify()
