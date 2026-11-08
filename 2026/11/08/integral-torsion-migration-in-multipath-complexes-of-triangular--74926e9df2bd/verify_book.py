#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse proof for the bidirected triangular-book multipath complexes.

Only the Python standard library is used. Every face, matching, cover and signed
critical-cell differential is reconstructed from the definition.
"""
from collections import Counter, deque
from functools import lru_cache
from math import gcd

ORDERS = {
 3:[9,12,5,8,13,10,0,11,2,7,6,1,4,3],
 4:[12,15,5,16,8,14,4,13,0,10,1,2,17,6,11,3,9,7],
 5:[21,0,8,5,17,18,2,16,20,10,7,19,4,3,15,13,1,9,6,12,14,11],
 6:[16,4,20,3,7,10,8,21,1,0,24,12,23,2,13,25,22,11,6,9,15,5,18,14,19,17],
}
EXPECTED = {
 3:({-1:1,0:14,1:54,2:60,3:12},{0:1,1:1,2:8},336,65,3,2),
 4:({-1:1,0:18,1:96,2:168,3:72},{0:1,2:18,3:1},984,167,8,2),
 5:({-1:1,0:22,1:150,2:360,3:240},{0:1,2:23,3:32},2340,358,20,2),
 6:({-1:1,0:26,1:216,2:660,3:600},{0:1,2:38,3:169},4812,647,0,0),
}

def graph_arcs(m):
    return [(0,1),(1,0)]+[(a,b) for j in range(m) for (a,b) in
              [(0,j+2),(j+2,0),(1,j+2),(j+2,1)]]

def enumerate_faces(m):
    arcs=graph_arcs(m)
    faces={0}
    def visit(mask,starting,indeg,outdeg,dsu):
        for i in range(starting,len(arcs)):
            a,b=arcs[i]
            if (indeg>>b)&1 or (outdeg>>a)&1:continue
            def root(z):
                while dsu[z]!=z:z=dsu[z]
                return z
            ra,rb=root(a),root(b)
            if ra==rb:continue
            newdsu=dsu.copy();newdsu[ra]=rb
            next_mask=mask|(1<<i)
            assert next_mask not in faces
            faces.add(next_mask)
            visit(next_mask,i+1,indeg|(1<<b),outdeg|(1<<a),newdsu)
    visit(0,0,0,0,list(range(m+2)))
    return sorted(faces)

def boundary(face):
    js=[j for j in range(face.bit_length()) if face>>j&1]
    return [(face^(1<<j),1 if p%2==0 else -1) for p,j in enumerate(js)]

def matching(faces,order):
    live=set(faces);pairs=[]
    for i in order:
        bit=1<<i
        for x in faces:
            if x not in live or x&bit:continue
            y=x|bit
            if y in live:
                pairs.append((x,y));live.remove(x);live.remove(y)
    return pairs,sorted(live)

def check_acyclicity(faces,pairs):
    nonempty=[f for f in faces if f]
    ids={f:i for i,f in enumerate(nonempty)}
    matched=set(pairs)
    indegrees=[0]*len(nonempty);successors=[[] for _ in nonempty]
    ncover=0
    for f in nonempty:
        for g,_ in boundary(f):
            if not g:continue
            ncover+=1
            source,target=(g,f) if (g,f) in matched else (f,g)
            s,t=ids[source],ids[target]
            successors[s].append(t);indegrees[t]+=1
    queue=deque(i for i,z in enumerate(indegrees) if not z)
    visited=0
    while queue:
        u=queue.popleft();visited+=1
        for v in successors[u]:
            indegrees[v]-=1
            if not indegrees[v]:queue.append(v)
    assert visited==len(nonempty),('nonacyclic',len(nonempty)-visited)
    return ncover

def morse_boundary(pairs,crit):
    low_to_high={a:b for a,b in pairs}
    higher={b for a,b in pairs}
    by_dimension={d:{x for x in crit if x.bit_count()-1==d} for d in range(4)}
    nonzero=[]
    for d in (1,2,3):
        targets=by_dimension[d-1]
        @lru_cache(None)
        def project(f):
            if f in targets:return {f:1}
            if f in higher:return {}
            assert f in low_to_high,('unmatched-facet',f,d)
            u=low_to_high[f]
            coeff=dict(boundary(u))[f]
            result={}
            for g,c in boundary(u):
                if g==f:continue
                for h,z in project(g).items():result[h]=result.get(h,0)-coeff*c*z
            return {x:c for x,c in result.items() if c}
        for x in sorted(by_dimension[d]):
            answer={}
            for y,c in boundary(x):
                for z,v in project(y).items():answer[z]=answer.get(z,0)+c*v
            nonzero.extend((d,x,y,c) for y,c in answer.items() if c)
    return nonzero

def main():
    for m,order in ORDERS.items():
        assert sorted(order)==list(range(4*m+2))
        faces=enumerate_faces(m)
        fv=dict(Counter(f.bit_count()-1 for f in faces))
        expected,critical_expected,covers,pair_count,ncoeff,content=EXPECTED[m]
        assert fv==expected,(m,fv)
        pairs,remaining=matching(faces,order)
        empty_pair=[(a,b) for a,b in pairs if not a]
        assert len(empty_pair)==1 and not any(f==0 for f in remaining)
        original_pairs=[(a,b) for a,b in pairs if a]
        critical=[empty_pair[0][1]]+remaining
        assert dict(Counter(x.bit_count()-1 for x in critical))==critical_expected
        assert len(original_pairs)==pair_count
        assert 2*len(original_pairs)+len(critical)==len(faces)-1
        assert check_acyclicity(faces,original_pairs)==covers
        nonzero=morse_boundary(original_pairs,critical)
        z=0
        for d,a,b,c in nonzero:z=gcd(z,abs(c))
        assert len(nonzero)==ncoeff and z==content,(m,len(nonzero),z)
        assert (m!=5 or len({b for d,a,b,c in nonzero})==1)
        # The only nonzero Morse matrix, where present, has rank one
        # and the gcd of its entries is two; hence its only nonzero
        # integer Smith invariant is 2.
        if nonzero:
            rows=sorted({b for _,_,b,_ in nonzero})
            cols=sorted({a for _,a,_,_ in nonzero})
            matrix={(b,a):c for d,a,b,c in nonzero}
            pivot=next(iter(matrix.items()))
            (r0,c0),v0=pivot
            for r in rows:
                for c in cols:
                    assert matrix.get((r,c),0)*v0 == matrix.get((r,c0),0)*matrix.get((r0,c),0)
        chi=sum((-1)**d*n for d,n in fv.items())
        chi_crit=sum((-1)**d*n for d,n in critical_expected.items())-1
        assert chi==chi_crit
        print(f'm={m} arcs={4*m+2} faces={len(faces)} f_vector={fv} covers={covers} '
              f'matched_pairs={pair_count} critical={critical_expected} '
              f'integer_boundary_entries={ncoeff} boundary_rank={int(bool(nonzero))} '
              f'only_nonzero_Smith_factor={z if nonzero else "none"} reduced_Euler={chi}')
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
