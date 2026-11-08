#!/usr/bin/env python3
"""Reproduce exact computations for four-row (1,1,1,2) multiple chessboard complexes.
Requires Python 3.10+ standard library only. This is exhaustive finite computation,
not a substitute for the published infinite-range shellability theorem.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial

CAP=(1,1,1,2)
ORDERS={
2:[2,4,1,0,5,7,6,3],
3:[8,11,6,5,0,4,7,1,3,2,10,9],
4:[8,13,15,3,4,14,1,5,6,7,2,0,9,10,12,11],
5:[3,8,19,17,1,12,10,9,13,16,2,14,18,6,5,4,7,15,0,11],
6:[15,19,22,6,18,9,11,3,5,2,7,14,16,4,13,12,1,8,10,21,23,20,0,17],
7:[22,27,26,23,17,0,24,16,5,11,1,19,15,3,9,18,13,2,25,7,21,4,12,6,14,20,10,8],
}
EXPECTED={1:{0:3},2:{1:6},3:{2:5},4:{2:9},5:{3:21},6:{3:53,4:1},7:{3:21,4:90}}
CRITICAL={2:{0:1,1:6},3:{0:1,2:5},4:{0:1,2:9},5:{0:1,3:21},6:{0:1,3:53,4:1},7:{0:1,3:23,4:92}}

def census_by_columns(m):
    # A column is either unoccupied (0) or occupied by one of four rows.
    S=set()
    for choices in product(range(5),repeat=m):
        if any(choices.count(r)>CAP[r-1] for r in range(1,5)):continue
        f=sum(1<<((r-1)*m+j) for j,r in enumerate(choices) if r)
        if f:S.add(f)
    return S

def census_by_rows(m):
    # Independent construction: choose disjoint column sets for each row.
    S=set()
    for a in [()] + [(x,) for x in range(m)]:
        A=set(a)
        for b in [()] + [(x,) for x in range(m) if x not in A]:
            B=A|set(b)
            for c in [()] + [(x,) for x in range(m) if x not in B]:
                C=B|set(c);free=sorted(set(range(m))-C)
                for dsize in range(min(2,len(free))+1):
                    for d in combinations(free,dsize):
                        mask=0
                        for r,cols in enumerate([a,b,c,d]):
                            for j in cols:mask|=1<<(r*m+j)
                        if mask:S.add(mask)
    return S

def boundary(f):
    bits=[];u=f
    while u:
        b=u&-u;u-=b;bits.append(b)
    return [(f-b,1 if i%2==0 else -1) for i,b in enumerate(bits)]

def matching(S,m):
    active=set(S);pairs=[]
    assert sorted(ORDERS[m])==list(range(4*m))
    for v in ORDERS[m]:
        bit=1<<v
        for f in sorted(S,key=lambda x:(x.bit_count(),x)):
            if f in active and not (f&bit) and (f|bit) in active:
                active.remove(f);active.remove(f|bit)
                pairs.append((f,f|bit))
    return pairs,active

def check_acyclic(S,pairs):
    matched=set(pairs);indeg={f:0 for f in S};edges=defaultdict(list);inc=0
    for upper in S:
        for lower,_ in boundary(upper):
            if lower not in S:continue
            a,b=(lower,upper) if (lower,upper) in matched else (upper,lower)
            edges[a].append(b);indeg[b]+=1;inc+=1
    q=deque(f for f in S if indeg[f]==0);seen=0
    while q:
        u=q.popleft();seen+=1
        for v in edges[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert seen==len(S),(seen,len(S))
    assert len(pairs)*2+len(S)-2*len(pairs)==len(S)
    return inc

def mod2_betti(S):
    F=defaultdict(list)
    for f in S:F[f.bit_count()-1].append(f)
    rank={}
    for d in range(max(F),0,-1):
        index={f:i for i,f in enumerate(sorted(F[d-1]))}
        piv={}
        for f in F[d]:
            col=0
            for g,_ in boundary(f):col ^= 1<<index[g]
            while col:
                p=col.bit_length()-1
                if p in piv:col ^= piv[p]
                else:piv[p]=col;break
        rank[d]=len(piv)
    return {d:len(F[d])-rank.get(d,0)-rank.get(d+1,0)-(d==0) for d in sorted(F)}

def morse_boundary(S,pairs,critical):
    low_to_hi=dict(pairs);high_to_lo={b:a for a,b in pairs}
    crit3=sorted(f for f in critical if f.bit_count()==4)
    crit4=sorted(f for f in critical if f.bit_count()==5)
    index={f:i for i,f in enumerate(crit3)}
    @lru_cache(None)
    def projection(f):
        if f in index:return {index[f]:1}
        if f in high_to_lo:return {}
        u=low_to_hi[f]
        incidence=dict(boundary(u));pivot=incidence[f]
        out=Counter()
        for g,sgn in incidence.items():
            if g==f:continue
            for i,c in projection(g).items():out[i]-=sgn*pivot*c
        return {i:c for i,c in out.items() if c}
    D=[]
    for u in crit4:
        out=Counter()
        for g,sgn in boundary(u):
            for i,c in projection(g).items():out[i]+=sgn*c
        D.append([out[i] for i in range(len(crit3))])
    return list(map(list,zip(*D)))

def check_m6_m7(D,m):
    assert m in (6,7)
    if m==6:
        assert len(D)==53 and len(D[0])==1
        assert all(v==0 for row in D for v in row)
        return 'zero integer Morse boundary'
    assert len(D)==23 and len(D[0])==92
    # Exact integral rank 2 and a unimodular 2x2 minor, without numerical algebra.
    a,b=11,33;i,j=1,3
    A,B=D[i][a],D[i][b];C,E=D[j][a],D[j][b]
    determinant=A*E-B*C
    assert determinant==-1,(A,B,C,E,determinant)
    for col in range(92):
        z,w=D[i][col],D[j][col]
        x=(E*z-B*w)//determinant
        y=(-C*z+A*w)//determinant
        assert all(D[row][col]==x*D[row][a]+y*D[row][b] for row in range(23)),col
    return 'rank 2, with unit minor rows (1,3), columns (11,33)'

def count_faces_formula(m,k):
    total=0
    for s in range(max(0,k-2),min(3,k)+1):
        if s>m or k-s>m-s:continue
        falling=factorial(m)//factorial(m-s)
        total+=comb(3,s)*falling*comb(m-s,k-s)
    return total

def beta4(m):
    v=sum((-1)**(k-1)*count_faces_formula(m,k) for k in range(1,6))-1
    poly=(m**5-15*m**4+76*m**3-151*m**2+97*m-2)//2
    assert v==poly
    return v

def main():
    for m in range(1,8):
        S=census_by_columns(m)
        assert S==census_by_rows(m)
        histogram=dict(sorted(Counter(f.bit_count()-1 for f in S).items()))
        beta={d:k for d,k in mod2_betti(S).items() if k}
        assert beta==EXPECTED[m],(m,beta)
        if m==1:
            print(f'm={m} faces={len(S)} f={histogram} betti={beta} four isolated vertices')
            continue
        pairs,critical=matching(S,m)
        assert len(pairs)*2+len(critical)==len(S)
        hist=dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
        assert hist==CRITICAL[m],(m,hist)
        incidences=check_acyclic(S,pairs)
        if m in (6,7):
            D=morse_boundary(S,pairs,critical)
            q=check_m6_m7(D,m)
        else:q='single positive critical dimension; all attaching maps trivial'
        print(f'm={m} faces={len(S)} f={histogram} pairs={len(pairs)} incidences={incidences} critical={hist} mod2_betti={beta} integral={q}',flush=True)
    assert beta4(8)==675
    for m in range(8,13):
        assert beta4(m)>=0
        print(f'm={m} Euler_top_rank={beta4(m)} shellability_applies_for_m>=8')
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
