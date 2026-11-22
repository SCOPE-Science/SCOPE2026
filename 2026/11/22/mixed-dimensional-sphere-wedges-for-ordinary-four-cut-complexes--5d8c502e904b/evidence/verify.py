#!/usr/bin/env python3
"""Exact finite witnesses for the ordinary four-cut dual of three-row rook graphs.
Does not rely on any external libraries. Infinite-parameter assertion uses the
separate combinatorial induction in RESULT.md, not finite enumeration.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from math import comb


def downsets(n):
    """The proposed maximal rectangle cover, plus isolated transversal triangles."""
    def submasks(s):
        t=s
        while True:
            yield t
            if t==0: break
            t=(t-1)&s
    rects=[]
    for r in range(3):
        rects.append(sum(1<<(r*n+c) for c in range(n)))
    for rows in combinations(range(3),2):
        for cols in combinations(range(n),3):
            rects.append(sum(1<<(r*n+c) for r in rows for c in cols))
    for cols in combinations(range(n),2):
        rects.append(sum(1<<(r*n+c) for r in range(3) for c in cols))
    Y={x for rect in rects for x in submasks(rect)}
    matching={sum(1<<(r*n+c) for r,c in enumerate(cs))
              for cols in combinations(range(n),3) for cs in permutations(cols)}
    assert Y.isdisjoint(matching)
    return Y, matching, Y|matching


def independent_faces(n):
    """Brute all-subsets construction, relying only on the defining 4-cut test."""
    N=3*n
    good=bytearray(1<<N)
    good[0]=1
    for s in range(1,1<<N):
        k=s.bit_count()
        if k<4:
            good[s]=1
        elif k==4:
            vs=[v for v in range(N) if s>>v&1]
            visited={vs[0]}; q=[vs[0]]
            while q:
                x=q.pop()
                for y in vs:
                    if y not in visited and (x//n==y//n or x%n==y%n):
                        visited.add(y);q.append(y)
            good[s]=(len(visited)==4)
        else:
            b=s;ok=True
            while b:
                bit=b&-b
                if not good[s^bit]:ok=False;break
                b-=bit
            good[s]=ok
    return {s for s in range(1<<N) if good[s]}


def specified_critical(n):
    C=set()
    # Three-row critical triangles, including some with repeated columns.
    for b in range(n):
        for c in range(n):
            if b==c: continue
            for a in range(1,n):
                if a!=max(b,c):
                    C.add((1<<a)|(1<<(n+b))|(1<<(2*n+c)))
    # Four cells from row one or row two, including the first column.
    for r in (1,2):
        for cs in combinations(range(1,n),3):
            C.add((1<<(r*n)) | sum(1<<(r*n+c) for c in cs))
    # Three cells from row two and one from row one at their least column.
    for a,b,c in combinations(range(n),3):
        C.add((1<<(n+a)) | sum(1<<(2*n+t) for t in (a,b,c)))
    return C


def lex_matching(faces,n):
    unmatched=set(faces); pairs=[]
    for v in range(3*n):
        bit=1<<v
        new_pairs=[]
        for s in unmatched:
            if not s&bit and (s|bit) in unmatched:
                new_pairs.append((s,s|bit))
        for s,t in new_pairs:
            unmatched.remove(s);unmatched.remove(t)
        pairs.extend(new_pairs)
    return unmatched,pairs


def dag_check(faces,pairs):
    """Every codimension-one incidence, reversed exactly on matched pairs."""
    ix={s:i for i,s in enumerate(x for x in faces if x!=0)}
    edges=[[] for _ in ix]; deg=[0]*len(ix)
    matched={(a,b) for a,b in pairs if a!=0}
    count=0
    for b in ix:
        subset=b
        while subset:
            bit=subset & -subset; subset-=bit
            a=b^bit
            if not a: continue
            source,target = (a,b) if (a,b) in matched else (b,a)
            edges[ix[source]].append(ix[target]);deg[ix[target]]+=1
            count+=1
    q=deque(i for i,d in enumerate(deg) if d==0);top=0
    while q:
        i=q.popleft();top+=1
        for j in edges[i]:
            deg[j]-=1
            if deg[j]==0:q.append(j)
    assert top==len(ix),f'Directed cycle: visited {top} of {len(ix)}'
    return count


def rank_mod_two(columns):
    basis={}
    for x in columns:
        while x:
            pivot=x.bit_length()-1
            if pivot not in basis:basis[pivot]=x;break
            x^=basis[pivot]
    return len(basis)


def homology_mod_two(faces):
    levels={k:[] for k in range(1,max(s.bit_count() for s in faces)+1)}
    for s in faces:
        if s:levels[s.bit_count()].append(s)
    ranks={1:0}
    for k in range(2,len(levels)+1):
        idx={s:i for i,s in enumerate(levels[k-1])}
        cols=[]
        for s in levels[k]:
            col=0;b=s
            while b:
                bit=b&-b;b-=bit
                col^=1<<idx[s^bit]
            cols.append(col)
        ranks[k]=rank_mod_two(cols)
    return {k-1:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==1 else 0)
            for k in levels}


def main():
    for n in range(3,9):
        Y, M, F=downsets(n)
        if n<=6:
            direct=independent_faces(n)
            assert F==direct,(n,len(F),len(direct),len(F^direct))
        crit,pairs=lex_matching(F,n)
        predicted=specified_critical(n)
        assert crit==predicted,(n,len(crit),len(predicted),len(crit^predicted))
        Ycrit,Ypairs=lex_matching(Y,n)
        assert Ycrit == {s for s in predicted if s.bit_count()==4}, (n,len(Ycrit))
        assert len(pairs)*2+len(crit)==len(F)
        assert len(Ypairs)*2+len(Ycrit)==len(Y)
        if n<=7:
            incidences=dag_check(F,pairs)
            dag_check(Y,Ypairs)
        else:incidences='not_checked'
        h={2: n*(n-1)*(n-2),3:(n-1)*(n-2)**2//2}
        assert Counter(x.bit_count()-1 for x in crit)==Counter({2:h[2],3:h[3]})
        if n<=6:
            hb=homology_mod_two(F)
            assert all(hb.get(k,0)==h.get(k,0) for k in hb),(n,hb)
        print(f'n={n} faces={len(F)} matching_triangles={len(M)} '
              f'critical2={h[2]} critical3={h[3]} pairs={len(pairs)} '
              f'hasse={incidences} checks=PASS')
    print('ALL_FINITE_CHECKS_PASS; infinite n uses the induction of RESULT.md')

if __name__=='__main__':main()
