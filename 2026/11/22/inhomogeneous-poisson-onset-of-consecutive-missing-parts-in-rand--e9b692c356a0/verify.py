"""Exact integer-partition r-chain mex enumerator and independent checks."""
from math import exp,pi,sqrt
from functools import lru_cache


def partnumbers(N):
    a=[0]*(N+1);a[0]=1
    for j in range(1,N+1):
        for t in range(j,N+1):a[t]+=a[t-j]
    return a


def no_r_chain_start_at_m(N,r,m):
    # Forbid absent blocks with starting index <=m.
    # Each part 1..m+r-1 either occurs at least once or is absent.
    top=m+r-1
    d=[[0]*(N+1) for _ in range(r)];d[0][0]=1
    for j in range(1,top+1):
        sd=[sum(d[k][t] for k in range(r)) for t in range(N+1)]
        nd=[[0]*(N+1) for _ in range(r)]
        for t in range(j,N+1):
            nd[0][t]=sd[t-j]+nd[0][t-j]
        for k in range(1,r):nd[k]=d[k-1]
        d=nd
    vec=[sum(d[k][t] for k in range(r)) for t in range(N+1)]
    for j in range(top+1,N+1):
        for t in range(j,N+1):vec[t]+=vec[t-j]
    return vec[N]


def parts_of(n, cap=None):
    if n==0:
        yield ()
    else:
        for j in range(min(n,cap if cap else n),1-1,-1):
            for p in parts_of(n-j,j):yield (j,)+p


def direct(n,r,m):
    ct=0
    for x in parts_of(n):
        st=set(x)
        if all(any(k+a in st for a in range(r)) for k in range(1,m+1)):
            ct+=1
    return ct


def run():
    checks=0
    for n in range(0,25):
        for r in range(1,5):
            for m in range(1,7):
                a=no_r_chain_start_at_m(n,r,m)
                b=direct(n,r,m)
                assert a==b,(n,r,m,a,b)
                checks+=1
    print('bruteforce comparisons:',checks)
    for r in [2,3,4]:
        alpha=r/(2*(r+1));c=pi/sqrt(6)
        print('r,alpha, Weibull lambda(y=1):',r,alpha,c**r/(r+1))
        for N in [300,1000,3000]:
            m=int(N**alpha)
            p=partnumbers(N)[N]
            a=no_r_chain_start_at_m(N,r,m)
            observed=a/p
            predicted=exp(-(c**r)*(m/(N**alpha))**(r+1)/(r+1))
            print(' n,m,exact survival, Poisson approximation:',N,m,format(observed,'.9f'),format(predicted,'.9f'))
    print('PASS')

if __name__=='__main__':run()
