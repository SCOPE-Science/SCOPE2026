"""Independent enumeration of period-three Greenberg-Hastings states on two cubic ladders."""
from itertools import product

def neighbors(n, twist=False):
    a = [set() for _ in range(2*n)]
    def add(x,y):
        assert x!=y
        a[x].add(y);a[y].add(x)
    for j in range(n):add(j,n+j)
    for j in range(n-1):
        for k in range(2):add(k*n+j,k*n+j+1)
    if twist:
        add(n-1,n)
        add(2*n-1,0)
    else:
        add(n-1,0)
        add(2*n-1,n)
    assert all(len(v)==3 for v in a)
    return a

def next_state(x, a):
    return tuple(2 if v==1 else 0 if v==2 else int(any(x[u]==1 for u in a[i])) for i,v in enumerate(x))

def enumeration(n, twisted):
    a=neighbors(n,twisted)
    local=0;by_sim=0
    for x in product(range(3),repeat=2*n):
        condition=all(any((x[u]-x[i])%3==1 for u in a[i]) for i in range(2*n))
        local+=condition
        if n<=5:
            u=next_state(x,a);v=next_state(u,a);w=next_state(v,a)
            true=(w==x and u!=x)
            assert condition==true,(n,twisted,x)
            by_sim+=true
    return local,by_sim if n<=5 else None

expected={
    3:(72,36),4:(252,48),5:(450,750),6:(1566,2454)
}
for n,(p,m) in expected.items():
    x,y=enumeration(n,False);u,v=enumeration(n,True)
    assert (x,u)==(p,m)
    if n<=5:assert y==p and v==m
    print('n',n,'prism',x,'mobius',u,'direct_map_checked',n<=5)
print('independent direct enumeration: PASS')
