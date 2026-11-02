#!/usr/bin/env python3
"""Exact finite certificates for bounded-degree two simplicial complexes of Möbius ladders."""
from collections import Counter, defaultdict, deque
from array import array
from functools import lru_cache
from itertools import combinations

EXPECTED = {
 3: (265,132,{3:1},{}),
 4: (1697,848,{5:1},{}),
 5: (10897,5446,{6:2,7:3},{7:[[1,0],[0,1],[-1,1]]}),
 6: (69941,34968,{7:1,8:4},{8:[[-1],[1],[-1],[1]]}),
 7: (448945,224471,{9:2,10:1},{10:[[1,1]]}),
}

def edge_list(n):
    return sorted({tuple(sorted((i,(i+1)%(2*n)))) for i in range(2*n)} |
                  {tuple(sorted((i,i+n))) for i in range(n)})

def generate(n):
    edges=edge_list(n); m=len(edges)
    incident=[0]*(2*n)
    for i,(u,v) in enumerate(edges):
        incident[u]|=1<<i;incident[v]|=1<<i
    # First membership test: direct degree computation with edge-bit incidence masks.
    faces=[]
    for F in range(1<<m):
        if all((F&v).bit_count()<=2 for v in incident):faces.append(F)
    # Second independent test on a stratified subset: reject iff three incident edges selected.
    if n<=7:
        triples=set()
        for v in incident:
            inds=[i for i in range(m) if (v>>i)&1]
            for a,b,c in combinations(inds,3): triples.add((1<<a)|(1<<b)|(1<<c))
        other=[F for F in range(1<<m) if all((F&t)!=t for t in triples)]
        assert faces == other
    return edges,faces,incident

def certify(n):
    edges,faces,inc=generate(n); m=len(edges)
    pairs={}; upper=set();paired=set()
    member=bytearray(1<<m)
    for F in faces:member[F]=1
    for b in range(m):
        flag=1<<b
        for F in faces:
            if member[F] and not (F&flag) and F not in paired:
                H=F|flag
                if member[H] and H not in paired:
                    pairs[F]=H; paired.add(F);paired.add(H);upper.add(H)
    critical=sorted((F for F in faces if F not in paired and F),key=lambda x:(x.bit_count(),x))
    assert not (0 in critical) and len(pairs)*2+len(critical)==len(faces)
    fv=Counter(F.bit_count()-1 for F in critical)
    N,matchN,vec,diffs=EXPECTED[n]
    assert (len(faces),len(pairs),dict(fv))==(N,matchN,vec)
    # Every incident oriented face-poset edge is accounted for. Explicit DAG test.
    indeg=bytearray(1<<m)
    incidence=0
    for H in faces:
        mask=H
        while mask:
            b=mask&-mask;mask-=b
            L=H^b
            if pairs.get(L)==H: indeg[H]+=1
            else: indeg[L]+=1
            incidence+=1
    queue=deque(F for F in faces if indeg[F]==0)
    count=0
    while queue:
        F=queue.popleft();count+=1
        mask=F
        while mask:
            b=mask&-mask;mask-=b
            L=F^b
            if pairs.get(L)!=F:
                indeg[L]-=1
                if indeg[L]==0:queue.append(L)
        if F in pairs:
            H=pairs[F];indeg[H]-=1
            if indeg[H]==0:queue.append(H)
    assert count==len(faces),(n,count,len(faces))
    # Signed chain projection for the elementary gradient cancellations.
    @lru_cache(None)
    def P(L):
        if L in upper:return ()
        if L not in pairs:return ((L,1),)
        H=pairs[L]; toggled=H^L
        eps=1 if ((H&(toggled-1)).bit_count()%2==0) else -1
        out=defaultdict(int);mask=H;i=0
        while mask:
            b=mask&-mask;mask-=b
            other=H^b
            if other!=L:
                coef=(-eps) * (1 if i%2==0 else -1)
                for C,c in P(other):out[C]+=coef*c
            i+=1
        return tuple((C,c) for C,c in out.items() if c)
    for k,expected in diffs.items():
        hi=[F for F in critical if F.bit_count()-1==k]
        lo=[F for F in critical if F.bit_count()-1==k-1]
        mat=[]
        for H in hi:
            out=defaultdict(int);mask=H;i=0
            while mask:
                b=mask&-mask;mask-=b
                for C,c in P(H^b): out[C]+=(1 if i%2==0 else -1)*c
                i+=1
            assert not any(val for C,val in out.items() if C not in lo)
            mat.append([out[L] for L in lo])
        assert mat==expected,(n,k,mat,expected)
    # Verify unimodular pivot structure; Smith computations are exact and tiny.
    # A unit pivot suffices in the one-row/one-column cases, and the
    # two-column degree-seven matrix has an identity 2-by-2 minor.
    for k,mat in diffs.items():
        assert mat and mat[0]
        if n==5:
            assert mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0] == 1
        else:
            assert any(abs(v)==1 for row in mat for v in row)
    print('CERTIFIED',n,'faces',len(faces),'incidences',incidence,'matched_pairs',len(pairs),'critical',dict(fv),'DAG',count,'OK',flush=True)

if __name__=='__main__':
    import sys
    if len(sys.argv)>1: ns=[int(x) for x in sys.argv[1:]]
    else:ns=list(EXPECTED)
    for n in ns:certify(n)
    print('MOBIUS_LADDER_TWO_MATCHING_CERTIFIED')
