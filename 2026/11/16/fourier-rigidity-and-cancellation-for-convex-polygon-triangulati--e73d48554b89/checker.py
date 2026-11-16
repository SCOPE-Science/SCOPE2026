"""Exact integer checks for Fourier cancellation and congruence on polygon triangulations.
Run: python checker.py (Python 3.9+, standard library only).
"""
from functools import lru_cache
from math import comb
from random import Random


def catalan(n):
    return comb(2*n,n)//(n+1)


def diagonals(n):
    return [(i,j) for i in range(n) for j in range(i+2,n) if (i,j)!=(0,n-1)]


def signed_dp(n, negatives):
    """Sum over triangulations of product of weights on present diagonals."""
    neg=set(negatives)
    v=[[0]*n for _ in range(n)]
    for i in range(n-1):v[i][i+1]=1
    for length in range(2,n):
        for i in range(n-length):
            j=i+length
            total=0
            for k in range(i+1,j):
                a=-1 if (i,k) in neg else 1
                b=-1 if (k,j) in neg else 1
                total+=a*b*v[i][k]*v[k][j]
            v[i][j]=total
    return v[0][n-1]


def all_masks(n):
    """Independent explicit list of triangulation diagonal masks (small n)."""
    ds=diagonals(n);index={d:k for k,d in enumerate(ds)}
    @lru_cache(None)
    def rec(i,j):
        if j==i+1:return (0,)
        out=[]
        for k in range(i+1,j):
            bridge=(1<<index[(i,k)] if k>i+1 else 0)|(1<<index[(k,j)] if j>k+1 else 0)
            for a in rec(i,k):
                for b in rec(k,j):out.append(a|b|bridge)
        return tuple(out)
    return ds,rec(0,n-1)


def directly(n, neg):
    ds,masks=all_masks(n)
    frequency=sum(1<<i for i,d in enumerate(ds) if d in neg)
    return sum(1 if ((t&frequency).bit_count()%2==0) else -1 for t in masks)


def parity_signs(n):
    return {(i,j) for i,j in diagonals(n) if i%2==0}


def run():
    rng=Random(741893)
    for n in range(3,10):
        ds,masks=all_masks(n)
        assert len(masks)==catalan(n-2)
        for trial in range(45):
            neg={d for d in ds if rng.randrange(2)}
            assert directly(n,neg)==signed_dp(n,neg)
    for n in range(3,31):
        res=signed_dp(n,parity_signs(n))
        target=0 if n%2==0 else catalan((n-3)//2)
        assert res==target,(n,res,target)
    for n in range(3,32,2):
        ds=diagonals(n);base=catalan(n-2)
        for trial in range(60):
            neg={d for d in ds if rng.randrange(2)}
            assert signed_dp(n,neg)%4==base%4,(n,neg)
    for n in (7,):
        ds,masks=all_masks(n)
        coeff=[0]*(1<<len(ds))
        for mask in masks:coeff[mask]=1
        for i in range(len(ds)):
            for a in range(len(coeff)):
                if not(a>>i&1):
                    v,w=coeff[a],coeff[a|(1<<i)]
                    coeff[a]=v+w;coeff[a|(1<<i)]=v-w
        assert all(x%4==2 for x in coeff)
        assert all(x!=0 for x in coeff)
    n=15
    neg=parity_signs(n)^ {(0,8),(2,6)}
    values=[signed_dp(n,base) for base in (parity_signs(n),parity_signs(n)^{(0,8)},parity_signs(n)^{(2,6)},neg)]
    assert values==[132,32,20,0],values
    assert ((values[0]-values[1])//2,(values[0]-values[2])//2,(values[3]-values[1]-values[2]+values[0])//4)==(50,56,20)
    for n in (3,5,7,9,11,13,17,19,21,25,33):
        if (n-1).bit_count()<=2:
            assert catalan(n-2)%4 in (1,2,3)
    print('TRIANGULATION_WALSH_EXACT_PASS; small independent enumeration n=3..9; sign-identity n=3..30; congruence odd n=3..31; exhaustive heptagon Walsh; 15-gon zero witness')

if __name__=='__main__':run()
