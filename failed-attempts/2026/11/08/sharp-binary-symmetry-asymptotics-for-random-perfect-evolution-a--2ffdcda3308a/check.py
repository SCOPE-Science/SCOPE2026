"""Exact small-dimensional validation of binary perfect-evolution symmetry laws."""
from itertools import permutations, product
from math import prod, comb

def invertible(rows,n):
    a=list(rows)
    rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if (a[i]>>col)&1),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        for i in range(n):
            if i!=rank and ((a[i]>>col)&1):
                a[i]^=a[rank]
        rank+=1
    return rank==n

def invariant(rows, sigma):
    n=len(rows)
    for i in range(n):
        for j in range(n):
            if ((rows[i]>>j)&1)!=((rows[sigma[i]]>>sigma[j])&1):
                return False
    return True

def fixed_count(n):
    perms=list(permutations(range(n)))
    identity=tuple(range(n))
    transpositions=[p for p in perms if sum(p[i]!=i for i in range(n))==2]
    counts={"invertible":0,"nontrivial":0,"only_single_swap":0,"transposition_incidences":0,
            "transposition_intersections":0,"other_symmetry":0,"pointwise_by_swap":0,"automorphism_incidences":0}
    for rows in product(range(1<<n),repeat=n):
        if not invertible(rows,n):continue
        counts['invertible']+=1
        aut=[p for p in perms if invariant(rows,p)]
        counts['automorphism_incidences']+=len(aut)
        if len(aut)>1: counts['nontrivial']+=1
        trans=sum(p in transpositions for p in aut)
        counts['transposition_incidences']+=trans
        if trans>1:counts['transposition_intersections']+=1
        if len(aut)==2 and trans==1: counts['only_single_swap']+=1
        if any(p!=identity and p not in transpositions for p in aut):counts['other_symmetry']+=1
        counts['pointwise_by_swap']+=int(trans>0)
    def gl(k):
        return prod((1<<k)-(1<<j) for j in range(k))
    centralizer=(1<<(2*n-3))*gl(n-2)
    counts['GL_n']=gl(n)
    counts['one_swap_centralizer']=centralizer
    counts['expected_swap_incidences']=comb(n,2)*centralizer
    from math import factorial
    assert counts['automorphism_incidences']%factorial(n)==0
    counts['isomorphism_classes']=counts['automorphism_incidences']//factorial(n)
    assert counts['invertible']==gl(n)
    assert counts['transposition_incidences']==counts['expected_swap_incidences']
    assert counts['only_single_swap']<=counts['nontrivial']
    return counts

def independent_transposition_centralizer_test(n=5):
    """Enumerate the full permutation-fixed binary matrix subspace by cell orbits."""
    tau=(1,0)+tuple(range(2,n))
    cells={(i,j) for i in range(n) for j in range(n)}
    orbits=[]
    while cells:
        i,j=min(cells)
        orb={(i,j),(tau[i],tau[j])}
        orbits.append(orb)
        cells-=orb
    assert len(orbits)==n*n-2*n+2
    rowbits=[]
    for orb in orbits:
        rows=[0]*n
        for i,j in orb:rows[i]|=1<<j
        rowbits.append(rows)
    count=0
    rows=[0]*n
    prior=0
    for g in range(1<<len(orbits)):
        if g:
            gray=g^(g>>1)
            changed=prior^gray
            flip=changed.bit_length()-1
            for i in range(n):rows[i]^=rowbits[flip][i]
            prior=gray
        if invertible(rows,n): count+=1
    def gl(k):return prod((1<<k)-(1<<j) for j in range(k))
    expected=(1<<(2*n-3))*gl(n-2)
    assert count==expected
    return len(orbits),count

if __name__=='__main__':
    for n in (2,3,4):
        c=fixed_count(n)
        print('N',n,' '.join(f'{k}={v}' for k,v in c.items()))
    d,c=independent_transposition_centralizer_test(5)
    print('N 5 independent_fixed_space_dimension',d,'centralizing_invertibles',c)
    print('VERIFY_OK')
