#!/usr/bin/env python3
"""Independent dynamic-programming verification of the proposed p=1 formulas.
Only integer arithmetic and standard-library modules are used.
"""
from itertools import product

def proposed(m,h):
    q=h+1; c=h*m-1; u=c//q
    w=[]
    for r in range(m):
        if r<=u-1: v=r*(m+1)+q*m
        elif r==u: v=(m-u)*c
        elif r==u+1: v=(u+1)*(m+1)
        else: v=(m-r)*c+q*m
        w.append(v)
    g=(m+1)*u+(h-1)*m-1+int(m%q==0)
    total=(m+1)*(u*(u+1)//2+1)+c*((m-u)*(m-u-1)//2+1)+q*m*(m-2)
    genus=(2*total-m*(m-1))//(2*m)
    assert (2*total-m*(m-1))%(2*m)==0
    return w,g,genus

def count_coinchange(coins,limit):
    ways=[0]*(limit+1); ways[0]=1
    for a in coins:
        for n in range(a,limit+1):
            ways[n]+=ways[n-a]
    return ways

def run():
    tests=0; residues=0; states=0
    for m in range(3,91):
        for h in range(2,m):
            w,g,genus=proposed(m,h)
            upper=max(w)+2*m
            ways=count_coinchange((m,m+1,h*m-1),upper)
            observed=[None]*m
            for n, count in enumerate(ways):
                if count>=2 and observed[n%m] is None:
                    observed[n%m]=n
            assert observed==w,(m,h,observed,w)
            gf=max(n for n,count in enumerate(ways) if count<=1)
            assert gf==g,(m,h,gf,g)
            nf=sum(count<=1 for count in ways)
            assert nf==genus,(m,h,nf,genus)
            assert all(ways[n]>=2 for n in range(g+1,upper+1))
            tests+=1; residues+=m;states+=upper+1
    print(f'DP PASS: {tests} parameter pairs; {residues} residue thresholds; {states} integer states.')
    return tests

if __name__=='__main__': run()
