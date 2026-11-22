#!/usr/bin/env python3
"""Standalone exact-integer checks for the chain-copies comparability spectrum."""
from itertools import product
from math import comb

def convolution(u, v):
    q = [0] * (len(u) + len(v) - 1)
    for i, x in enumerate(u):
        for j, y in enumerate(v):
            q[i+j] += x*y
    return q

def spectrum(a,k):
    p=[1]
    for _ in range(k):
        q=[]
        running=0
        for j in range(len(p)+a):
            if j<len(p):running+=p[j]
            if j-a-1>=0:running-=p[j-a-1]
            q.append(running)
        p=q
    p=[2*x for x in p]
    p[0]-=1
    for j in range(2,a+1):
        p[j]+=k*(j-1)
    return p

def brute(a,k):
    n=a*k
    rel={(u,v) for block in range(k)
         for u in range(block*a,(block+1)*a)
         for v in range(u+1,(block+1)*a)}
    ans=[0]*(n+1)
    for state in product((-1,0,1), repeat=n):
        # state -1 means old below new, +1 means new below old
        L={i for i in range(n) if state[i]==-1}
        U={i for i in range(n) if state[i]==1}
        if any(y in L and x not in L for x,y in rel): continue
        if any(x in U and y not in U for x,y in rel): continue
        if any((x,y) not in rel for x in L for y in U): continue
        ans[len(L)+len(U)]+=1
    return ans

def predicate(a,k):
    return k==1 or a==1 or (a==2) or (k>=5) or (k==4 and a==3)

def run():
    exhaustive=0
    for a in range(1,10):
        for k in range(1,10):
            if a*k>9:continue
            calc=spectrum(a,k)
            direct=brute(a,k)
            assert calc==direct,(a,k,calc,direct)
            exhaustive+=1
    checked=0
    for a in range(1,151):
        for k in range(1,26):
            p=spectrum(a,k)
            good=all(p[i]*p[i]>=p[i-1]*p[i+1] for i in range(1,len(p)-1))
            target=predicate(a,k)
            assert good==target,(a,k,good,target)
            checked+=1
    for a in range(2,70):
        for k in range(5,70):
            B=comb(a+k,k-1)
            f=a**3+4*a*a+a*k*k-3*a*k+7*a-k*k+3*k
            assert 2*(k-1)*B >= k*f
    print('VERIFY_OK', 'direct_spectra',exhaustive, 'coefficient_shape_profiles',checked,
          'boundary_inequalities',68*65)
if __name__=='__main__':run()
