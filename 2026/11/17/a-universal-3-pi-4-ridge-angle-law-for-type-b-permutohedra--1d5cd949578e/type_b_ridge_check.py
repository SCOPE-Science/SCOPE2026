"""Exact low-rank checks for type-B permutohedral ridge-angle classification.
Python standard library only. These finite tests do not certify the limit theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, pi, acos, sqrt


def rank_integer(rows, n):
    # Fraction-exact row reduction, no floating rank decisions.
    basis = {}
    for orig in rows:
        row = [Fraction(x) for x in orig]
        for pivot, base in sorted(basis.items()):
            if row[pivot]:
                factor=row[pivot]
                row=[x-factor*y for x,y in zip(row,base)]
        piv = next((i for i,x in enumerate(row) if x), None)
        if piv is not None:
            factor=row[piv]
            basis[piv]=[x/factor for x in row]
            if len(basis)==n:
                return n
    return len(basis)


def orbit(n):
    return sorted({tuple(e[i]*p[i] for i in range(n))
                   for p in permutations(range(1,n+1))
                   for e in product((-1,1),repeat=n)})


def get_facets(n,vertices):
    out=[]
    for u in product((-1,0,1),repeat=n):
        k=sum(t!=0 for t in u)
        if not k:
            continue
        h=sum(range(n-k+1,n+1))
        touched=[idx for idx,v in enumerate(vertices)
                 if sum(x*y for x,y in zip(u,v))==h]
        assert rank_integer(((vertices[j][i]-vertices[touched[0]][i]
                        for i in range(n)) for j in touched[1:]),n)==n-1
        out.append((u,k,frozenset(touched)))
    assert len(out)==3**n-1
    return out


def checked_pair(a,b,n,vertices):
    common=a[2] & b[2]
    if not common:
        return False
    inds=list(common)
    base=vertices[inds[0]]
    return rank_integer(((vertices[j][i]-base[i] for i in range(n))
                         for j in inds[1:]),n)==n-2


def predicted_pair(a,b):
    small,large=sorted((a,b),key=lambda t:t[1])
    if small[1]>=large[1]:
        return False
    return all(x==0 or x==y for x,y in zip(small[0],large[0]))


def verify(n):
    vs=orbit(n)
    fs=get_facets(n,vs)
    table=Counter()
    for a,b in combinations(fs,2):
        observed=checked_pair(a,b,n,vs)
        claimed=predicted_pair(a,b)
        assert observed==claimed,(n,a[0],b[0],observed,claimed)
        if observed:
            small,large=sorted((a,b),key=lambda t:t[1])
            k,l=small[1],large[1]
            assert sum(x*y for x,y in zip(small[0],large[0]))==k
            theta=pi-acos(sqrt(k/l))
            assert pi/2<theta<pi
            table[(k,l)]+=1
    assert sum(table.values())==5**n-2*3**n+1
    assert all(table[(k,l)]==2**l*comb(n,l)*comb(l,k)
          for l in range(2,n+1) for k in range(1,l))
    # Symbolic pairing of (A,B) and (B,A) proves the exact mean;
    # this numerical check independently guards the convention.
    mean=sum(count*(pi-acos(sqrt(k/l)))
       for (k,l),count in table.items())/sum(table.values())
    assert abs(mean-3*pi/4)<1e-12
    print(f'PASS n={n} vertices={len(vs)} facets={len(fs)} ridges={sum(table.values())} rank_pairs={len(table)}')

if __name__=='__main__':
    for n in (2,3,4):
        verify(n)
    print('TYPE_B_RIDGE_SPECTRUM_PASS')
