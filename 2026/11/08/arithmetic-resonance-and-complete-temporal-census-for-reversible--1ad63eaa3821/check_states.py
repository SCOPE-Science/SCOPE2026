"""Independent direct configuration iteration for small wheel waves.
Run: python check_states.py. Finite evidence only.
"""
from collections import Counter
from math import gcd, lcm

def expected_order(n):
    if n % 2: return lcm(6,n)
    h = n & -n
    return 4*n if h == 2 else (2*n if h == 4 else n)

def exponent(n, t):
    v=1
    while t%(2*v)==0: v*=2
    d=gcd(n,t)
    if n%2: return 2*(d-1)+(2*min(v,2) if t%3==0 else 0)
    h=n&-n
    if h==2: return 2*d+min(v,6)-2*min(v,2)
    if h==4: return 2*d+min(v,6)+2*min(v,2)-2*min(v,4)
    return 2*d+min(v,2)

def update(state,n):
    m=n+1
    lowmask=(1<<m)-1
    u=state&lowmask
    v=state>>m
    hub=u&1
    rim=u>>1
    nbr= rim.bit_count()&1
    for j in range(n):
        val=hub^((rim>>((j-1)%n))&1)^((rim>>((j+1)%n))&1)
        nbr|=val<<(1+j)
    return (nbr^v)|(u<<m)

for n in range(3,9):
    m=n+1; L=expected_order(n)
    periodic=Counter()
    for state in range(1<<(2*m)):
        x=state
        for t in range(1,L+1):
            x=update(x,n)
            if x==state:
                periodic[t]+=1
                break
        else: raise AssertionError((n,state,'no return at global order'))
    for t in range(1,L+1):
        if L%t==0:
            actual=sum(count for p,count in periodic.items() if t%p==0)
            assert actual==2**exponent(n,t), (n,t,actual,2**exponent(n,t))
    assert sum(periodic.values()) == 2**(2*m)
    print(f'n={n} states={2**(2*m)} order={L} primitive_periods={sorted(periodic.items())}')
print('PASS direct iteration: 349440 labelled paired states, all return times and divisor fixed-point counts')
