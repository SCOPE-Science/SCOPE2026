"""Checks for a capacity-two Burgers cellular automaton on labelled rings.

Uses only the Python standard library. Finite tests corroborate, but do not
replace, the general max-plus proof in RESULT.md.
"""
from itertools import product
from math import gcd
from collections import Counter

A=((1,1,1),(1,1,0),(1,0,0))

def matrix_multiply(X,Y):
    d=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(d)) for j in range(d)] for i in range(d)]

def trace_power(n):
    M=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(n): M=matrix_multiply(M,A)
    return sum(M[i][i] for i in range(3))

def rule(x):
    n=len(x)
    flow=[min(x[i],2-x[(i+1)%n]) for i in range(n)]
    return tuple(x[i]+flow[(i-1)%n]-flow[i] for i in range(n))

def recurrent_test(x):
    n=len(x)
    sums=[x[i]+x[(i+1)%n] for i in range(n)]
    return all(s<=2 for s in sums) or all(s>=2 for s in sums)

def boundary(n):
    return n // gcd(n,2)-1

def mu(d):
    if d==1:return 1
    z=d; sign=1;p=2
    while p*p<=z:
        if z%p==0:
            z//=p;sign=-sign
            if z%p==0:return 0
            while z%p==0:z//=p
        p+=1
    return -sign if z>1 else sign

def R(n):
    return 2*trace_power(n)-1-(2 if n%2==0 else 0)

def period_orbits(d):
    s=sum(mu(d//e)*R(e) for e in range(1,d+1) if d%e==0)
    assert s % d == 0
    return s//d

def height(x,i):
    n=len(x)
    q,r=divmod(i,n)
    return sum(x[j % n]-1 for j in range(1,r+1))+q*(sum(x)-n)

def height_update(x,t,i):
    return max(height(x,i-t+2*k) for k in range(t+1))-t

count_states=0
for n in range(1,11):
    k=boundary(n)
    states=list(product(range(3),repeat=n))
    recurrent=[]; max_time=0
    for x in states:
        assert sum(rule(x))==sum(x)
        assert all(0<=z<=2 for z in rule(x))
        y=x;t=0
        while not recurrent_test(y):
            y=rule(y);t+=1
            assert t<=k
        max_time=max(max_time,t)
        if recurrent_test(x):
            recurrent.append(x)
            # Action equals an appropriate rigid shift
            f=rule(x)
            low=all(x[i]+x[(i+1)%n]<=2 for i in range(n))
            high=all(x[i]+x[(i+1)%n]>=2 for i in range(n))
            if low:assert f==x[-1:]+x[:-1]
            if high:assert f==x[1:]+x[:1]
        # All configurations arrive on a cycle at the first recurrence step.
        z=y
        for _ in range(n):z=rule(z)
        assert z==y
    assert max_time==k,(n,max_time,k)
    assert len(recurrent)==R(n),(n,len(recurrent),R(n))
    # Independent enumeration of primitive temporal cycles in the recurrent set.
    unseen=set(recurrent);c=Counter()
    while unseen:
        seed=next(iter(unseen));period=0; y=seed
        while True:
            assert y in unseen
            unseen.remove(y);period+=1;y=rule(y)
            if y==seed:break
        assert n%period==0
        c[period]+=1
    assert {d:c.get(d,0) for d in range(1,n+1) if n%d==0}=={
        d:period_orbits(d) for d in range(1,n+1) if n%d==0}
    count_states+=len(states)
    print(f'n={n:2d} states={len(states):6d} recurrent={len(recurrent):5d} '
          f'last_entry={max_time:2d} orbits={dict(sorted(c.items()))}')

# Explicit critical-density sharpness witnesses, including long odd-length clocks.
for n in range(3,20):
    m=n//2
    x=(0,)*m+(1,)+(2,)*m if n%2 else (2,)*m+(0,)*m
    assert len(x)==n and sum(x)==n
    y=x
    for t in range(boundary(n)):
        assert not recurrent_test(y) if t==boundary(n)-1 else True
        y=rule(y)
    assert recurrent_test(y)
print('Sharpness witnesses: all n=3,...,19 checked')

# Height-potential evolution independently checks the nonstandard linearization.
height_cases=0
for n in range(1,8):
    for x in product(range(3),repeat=n):
        y=x
        for t in range(boundary(n)+2):
            for i in range(-n,n+1):
                assert y[i%n]-1 == height_update(x,t,i)-height_update(x,t,i-1)
            y=rule(y);height_cases+=1
print(f'Height-potential checks: {height_cases} time slices')
print('Characteristic polynomial: lambda^3-2lambda^2-lambda+1')
print(f'All tests passed; full direct configuration coverage: {count_states} labelled states')
