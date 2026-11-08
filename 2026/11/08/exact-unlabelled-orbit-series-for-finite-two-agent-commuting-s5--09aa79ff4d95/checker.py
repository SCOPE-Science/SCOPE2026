#!/usr/bin/env python3
"""Exact orbit-series and direct small-frame verification for commuting equivalences.
Requires Python >= 3.9 and only its standard library.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial, gcd, lcm

LIMIT = 12
EXPECTED_CONNECTED = [0,1,3,5,10,14,27,36,64,90,150,213,358]
EXPECTED_ALL = [1,1,4,9,25,54,136,294,684,1476,3271,6958,14980]
OEIS_LABELLED = [1,1,4,19,117,864,7459]
TRANSITIVE_CLASSES = [0,1,4,4,10,4,16]

@lru_cache(None)
def parts(n, mx=None):
    if mx is None: mx=n
    if n == 0: return ((),)
    return tuple((k,)+p for k in range(min(n,mx),0,-1) for p in parts(n-k,k))

def cycle_data(part):
    counts={}
    for i in part: counts[i]=counts.get(i,0)+1
    centralizer=1
    for i,m in counts.items(): centralizer*=i**m*factorial(m)
    return counts,centralizer

def mul(a,b):
    out=[Fraction(0) for _ in range(LIMIT+1)]
    for i,x in enumerate(a):
        if x:
            for j in range(LIMIT+1-i):
                if b[j]:out[i+j]+=x*b[j]
    return out

def fixed_positive_orbit_poly(length,count):
    # [(z^length)/(1-z^length)]^count
    return [Fraction(comb(k//length-1,count-1)) if k%length==0 and k//length>=count
            else Fraction(0) for k in range(LIMIT+1)]

def coefficient_series():
    connected=[Fraction(0) for _ in range(LIMIT+1)]
    for rows in range(1,LIMIT+1):
        for cols in range(1,LIMIT//rows+1):
            for lam in parts(rows):
                left,zleft=cycle_data(lam)
                for mu in parts(cols):
                    right,zright=cycle_data(mu)
                    p=[Fraction(1)]+[Fraction(0)]*LIMIT
                    for i,a in left.items():
                        for j,b in right.items():
                            p=mul(p, fixed_positive_orbit_poly(lcm(i,j),gcd(i,j)*a*b))
                    for n in range(LIMIT+1):connected[n]+=p[n]/(zleft*zright)
    # The ordinary generating function for a multiset of connected types is
    # exp(sum_{k>=1} connected(z^k)/k).
    logarithm=[Fraction(0) for _ in range(LIMIT+1)]
    for k in range(1,LIMIT+1):
        for d in range(1,LIMIT//k+1): logarithm[d*k]+=connected[d]/k
    all_counts=[Fraction(1)]+[Fraction(0)]*LIMIT
    for n in range(1,LIMIT+1):
        all_counts[n]=sum(k*logarithm[k]*all_counts[n-k] for k in range(1,n+1))/n
    return connected,all_counts

@lru_cache(None)
def restricted_growth(n):
    if not n:return [()]
    out=[]
    def grow(prefix,m):
        if len(prefix)==n:
            out.append(tuple(prefix));return
        for v in range(m+2):grow(prefix+[v],max(m,v))
    grow([0],0)
    return out

@lru_cache(None)
def canonical_matrix(mat):
    r=len(mat);s=len(mat[0]);best=None
    for a in permutations(range(r)):
        for b in permutations(range(s)):
            candidate=tuple(mat[a[i]][b[j]] for i in range(r) for j in range(s))
            if best is None or candidate<best:best=candidate
    return (r,s,best)

def canonical_frame(e,f):
    n=len(e);r=max(e)+1;s=max(f)+1
    mat=[[0]*s for _ in range(r)]
    for i,j in zip(e,f):mat[i][j]+=1
    unseen=set(range(r+s)); pieces=[]
    while unseen:
        initial=min(unseen);unseen.remove(initial);stack=[initial];visited={initial}
        while stack:
            a=stack.pop()
            neighbors=( (r+j for j in range(s) if mat[a][j]) if a<r
                        else (i for i in range(r) if mat[i][a-r]) )
            for b in neighbors:
                if b in unseen:unseen.remove(b);visited.add(b);stack.append(b)
        rows=sorted(i for i in visited if i<r)
        cols=sorted(j-r for j in visited if j>=r)
        if not all(mat[i][j]>0 for i in rows for j in cols):return None
        pieces.append(canonical_matrix(tuple(tuple(mat[i][j] for j in cols) for i in rows)))
    return tuple(sorted(pieces))

def main():
    connected,all_counts=coefficient_series()
    assert all(int(x)==x for x in connected+all_counts)
    assert [int(v) for v in connected]==EXPECTED_CONNECTED
    assert [int(v) for v in all_counts]==EXPECTED_ALL
    print('BURNSIDE_SERIES_OK nmax=',LIMIT,' connected=',EXPECTED_CONNECTED,' all=',EXPECTED_ALL)
    nframes=0
    for n in range(1,7):
        P=restricted_growth(n)
        classes=set(); labelled=0
        for e in P:
            for f in P:
                sig=canonical_frame(e,f)
                if sig is not None: classes.add(sig);labelled+=1
        assert len(classes)==EXPECTED_ALL[n],(n,len(classes),EXPECTED_ALL[n])
        assert labelled==OEIS_LABELLED[n],(n,labelled,OEIS_LABELLED[n])
        homogeneous=sum(1 for sig in classes if len(set(sig))==1 and len(set(sig[0][2]))==1)
        assert homogeneous==TRANSITIVE_CLASSES[n],(n,homogeneous,TRANSITIVE_CLASSES[n])
        nframes+=len(P)**2
        print('DIRECT_PARTITION_ORBITS_OK n=',n,'pairs_tested=',len(P)**2,
              'commuting_labelled=',labelled,'unlabelled=',len(classes),
              'vertex_transitive=',homogeneous)
    print('COMMUTING_EQUIVALENCE_CENSUS_OK pairs_tested=',nframes)

if __name__=='__main__':main()
