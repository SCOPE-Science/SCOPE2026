#!/usr/bin/env python3
"""Finite exhaustive cross-check of counting-free fixed-variable formulas.
The algorithm refines all k-ary assignment types by the sets of replacement
colors in each coordinate (sets, not multisets: no counting quantifiers).
"""
from itertools import product
from collections import defaultdict

def digraph(sizes):
    assert len(sizes)>=3 and min(sizes)>=1
    layer=[i for i,n in enumerate(sizes) for _ in range(n)]
    edge=tuple(tuple(int((layer[b]-layer[a])%len(sizes)==1) for b in range(len(layer))) for a in range(len(layer)))
    return edge,layer

def necklace(w):
    w=tuple(w)
    return min(w[i:]+w[:i] for i in range(len(w)))

def predicted(a,b,k):
    return len(a)==len(b) and necklace(tuple(min(v,k) for v in a))==necklace(tuple(min(v,k) for v in b))

def game_equal(a,b,k):
    ea,_=digraph(a); eb,_=digraph(b)
    na,nb=len(ea),len(eb)
    tuples=[list(product(range(n),repeat=k)) for n in (na,nb)]
    edges=(ea,eb)
    # Initial atomic k-tuple types globally; comparisons include ordered edge directions.
    types=[]
    for ed,ts in zip(edges,tuples):
        types.append([tuple(int(t[i]==t[j]) if i==j else (int(t[i]==t[j]), ed[t[i]][t[j]], ed[t[j]][t[i]]) for i in range(k) for j in range(i,k)) for t in ts])
    alltypes=sorted(set(types[0]+types[1]))
    palette={v:i for i,v in enumerate(alltypes)}
    colors=[[palette[t] for t in sub] for sub in types]
    rounds=0
    while True:
        roundkeys=[]
        for n,ts,col in zip((na,nb),tuples,colors):
            loc={t:i for i,t in enumerate(ts)}
            arr=[]
            for t,oldc in zip(ts,col):
                neighborhoods=[]
                for p in range(k):
                    neighborhoods.append(tuple(sorted({col[loc[t[:p]+(v,)+t[p+1:]]] for v in range(n)})))
                arr.append((oldc,tuple(neighborhoods)))
            roundkeys.append(arr)
        newtypes=sorted(set(roundkeys[0]+roundkeys[1]))
        p2={v:i for i,v in enumerate(newtypes)}
        nxt=[[p2[x] for x in xlist] for xlist in roundkeys]
        rounds+=1
        if nxt==colors:
            break
        if rounds>100:
            raise AssertionError('refinement did not stabilize')
        colors=nxt
    return set(colors[0])==set(colors[1]),rounds

def main():
    # Nontrivial positive and negative cross-checks, plus rotations and
    # a threshold collision. Size bounded for direct exhaustive tuple refinement.
    triples=[(1,1,1),(1,1,2),(1,2,1),(2,1,1),(1,2,2),(2,1,2),(2,2,1),
             (1,1,3),(1,3,1),(3,1,1),(2,2,2),(1,2,3),(1,3,2),
             (2,1,3),(2,3,1),(3,1,2),(3,2,1),(2,2,3),(2,3,2),(3,2,2),
             (1,1,4),(1,4,1),(4,1,1),(1,2,4),(2,4,1)]
    different=[(1,1,1,1),(1,1,1,2),(1,1,2,1),(2,1,1,1),(1,2,1,1),
               (1,1,2,2),(2,2,1,1),(2,1,2,1),(1,2,1,2)]
    # Width two is exceptional: all sufficiently thick cyclic blow-ups
    # collapse into one theory, as do all cycles with at least four layers.
    def two_type(w):
        if len(w)>3:return 0
        return sum(v==1 for v in w)
    comparisons=[]
    low=triples+different+[(1,1,1,1,1),(1,1,1,1,2),(1,2,1,1,1)]
    low=[w for w in low if sum(w)<=8]
    for i,a in enumerate(low):
        for b in low[i:]:
            got,r=game_equal(a,b,2)
            target=two_type(a)==two_type(b)
            if got!=target:raise AssertionError(('low',a,b,got,target))
            comparisons.append((2,got))
    # Compare selected pairs, preserving different orientation necklaces.
    for k in (3,4):
        chosen=[t for t in triples+different if sum(t)<= (7 if k==3 else 6)]
        for i,a in enumerate(chosen):
            for b in chosen[i:]:
                if sum(a)+sum(b)> (12 if k==3 else 10): continue
                got,r=game_equal(a,b,k)
                target=predicted(a,b,k)
                if got!=target: raise AssertionError((k,a,b,got,target))
                comparisons.append((k,got))
    # Explicit 3-pebble invisibility for 3 versus 4 clone copies.
    got,_=game_equal((3,1,1),(4,1,1),3)
    assert got
    got,_=game_equal((3,1,1),(4,1,1),4)
    assert not got
    counts=defaultdict(int)
    for k,c in comparisons:counts[(k,c)]+=1
    for k in (2,3,4):
        print('k={} cases={} equivalent={} inequivalent={}'.format(k,sum(counts[(k,c)] for c in (False,True)),counts[(k,True)],counts[(k,False)]))
    print('threshold 3 vs 4: equivalent at width 3, distinguishable at width 4')
    print('all finite-variable comparison checks PASS')
if __name__=='__main__':main()
