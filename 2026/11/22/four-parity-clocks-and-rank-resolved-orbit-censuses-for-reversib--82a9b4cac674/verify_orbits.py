"""Separate direct-state check of small symmetric-design reversible waves."""
from collections import Counter

def design(v):
    # Symmetric (v,v-1,v-2), with diagonal zero and all other entries one.
    return [[int(i != j) for j in range(v)] for i in range(v)]

def image_under_wave(a,v,state):
    # direct coordinate rules on the point/block bipartite graph
    n=2*v; bits=[(state>>i)&1 for i in range(2*n)]
    result=0
    for i in range(v):
        value=(sum(bits[v+j] for j in range(v) if a[i][j])+bits[n+i])%2
        result |= value << i
    for j in range(v):
        value=(sum(bits[i] for i in range(v) if a[i][j])+bits[n+v+j])%2
        result |= value << (v+j)
    for i in range(n):result |=bits[i] << (n+i)
    return result

def primitive_period(n,v,a):
    x=n
    for t in range(1,13):
        x=image_under_wave(a,v,x)
        if x==n:return t
    raise ValueError('not periodic by time 12')

def prediction(v,k,l,rho,t):
    power=t&(-t)
    x=min(2,power);y=min(4,power);z=2*x if t%3==0 else 0
    if k%2==0 and l%2==0:return 2*rho*y+(2*v-4*rho)*x
    if k%2 and not l%2:return v*z
    if not k%2 and l%2:return 2*x+(v-1)*z
    return z+2*(rho-1)*y+(2*v+2-4*rho)*x

for v,rho in [(3,2),(4,4)]:
    a=design(v)
    cycle_population=Counter(primitive_period(s,v,a) for s in range(1<<(4*v)))
    for t in range(1,13):
        empirical=sum(count for d,count in cycle_population.items() if t%d==0)
        expected=2**prediction(v,v-1,v-2,rho,t)
        assert empirical==expected,(v,t,empirical,expected)
    assert sum(cycle_population.values())==2**(4*v)
    print('direct_state_verified',v,dict(sorted(cycle_population.items())))
