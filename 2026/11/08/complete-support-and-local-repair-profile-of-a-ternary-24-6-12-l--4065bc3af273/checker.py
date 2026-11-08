"""Exact finite certificates for the support and locality profile of a ternary linear code.

Run with Python 3, no third-party dependencies.
"""
from collections import Counter
from itertools import combinations, product

ROWS = (
    '100002211002021122200001',
    '010201002021102121022221',
    '001200122202102020111020',
    '000011112222111100000111',
    '000102011100210200110102',
    '000000121101110122021102',
)
EXPECTED_WEIGHTS = {0:1,12:32,13:70,14:108,15:100,16:126,17:96,18:84,
                    19:54,20:48,21:8,22:2}
EXPECTED_SUPPORT = {
  1:{12:16,13:35,14:54,15:50,16:63,17:48,18:42,19:27,20:24,21:4,22:1},
  2:{16:1,17:41,18:307,19:955,20:1721,21:2598,22:2716,23:2018,24:654},
  3:{19:3,20:150,21:1511,22:5577,23:12738,24:13901},
  4:{21:3,22:267,23:2361,24:8380},
  5:{23:24,24:340},
  6:{24:1},
}
EXPECTED_TRIPLES = ((1,15,23),(2,5,11),(8,12,24))
EXPECTED_MIN2_BASIS = ((0,0,1,1,0,2),(0,0,0,0,1,2))
EXPECTED_MIN2_ZEROS = (1,2,9,10,14,15,22,23)

def rank_mod3(rows, width):
    a=[list(row) for row in rows]
    h=0
    for j in range(width):
        pivot=next((i for i in range(h,len(a)) if a[i][j]%3),None)
        if pivot is None: continue
        a[h],a[pivot]=a[pivot],a[h]
        inv=1 if a[h][j]%3==1 else 2
        a[h]=[(inv*z)%3 for z in a[h]]
        for i in range(len(a)):
            if i!=h:
                coeff=a[i][j]%3
                if coeff:
                    a[i]=[(u-coeff*v)%3 for u,v in zip(a[i],a[h])]
        h+=1
        if h==len(a): break
    return h

def rref_subspaces(k,r):
    """One reduced row-echelon basis for each dimension-r subspace of F_3^k."""
    for pivots in combinations(range(k),r):
        free=[(i,j) for i in range(r) for j in range(pivots[i]+1,k)
              if j not in pivots]
        for values in product(range(3),repeat=len(free)):
            rows=[[0]*k for _ in range(r)]
            for i,j in enumerate(pivots): rows[i][j]=1
            for (i,j),value in zip(free,values): rows[i][j]=value
            yield tuple(tuple(row) for row in rows)

def support_and_zeros(basis,cols):
    zeros=[]
    for j,col in enumerate(cols,1):
        if all(sum(a*b for a,b in zip(row,col))%3==0 for row in basis):
            zeros.append(j)
    return len(cols)-len(zeros), tuple(zeros)

def main():
    assert len(ROWS)==6 and all(len(row)==24 for row in ROWS)
    g=[tuple(map(int,row)) for row in ROWS]
    k=len(g); n=len(g[0]); cols=list(zip(*g))
    assert rank_mod3(g,n)==6
    gram=[[sum(g[i][j]*g[h][j] for j in range(n))%3 for h in range(k)] for i in range(k)]
    assert rank_mod3(gram,k)==k

    weights=Counter()
    for x in product(range(3),repeat=k):
        word=[sum(x[i]*g[i][j] for i in range(k))%3 for j in range(n)]
        weights[sum(z!=0 for z in word)]+=1
    assert dict(weights)==EXPECTED_WEIGHTS and sum(weights.values())==3**k

    all_support={}; min2=[]
    counts={1:364,2:11011,3:33880,4:11011,5:364,6:1}
    for r in range(1,k+1):
        dist=Counter()
        for basis in rref_subspaces(k,r):
            size, zeros=support_and_zeros(basis,cols)
            dist[size]+=1
            if r==2 and size==16: min2.append((basis,zeros))
        assert dict(dist)==EXPECTED_SUPPORT[r]
        assert sum(dist.values())==counts[r]
        all_support[r]=dict(dist)
    assert min2==[(EXPECTED_MIN2_BASIS,EXPECTED_MIN2_ZEROS)]
    assert {w:2*c for w,c in all_support[1].items()} == {w:c for w,c in weights.items() if w!=0}

    # A coordinate is locally recoverable from r others precisely when the
    # corresponding generator column is a linear combination of those r columns.
    # No zero/proportional columns, and the minimal rank-deficient triples / quadruples
    # therefore coincide with all size-three / size-four circuits.
    assert all(any(col) for col in cols)
    assert all(rank_mod3([cols[i],cols[j]],k)==2 for i,j in combinations(range(n),2))
    triples=tuple(tuple(j+1 for j in ids)
                  for ids in combinations(range(n),3)
                  if rank_mod3([cols[j] for j in ids],k)==2)
    assert triples==EXPECTED_TRIPLES
    quads=tuple(tuple(j+1 for j in ids)
                for ids in combinations(range(n),4)
                if rank_mod3([cols[j] for j in ids],k)==3 and
                all(rank_mod3([cols[j] for j in sub],k)==3
                    for sub in combinations(ids,3)))
    assert len(quads)==102
    local2={j for triple in triples for j in triple}
    local3={j for quad in quads for j in quad}-local2
    assert local2=={1,2,5,8,11,12,15,23,24}
    assert local3==set(range(1,n+1))-local2
    print('PASS: [24,6,12]_3 LCD rank, Gram rank, all 729 weights')
    print('PASS: all 56,631 nonzero subspaces, exact higher-support histograms')
    print('PASS: unique minimum 2D subcode; weight hierarchy (12,16,19,21,23,24)')
    print('PASS: exactly three size-three circuits, 102 size-four circuits')
    print('PASS: nine locality-2 and fifteen locality-3 coordinates')

if __name__=='__main__': main()
