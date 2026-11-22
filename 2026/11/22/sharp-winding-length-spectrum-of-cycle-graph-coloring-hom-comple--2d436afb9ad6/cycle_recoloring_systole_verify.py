#!/usr/bin/env python3
"""Finite, self-contained checks for the stated cycle-recoloring systole theorem.
This verifier is supplementary to the all-parameter mathematical proof.
"""
from collections import deque
from itertools import combinations
from math import gcd


def image_colors(m,n,r,first=0):
    """Each state is (initial target color, positions with negative edges)."""
    if not 0 < r < m or (m-2*r)%n:
        raise ValueError('Invalid nonextreme winding sector')
    states={}
    for ss in combinations(range(m),r):
        sign=[-1 if i in ss else 1 for i in range(m)]
        for a in range(n):
            vals=[a]
            for j in range(m-1):
                vals.append((vals[-1]+sign[j])%n)
            assert (vals[-1]+sign[-1])%n==a
            states[(a,ss)]=tuple(vals)
    return states


def steps(m,n,r,state):
    a,ss=state
    S=set(ss)
    for i in list(S):
        for d in (-1,1):
            j=(i+d)%m
            if j in S:
                continue
            T=tuple(sorted((S-{i})|{j}))
            # A token crossing the source-index cut changes initial color by +/- 2.
            newa=(a+2*d)%n if {i,j}=={0,m-1} else a
            # A move 0 -> m-1 is NEGATIVE while m-1 -> 0 is POSITIVE.
            if i==0 and j==m-1: newa=(a-2)%n
            if i==m-1 and j==0: newa=(a+2)%n
            yield ((newa,T),d)


def direct_coloring_moves(m,n,r):
    states=image_colors(m,n,r)
    inverse={f:v for v,f in states.items()}
    assert len(inverse)==len(states)
    for v,f in states.items():
        predicted=set()
        for u,d in steps(m,n,r,v):
            assert u in states
            g=states[u]
            changes=sum(x!=y for x,y in zip(f,g))
            assert changes==1, (m,n,r,v,u,f,g)
            assert all((g[(i+1)%m]-g[i])%n in (1,n-1) for i in range(m))
            predicted.add(u)
        # Exhaust the TRUE direct single-coordinate recolorings, including
        # alternatives not supplied by the particle-move generator.
        actual=set()
        for i in range(m):
            for c in range(n):
                if c==f[i]:continue
                if all((c-f[j])%n in (1,n-1) for j in ((i-1)%m,(i+1)%m)):
                    g=list(f);g[i]=c
                    assert tuple(g) in inverse
                    actual.add(inverse[tuple(g)])
        assert predicted==actual,(m,n,r,v,predicted,actual)
    return len(states)


def base_monotone_cycle(m,r):
    """An m-move oriented loop in exclusion configuration space."""
    S=set(range(r));start=frozenset(S)
    path=[tuple(sorted(S))]
    def move(i):
        assert i in S and (i+1)%m not in S
        S.remove(i);S.add((i+1)%m)
        path.append(tuple(sorted(S)))
    for i in range(r-1,-1,-1):move(i)
    for i in range(r,m-1):move(i)
    move(m-1)
    assert frozenset(S)==start and len(path)==m+1
    return path


def lift_path(m,n,r):
    a=0;cur=(a,tuple(range(r))); original=cur
    N=n//gcd(n,2)
    base=base_monotone_cycle(m,r)
    out=[cur]
    for _ in range(N):
        for wanted in base[1:]:
            opts=[v for v,d in steps(m,n,r,cur) if v[1]==wanted and d==1]
            assert len(opts)==1,(m,n,r,cur,wanted,opts)
            cur=opts[0];out.append(cur)
    assert cur==original and len(out)-1==m*N
    return out


def minimal_nontrivial_loop_length(m,n,r):
    """BFS in a finite lift with signed total displacement; origin fixed.
    Only explores signed displacement up to the predicted sharp bound.
    Note: NONZERO displacement after a closed Hom edge path is essential.
    """
    target=m*n//gcd(n,2)
    start=(0,tuple(range(r)))
    # signed edge count between -target and target
    dct={(start,0):0}; todo=deque([(start,0)]); found=None
    while todo:
        v,delta=todo.popleft()
        dist=dct[(v,delta)]
        if dist>=target:continue
        for u,step in steps(m,n,r,v):
            nd=delta+step
            if nd<-target or nd>target:continue
            if u==start and nd!=0:
                found=dist+1
                return found,len(dct)
            node=(u,nd)
            if node not in dct:
                dct[node]=dist+1;todo.append(node)
    return found,len(dct)


def main():
    examples=[(4,5,2),(6,5,3),(7,5,1),(8,6,1),(8,6,4),
              (9,5,2),(10,6,2)]
    for m,n,r in examples:
        if (m-2*r)%n:continue
        N=n//gcd(n,2)
        total=direct_coloring_moves(m,n,r)
        witness=lift_path(m,n,r)
        # Use minimal BFS only for manageable instances
        extra=''
        if m<=9:
            length,states=minimal_nontrivial_loop_length(m,n,r)
            assert length==m*N,(m,n,r,length,m*N)
            extra=f', exhaustive signed-voltage BFS: length={length}, states={states}'
        print(f'(m,n,r)=({m},{n},{r}): coloring vertices={total}, shortest witness={len(witness)-1}{extra}')
    print('CYCLE_RECOLORING_SYSTOLE_CHECKS_OK')

if __name__=='__main__':main()
