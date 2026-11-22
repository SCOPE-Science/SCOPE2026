from math import isqrt, sqrt
from collections import Counter
from itertools import product

def squarefree(n):
    p=2
    while p*p<=n:
        if n%(p*p)==0:return False
        p+=1
    return True

def run(N=150000):
    bmax=int((N+4)**(2/3))+5
    hits=[0]*(N+5)
    for b in range(2,bmax+1):
        if not squarefree(b): continue
        a=1
        while a*a*b*b*b<(N+4)**2:
            r=isqrt(a*a*b*b*b)
            if r<=N+2: hits[r]+=1
            a+=1
    ctr=Counter(tuple(hits[n:n+3]) for n in range(1,N+1))
    for pattern in [(0,0,0),(0,1,0),(1,0,0),(1,0,1),(1,1,0),(1,1,1),(0,2,0)]:
        print('pattern',pattern,'frequency',round(ctr[pattern]/N,6))
    mean=sum(hits[1:N+1])/N
    pair01=sum(hits[n]*hits[n+1] for n in range(1,N+1))/N
    pair02=sum(hits[n]*hits[n+2] for n in range(1,N+1))/N
    print('empirical lag 2 minus lag 1 raw mixed moment',pair02-pair01)
    print('predicted lag 2 minus lag 1',3/(2*sqrt(2))-1)
    print('nonzero observed min',min(sum(t) for t in ctr))
if __name__=='__main__':run()
