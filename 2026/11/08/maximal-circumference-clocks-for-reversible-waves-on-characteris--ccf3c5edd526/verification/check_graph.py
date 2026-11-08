"""Independent GF(2) matrix check of reversible nearest-neighbor waves on small tori."""
from itertools import product
from math import prod


def rank(columns):
    piv = {}
    for col in columns:
        v = col
        while v:
            p = v.bit_length()-1
            if p not in piv:
                piv[p] = v
                break
            v ^= piv[p]
    return len(piv)


def mul(a, b):
    output = []
    for col in b:
        v = 0
        while col:
            bit = col & -col
            v ^= a[bit.bit_length()-1]
            col ^= bit
        output.append(v)
    return output


def ident(n):
    return [1 << j for j in range(n)]


def verify(shape):
    coords = list(product(*(range(s) for s in shape)))
    loc = {x:i for i,x in enumerate(coords)}
    n=len(coords)
    a=[]
    for x in coords:
        bits=0
        for axis,size in enumerate(shape):
            for e in [-1,1]:
                y=list(x); y[axis]=(y[axis]+e)%size
                bits ^= 1 << loc[tuple(y)]
        a.append(bits)
    f=[a[j] | (1<<(n+j)) for j in range(n)]+[1<<j for j in range(n)]
    m=2*n
    g=[f[j]^(1<<j) for j in range(m)]
    h=max(shape)//2
    c=n//h
    gp=ident(m)
    for j in range(0,2*h+1):
        got=rank(gp)
        expected=c*max(2*h-j,0)
        assert got==expected, (shape,j,got,expected)
        gp=mul(g,gp)
    fp=ident(m)
    samples=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for t in range(1,min(2*h+1,17)):
        fp=mul(f,fp)
        v2=(t&-t)
        dim=c*min(v2,2*h)
        assert m-rank([fp[j]^(1<<j) for j in range(m)])==dim,(shape,t)
    # test a maximal-period witness: one single-coordinate pair
    target=ident(m)[0]
    state=target; visited=[]
    for k in range(1,2*h+1):
        col = 0
        for j,one in enumerate(f):
            if state >> j &1: col^=one
        state=col
        if state==target: visited.append(k)
    # Single-basis vector need not be maximal; no assertion required.
    print(f"shape={shape} positions={n} phase_dimension={m} nilpotent_height={2*h} blocks={c} rank_checks={2*h+1} fixed_checks={min(2*h,16)}")


if __name__=='__main__':
    for shape in [(4,4),(4,8),(8,4),(8,8),(4,16),(4,4,4),(4,4,8)]:
        verify(shape)
    print('PASS: graph-matrix ranks, full unipotent Jordan profiles, fixed-point dimensions')
