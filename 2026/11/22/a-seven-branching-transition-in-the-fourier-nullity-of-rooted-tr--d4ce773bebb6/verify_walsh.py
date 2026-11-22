#!/usr/bin/env python3
"""Independent exhaustive Walsh check of rooted-tree order-ideal spectra."""

def tree_parents(d, h):
    parents = [-1]
    layer = [0]
    for _ in range(h):
        nxt = []
        for p in layer:
            for _ in range(d):
                nxt.append(len(parents))
                parents.append(p)
        layer = nxt
    return parents


def transform(d, h):
    parents = tree_parents(d, h)
    n = len(parents)
    if n > 16:
        raise ValueError('exact exhaustive demo limited to 16 vertices')
    a = [0] * (1 << n)
    for mask in range(1 << n):
        if all(not (mask & (1 << i)) or (mask & (1 << p))
               for i,p in enumerate(parents) if p >= 0):
            a[mask] = 1
    count_ideals = sum(a)
    width = 1
    while width < len(a):
        for start in range(0, len(a), width*2):
            for k in range(start,start+width):
                x,y=a[k],a[k+width]
                a[k],a[k+width]=x+y,x-y
        width *= 2
    return n, count_ideals, sum(v == 0 for v in a), sum(abs(v) == 1 for v in a)


def exact_recurrence(d, height):
    N = 1
    ideals = 2
    zero = 1
    unit = 0
    for j in range(1,height+1):
        all_child_freqs = 1 << N
        child_ideals = ideals
        child_zero,child_unit=zero,unit
        N = 1+d*N
        ideals = 1+child_ideals**d
        if j % 2:
            zero = 0
            unit = 2*(all_child_freqs**d - (all_child_freqs-child_zero)**d)
        else:
            zero = child_unit**d
            unit = 0
    return N,ideals,zero,unit

if __name__=='__main__':
    for d,h in [(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)]:
        a=transform(d,h)
        b=exact_recurrence(d,h)
        assert a==b, (d,h,a,b)
        print('PASS d=%d h=%d n=%d ideals=%d zero=%d unit=%d'%(d,h,*a))
    print('PASS exhaustive Walsh checks')
