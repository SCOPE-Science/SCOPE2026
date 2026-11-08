#!/usr/bin/env python3
"""Direct multiplication checks of idempotent-commutant rank enumerators.

No symbolic formula is used to test whether two partial maps commute.
"""
from itertools import permutations
from math import comb, gcd, lcm


def compose(p, q):
    """First p, then q, -1 denoting undefined."""
    return tuple(-1 if x == -1 else q[x] for x in p)


def full_compose(p, q):
    return tuple(q[x] for x in p)


def cyclic(n):
    return [tuple((i + a) % n for i in range(n)) for a in range(n)]


def elementary_two():
    return [tuple(i ^ a for i in range(4)) for a in range(4)]


def symmetric_three_regular():
    elements = list(permutations(range(3)))
    assert len(elements) == 6
    return [tuple(elements.index(full_compose(g, h)) for h in elements) for g in elements]


def dihedral_four_regular():
    # D_8 as permutations of a four-point square.
    generators = [tuple((i+1) % 4 for i in range(4)), tuple((-i) % 4 for i in range(4))]
    elements = {tuple(range(4))}
    while True:
        more = elements | {full_compose(p,g) for p in elements for g in generators}
        if more == elements: break
        elements = more
    elements = sorted(elements)
    assert len(elements) == 8
    return [tuple(elements.index(full_compose(g,h)) for h in elements) for g in elements]


def permutation_order(p):
    n=len(p); visited=set(); ans=1
    for i in range(n):
        if i in visited:continue
        j=i; count=0
        while j not in visited:
            visited.add(j); j=p[j]; count+=1
        ans=lcm(ans,count)
    return ans


def convolve(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def cycle_polynomial(l):
    out=[comb(l,j)*2**(l-j) for j in range(l+1)]
    out[-1]+=1
    return out


def predicted(elements):
    n=len(elements)
    result=[2**n*comb(n,r) for r in range(n+1)]
    for p in elements:
        k=permutation_order(p)
        if k==1:continue
        assert n%k==0
        poly=[1]
        for _ in range(n//k):poly=convolve(poly,cycle_polynomial(k))
        for r in range(1,n+1):result[r]+=poly[r]
    return result


def recover_order_profile(elements):
    n=len(elements)
    p=predicted(elements)
    baseline=[2**n*comb(n,r) for r in range(n+1)]
    for r in range(1,n+1): baseline[r]+=(n-1)*comb(n,r)*2**(n-r)
    residual=[p[r]-baseline[r] for r in range(n+1)]
    found={}
    for order in range(2,n+1):
        if n%order:continue
        plus=[1]
        for _ in range(n//order):plus=convolve(plus,cycle_polynomial(order))
        base=[comb(n,r)*2**(n-r) for r in range(n+1)]
        h=[plus[r]-base[r] for r in range(n+1)]
        assert all(h[r]==0 for r in range(order))
        assert h[order]==(n//order)*2**(n-order)
        count=residual[order]//h[order]
        assert residual[order]%h[order]==0
        assert count>=0
        found[order]=count
        for r in range(n+1):residual[r]-=count*h[r]
    assert all(x==0 for x in residual)
    real={i:sum(permutation_order(p)==i for p in elements) for i in found}
    assert found==real,(found,real)
    return found


def direct(elements):
    n=len(elements)
    inverse_restrictions=[tuple([-1]*n)]
    for p in elements:
        for mask in range(1,1<<n):
            inverse_restrictions.append(tuple(p[i] if mask>>i&1 else -1 for i in range(n)))
    assert len(set(inverse_restrictions))==len(inverse_restrictions)
    result=[0]*(n+1)
    for mask in range(1<<n):
        e=tuple(i if mask>>i&1 else -1 for i in range(n))
        for s in inverse_restrictions:
            if compose(e,s)==compose(s,e):
                result[sum(x>=0 for x in s)]+=1
    return result


def main():
    groups=[('cyclic '+str(n),cyclic(n)) for n in range(1,8)]
    groups += [('Klein four',elementary_two()),('S3',symmetric_three_regular()),('D8',dihedral_four_regular())]
    for label,elements in groups:
        p=predicted(elements); d=direct(elements)
        assert p==d,(label,p,d)
        recover_order_profile(elements)
        print('DIRECT_OK',label,p)
    for n in range(1,151):
        got=predicted(cyclic(n))
        assert got[0]==2**n
        assert got[1]==n*(n+1)*2**(n-1)
        assert got[n]==2**n+sum(2**gcd(n,a) for a in range(1,n))
        assert sum(got)==4**n+sum((3**(n//gcd(n,a))+1)**gcd(n,a)-2**n for a in range(1,n))
    print('IDENTITIES_OK cyclic 1..150')
    print('VERIFY_OK')

if __name__=='__main__':main()
