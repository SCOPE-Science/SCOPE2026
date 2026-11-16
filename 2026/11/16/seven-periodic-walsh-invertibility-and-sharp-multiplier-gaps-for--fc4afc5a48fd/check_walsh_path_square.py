#!/usr/bin/env python3
"""Exact independent checks of a path-square Fourier statement."""
from itertools import product

SIGNS=(1,-1)


def recurrence(signs):
    prev2=prev1=now=1
    for sign in signs:
        prev2,prev1,now=prev1,now,now+sign*prev2
    return now


def is_independent(mask,n):
    return (mask & (mask<<1))==0 and (mask & (mask<<2))==0


def direct_signed_sum(signs):
    n=len(signs)
    total=0
    for mask in range(1<<n):
        if is_independent(mask,n):
            prod=1
            for i in range(n):
                if mask>>i & 1: prod*=signs[i]
            total+=prod
    return total


def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))

I=((1,0,0),(0,1,0),(0,0,1))

def matrix_for(signs):
    M=I
    for sign in signs:
        step=((1,0,sign),(1,0,0),(0,1,0))
        M=matmul(step,M)
    return M


def block_family():
    for first5 in product(SIGNS,repeat=5):
        yield first5+(-first5[4],-1)


def fast_transform_independent_set(n):
    a=[int(is_independent(mask,n)) for mask in range(1<<n)]
    step=1
    while step < (1<<n):
        for start in range(0,1<<n,step*2):
            for i in range(start,start+step):
                x,y=a[i],a[i+step]
                a[i],a[i+step]=x+y,x-y
        step*=2
    return a


def main():
    # Symbol-free test of the 3x3 matrix identity in all 32 admissible cases.
    blocks=list(block_family())
    assert len(blocks)==32 and len(set(blocks))==32
    for s in blocks:
        M=matrix_for(s)
        assert M[0]==(-s[2]*s[4],0,0), (s,M)
    all_preserving=[s for s in product(SIGNS,repeat=7)
                    if matrix_for(s)[0][1:]==(0,0) and abs(matrix_for(s)[0][0])==1]
    assert set(blocks)==set(all_preserving)

    # Independent direct sum versus three-state recursion, for all signs through n=10.
    for n in range(0,11):
        for signs in product(SIGNS,repeat=n):
            assert recurrence(signs)==direct_signed_sum(signs)

    # Fully independent fast Walsh transform through n=16 (65,536 frequencies at n=16).
    zeros={}; least={}
    for n in range(1,17):
        vals=fast_transform_independent_set(n)
        residue=n%7
        expected_min=2 if residue in (1,3,4) else 1
        zeros[n]=sum(v==0 for v in vals)
        least[n]=min(abs(v) for v in vals if v)
        assert least[n]==expected_min,(n,least[n])
        assert (zeros[n]>0)==(residue in (1,3,4)),(n,zeros[n])
        assert all(v%2==(residue not in (1,3,4)) for v in vals)

    zero_seeds={1:(-1,),3:(1,-1,-1),4:(1,1,-1,-1)}
    min_seeds={0:(),1:(1,),2:(1,-1),3:(1,1,-1),4:(1,1,1,-1),
               5:(1,1,1,-1,-1),6:(1,1,1,1,-1,-1)}
    for r,seed in zero_seeds.items():assert recurrence(seed)==0
    for r,seed in min_seeds.items():
        assert abs(recurrence(seed))==(2 if r in (1,3,4) else 1)
    for k in range(0,3):
        for r,seed in zero_seeds.items():
            words=set()
            for blkseq in product(blocks,repeat=k):
                seq=seed+tuple(i for block in blkseq for i in block)
                words.add(seq)
                assert recurrence(seq)==0
            assert len(words)==32**k

    # Deterministic varied-sign witnesses beyond exhaustive Fourier dimensions.
    for n in range(1,202):
        r=n%7
        k=n//7
        for variant in range(5):
            b=[blocks[(i*7+variant*11)%32] for i in range(k)]
            if r in zero_seeds:
                s=zero_seeds[r]+tuple(z for t in b for z in t)
                assert len(s)==n and recurrence(s)==0
            s=min_seeds[r]+tuple(z for t in b for z in t)
            assert len(s)==n and abs(recurrence(s))==(2 if r in zero_seeds else 1)
    # Direct finite-field parity check across many positions.
    counts=[1,1,1]
    for n in range(1,1001):
        counts=[counts[1],counts[2],counts[2]+counts[0]]
        assert counts[2]%2==(n%7 not in (1,3,4))
    print('PATH_SQUARE_WALSH_EXACT_PASS direct_signs_n_le_10=2047',
          'full_FFT_n_le_16=131070',
          'seven_blocks=32', 'zero_seeds=1,3,4',
          'min_seeds=0..6',
          'long_witnesses_n_le_201',
          'parity_n_le_1000')
    print('n=1..16 zeros:',','.join(str(zeros[n]) for n in range(1,17)))

if __name__=='__main__':main()
