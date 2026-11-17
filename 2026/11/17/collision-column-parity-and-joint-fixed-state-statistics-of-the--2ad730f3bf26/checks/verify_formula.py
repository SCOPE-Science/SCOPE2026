"""Exact integer-polynomial evaluation of the HPP two-row fixed-point census.

No symbolic algebra package is required; exponents encode (particles, collision columns).
"""
from collections import Counter
from math import comb


def add(*parts):
    out = Counter()
    for p in parts:
        for key, val in p.items():
            out[key] += val
    return {key: val for key, val in out.items() if val}


def mul(x, y):
    out = Counter()
    for (p, k), a in x.items():
        for (q, l), b in y.items():
            out[(p+q, k+l)] += a*b
    return dict(out)


def power(p, n):
    ans={(0,0):1}
    for _ in range(n):
        ans=mul(ans, p)
    return ans


def scale(p, s):
    return {key: s*value for key,value in p.items()}


a={(2,0):1, (4,0):2, (6,0):1}
b={(1,0):1, (3,0):2}
c={(5,0):2, (7,0):1}
d={(0,0):1, (2,0):2}
e={(6,0):2, (8,0):1}
f={(4,0):2}
collision={(4,1):1}


def census(n):
    # Collision-free sector and the even nonempty collision-column sector.
    free=add(scale(power(a,n),4),scale(power(b,n),4),
             scale(power(c,n),4),power(d,n),power(e,n),scale(power(f,n),2))
    active={}
    for k in range(2,n+1,2):
        term=mul(power(a,n-k),power(collision,k))
        active=add(active,scale(term,2*comb(n,k)))
    return add(free,active)

if __name__=='__main__':
    for n in range(2,11):
        poly=census(n)
        count=sum(poly.values())
        closed=5**n+2*4**n+11*3**n+2*2**n
        assert count==closed, (n,count,closed)
        assert all(k%2==0 for (_,k) in poly)
        assert all(poly.get((p,k),0)==poly.get((8*n-p,k),0) for p,k in poly)
        print(f'n={n} total={count} terms={len(poly)}')
        if n<=4:
            for (particles, collisions), number in sorted(poly.items()):
                print(f'occupancy={particles} collision_columns={collisions} count={number}')
