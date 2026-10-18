#!/usr/bin/env python3
"""Exhaustive integral character computation for the tetrahedral Morse complex.
Only Python standard library. All face masks are nonzero subsets of {0,1,2,3}.
An acyclic Hasse matching is a simplex of the Chari--Joswig complex.
"""
from itertools import permutations
from collections import defaultdict
from math import factorial

FACES=list(range(1,16))
EDGES=sorted((a, a | (1<<v)) for a in FACES for v in range(4)
             if not(a & (1<<v)))
assert len(EDGES)==28 and len(set(EDGES))==28
EDGE_ID={e:i for i,e in enumerate(EDGES)}
COVERS=[(a,b) for a,b in EDGES]

def acyclic(bit):
    out={a:[] for a in FACES}
    indeg={a:0 for a in FACES}
    for i,(a,b) in enumerate(COVERS):
        u,v=(b,a) if bit>>i & 1 else (a,b)
        out[u].append(v)
        indeg[v]+=1
    todo=[a for a in FACES if indeg[a]==0]
    seen=0
    while todo:
        u=todo.pop()
        seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:todo.append(v)
    return seen==len(FACES)

def action(p):
    def image(a):return sum(1<<p[i] for i in range(4) if a&(1<<i))
    return [EDGE_ID[(image(a),image(b))] for a,b in EDGES]

def perm_sign(a):
    return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def sum_trace_for_masks(masklist, p):
    eperm=action(p)
    trace=0
    fixed_by_card=defaultdict(int)
    for mask in masklist:
        els=[i for i in range(28) if mask>>i & 1]
        permuted=[eperm[i] for i in els]
        if set(els)!=set(permuted):continue
        positions={x:i for i,x in enumerate(els)}
        sign=perm_sign([positions[x] for x in permuted])
        trace += ((-1)**(len(els)-1))*sign
        fixed_by_card[len(els)]+=1
    return trace,dict(fixed_by_card)

# Enumerate all Hasse matchings; note acyclic is checked on the FULL matching
# rather than pruning a cyclic prefix (so no monotonicity assumption needed).
def all_acyclic_matchings():
    conflict=[]
    for i,(a,b) in enumerate(EDGES):
        conflict.append(sum((1<<j) for j,(c,d) in enumerate(EDGES)
                            if j>i and (a==c or a==d or b==c or b==d)))
    out=[]; all_matchings=0; f=defaultdict(int)
    def rec(selected,available):
        nonlocal all_matchings
        if selected:
            all_matchings+=1
            if acyclic(selected):
                out.append(selected)
                f[selected.bit_count()-1]+=1
        while available:
            lowbit=available & -available
            available-=lowbit
            i=lowbit.bit_length()-1
            rec(selected|lowbit, available&~conflict[i])
    rec(0,(1<<len(EDGES))-1)
    return out,all_matchings, [f.get(i,0) for i in range(7)]

# Separate enumeration over WHOLE cyclic orbits of Hasse edges under given S4
# permutation, not filtering the full precomputed simplex collection.
def orbit_fixed_trace(p):
    act=action(p)
    unseen=set(range(len(EDGES)))
    orbits=[]
    while unseen:
        cur=min(unseen); cyc=[]; j=cur
        while j in unseen:
            unseen.remove(j); cyc.append(j); j=act[j]
        assert j==cur
        used=[]
        for i in cyc:
            used.extend(EDGES[i])
        if len(used)==len(set(used)):
            orbits.append(cyc)
    acc=0; fixed=0
    def rec(pos, chosen, used_faces, perm_sign):
        nonlocal acc,fixed
        if pos==len(orbits):
            if chosen and acyclic(chosen):
                k=chosen.bit_count()
                fixed+=1
                acc+=(-1)**(k-1)*perm_sign
            return
        rec(pos+1,chosen,used_faces,perm_sign)
        cyc=orbits[pos]
        faces={x for i in cyc for x in EDGES[i]}
        if used_faces.isdisjoint(faces):
            rec(pos+1,chosen|sum(1<<i for i in cyc),used_faces|faces,
                perm_sign*(-1)**(len(cyc)-1))
    rec(0,0,set(),1)
    return acc,fixed,len(orbits)

REP=[(0,1,2,3),(1,0,2,3),(1,0,3,2),(1,2,0,3),(1,2,3,0)]
SHAPES=['(1,1,1,1)','(2,1,1)','(2,2)','(3,1)','(4)']
SZ=[1,6,3,8,6]
CHAR={
    '[4]':[1,1,1,1,1],
    '[3,1]':[3,1,-1,0,-1],
    '[2,2]':[2,0,2,-1,0],
    '[2,1,1]':[3,-1,-1,0,1],
    '[1,1,1,1]':[1,-1,1,1,-1],
}

def main():
    all_masks,all_possible, f=all_acyclic_matchings()
    assert f==[28,300,1544,3932,4632,2128,256]
    assert len(all_masks)==12820
    print('ALL_MATCHINGS',all_possible,'ACYCLIC',len(all_masks),'F_VECTOR',f)
    traces=[]
    for shape,size,p in zip(SHAPES,SZ,REP):
        left,bycard=sum_trace_for_masks(all_masks,p)
        right,fixed,orbits=orbit_fixed_trace(p)
        assert left==right
        trH4=left-1
        print('CLASS',shape,'SIZE',size,'ORDINARY_LEFSCHETZ',left,
              'H4_TRACE',trH4,'FIXED',fixed,'ACTION_EDGE_ORBITS',orbits,'FIXED_CARD',bycard)
        traces.append(trH4)
    assert traces[0]==99
    irreps={}
    for ir,chars in CHAR.items():
        val=sum(SZ[i]*traces[i]*chars[i] for i in range(5))
        assert val%24==0,(ir,val)
        irreps[ir]=val//24
        assert irreps[ir]>=0
    assert sum(irreps[ir]*CHAR[ir][0] for ir in CHAR)==99
    print('IRREDUCIBLE_MULTIPLICITIES',irreps)
    # Conjugacy class invariance independently for each of the 24 S4 elements.
    all_other=[]
    for p in permutations(range(4)):
        L,_=sum_trace_for_masks(all_masks,p)
        ctype=tuple(sorted((len(c) for c in cycles(p)),reverse=True))
        all_other.append((ctype,L))
    assert len(all_other)==24
    class_map={tuple(sorted((len(c) for c in cycles(p)),reverse=True)):sum_trace_for_masks(all_masks,p)[0] for p in REP}
    assert all(L==class_map[typ] for typ,L in all_other)
    print('ALL_24_PERMUTATIONS_CHECKED')
    print('VERIFY_OK')

def cycles(p):
    unseen=set(range(4));c=[]
    while unseen:
        i=unseen.pop(); cyc=[i]; x=p[i]
        while x not in cyc:
            unseen.remove(x);cyc.append(x);x=p[x]
        c.append(cyc)
    return c

if __name__=='__main__':main()
