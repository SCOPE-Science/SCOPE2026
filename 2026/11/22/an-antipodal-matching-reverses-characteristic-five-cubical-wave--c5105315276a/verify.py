"""Exact independent finite-field matrix checks for antipodal-augmented cube waves.
Usage: python3 verify.py. Python standard library only.
"""
from math import comb, lcm

ORDERS = {0:4, 1:6, 2:5, 3:10, 4:3}


def multiplicities(d, augmented):
    out = [0] * 5
    for k in range(d+1):
        val = d-2*k+ ((-1)**k if augmented else 0)
        out[val%5] += comb(d,k)
    return out


def fixed_exponent(d, augmented, t):
    z, one, plus2, minus2, minus1 = multiplicities(d, augmented)
    return (2*z*(t%4 == 0) + 2*one*(t%6==0)
            + plus2*(1+(t%5==0))
            + minus2*(t%2==0)*(1+(t%5==0))
            + 2*minus1*(t%3==0))


def theoretical_order(d, augmented):
    m=multiplicities(d, augmented)
    return lcm(*(ORDERS[r] for r in range(5) if m[r]))


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def mul(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    C[i][j]+=a*b
        C[i]=[v%5 for v in C[i]]
    return C


def powmat(A,t):
    B=eye(len(A))
    while t:
        if t&1:B=mul(B,A)
        A=mul(A,A)
        t//=2
    return B


def rank5(A):
    A=[list(x) for x in A]
    n=len(A); piv=0
    for j in range(len(A[0])):
        row=next((i for i in range(piv,n) if A[i][j]%5),None)
        if row is None:continue
        A[piv],A[row]=A[row],A[piv]
        k=pow(A[piv][j],-1,5)
        A[piv]=[(x*k)%5 for x in A[piv]]
        for i in range(piv+1,n):
            a=A[i][j]
            if a:
                A[i]=[(x-a*y)%5 for x,y in zip(A[i],A[piv])]
        piv+=1
        if piv==n: break
    return piv


def transition(d,augmented):
    N=1<<d
    M=[[0]*(2*N) for _ in range(2*N)]
    for x in range(N):
        for j in range(d):
            M[x][x^(1<<j)] += 1
        if augmented:M[x][x^(N-1)] += 1
        M[x][N+x] = 4
        M[N+x][x] = 1
    return M


def divisors(n):
    return [t for t in range(1,n+1) if n%t==0]


def run():
    tests=0
    for d in range(2,6):
      for augmented in (False,True):
        order=theoretical_order(d,augmented)
        print(f'd={d} augmented={augmented} order={order} multiplicities={multiplicities(d,augmented)}')
        M=transition(d,augmented); N=len(M)
        for t in divisors(60):
            X=powmat(M,t)
            for i in range(N):X[i][i]=(X[i][i]-1)%5
            actual=N-rank5(X)
            expected=fixed_exponent(d,augmented,t)
            assert actual==expected,(d,augmented,t,actual,expected)
            tests+=1
        assert powmat(M,order)==eye(N)
        for p in (2,3,5):
            if order%p==0:assert powmat(M,order//p)!=eye(N)
    for d in range(2,20):
        ordinary=theoretical_order(d,False)
        folded=theoretical_order(d,True)
        expected_folded={2:30,3:12,4:60,5:30}.get(d,60)
        expected_ordinary={2:20,3:30}.get(d,60)
        assert ordinary==expected_ordinary and folded==expected_folded
    assert fixed_exponent(2,True,30)==8
    assert fixed_exponent(3,True,12)==16
    print(f'PASS: {tests} independent rank comparisons, 8 full matrix-order tests, 36 dimension clock tests')

if __name__=='__main__':run()
