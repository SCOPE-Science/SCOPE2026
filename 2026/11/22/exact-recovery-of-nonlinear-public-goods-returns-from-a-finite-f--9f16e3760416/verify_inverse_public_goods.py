#!/usr/bin/env python3
"""Exact and numerical checks for a public-goods fixation-profile inverse theorem.
All random test profiles and observations are synthetic mathematical examples.
"""
from fractions import Fraction as Q
from math import comb, exp, log, isclose
from random import Random

def choose(a,b):
    return comb(a,b) if a>=0 and 0<=b<=a else 0

def matrix(N,n):
    den=choose(N-1,n-1)
    return [[Q(j,n*den)*(choose(i-1,j-1)*choose(N-i,n-j)-choose(i,j)*choose(N-i-1,n-1-j))
             for j in range(1,n+1)] for i in range(1,N)]

def payoffs(N,n,r):
    den=choose(N-1,n-1)
    ans=[]
    for i in range(1,N):
        pc=-Q(1); pd=Q(0)
        for j in range(0,n):
            pc+=Q(choose(i-1,j)*choose(N-i,n-1-j),den)*Q(j+1,n)*r[j]
            if j:
                pd+=Q(choose(i,j)*choose(N-i-1,n-1-j),den)*Q(j,n)*r[j-1]
        ans.append(pc-pd)
    return ans

def recover(N,n,delta):
    a=matrix(N,n)
    r=[]
    for i in range(n):
        r.append((delta[i]-sum(a[i][j]*r[j] for j in range(i)))/a[i][i])
    return r

def fixation(N,n,r,beta):
    diffs=payoffs(N,n,r)
    weights=[1.]
    for v in diffs:weights.append(weights[-1]*exp(-beta*float(v)))
    den=sum(weights)
    h=[0.]
    for w in weights: h.append(h[-1]+w/den)
    return h

def checks():
    count=0; random=Random(1729)
    for N in range(3,14):
      for n in range(2,N):
        A=matrix(N,n)
        for i in range(n):
            assert all(A[i][j]==0 for j in range(i+1,n))
            diag=Q(i+1,n)*Q(choose(N-i-2,n-i-1),choose(N-1,n-1))
            assert A[i][i]==diag and diag>0
        assert A[n-1][n-1]==Q(1,choose(N-1,n-1))
        for k in range(3):
            r=[Q(random.randint(1,30),random.randint(1,7)) for _ in range(n)]
            ds=payoffs(N,n,r)
            assert ds==[sum(A[i][j]*r[j] for j in range(n))-1 for i in range(N-1)]
            assert recover(N,n,[v+1 for v in ds[:n]])==r
            assert sum(ds)==Q(N-n,n)*r[-1]+1-N
            beta=0.11+0.02*k
            h=fixation(N,n,r,beta)
            for i in range(1,n+1):
                L=-log((h[i+1]-h[i])/(h[i]-h[i-1]))/beta
                assert isclose(L,float(ds[i-1]),rel_tol=5e-8,abs_tol=5e-8)
            fc=h[1]/(h[1]+1-h[N-1])
            exact=1/(1+exp(-beta*float(Q(N-n,n)*r[-1]+1-N)))
            assert isclose(fc,exact,rel_tol=3e-8,abs_tol=3e-8)
            count+=1
    N,n=4,3
    A=matrix(N,n)
    assert A==[[Q(1,9),Q(0),Q(0)],[-Q(1,9),Q(2,9),Q(0)],[Q(0),-Q(2,9),Q(1,3)]]
    assert payoffs(4,3,[Q(1),Q(1),Q(9)])==[Q(-8,9),Q(-8,9),Q(16,9)]
    # Nonzero selection and exact, rational four-person fixation certificate.
    assert payoffs(4,3,[Q(18),Q(9),Q(9)])==[Q(1),Q(-1),Q(0)]
    weights=[Q(1),Q(1,2),Q(1),Q(1)] # exp(-beta cumulative payoff), beta=log 2
    H=[Q(0)]; total=sum(weights)
    for w in weights:H.append(H[-1]+w/total)
    assert H==[Q(0),Q(2,7),Q(3,7),Q(5,7),Q(1)]
    for i,gamma in enumerate([Q(1,2),Q(2),Q(1)],1):
        assert (H[i+1]-H[i])==gamma*(H[i]-H[i-1])
    assert payoffs(4,3,[Q(9),Q(9),Q(9)])==[Q(0),Q(0),Q(0)]
    for N in range(2,14):
        for k in range(3):
            r=[Q(random.randint(1,30),random.randint(1,7)) for _ in range(N)]
            assert payoffs(N,N,r)==[Q(-1)]*(N-1)
    print('PASS:',count,'rational/numerical profile-and-recovery cases; exact 4-person certificate; 36 full-group degeneracy cases')
if __name__=='__main__':checks()
