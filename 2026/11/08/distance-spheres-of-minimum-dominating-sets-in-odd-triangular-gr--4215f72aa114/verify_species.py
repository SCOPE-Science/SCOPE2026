#!/usr/bin/env python3
"""Independent symbolic combinatorial-component recurrence for distance spheres."""
from math import comb, factorial

def add(p, q):
    z = dict(p)
    for d, c in q.items():
        z[d] = z.get(d, 0)+c
    return z

def shift_scale(p, shift, scale):
    return {d+shift: c*scale for d, c in p.items()}

def polynomials(maxk):
    cycle = [{0: 1}]
    for m in range(1, maxk+1):
        ans = dict(cycle[m-1])  # Pair containing atom 1 is unchanged.
        for r in range(2, m+1):
            ways = comb(m-1, r-1)*2**(r-1)*factorial(r-1)
            ans = add(ans, shift_scale(cycle[m-r], r+1, ways))
        cycle.append(ans)
    result = []
    for k in range(maxk+1):
        ans = {}
        for r in range(k+1):
            ways = comb(k, r)*2**r*factorial(r)
            ans = add(ans, shift_scale(cycle[k-r], r, ways))
        result.append(ans)
    return result

def double_factorial_odd(k):
    result = 1
    for j in range(1,k+1):
        result *= 2*j+1
    return result

def antipodes(k):
    h=k//2
    if k%2 == 0:
        return factorial(k)//factorial(h)
    return factorial(k)*(6+4*h)//(3*factorial(h))

if __name__=='__main__':
    polys = polynomials(12)
    for k in range(1,13):
        p=polys[k]
        diameter = k+k//2
        assert max(p) == diameter
        assert p[diameter] == antipodes(k)
        assert sum(p.values()) == double_factorial_odd(k)
        assert p.get(1,0) == 2*k
        if k<=5:
            print('k=', k, 'polynomial coefficients=', [p.get(j,0) for j in range(diameter+1)])
        else:
            print('k=', k, 'total=', sum(p.values()), 'diameter=', diameter, 'antipodes=', p[diameter])
    print('COMPONENT_RECURRENCE_PASS')
