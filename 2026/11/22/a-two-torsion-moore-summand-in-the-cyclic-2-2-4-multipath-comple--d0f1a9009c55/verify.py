"""Exact finite simplicial/discrete-Morse verification for a directed multipartite graph.

Uses only the Python 3 standard library, including exact rational arithmetic
and determinantal divisors to establish the integral Smith invariants.
"""
from itertools import combinations
from collections import Counter
from functools import lru_cache
import math
from fractions import Fraction
import random


def arcs(n):
    a=[f'a{i}' for i in range(2)]
    b=[f'b{i}' for i in range(2)]
    c=[f'c{i}' for i in range(n)]
    return sorted([(u,v) for u in a for v in b]
                  + [(u,v) for u in b for v in c]
                  + [(u,v) for u in c for v in a])


def is_face(edges, mask):
    chosen=[(u,v) for i,(u,v) in enumerate(edges) if mask>>i&1]
    if len({u for u,v in chosen})<len(chosen) or len({v for u,v in chosen})<len(chosen):
        return False
    nxt=dict(chosen)
    for x in nxt:
        cur=x
        for _ in range(len(chosen)):
            if cur not in nxt:break
            cur=nxt[cur]
            if cur==x:return False
    return True


def generate(edges):
    K={1:[1<<i for i in range(len(edges))]}
    for k in range(2,len(edges)+1):
        new=[]
        for face in K[k-1]:
            for j in range(face.bit_length(),len(edges)):
                sup=face|(1<<j)
                if is_face(edges,sup):new.append(sup)
        if not new:break
        K[k]=new
    return K


def matching(allfaces,order):
    unused=set(allfaces);pairs=[]
    for j in order:
        bit=1<<j
        for low in tuple(unused):
            if low&bit:continue
            high=low|bit
            if high in unused:
                unused.remove(low);unused.remove(high)
                pairs.append((low,high))
    return pairs,unused


def acyclic(faces,pairs):
    upward=dict(pairs);matched=set(pairs)
    adjacency={face:[] for face in faces}
    for high in faces:
        if high in upward:adjacency[high].append(upward[high])
        for j in range(high.bit_length()):
            if not (high>>j&1):continue
            low=high^(1<<j)
            if low and (low,high) not in matched:adjacency[high].append(low)
    done=set();processing=set()
    for face in faces:
        if face in done:continue
        processing.add(face)
        stack=[(face,iter(adjacency[face]))]
        while stack:
            u,it=stack[-1]
            try:v=next(it)
            except StopIteration:
                processing.remove(u);done.add(u);stack.pop();continue
            if v in processing:return False
            if v in done:continue
            processing.add(v);stack.append((v,iter(adjacency[v])))
    return True


def codim_one(face):
    while face:
        bit=face&-face;face-=bit
        yield (bit.bit_length()-1,bit)


def morse_boundary(critical,pairs):
    upward=dict(pairs);downward={h:l for l,h in pairs}
    @lru_cache(None)
    def projection(face):
        if face in critical:return {face:1}
        if face in downward:return {}
        upper=upward[face]
        pivot_sign=(-1)**sum((upper&((1<<j)-1)).bit_count() for j,bit in codim_one(upper) if (upper^bit)==face)
        assert pivot_sign in (-1,1)
        out=Counter()
        for j,bit in codim_one(upper):
            sub=upper^bit
            if sub==face:continue
            sign=(-1)**((upper&(bit-1)).bit_count())
            for target,val in projection(sub).items():out[target]-=sign*pivot_sign*val
        return {x:y for x,y in out.items() if y}
    out={}
    for face in critical:
        if face.bit_count()==1:continue
        accum=Counter()
        for j,bit in codim_one(face):
            sign=(-1)**((face&(bit-1)).bit_count())
            for target,val in projection(face^bit).items():accum[target]+=sign*val
        out[face]={t:x for t,x in accum.items() if x}
    return out


def mod_rank(columns,rows,p):
    pivots={};rank=0
    for col in columns:
        vector={r:(v%p) for r,v in col.items() if v%p}
        while vector:
            i=max(vector)
            if i in pivots:
                prev=pivots[i];a=vector[i]
                for j,v in prev.items():
                    x=(vector.get(j,0)-a*v)%p
                    if x:vector[j]=x
                    else:vector.pop(j,None)
            else:
                inv=pow(vector[i],-1,p)
                pivots[i]={j:v*inv%p for j,v in vector.items()}
                rank+=1
                break
    return rank


