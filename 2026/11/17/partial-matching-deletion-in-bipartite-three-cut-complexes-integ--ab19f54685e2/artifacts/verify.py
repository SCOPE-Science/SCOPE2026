#!/usr/bin/env python3
"""Finite checks of partial-matching-deleted biclique three-cut duals.
Python 3 standard library only. Finite checks supplement the all-parameter proof.
"""
from itertools import combinations
from math import comb


def rank_binary(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length()-1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def betti(faces, n):
    layers = [sorted(f for f in faces if len(f)==k) for k in range(5)]
    ranks=[]
    for k in range(1,5):
        previous={f:i for i,f in enumerate(layers[k-1])}
        columns=[]
        for face in layers[k]:
            bits=0
            for sub in combinations(face,k-1):
                bits ^= (1<<previous[sub])
            columns.append(bits)
        ranks.append(rank_binary(columns))
    return tuple(len(layers[k])-ranks[k-1]-(ranks[k] if k<4 else 0) for k in range(1,5)), tuple(len(v) for v in layers), tuple(ranks)


def dual_from_graph(a,b,t):
    n=a+b
    edges={(i,a+j) for i in range(a) for j in range(b) if not (i==j and i<t)}
    disconnected=[]
    for tri in combinations(range(n),3):
        # The induced triple is connected iff its two-edge graph has a spanning tree.
        covered={i: set() for i in tri}
        for x,y in combinations(tri,2):
            if (min(x,y),max(x,y)) in edges:
                covered[x].add(y);covered[y].add(x)
        found={tri[0]};queue=[tri[0]]
        while queue:
            z=queue.pop()
            for w in covered[z]-found:
                found.add(w);queue.append(w)
        if len(found)!=3:
            disconnected.append(frozenset(tri))
    fs={()}
    for k in range(1,5):
        for face in combinations(range(n),k):
            s=set(face)
            if not any(D<=s for D in disconnected):
                fs.add(face)
    return fs, len(disconnected)


def model(a,b,t):
    fs={()}
    for k in range(1,5):
        for face in combinations(range(a+b),k):
            x=sum(i<a for i in face);y=k-x
            bad=sum(i in face and a+i in face for i in range(t))
            if x<=2 and y<=2 and (bad==0 or (k==2 and bad==1)):
                fs.add(face)
    return fs


def expected(a,b,t):
    if a==b==3 and t==3:
        return (0,4,0,0)
    if a==b==4 and t==4:
        return (0,4,1,0)
    B=comb(a-1,2)*comb(b-1,2)-t*(a-2)*(b-2)+comb(t,2)
    assert B>=0, (a,b,t,B)
    return (0,t,0,B)


def square_cycle_rank(u,v,d):
    es=[(i,j) for i in range(u) for j in range(v) if not (i==j and i<d)]
    idx={e:k for k,e in enumerate(es)}
    squares=[]
    for U in combinations(range(u),2):
        for V in combinations(range(v),2):
            box=[(i,j) for i in U for j in V]
            if all(e in idx for e in box):
                squares.append(sum(1<<idx[e] for e in box))
    parent=list(range(u+v))
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    for i,j in es:
        parent[root(i)]=root(u+j)
    components=len({root(i) for i in range(u+v)})
    return rank_binary(squares), len(es)-(u+v)+components,components


def main():
    total=0; largest=0
    for a in range(3,8):
        for b in range(a,8):
            for t in range(1,min(a,b)+1):
                direct, disc=dual_from_graph(a,b,t)
                assert direct==model(a,b,t),(a,b,t,'model')
                actual,counts,ranks=betti(direct,a+b)
                assert actual==expected(a,b,t),(a,b,t,actual,expected(a,b,t))
                square,cycle,components=square_cycle_rank(a-1,b-1,t-1)
                if (a,b,t)!=(4,4,4):
                    assert square==cycle,(a,b,t,square,cycle)
                else:
                    assert square==0 and cycle==1
                if (a,b,t)!=(3,3,3):
                    assert components==1,(a,b,t,components)
                else:
                    assert components==2
                largest=max(largest,len(direct));total+=1
    print('DUAL_PARTIAL_MATCHING_PASS', 'instances='+str(total),'max_faces='+str(largest))
    for a,b,t in [(3,3,1),(3,3,3),(4,4,4),(5,5,5),(5,6,3),(6,7,6),(7,7,7)]:
        fs,dis=dual_from_graph(a,b,t)
        hom,counts,ranks=betti(fs,a+b)
        print(f'a={a} b={b} t={t} faces={len(fs)} triple_nonfaces={dis} mod2_reduced_betti={hom} ranks={ranks}')

if __name__=='__main__':main()
