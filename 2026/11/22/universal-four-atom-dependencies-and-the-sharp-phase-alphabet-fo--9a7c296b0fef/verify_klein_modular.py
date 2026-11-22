#!/usr/bin/env python3
"""Independent modular rank certificate for a four-coordinate finite Gabor system.

The characteristic-seven-window evaluation takes place in F_43: 4 has
multiplicative order 7 in that field, giving a well-defined map
Z[zeta_7] -> F_43. A nonzero minor modulo 43 cannot be zero over C.
"""
from itertools import combinations
from collections import Counter

P=43
PHASES=(0,1,2,4)
ROOT=4
assert pow(ROOT,7,P)==1 and all(pow(ROOT,k,P)!=1 for k in range(1,7))


def bitdot(a,b):
    return (a&b).bit_count()%2


def col(j):
    t,m=divmod(j,4)
    return [((1 if bitdot(m,x)==0 else -1)*pow(ROOT,PHASES[x^t],P))%P for x in range(4)]


def rank_mod(columns):
    a=[[col_j[i] for col_j in columns] for i in range(4)]
    rank=0
    n=len(columns)
    for j in range(n):
        k=next((i for i in range(rank,4) if a[i][j]),None)
        if k is None:
            continue
        a[k],a[rank]=a[rank],a[k]
        inv=pow(a[rank][j],-1,P)
        for i in range(rank+1,4):
            fac=a[i][j]*inv%P
            if fac:
                a[i]=[(v-fac*w)%P for v,w in zip(a[i],a[rank])]
        rank+=1
        if rank==n:
            break
    return rank


def omega(u,v):
    tu,mu=divmod(u,4)
    tv,mv=divmod(v,4)
    return bitdot(tu,mv)^bitdot(tv,mu)


def geometric_circuit(seq):
    anchor=seq[0]
    a,b,c=(x^anchor for x in seq[1:])
    return a^b^c!=0 and all(omega(u,v)==1 for u,v in ((a,b),(a,c),(b,c)))


def main():
    cols=[col(j) for j in range(16)]
    r3=Counter(rank_mod([cols[j] for j in ids]) for ids in combinations(range(16),3))
    r4=Counter()
    geometric=0
    for ids in combinations(range(16),4):
        k=rank_mod([cols[j] for j in ids]);r4[k]+=1
        c=geometric_circuit(ids)
        geometric+=c
        assert (k==3)==c,(ids,k,c)
    assert r3=={3:560},r3
    assert r4=={3:240,4:1580},r4
    assert geometric==240
    print('FIELD=F_43; PRIMITIVE_SEVENTH_ROOT=4')
    print('INDEPENDENT_TRIPLES=560/560')
    print('FOUR_SETS_RANK3=240; RANK4=1580; SYMPLECTIC_CLASSIFICATION_MATCHES=1820')
    print('NONZERO_FINITE_FIELD_MINORS_LIFT_TO_NONZERO_COMPLEX_CYCLOTOMIC_MINORS')
    print('OK')

if __name__=='__main__':main()
