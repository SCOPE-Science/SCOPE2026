"""Independent cyclic-word transfer and probabilistic checks for OR circulants."""
from itertools import product
from math import gcd, exp

def mult(A,B):
    n=len(A); k=len(B); m=len(B[0]); R=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(k):
            if A[i][j]:
                for h in range(m):R[i][h]+=A[i][j]*B[j][h]
    return R

def matpow(A,p):
    d=len(A);R=[[int(i==j) for j in range(d)] for i in range(d)]
    while p:
        if p&1:R=mult(R,A)
        A=mult(A,A);p>>=1
    return R

def C(m,t):
    assert 0<=t<m
    M=[[0]*(t+1) for _ in range(t+1)]
    for j in range(t+1):
        M[j][0]+=1
        if j<t:M[j][j+1]+=1
    P=matpow(M,m)
    return 1+sum(P[j][j] for j in range(t+1))

def brute_cyclic(m,t):
    count=1
    for x in range(1,1<<m):
        good=True
        for i in range(m):
            if not any((x>>((i-j)%m))&1 for j in range(t+1)):
                good=False;break
        count+=good
    return count

def main():
    cells=0
    for m in range(2,15):
        for t in range(m):
            a=C(m,t); b=brute_cyclic(m,t)
            assert a==b,(m,t,a,b)
            cells+=1
        assert C(m,0)==2
        assert C(m,m-2)==2**m-m
        assert C(m,m-1)==2**m
    print('PASS transfer versus direct gap enumeration',cells,'cells')
    for g,m in [(3,4),(2,6),(1,10),(4,3)]:
        cum=[C(m,t)**g for t in range(m)]
        hits=[cum[0]]+[cum[t]-cum[t-1] for t in range(1,m)]
        assert sum(hits)==2**(g*m)
        assert hits[-1]==2**(g*m)-(2**m-m)**g
        print('n,g,m',g*m,g,m,'first-entry',hits)
    for g in (1,2,3):
        for h in (6,8,10):
            m=2**h
            for c in (-2,0,2):
                t=h+c-1
                exact=C(m,t)/2**m
                predicted=exp(-2**(-c-1))
                assert abs(exact-predicted)<0.09,(h,c,exact,predicted)
                print('asymptotic m,c,one-coset exact/limit',m,c,round(exact,6),round(predicted,6))
    print('PASS')

if __name__=='__main__':main()
