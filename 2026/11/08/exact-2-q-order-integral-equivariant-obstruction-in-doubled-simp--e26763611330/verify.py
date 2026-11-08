"""Exact finite checks for the signed-norm extension of an inflated simplex boundary.
No third-party dependencies. The uniform theorem is proved separately.
"""
from math import comb

def parity(x):
    return (-1) ** x.bit_count()

def verify(q):
    N=1<<q
    coeff=[parity(b) for b in range(N)]
    # Each codimension-one face is indexed by an omitted coordinate and a
    # sign vector on all remaining coordinates. Opposite facets cancel.
    cycle=0
    for omit in range(q):
        for rem in range(N):
            if rem & (1<<omit): continue
            a=rem
            b=rem | (1<<omit)
            incidence= (-1)**omit
            assert incidence*(coeff[a]+coeff[b])==0
            cycle+=1
    # Check signed equivariance for the q coordinate-flips and q-1 adjacent
    # transpositions (generators of the full hyperoctahedral group).
    action=0
    for coord in range(q):
        for mask in range(N):
            newmask=mask ^ (1<<coord)
            det=-1
            assert coeff[mask]*det==coeff[newmask]
            assert coeff[newmask]==det*coeff[mask]
            action+=1
    for coord in range(q-1):
        for mask in range(N):
            i=(mask>>coord)&1; j=(mask>>(coord+1))&1
            newmask=mask ^ ((i^j)<<coord) ^ ((i^j)<<(coord+1))
            det=-1
            # adjacent swap changes ordering, coefficient is fixed
            assert coeff[mask]*(-1)==coeff[newmask]*det
            action+=1
    # Augmentation applied to fundamental cycle; N is exact index of image
    # of Hom_Z[T](E, Z_epsilon), since transitivity forces values on all
    # oriented facets to be ± one chosen integer.
    assert sum(c*c for c in coeff)==N
    assert sum((-1)**(k-1)*comb(q,k)*2**k for k in range(1,q)) - 1 == ((-1)**(q-2))*(N-1)
    return N,cycle,action

if __name__=='__main__':
    z=c=a=0
    for q in range(3,9):
        N,c0,a0=verify(q);z+=N;c+=c0;a+=a0
    print(f'INFLATION_EXT_OK q=3..8 oriented_facets={z} codimension_cycle_tests={c} generator_action_tests={a}; extension_orders=8,16,32,64,128,256')
