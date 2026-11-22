#!/usr/bin/env python3
"""Reproducible integer verification of low-rank finite Fourier restrictions.

Python 3 standard library. No numerical matrix ranks are used. For order six,
one prime specialization suffices; at order twenty-one, two prime-field
specializations suffice by the cyclotomic norm bound explained below.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial, gcd


def is_prime(n):
    if n < 2: return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0: return False
    return True


def order_n_root(n, p):
    assert is_prime(p) and (p-1) % n == 0
    prime_factors = [d for d in range(2,n+1) if n%d == 0 and all(d%j for j in range(2,int(d**0.5)+1))]
    for a in range(2,1000):
        w = pow(a,(p-1)//n,p)
        if pow(w,n,p)==1 and all(pow(w,n//d,p)!=1 for d in prime_factors):
            return [pow(w,j,p) for j in range(n)]
    raise AssertionError('primitive root missing')


def rank_mod(mat, p):
    a = [list(row) for row in mat]
    m, n = len(a), len(a[0])
    rank = 0
    for j in range(n):
        k = next((k for k in range(rank,m) if a[k][j]%p), None)
        if k is None: continue
        a[rank], a[k] = a[k], a[rank]
        inv = pow(a[rank][j],p-2,p)
        for i in range(rank+1,m):
            if a[i][j]:
                factor = a[i][j]*inv%p
                for l in range(j,n):
                    a[i][l]=(a[i][l]-factor*a[rank][l])%p
        rank+=1
        if rank==m: break
    return rank


def coset_prediction(n, rows, cols):
    d_c = gcd(n,*[c-cols[0] for c in cols])
    d_r = gcd(n,*[r-rows[0] for r in rows])
    classes_r = len({r%(n//d_c) for r in rows})
    classes_c = len({c%(n//d_r) for c in cols})
    return min(3,classes_r,classes_c)


def check_all_rectangular_order_six():
    n,p=6,1000000009
    assert p > factorial(n)**2   # phi(6)=2: nonzero minor norm bound
    roots = order_n_root(n,p)
    sizes=Counter()
    total=0
    subsets=[list(combinations(range(n),k)) for k in range(n+1)]
    for k in range(1,n+1):
        for ell in range(1,n+1):
            for R in subsets[k]:
                for C in subsets[ell]:
                    actual=rank_mod([[roots[r*c%n] for c in C] for r in R],p)
                    asserted=coset_prediction(n,R,C)
                    assert min(3,actual)==asserted,(R,C,actual,asserted)
                    sizes[(k,ell)]+=1
                    total+=1
    assert total==3969
    print('ORDER 6: all',total,'nonempty rectangular restrictions verify the rank-two criterion')


def affine_orbits(n,k):
    units=[a for a in range(n) if gcd(a,n)==1]
    visited=set();orbits=[]
    for R in combinations(range(n),k):
        if R in visited:continue
        orbit={tuple(sorted((a*r+b)%n for r in R)) for a in units for b in range(n)}
        visited.update(orbit)
        orbits.append((R,len(orbit)))
    assert len(visited)==comb(n,k)
    return orbits


def check_all_square_order_21():
    n=21
    primes=[1000000009,1000000093]
    assert all(is_prime(p) and (p-1)%n==0 for p in primes)
    # Degree phi(21)=12. A k x k determinant of roots of unity has all
    # Galois conjugates of magnitude <=k!, hence absolute norm <=(k!)^12.
    # If a nonzero determinant vanished modulo both distinct primes in
    # two integral specializations, its nonzero norm would be divisible
    # by their product, contradicting this bound for k<=4.
    assert primes[0]*primes[1] > factorial(4)**12
    roots=[order_n_root(n,p) for p in primes]
    orbits=affine_orbits(n,4)
    assert len(orbits)==33
    counts=Counter(); tested=0; disagreements=0; two_class_weight=0
    for R,sr in orbits:
        for C,sc in orbits:
            ranks=[rank_mod([[tbl[r*c%n] for c in C] for r in R],p)
                   for tbl,p in zip(roots,primes)]
            if ranks[0]!=ranks[1]: disagreements+=1
            k=max(ranks)
            pred=coset_prediction(n,R,C)
            assert min(k,3)==pred,(R,C,ranks,pred)
            weight=sr*sc
            counts[k]+=weight
            if k==2:
                two_class_weight+=weight
                assert (len({r%3 for r in R})==1 and len({c%7 for c in C})==2) or (len({c%3 for c in C})==1 and len({r%7 for r in R})==2)
            tested+=1
    assert tested==33**2 and disagreements==0
    assert sum(counts.values())==comb(n,4)**2
    assert dict(counts)=={2:66150,3:1942164,4:33811911}
    assert two_class_weight==90*comb(7,4)*comb(7,2)
    print('ORDER 21: 33 affine row orbits x 33 affine column orbits,',tested,'pairs')
    print('ORDER 21: exact rank distribution',dict(sorted(counts.items())))
    print('ORDER 21: rank-two prediction and formula both give',two_class_weight)
    print('ORDER 21: modular rank disagreements',disagreements)


if __name__=='__main__':
    check_all_rectangular_order_six()
    check_all_square_order_21()
    print('VERIFICATION PASS')
