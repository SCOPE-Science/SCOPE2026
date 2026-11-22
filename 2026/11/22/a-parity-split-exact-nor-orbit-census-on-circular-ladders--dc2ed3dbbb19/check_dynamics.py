#!/usr/bin/env python3
"""Independent exhaustive evaluation of synchronous open-neighbor NOR on prisms."""

def adjacency(n):
    assert n >= 3
    neighbors = []
    for row in range(2):
        for i in range(n):
            neighbors.append((1 << (row*n + (i-1)%n)) |
                             (1 << (row*n + (i+1)%n)) |
                             (1 << ((1-row)*n + i)))
    return neighbors

def fixed_formula(n):
    luc0, luc1 = 2, 1
    for _ in range(n):
        luc0, luc1 = luc1, luc0 + luc1
    return luc0 + (2 if n % 3 == 0 else -1)

def expected(n):
    m = fixed_formula(n)
    r = (m*m if n%2==0 else fixed_formula(2*n))
    return m, r, (r-m)//2

def check(n):
    masks=adjacency(n)
    nxt=[]
    for x in range(1<<(2*n)):
        y=0
        for v,neighbor_mask in enumerate(masks):
            if not x & neighbor_mask:
                y |= 1<<v
        nxt.append(y)
    fixed=recurrent=cycles3bad=0
    for x,y in enumerate(nxt):
        if y==x: fixed += 1
        z=nxt[y]
        if z==x: recurrent += 1
        if nxt[z]!=y: cycles3bad += 1
    assert not cycles3bad
    assert (fixed,recurrent,(recurrent-fixed)//2)==expected(n), (n,fixed,recurrent,expected(n))
    return n,fixed,recurrent,(recurrent-fixed)//2,len(nxt)

if __name__=='__main__':
    for n in range(3,9):
        print('prism',*check(n))
    print('PASS: all 87,360 states for n=3,...,8 satisfy F^3=F and formulas')
