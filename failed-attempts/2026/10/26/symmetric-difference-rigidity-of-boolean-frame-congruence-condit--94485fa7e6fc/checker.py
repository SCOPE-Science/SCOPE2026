#!/usr/bin/env python3
"""Independent finite diagnostics for Boolean quasi-identity and join preservation."""
from itertools import product

def is_qi(f, n):
    m=1<<n
    for x in range(m):
        for y in range(m):
            for z in range(m):
                if ((x^y) & ~z)==0 and ((f[x]^f[y]) & ~f[z]):
                    return False, (x,y,z)
    return True, None

def is_join(f, n):
    m=1<<n
    return all(f[x|y] == (f[x]|f[y]) for x in range(m) for y in range(m))

def from_coordinates(coords,n):
    out=[]
    for x in range(1<<n):
        v=0
        for j,p in enumerate(coords):
            if p == (1<<n) or (p & x): v |= 1<<j
        out.append(v)
    return tuple(out)

def verify(n):
    m=1<<n
    all_maps={from_coordinates(p,n) for p in product(range(m+1),repeat=n)}
    assert len(all_maps)==(m+1)**n
    for f in all_maps:
        assert is_qi(f,n)[0]
        assert is_join(f,n)
    if n<=2:
        qi=set(); join=set()
        for f in product(range(m),repeat=m):
            if is_qi(f,n)[0]: qi.add(f)
            if is_join(f,n): join.add(f)
        assert qi==join==all_maps
    by_c = {}
    for f in all_maps:
        by_c[f[0]]=by_c.get(f[0],0)+1
    for c,k in by_c.items():
        assert k == 2**(n*(n-c.bit_count()))
    assert len(by_c)==m
    print('n=',n,'total=',len(all_maps),'normal=',by_c.get(0,0),'fixed_bottom_distribution=', sorted((c.bit_count(),k) for c,k in by_c.items()))

for n in (1,2,3):
    verify(n)

n=3; full=7; distinguished=5; f=tuple(full if x==distinguished else x for x in range(1<<n))
assert (distinguished^1)==4
assert f[distinguished]^f[1]==6
assert f[4]==4
assert not is_qi(f,n)[0]
assert not is_join(f,n)
print('explicit_example_violation',(distinguished,1,4), 'lhs',f[distinguished]^f[1], 'rhs',f[4]);print('ALL_CHECKS_OK')
