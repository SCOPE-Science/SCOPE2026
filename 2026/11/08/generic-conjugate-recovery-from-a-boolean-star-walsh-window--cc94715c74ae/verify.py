"""Exact Boolean-star STFT correlation checks and recursive recovery checks.
Scientific reproducibility: python3 verify.py (standard library only).
The universal theorem uses Walsh orthogonality and linear algebra; these finite
calculations check its conventions, nonzero coefficients and reconstruction.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def parity(x):
    return x.bit_count() & 1


def stars(n):
    return [0] + [1 << i for i in range(n)]


def check(n):
    N=1 << n
    S=stars(n)
    z=[complex(1,v) for v in range(N)]  # all pairs are independent over R
    M=[]
    for t in range(N):
        row=[]
        for b in range(N):
            c=sum(z[t^s]*((-1)**parity(b&s)) for s in S)
            row.append(int(c.real*c.real+c.imag*c.imag))
        M.append(row)
    C=[[sum(M[t][b]*((-1)**parity(a&b)) for b in range(N))//N for a in range(N)] for t in range(N)]
    assert all(sum(M[t][b]*((-1)**parity(a&b)) for b in range(N))%N==0 for t in range(N) for a in range(N))
    for t in range(N):
        assert C[t][0]==sum(int(z[t^s].real**2+z[t^s].imag**2) for s in S)
        for i in range(n):
            a=1<<i
            assert C[t][a]==2*int((z[t]*z[t^a].conjugate()).real)
        for i,j in combinations(range(n),2):
            a=(1<<i)^(1<<j)
            assert C[t][a]==2*int((z[t^(1<<i)]*z[t^(1<<j)].conjugate()).real)
        assert all(C[t][a]==0 for a in range(N) if a.bit_count()>=3)
    if n%2==0:
        H=[sum(C[t][0]*((-1)**parity(b&t)) for t in range(N)) for b in range(N)]
        diag_hat=[Fraction(H[b], n+1-2*b.bit_count()) for b in range(N)]
        diag=[sum(diag_hat[b]*((-1)**parity(b&t)) for b in range(N))/N for t in range(N)]
        assert diag==[int(v.real**2+v.imag**2) for v in z]
        # Determine every local correlation from C and use a two-neighbor ordering.
        gram={}
        for x in range(N):
            gram[(x,x)]=diag[x]
        for x in range(N):
            for i in range(n):
                y=x^(1<<i)
                gram[(x,y)]=Fraction(C[x][1<<i],2)
            for i,j in combinations(range(n),2):
                y=x^(1<<i)^(1<<j)
                t=x^(1<<i)
                gram[(x,y)]=Fraction(C[t][(1<<i)^(1<<j)],2)
        # Coordinates constructed in fixed real reference orientation.
        R={0:(Fraction(1),Fraction(0)),1:(Fraction(1),Fraction(1))}
        for w in range(1,n+1):
            for x in range(1,N):
                if x in R or x.bit_count()!=w: continue
                if w==1:
                    u,v=0,1
                else:
                    coords=[1<<i for i in range(n) if x&(1<<i)]
                    u,v=x^coords[0],x^coords[1]
                (a,b),(c,d)=R[u],R[v]
                det=a*d-b*c
                assert det
                p,q=gram[(x,u)],gram[(x,v)]
                R[x]=((p*d-b*q)/det,(a*q-p*c)/det)
        assert len(R)==N
        assert all(R[x]==(Fraction(1),Fraction(x)) for x in range(N))
        rank=N + (n+comb(n,2))*N//2
    else:
        rank=N-comb(n,(n+1)//2)+(n+comb(n,2))*N//2
    # Weyl ambiguity nonzero counts, no floating arithmetic.
    count=0
    for a in range(N):
        for b in range(N):
            val=sum((-1)**parity(b&s) for s in S if (s^a) in S)
            count+=(val!=0)
    assert rank==count,(n,rank,count)
    print(f'n={n}: Walsh inversion PASS, all lag identities PASS, rank={rank}', 'Gram lateration PASS' if n%2==0 else 'singular diagonal convolution (not used)')

for n in [2,3,4,5,6]:
    check(n)
print('BOOLEAN_STAR_WALSH_STFT_CHECKS_OK')
