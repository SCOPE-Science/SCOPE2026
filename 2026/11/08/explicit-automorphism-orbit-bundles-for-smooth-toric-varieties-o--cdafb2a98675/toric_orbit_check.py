"""Finite-field checks of projective-bundle flag-orbit point counts.

The infinite-dimensional geometric statements require the accompanying proof.
"""
from itertools import combinations_with_replacement, product

def projective_vectors(q, n):
    return [v for v in product(range(q), repeat=n)
            if any(v) and next(c for c in v if c) == 1]

def calc(q, degrees):
    distinct=sorted(set(degrees))
    mult=[degrees.count(d) for d in distinct]
    counts=[]
    for d in distinct:
        counts.append(sum(min(degrees[i] for i,x in enumerate(v) if x) == d
                          for v in projective_vectors(q,len(degrees))))
    expected=[]
    for j,m in enumerate(mult):
        higher=sum(mult[j+1:])
        expected.append(((q**m-1)//(q-1))*q**higher)
    assert counts==expected,(q,degrees,counts,expected)
    assert sum(counts)==(q**len(degrees)-1)//(q-1)
    return counts

if __name__=='__main__':
    tested=0
    for q in (2,3,5):
        for n in range(2,6):
            for tail in combinations_with_replacement(range(4), n-1):
                a=(0,*tail)
                calc(q,a)
                tested+=1
    print('FLAG_ORBIT_COUNTS_OK', tested)
    print('INFINITE_PROOF_USES_PROJECTIVE_BUNDLE_FILTRATION')
