#!/usr/bin/env python3
"""Independent finite exhaustive and symbolic checks for one-bridge AND ring dynamics."""
from math import gcd,lcm
from itertools import product

def F(a,b,A,B):
    return tuple(A[(i-1)%a] for i in range(a)), tuple((B[-1] & A[0]) if j==0 else B[j-1] for j in range(b))

def model_delay(a,b,A,B):
    L=lcm(a,b)
    deaths=[]
    for j in range(b):
        if not B[j]:continue
        for s in range(L):
            if s%b==(b-1-j)%b and not A[-s%a]:
                deaths.append(s+1);break
    return max(deaths,default=0)

def census_formula(a,b,t):
    g=gcd(a,b);out=1
    for u in range(g):
        aclass=[k for k in range(a) if k%g==u]
        bclass=[j for j in range(b) if (j+1)%g==u]
        total=0
        for w in product((0,1),repeat=len(aclass)):
            aa=dict(zip(aclass,w));allone=all(w)
            safe=0
            for j in bclass:
                visited=[-s%a for s in range(t) if s%b==(b-1-j)%b]
                if allone or any(aa[k]==0 for k in visited):safe+=1
            total+=1<<safe
        out*=total
    return out

def closed_tail(a,b,r):
    g=gcd(a,b);alpha=a//g
    out=1<<b
    for u in range(g):
        ss=0
        for k in range(u,a,g):
            c=sum((j+1)%a==k for j in range(r))
            ss+=1<<(r-c) # numerator for 2^-c, common denom 2^r
        out*=((1<<alpha)-alpha)*(1<<r)+ss
    return out//(1<<r)**g

def full_census(a,b):
    L=lcm(a,b);hist=[0]*(L+1)
    for abits in product((0,1),repeat=a):
        for bbits in product((0,1),repeat=b):
            T=model_delay(a,b,abits,bbits)
            hist[T]+=1
            x=(abits,bbits);orbit_seen={}; t=0
            while x not in orbit_seen:
                orbit_seen[x]=t;x=F(a,b,*x);t+=1
            assert orbit_seen[x]==T,(a,b,abits,bbits,orbit_seen[x],T)
    return hist

def main():
    cases=0
    for a in range(2,7):
        for b in range(2,7):
            h=full_census(a,b);cum=0;L=lcm(a,b);g=gcd(a,b)
            for t,x in enumerate(h):
                cum+=x
                assert cum==census_formula(a,b,t),(a,b,t,cum,census_formula(a,b,t))
            for r in range(b+1):
                assert sum(h[:L-r+1])==closed_tail(a,b,r),(a,b,r)
            assert h[-1]==2**(a+b-a//g-1),(a,b,h[-1])
            print('PASS',a,b,'L',L,'recurrent',h[0],'terminal',h[-1])
            cases+=1
    print('BRUTE_SHELLS_OK',cases)
if __name__=='__main__':main()