def verify(n,order=None):
    E=arcs(n);K=generate(E);faces=set().union(*[set(v) for v in K.values()]);assert len(faces)==sum(map(len,K.values()))
    if order is None:order=list(range(len(E)))
    pairs,crit=matching(faces,order)
    assert len(set().union(*(set(x) for x in pairs)))==2*len(pairs)
    assert 2*len(pairs)+len(crit)==len(faces)
    assert acyclic(faces,pairs)
    delta=morse_boundary(crit,pairs)
    c3=sorted(f for f in crit if f.bit_count()==4)
    c4=sorted(f for f in crit if f.bit_count()==5)
    cols=[{c3.index(x):v for x,v in delta[y].items()} for y in c4]
    assert not any(d for f,d in delta.items() if f not in c4)
    assert all(x in c3 for d in delta.values() for x in d)
    M=[[col.get(i,0) for col in cols] for i in range(len(c3))]
    def exact_rank(mat):
        A=[[Fraction(x) for x in row] for row in mat]
        m=len(A);n=len(A[0]) if m else 0
        pivot_row=0
        for j in range(n):
            candidate=next((i for i in range(pivot_row,m) if A[i][j]),None)
            if candidate is None:continue
            A[pivot_row],A[candidate]=A[candidate],A[pivot_row]
            t=A[pivot_row][j]
            for k in range(j,n):A[pivot_row][k]/=t
            for i in range(pivot_row+1,m):
                t=A[i][j]
                if t:
                    for k in range(j,n):A[i][k]-=t*A[pivot_row][k]
            pivot_row+=1
            if pivot_row==m:break
        return pivot_row
    rank=exact_rank(M)
    invariants=None
    if rank==2:
        d1=math.gcd(*[v for row in M for v in row])
        d2=0
        for i,j in combinations(range(len(c3)),2):
            for k,l in combinations(range(len(c4)),2):
                d2=math.gcd(d2,M[i][k]*M[j][l]-M[i][l]*M[j][k])
        invariants=[d1,d2//d1]
    for p in [2,3,5,7]:
        pr=mod_rank(cols,len(c3),p)
        if invariants is not None:assert pr==sum(s%p!=0 for s in invariants),(p,invariants)
    return E,K,faces,pairs,crit,M,invariants,rank

if __name__=='__main__':
    ORDER=[17,13,6,2,4,3,15,11,1,0,8,14,10,7,19,9,12,18,16,5]
    E,K,faces,pairs,crit,M,diag,rank=verify(4,ORDER)
    print('vertices',len(E),'face_counts',[(k,len(v)) for k,v in sorted(K.items())]);print('pairs',len(pairs),'critical',dict(Counter(f.bit_count()-1 for f in crit)))
    print('morse_matrix',M);print('smith',diag);assert rank==2
    assert [len(K[k]) for k in range(1,7)]==[20,154,560,976,720,144]
    assert len(pairs)==1269 and Counter(f.bit_count()-1 for f in crit)=={0:1,3:5,4:30}
    assert diag==[1,2]
    print('independent_prime_checks',[(p,sum(x%p!=0 for x in diag)) for p in (2,3,5,7)])
    assert len(K[6])==144
    # A separate full simplicial-chain calculation, without the Morse matching.
    for prime, expected in [(2,{3:4,4:29}),(3,{3:3,4:28}),(5,{3:3,4:28})]:
        fullranks={}
        for k in range(2,7):
            lower={face:i for i,face in enumerate(K[k-1])}
            columns=[]
            for face in K[k]:
                columns.append({lower[face^bit]:(-1)**((face&(bit-1)).bit_count())
                                for j,bit in codim_one(face)})
            fullranks[k]=mod_rank(columns,len(K[k-1]),prime)
        full_betti={k-1:len(K[k])-fullranks.get(k,0)-fullranks.get(k+1,0)-(k==1) for k in K}
        assert {i:b for i,b in full_betti.items() if b}==expected,(prime,full_betti)
        print('full_simplicial_F',prime,'boundary_ranks',fullranks,'betti',expected)
    # Separate deterministic matching orders reproduce the same torsion invariant.
    for seed in range(3):
        another=list(range(20));random.Random(seed).shuffle(another)
        _,_,_,_,crit2,M2,_,r=verify(4,another)
        cols2=[{i:M2[i][j] for i in range(len(M2)) if M2[i][j]} for j in range(len(M2[0]))]
        assert mod_rank(cols2,len(M2),2)==r-1
        assert mod_rank(cols2,len(M2),3)==r
        print('alternate_order',seed,'critical_count',len(crit2),'rational_rank',r,'mod_two_rank',r-1)
    print('VERIFIED: exact integral Morse normal form, full-chain field checks, three independent matchings')
