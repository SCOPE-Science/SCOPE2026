#!/usr/bin/env python3
"""Direct iteration checks for a one-leaf cycle under synchronous majority."""

def update_cycle(state, n):
    return sum(((((state >> ((i-1) % n)) & 1) + ((state >> ((i+1) % n)) & 1) > 1) or (
        (((state >> ((i-1) % n)) & 1) + ((state >> ((i+1) % n)) & 1) == 1) and ((state >> i) & 1))) << i for i in range(n))

def update_leaf(state, n):
    core=state & ((1<<n)-1)
    leaf=(state>>n)&1
    result=0
    for i in range(n):
        nb=[(core>>((i-1)%n))&1, (core>>((i+1)%n))&1]
        if i==0:
            nb.append(leaf)
        t=sum(nb)
        curr=(core>>i)&1
        bit=int(t>len(nb)//2) if t != len(nb)/2 else curr
        result |=bit<<i
    result |= (core&1)<<n
    return result

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def corr(n):return (4,2,2,-2,0,0)[n%6]

for n in range(3,14):
    nstate=1<<(n+1)
    fixed=period2=0
    for state in range(nstate):
        nextstate=update_leaf(state,n)
        if nextstate==state:
            fixed+=1
        elif update_leaf(nextstate,n)==state:
            period2+=1
    baseline=0
    for state in range(1<<n):
        nxt=update_cycle(state,n)
        if nxt!=state and update_cycle(nxt,n)==state:
            baseline+=1
    formula=2*fib(n-2)+corr(n)
    assert period2==formula, (n,period2,formula)
    assert baseline==2*(n%2==0), (n,baseline)
    print(f'n={n:2d} fixed={fixed:5d} primitive2={period2:5d} cycle_primitive2={baseline:2d} formula={formula:5d}')
print('DIRECT_CHECK_PASS')
