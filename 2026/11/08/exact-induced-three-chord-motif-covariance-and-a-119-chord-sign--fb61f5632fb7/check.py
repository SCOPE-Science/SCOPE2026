"""Reproduce exact joint-inducement tables and covariance in a random chord diagram.

Python >=3.9, standard library only. Run: python3 check.py
All computations are exact integers or rational fractions.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

Q1_NUM = (
    (362, 377, 158, 48),
    (377, 455, 227, 75),
    (158, 227, 134, 48),
    (48, 75, 48, 18),
)
Q2_NUM = (
    (56, 40, 9, 0),
    (40, 54, 24, 8),
    (9, 24, 22, 8),
    (0, 8, 8, 5),
)
Q3_NUM = ((5, 0, 0, 0), (0, 6, 0, 0), (0, 0, 3, 0), (0, 0, 0, 1))
Q_DEN = {1: 2835, 2: 315, 3: 15}
Q_NUM = {1: Q1_NUM, 2: Q2_NUM, 3: Q3_NUM}

# C(n) = binom(n,3)*(AA*n*n + BB*n + CC)/9450
AA = ((235, -5, -155, -75),
      (-5, 7, 1, -3),
      (-155, 1, 103, 51),
      (-75, -3, 51, 27))
BB = ((245, -145, 5, -105),
      (-145, 275, -115, -15),
      (5, -115, 125, -15),
      (-105, -15, -15, 135))
CC = ((-750, -780, 750, 780),
      (-780, 1380, -420, -180),
      (750, -420, 210, -540),
      (780, -180, -540, -60))
PQ = (Fraction(1,3),Fraction(2,5),Fraction(1,5),Fraction(1,15))

def words(k):
    """All ordered length-2k words with each of k named labels twice."""
    count=[2]*k
    path=[]
    def dfs():
        if len(path)==2*k:
            yield tuple(path)
        else:
            for i in range(k):
                if count[i]:
                    count[i]-=1
                    path.append(i)
                    yield from dfs()
                    path.pop()
                    count[i]+=1
    yield from dfs()

def typ_from_word(word, triple):
    pp={i:[] for i in triple}
    for index, label in enumerate(word):
        if label in pp:
            pp[label].append(index)
    s=0
    for a,b in combinations(triple,2):
        u,v=pp[a]
        x,y=pp[b]
        s+=((u<x<v) != (u<y<v))
    return s

def check_word_tables():
    for r in (1,2,3):
        k=6-r
        A=(0,1,2)
        B=tuple(range(3-r,k))
        counts=[[0]*4 for _ in range(4)]
        observed=0
        for word in words(k):
            counts[typ_from_word(word,A)][typ_from_word(word,B)]+=1
            observed+=1
        expected=factorial(2*k)//(2**k)
        assert observed==expected
        for a in range(4):
            for b in range(4):
                assert counts[a][b]*Q_DEN[r]==expected*Q_NUM[r][a][b], (r,a,b,counts[a][b])
        print(f"overlap r={r}: {observed} double-occurrence words; 16 exact table checks")
    return True

@lru_cache(maxsize=None)
def matchings(indices):
    if not indices:
        return ((),)
    a=indices[0]
    out=[]
    for b in indices[1:]:
        remainder=tuple(x for x in indices[1:] if x!=b)
        for m in matchings(remainder):
            out.append(((a,b),)+m)
    return tuple(out)

def typ_from_matching(m, triple):
    total=0
    for a,b in combinations(triple,2):
        u,v=m[a]
        x,y=m[b]
        total+=((u<x<v)!=(u<y<v))
    return total

def predicted(n,a,b):
    return Fraction(comb(n,3)*(AA[a][b]*n*n + BB[a][b]*n + CC[a][b]),9450)

def check_whole_matchings():
    for n in range(3,8):
        all_m=matchings(tuple(range(2*n)))
        N=len(all_m)
        assert N==factorial(2*n)//(2**n*factorial(n))
        triples=tuple(combinations(range(n),3))
        sums=[0]*4
        prods=[[0]*4 for _ in range(4)]
        for m in all_m:
            counts=[0]*4
            for A in triples:
                counts[typ_from_matching(m,A)]+=1
            for i in range(4):
                sums[i]+=counts[i]
                for j in range(4):
                    prods[i][j]+=counts[i]*counts[j]
        for a in range(4):
            assert Fraction(sums[a],N)==comb(n,3)*PQ[a]
            for b in range(4):
                actual=Fraction(prods[a][b],N)-Fraction(sums[a]*sums[b],N*N)
                assert actual==predicted(n,a,b), (n,a,b,actual,predicted(n,a,b))
        print(f"full n={n}: {N} perfect matchings; 4 exact means, 16 exact covariances")

def check_algebra():
    # Obtain the symbolic polynomial via three evaluations at n=3,4,5.
    # The overlap expression is degree <=2 after factoring binom(n,3).
    for n in (3,4,5,17,118,119,200):
        for a in range(4):
            for b in range(4):
                expand=Fraction(0)
                for r in (1,2,3):
                    if n-3>=3-r:
                        w=comb(3,r)*comb(n-3,3-r)
                        q=Fraction(Q_NUM[r][a][b],Q_DEN[r])
                        expand+=w*(q-PQ[a]*PQ[b])
                assert expand*comb(n,3)==predicted(n,a,b)
    for a in range(4):
        assert sum(AA[a])==sum(BB[a])==sum(CC[a])==0
    assert 118**2-115*118-420==-66
    assert 119**2-115*119-420==56
    assert 51*3**2-15*3-540<0<51*4**2-15*4-540
    for n in range(3,400):
        for a in range(4):
            assert predicted(n,a,a)>0
        assert all(predicted(n,0,j)<0 for j in (1,2,3))
        assert predicted(n,1,3)<0
        assert (predicted(n,1,2)>0)==(n>=119)
        assert (predicted(n,2,3)>0)==(n>=4)
    print('overlap expansion, deterministic row sums and exact cutoff checks passed')

if __name__=='__main__':
    check_word_tables()
    check_whole_matchings()
    check_algebra()
    print('ALL CHECKS PASSED')
