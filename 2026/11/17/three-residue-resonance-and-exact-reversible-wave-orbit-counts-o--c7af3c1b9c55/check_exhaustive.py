#!/usr/bin/env python3
"""Independent direct state-orbit enumeration on the first two graph sizes."""
from math import gcd

def divisors(n):return [d for d in range(1,n+1) if n%d==0]

def fixed_dimension(k,t):
    e=1
    while t%3==0:
        e*=3;t//=3
    two=min(2,e)
    if k%3==0:return 2*(t%4==0)+ (t%2==0)*(min(4,e)+(k-2)*two)+k*two
    if k%3==1:return min(4,e)+k*two+(t%2==0)*(k-1)*two
    return 4*(t%10==0)+k*two+(t%2==0)*(k-1)*two

def period(k):return 9 if k==1 else {0:36,1:18,2:30}[k%3]

def state(x,n):
    a=[]
    for _ in range(2*n):a.append(x%3);x//=3
    return a

def step(a,k):
    n=2*k+1
    cur,old=a[:n],a[n:]
    nxt=[0]*n
    nxt[0]=(sum(cur[1:])-old[0])%3
    for j in range(k):
        u,v=2*j+1,2*j+2
        nxt[u]=(cur[0]+cur[v]-old[u])%3
        nxt[v]=(cur[0]+cur[u]-old[v])%3
    return nxt+cur

def main():
    for k in (2,):
        n=2*k+1; L=period(k)
        actual={d:0 for d in divisors(L)}
        for x in range(3**(2*n)):
            init=state(x,n); a=init[:]
            for d in range(1,L+1):
                a=step(a,k)
                if a==init:
                    assert d in actual
                    actual[d]+=1
                    break
            else:raise AssertionError('nonperiodic state')
        wanted={}
        for d in divisors(L):
            wanted[d]=3**fixed_dimension(k,d)-sum(wanted[e] for e in wanted if d%e==0)
        assert actual==wanted,(k,actual,wanted)
        print('k',k,'total states',3**(2*n),'exact order',L,'primitive populations',actual,'orbit populations',{d:p//d for d,p in actual.items()})
    print('OK exhaustive direct trajectories')
if __name__=='__main__':main()
