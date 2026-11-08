"""Independent checks of finite-matrix Fourier rank-ball coefficients and signs.
Uses Python 3 standard library, and NumPy for the optional full Fourier transforms.
"""
from math import prod

def gaussian(n,k,q):
    if not 0<=k<=n: return 0
    top=prod(q**(n-i)-1 for i in range(k))
    bot=prod(q**(k-i)-1 for i in range(k))
    assert top%bot==0
    return top//bot

def rank_count(m,n,r,q):
    if r<0 or r>min(m,n): return 0
    numerator=prod((q**m-q**i)*(q**n-q**i) for i in range(r))
    denominator=prod((q**r-q**i) for i in range(r))
    assert numerator%denominator==0
    return numerator//denominator

def eigen(m,n,k,q):
    return q**(2*n)*gaussian(k,2,q)-q**(n+1)*gaussian(m-2,1,q)*gaussian(k,1,q)+q**3*gaussian(m-1,2,q)

def norm(m,n,q):
    assert m>=3 and n>=m and q>=2
    negatives=[s for s in range(m+1) if eigen(m,n,m-s,q)<0]
    return negatives, 1+sum(2*rank_count(m,n,s,q)*(-eigen(m,n,m-s,q)) for s in negatives)/q**(m*n)

def matrix_rank(vec,q):
    a=[list(v) for v in vec]; rows=len(a); cols=len(a[0]); pivot=0
    for j in range(cols):
        k=next((i for i in range(pivot,rows) if a[i][j]%q),None)
        if k is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=pow(int(a[pivot][j]),-1,q)
        a[pivot]=[(z*inv)%q for z in a[pivot]]
        for i in range(rows):
            if i!=pivot and a[i][j]:
                z=a[i][j];a[i]=[(x-z*y)%q for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==rows: break
    return pivot

def check_fft(m,n,q):
    import numpy as np
    import itertools
    shape=(q,)*(m*n)
    f=np.zeros(shape,dtype=float)
    for tup in itertools.product(range(q),repeat=m*n):
        a=[tup[i*n:(i+1)*n] for i in range(m)]
        f[tup]= int(matrix_rank(a,q)<=2)
    ft=np.fft.fftn(f)
    counts={}
    for tup in itertools.product(range(q),repeat=m*n):
        a=[tup[i*n:(i+1)*n] for i in range(m)]
        k=m-matrix_rank(a,q)
        target=eigen(m,n,k,q)
        assert abs(ft[tup]-target)<1e-6,(m,n,q,tup,k,ft[tup],target)
        counts[k]=counts.get(k,0)+1
    assert all(counts.get(m-r,0)==rank_count(m,n,r,q) for r in range(m+1))
    assert abs(sum(abs(x) for x in ft.flat)/q**(m*n)-norm(m,n,q)[1])<1e-6
    print('FFT_PASS',q,m,n,'norm',norm(m,n,q)[1])

def check_binary_five(n=5):
    # Independently enumerate all rank-zero, one and two matrices, computing
    # additive Fourier sums at diagonal frequency representatives of each rank.
    m=5
    planes={}
    for u in range(1,32):
        for v in range(1,32):
            if v==u: continue
            triple=tuple(sorted((u,v,u^v)))
            if triple not in planes: planes[triple]=(triple[0],triple[1])
    assert len(planes)==155
    reps=[0]*6
    def accum(cols):
        for r in range(6):
            parity=sum((cols[j]>>j)&1 for j in range(r))&1
            reps[r]+=(-1 if parity else 1)
    accum([0]*n)
    for u in range(1,32):
        for p in range(1,2**n):
            accum([u if (p>>j)&1 else 0 for j in range(n)])
    for u,v in planes.values():
        for p in range(1,2**n):
            for w in range(1,2**n):
                if w==p: continue
                accum([(u if (p>>j)&1 else 0) ^ (v if (w>>j)&1 else 0) for j in range(n)])
    assert all(reps[r]==eigen(5,n,5-r,2) for r in range(6)),(n,reps,[eigen(5,n,5-r,2) for r in range(6)])
    assert reps[3]<0 and reps[4]<0 if n==5 else reps[3]>0 and reps[4]<0
    print('DIRECT_RANK2_ENUM_PASS',2,5,n,reps)

if __name__=='__main__':
    for q in (2,3,4,5,7,8,9):
        for m in range(3,18):
            for n in (m,m+1,m+3):
                negatives, _ =norm(m,n,q)
                expected=([m-2,m-1] if q==2 and m==n and m>=5 else [m-1])
                assert negatives==expected,(q,m,n,negatives,expected)
                assert sum(rank_count(m,n,r,q) for r in range(m+1))==q**(m*n)
                assert sum(rank_count(m,n,m-k,q)*eigen(m,n,k,q) for k in range(m+1))==q**(m*n)
    print('INTEGER_SIGN_MULTIPLICITY_PASS')
    check_fft(3,3,2)
    check_fft(4,4,2)
    check_fft(3,3,3)
    check_binary_five(5)
    check_binary_five(6)
    print('ALL_RANK_TWO_BALL_CHECKS_PASS')
