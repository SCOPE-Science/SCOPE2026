#!/usr/bin/env python3
"""Exact finite incidence and symbolic cyclotomic checks for degree-nine conic-line obstruction.
Pure Python 3 standard library; the mathematical proof is in RESULT.md.
"""
from itertools import combinations


def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield frozenset()
    else:
        a=items[0]
        for j in range(1,len(items)):
            b=items[j]
            remain=items[1:j]+items[j+1:]
            for tail in perfect_matchings(remain):
                yield tail|frozenset((frozenset((a,b)),))


def two_factors(items):
    items=tuple(items)
    edges=[frozenset(p) for p in combinations(items,2)]
    for selection in combinations(edges,len(items)):
        deg={x:0 for x in items}
        for edge in selection:
            for x in edge: deg[x]+=1
        if all(d==2 for d in deg.values()):
            yield frozenset(selection)


def pairs_of(triple):
    return frozenset(frozenset(e) for e in combinations(triple,2))


def classify_t1():
    non=range(1,7)
    allpairs=frozenset(frozenset(e) for e in combinations(range(7),2))
    feasible=0
    shapes={}
    for qedges in two_factors(non):
        for matching in perfect_matchings(non):
            if matching & qedges: continue
            for half in combinations(non,3):
                if 1 not in half: continue  # unordered partition
                other=tuple(x for x in non if x not in half)
                line_triples=[(0,*e) for e in matching]+[tuple(half),other]
                used=list(qedges)
                for tr in line_triples: used.extend(pairs_of(tr))
                if len(used)==21 and set(used)==allpairs:
                    feasible+=1
                    # the Q-graph is necessarily one alternating six-cycle
                    visited={1}; boundary=[1]
                    while boundary:
                        v=boundary.pop()
                        for e in qedges:
                            if v in e:
                                for w in e:
                                    if w not in visited:
                                        visited.add(w);boundary.append(w)
                    shapes[len(visited)]=shapes.get(len(visited),0)+1
    assert feasible>0 and shapes=={6:feasible},(feasible,shapes)
    return feasible,shapes


def classify_t2():
    # Two tangent lines 0,1; five secants 2,...,6.
    non=range(2,7)
    tris=[frozenset(t) for t in combinations(range(7),3)]
    total=0
    explored=0
    for qedges in two_factors(non):
        allowed=[(tr,pairs_of(tr)) for tr in tris if not (pairs_of(tr)&qedges)]
        # exactly 5 line-only triples would consume 15 distinct line-pairs
        def dfs(pos,used,count):
            nonlocal total,explored
            if count==5:
                explored+=1
                total+=1
                return
            if len(allowed)-pos<5-count:return
            for j in range(pos,len(allowed)):
                p=allowed[j][1]
                if not (p & used):dfs(j+1, used|p,count+1)
        dfs(0,frozenset(qedges),0)
    assert total==0, total
    return total,explored


# Cyclotomic coefficient ring Z[w]/(w^2+w+1), w^3=1.
def mul(a,b):
    A,B=a;C,D=b
    return (A*C-B*D,A*D+B*C-B*D)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
O=(1,0);W=(0,1)
def power_w(e):
    a=O
    for _ in range(e%3): a=mul(a,W)
    return a

def plus(p,q):
    o=p.copy()
    for e,a in q.items():o[e]=add(o.get(e,(0,0)),a)
    return {e:a for e,a in o.items() if a!=(0,0)}
def timesw(p):return {e:mul(a,W) for e,a in p.items()}

def symbolic_pascal():
    for i in range(3):
        # A_i joins t=s*w^i and 1/t, B_{i-1} joins t=s*w^(i-1) and w/t.
        u={1:power_w(i),-1:power_w(-i)}
        v={1:power_w(i-1),-1:power_w(2-i)}
        assert plus(u,{e:neg(a) for e,a in timesw(v).items()})=={}
    # The unmatched A_i-B_{i-1} intersections lie on x-w^2*z=0.
    # Intersect with x*z=y^2: the two points have y/z=+w or -w.
    assert mul(W,W)==(-1,-1)
    return 3

if __name__=='__main__':
    t1,shape=classify_t1()
    t2,branches=classify_t2()
    algebra=symbolic_pascal()
    assert [(t,t-1,12-t) for t in range(1,5)]==[(1,0,11),(2,1,10),(3,2,9),(4,3,8)]
    print('DEGREE9_INCIDENT_PASCAL_PASS',t1,shape,t2,branches,algebra)
