"""Standalone finite verification of maximal-intersecting-pair shattering."""
from itertools import combinations
from math import comb

def check(n):
    E=list(combinations(range(n),2))
    concepts=[]
    for a in range(n):
        concepts.append(frozenset(e for e in E if a in e))
    for T in combinations(range(n),3):
        concepts.append(frozenset(e for e in E if set(e)<=set(T)))
    assert len(concepts)==n+comb(n,3) and len(set(concepts))==len(concepts)
    got=[]
    for k in range(5):
        total=0
        for F in combinations(E,k):
            patterns={sum((1<<j) for j,e in enumerate(F) if e in h) for h in concepts}
            shattered=len(patterns)==2**k
            clique= k<=3 and all(set(a)&set(b) for a,b in combinations(F,2))
            assert shattered==clique,(n,F,shattered,clique)
            total+=shattered
        got.append(total)
    expected=[1,comb(n,2),n*comb(n-1,2),n*comb(n-1,3)+comb(n,3),0]
    assert got==expected,(n,got,expected)
    faces=[]
    for F in combinations(E,3):
        if all(set(a)&set(b) for a,b in combinations(F,2)):
            faces.append(F)
    return n,len(concepts),got,expected[-2],homology(n,E,faces)

def gf2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in pivots:x^=pivots[p]
            else:pivots[p]=x;break
    return len(pivots)

def homology(n,E,triangles):
    vertices={e:i for i,e in enumerate(E)}
    pairs=sorted({tuple(sorted((vertices[x],vertices[y]))) for F in triangles for x,y in combinations(F,2)})
    pair_index={p:i for i,p in enumerate(pairs)}
    bd1=[(1<<a)|(1<<b) for a,b in pairs]
    bd2=[]
    for F in triangles:
        V=[vertices[x] for x in F]
        bd2.append(sum(1<<pair_index[tuple(sorted((a,b)))] for a,b in combinations(V,2)))
    r1=gf2_rank(bd1);r2=gf2_rank(bd2)
    assert r1==len(E)-1 and r2==len(pairs)-r1
    return {'rank_d1':r1,'rank_d2':r2,'beta1':len(pairs)-r1-r2,'beta2':len(triangles)-r2}

if __name__=='__main__':
    for n in range(4,9):
        print(check(n))
    print('VERIFY_OK')
