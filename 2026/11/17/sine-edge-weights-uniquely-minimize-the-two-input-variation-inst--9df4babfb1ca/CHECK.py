"""Reproducible finite tests for optimal weighted-BV stability of increasing sorting.

Only standard Python 3. The theorem for all dimensions follows from the proof,
not from the bounded tests performed here.
"""
import itertools
import math
import random


def weighted_variation(v, w):
    return sum(z * abs(v[j+1]-v[j]) for j,z in enumerate(w))


def sorting_lipschitz_exact_from_masks(w):
    n=len(w)+1
    out=[]
    for k in range(1,n):
        best=0.0
        for rare in itertools.combinations(range(n),k):
            bits=[int(i in rare) for i in range(n)]
            gain=weighted_variation(bits,w)
            best=max(best,gain)
        out.append(best/w[k-1])
    return max(out),out


def central_row(n,k):
    m=(n-1)//2
    q=min(k,n-k)
    if n%2:
        # n=2m+1; exactly 2q central edges
        return [float(m-q+1<=j<=m+q) for j in range(1,n)]
    m=n//2
    if q==m:
        return [1.0]*(n-1)
    # n=2m; the two equally optimal central blocks of 2q edges
    return [(int(m-q<=j<=m+q-1)+int(m-q+1<=j<=m+q))/2
            for j in range(1,n)]


def lambda_star(n):
    return (1/math.tan(math.pi/(2*n))) if n%2==0 else (1/math.sin(math.pi/(2*n)))


def sine_weights(n):
    return [math.sin(math.pi*j/n) for j in range(1,n)]


def check():
    rng=random.Random(27591)
    count=0
    for n in range(2,12):
        w=sine_weights(n)
        lam=lambda_star(n)
        vals,cols=sorting_lipschitz_exact_from_masks(w)
        assert abs(vals-lam)<3e-12*(1+lam),(n,vals,lam)
        for k,row in enumerate([central_row(n,j) for j in range(1,n)],1):
            aw=sum(a*b for a,b in zip(row,w))
            assert abs(aw-lam*w[k-1])<3e-12*(1+lam),(n,k,aw,lam*w[k-1])
            assert abs(cols[k-1]-lam)<3e-12*(1+lam),(n,k,cols[k-1],lam)
            count+=1
        for _ in range(40):
            randw=[0.1+3*rng.random() for j in range(n-1)]
            L,_=sorting_lipschitz_exact_from_masks(randw)
            assert L>=lam-1e-10,(n,L,lam)
            count+=1
        # A realization in a strict sorting chamber for the maximizing mask:
        # a step at k is reordered by an arbitrary sorting permutation.
        k=rng.randrange(1,n)
        best=-1; bitsstar=None
        for rare in itertools.combinations(range(n),k):
            bits=[int(i in rare) for i in range(n)]
            z=weighted_variation(bits,w)
            if z>best:best=z;bitsstar=bits
        # Input original indices 0..k-1 are the minority (0 in the step).
        minority=list(range(k));majority=list(range(k,n))
        perm=[]
        for v in bitsstar:
            perm.append((minority if v==1 else majority).pop(0))
        x=[0.0]*n
        for rank,ind in enumerate(perm):x[ind]=3.0*rank
        eps=0.1
        y=[x[i]+eps*(i>=k) for i in range(n)]
        sx=sorted(x);sy=sorted(y)
        ratio=weighted_variation([sy[i]-sx[i] for i in range(n)],w)/(
                weighted_variation([y[i]-x[i] for i in range(n)],w))
        assert abs(ratio-best/w[k-1])<1e-10,(n,k,ratio,best/w[k-1])
        count+=1
    for n in range(12,251):
        w=sine_weights(n);lam=lambda_star(n)
        for k in range(1,n):
            aw=sum(a*b for a,b in zip(central_row(n,k),w))
            assert abs(aw-lam*w[k-1])<3e-11*(1+lam)
            count+=1
    assert abs(lambda_star(4)-(1+math.sqrt(2)))<1e-12
    assert abs(lambda_star(5)-(1+math.sqrt(5)))<1e-12
    print('CENTRAL_CUT_MATRIX_AND_POSITIVE_SINE_EIGENVECTOR_PASS',count)
    print('ALL_BINARY_REORDERINGS_AND_RANDOM_WEIGHT_LOWER_BOUNDS_PASS',sum(2**n for n in range(2,12)))
    print('ATTAINING_STRICT_SORTING_CHAMBER_PAIRS_PASS',10)
    print('SHARP_PARITY_VALUES_PASS n=4:',lambda_star(4),'n=5:',lambda_star(5))
    print('ALL_SORTING_WEIGHTED_VARIATION_TESTS_PASS')

if __name__=='__main__':check()
