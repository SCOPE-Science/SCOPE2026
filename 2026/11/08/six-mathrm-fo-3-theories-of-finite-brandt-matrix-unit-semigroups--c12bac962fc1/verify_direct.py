#!/usr/bin/env python3
"""Independent concrete-state check of exact FO^3 rank profiles for B_1..B_6.
Each tuple is a genuine triple of named semigroup elements, not an orbit.
The refinement uses existential availability sets, never multiplicities.
"""
from itertools import product

def model(n):
    elements = tuple(range(n*n+1))
    def multiply(x,y):
        if x == 0 or y == 0:
            return 0
        a,b=divmod(x-1,n)
        c,d=divmod(y-1,n)
        return 1+a*n+d if b==c else 0
    table=tuple(tuple(multiply(i,j) for j in elements) for i in elements)
    return elements,table

def atomic(t,mul):
    v=(0,)+t
    return (tuple(v[a]==v[b] for a in range(4) for b in range(4)),
            tuple(mul[x][y]==z for x in v for y in v for z in v))

def normalize(signatures):
    types={a:i for i,a in enumerate(sorted(set(signatures.values())))}
    return {key:types[v] for key,v in signatures.items()}

def main():
    values = {}
    tuples={}
    for n in range(1,7):
        domain,mul=model(n)
        tuples[n]=tuple(product(domain,repeat=3))
        for t in tuples[n]:
            values[n,t]=atomic(t,mul)
    colors=normalize(values)
    root=(0,0,0)
    expected=[1,2,3,5,6]
    for rank in range(12):
        keys=[colors[n,root] for n in range(1,7)]
        groups=len(set(keys))
        print(f'rank={rank} theories={groups} root_colors={keys} state_colors={len(set(colors.values()))}')
        assert groups==expected[rank]
        nxt={}
        for n in range(1,7):
            domain=range(n*n+1)
            for t in tuples[n]:
                signature=(colors[n,t],tuple(tuple(sorted({colors[n,t[:i]+(a,)+t[i+1:]] for a in domain})) for i in range(3)))
                nxt[n,t]=signature
        new=normalize(nxt)
        if len(set(new.values()))==len(set(colors.values())):
            assert rank==4
            print('stable_rank=4')
            break
        colors=new
    else:
        raise AssertionError('Refinement did not stabilize')
    print('DIRECT_CHECK_PASS')

if __name__=='__main__':main()
