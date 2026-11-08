"""Independent polynomial-basis exact check of power-of-two toroidal adjacency."""
from itertools import product
from math import prod


def rank(cols):
    basis={}
    for v in cols:
        while v:
            h=v.bit_length()-1
            if h in basis:v^=basis[h]
            else:basis[h]=v;break
    return len(basis)


def mul(a,b):
    out=[]
    for v in b:
        q=0
        while v:
            bit=v&-v; q^=a[bit.bit_length()-1]; v-=bit
        out.append(q)
    return out


def adjacency_on_nilpotent_coordinates(shape):
    coords=list(product(*(range(s) for s in shape)))
    ix={x:i for i,x in enumerate(coords)}
    out=[]
    for x in coords:
        bits=0
        for k,L in enumerate(shape):
            # With z=x+1, the genuine shift sum is z^2+z^3+...+z^(L-1).
            for e in range(x[k]+2,L):
                y=list(x);y[k]=e
                bits ^= 1<<ix[tuple(y)]
        out.append(bits)
    return out


def test(shape):
    n=prod(shape); h=max(shape)//2; c=n//h
    a=adjacency_on_nilpotent_coordinates(shape)
    a_power=[1<<j for j in range(n)]
    for k in range(h+1):
        got=rank(a_power)
        expected=c*max(h-k,0)
        assert got==expected,(shape,k,got,expected)
        a_power=mul(a,a_power)
    print(f"shape={shape} rank(A^j)=(N/H)max(H-j,0), H={h}, N/H={c}, checks={h+1}")

if __name__=='__main__':
    for shape in [(4,4),(4,8),(8,8),(4,16),(4,4,4),(4,4,8),(4,4,4,4)]:test(shape)
    print('PASS: independent truncated-polynomial operator and nilpotent Jordan profile')
