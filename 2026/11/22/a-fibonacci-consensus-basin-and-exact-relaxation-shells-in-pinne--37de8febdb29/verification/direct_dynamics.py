#!/usr/bin/env python3
"""Independent full-state majority simulator and terminal-count check."""
from collections import Counter

def update(x,n):
    out=0
    for i in range(1,n):
        a=(x>>((i-1)%n))&1
        b=(x>>i)&1
        c=(x>>((i+1)%n))&1
        if a+b+c>=2:out|=1<<i
    return out

def wall_run_time(x,n):
    edges=[((x>>i)&1)^((x>>((i+1)%n))&1) for i in range(n)]
    r=big=0
    for e in edges:
        if e:r+=1; big=max(big,r)
        else:r=0
    return big//2

def fixed_count_by_t(n,t):
    cnt=0
    for w in range(1<<n):
        if w.bit_count()%2:continue
        r=0
        for j in range(n):
            if (w>>j)&1:
                r+=1
                if r>2*t+1:break
            else:r=0
        else:cnt+=1
    return cnt

for n in range(3,16):
    histogram=Counter();zeros=0
    for state in range(1<<(n-1)):
        x=state<<1
        predicted=wall_run_time(x,n)
        t=0
        while True:
            y=update(x,n)
            if x==y:break
            x=y; t+=1
            assert t<=n
        assert t==predicted,(n,state,t,predicted)
        histogram[t]+=1
        if x==0:zeros+=1
    assert sum(histogram.values())==1<<(n-1)
    for t in range(n//2+1):
        assert sum(histogram[i] for i in range(t+1))==fixed_count_by_t(n,t)
    assert max(histogram)==n//2
    assert histogram[n//2]==(1 if n%2==0 else 2)
    print(f'n={n}: total={1<<(n-1)}, depths={sorted(histogram.items())}, consensus={zeros}')
print('DYNAMICS_OK')
