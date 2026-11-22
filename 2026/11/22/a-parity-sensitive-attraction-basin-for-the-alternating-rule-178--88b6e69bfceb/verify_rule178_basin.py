#!/usr/bin/env python3
"""Finite independent orbit and run-word checks for fixed-zero-boundary Rule 178."""

def step(x, n):
    y=0
    for i in range(n):
        left=((x>>(i-1))&1) if i else 0
        center=(x>>i)&1
        right=((x>>(i+1))&1) if i+1<n else 0
        y |= ((left | right) if center==0 else (left & right)) << i
    return y

def language(x, n):
    runs=[]
    for i in range(n):
        b=(x>>i)&1
        if runs and runs[-1][0]==b:runs[-1][1]+=1
        else:runs.append([b,1])
    if len(runs)==1:return runs[0][0]==1 and n%2==1
    return all(length%2 for bit,length in runs[1:-1]) and all(
        bit==0 or length%2==1 or length==2 for bit,length in (runs[0],runs[-1]))

def coeffs(max_n):
    # Reduced exact rational generating function, derived from the run decomposition.
    numerator=[0,1,1,2,2,-5,-1,1,1]
    denominator=[1,-1,-3,3,1,-1]
    a=[]
    for n in range(max_n+1):
        v=(numerator[n] if n<len(numerator) else 0)
        v-=sum(denominator[k]*a[n-k] for k in range(1,min(n,5)+1))
        a.append(v)
    return a

def graph_check(n):
    count=1<<n
    nxt=[step(x,n) for x in range(count)]
    alt=sum(1<<i for i in range(1,n,2))
    other=alt^(count-1)
    assert nxt[alt]==other and nxt[other]==alt
    basin=bytearray([255])*count
    basin[alt]=basin[other]=1
    basin[0]=0
    for seed in range(count):
        if basin[seed]!=255:continue
        trail=[]; seen={};x=seed
        while basin[x]==255 and x not in seen:
            seen[x]=len(trail);trail.append(x);x=nxt[x]
        if basin[x]!=255:val=basin[x]
        else:
            # This orbit is recurrent but is not the distinguished alternating pair.
            val=0
        for y in trail:basin[y]=val
    for x in range(count):
        assert basin[x]==language(x,n),(n,x,basin[x],language(x,n))
    return sum(basin)

def check():
    a=coeffs(100)
    fib=[0,1];lucas=[2,1]
    for n in range(2,101):
        fib.append(fib[-1]+fib[-2]);lucas.append(lucas[-1]+lucas[-2])
    for n in range(4,101):
        if n%2==0:expected=2*lucas[n]-2
        elif n==5:expected=21
        else:expected=2*lucas[n]+fib[n-6]-2
        assert a[n]==expected,(n,a[n],expected)
    assert a[3]==7
    total=0
    for n in range(3,19):
        observed=graph_check(n)
        assert observed==a[n],(n,observed,a[n])
        total+=1<<n
        print(f'n={n} basin={observed} PASS')
    assert total==524280
    print('ALL_RUN_BASIN_CHECKS_PASSED states=%d algebra_n=3..100'%total)

if __name__=='__main__':check()
