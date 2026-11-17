"""Standalone finite verification of the one-sided three-tap majority theorem.
No external packages. The proof is independent of this finite check.
"""
from math import gcd
from collections import Counter

def next_state(x,n):
    y=0
    for i in range(n):
        a,b,c=((x>>((i-j)%n))&1 for j in (1,2,3))
        y|=((a+b+c>=2)<<i)
    return y

def cyclic_no_singletons(x,n):
    return all(not (((x>>((i-1)%n))&1)==((x>>((i+1)%n))&1)!=((x>>i)&1)) for i in range(n))

def kcount(d):
    return sum(cyclic_no_singletons(x,d) for x in range(1<<d))

def predicted_fixed(n,t):
    return kcount(gcd(n,2*t)) + (2 if n%2==0 and t%2==0 else 0)

def test(n):
    N=1<<n
    nxt=[next_state(x,n) for x in range(N)]
    periodic=[False]*N
    # Detect recurrent states via a completely independent functional-graph walk.
    cycles=[]
    used=bytearray(N)
    for x in range(N):
        if used[x]:continue
        stack=[];loc={};z=x
        while not used[z] and z not in loc:
            loc[z]=len(stack);stack.append(z);z=nxt[z]
        if z in loc:
            orbit=stack[loc[z]:]
            for y in orbit: periodic[y]=True
            cycles.append(len(orbit))
        for y in stack:used[y]=1
    expected_recurrent=sum(cyclic_no_singletons(x,n) for x in range(N))+(2 if n%2==0 else 0)
    assert sum(periodic)==expected_recurrent,(n,sum(periodic),expected_recurrent)
    for x in range(N):
        alt=(n%2==0 and all(((x>>i)&1)!=((x>>((i+1)%n))&1) for i in range(n)))
        assert periodic[x] == (cyclic_no_singletons(x,n) or alt), (n,x)
    fixed={}
    for t in range(1,n+1):
        fixed[t]=sum(periodic[x] and (lambda y: y==x)(__import__('functools').reduce(lambda z,_:nxt[z],range(t),x)) for x in range(N))
        assert fixed[t]==predicted_fixed(n,t),(n,t,fixed[t],predicted_fixed(n,t))
    cyc=Counter(cycles)
    order=1
    from math import lcm
    for k in cycles:order=lcm(order,k)
    expected_order=n if n%2 else (n//2 if n%4==0 else n)
    assert order==expected_order,(n,order,expected_order)
    if n%4==2: assert n not in cyc,(n,cyc)
    return sum(periodic),order,dict(sorted(cyc.items()))

if __name__=='__main__':
    for n in range(5,15):
        rec,order,cyc=test(n)
        print(f'n={n:2} recurrent={rec:5} global_order={order:2} primitive_orbits={cyc}')
    print('ALL FINITE CHECKS PASSED')
