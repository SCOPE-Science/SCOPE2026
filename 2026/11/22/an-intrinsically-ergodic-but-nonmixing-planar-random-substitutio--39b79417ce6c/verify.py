#!/usr/bin/env python3
"""Finite exact tests for the hierarchical planar binary block substitution."""
from itertools import product

def lift(base):
    m=len(base)
    for bits in product((0,1), repeat=m*m):
        out=[[None]*(2*m) for _ in range(2*m)]
        for i in range(m):
            for j in range(m):
                a=base[i][j]
                out[2*i][2*j]=a
                out[2*i+1][2*j]=a
                out[2*i][2*j+1]=a
                out[2*i+1][2*j+1]=bits[i*m+j]
        yield tuple(tuple(r) for r in out)

def level(n,root):
    patterns={((root,),)}
    for _ in range(n):
        patterns={b for a in patterns for b in lift(a)}
    return patterns

def parent(b):
    n=len(b)
    assert n%2==0
    out=[]
    for i in range(0,n,2):
        row=[]
        for j in range(0,n,2):
            a=b[i][j]
            if b[i+1][j]!=a or b[i][j+1]!=a:
                return None
            row.append(a)
        out.append(tuple(row))
    return tuple(out)

def false_phase_witness(b,shift):
    si,sj=shift
    n=len(b)
    for i in range(si,n-1,2):
        for j in range(sj,n-1,2):
            if sum(b[i+di][j+dj] for di in (0,1) for dj in (0,1))==2:
                return (i,j)
    return None

def test():
    for n in (0,1,2):
        size=1 << n
        A=level(n,0)
        B=level(n,1)
        expected=2**((4**n-1)//3)
        assert len(A)==len(B)==expected,(n,len(A),len(B),expected)
        assert A.isdisjoint(B)
        if n:
            for root,P in ((0,A),(1,B)):
                for b in P:
                    a=b
                    for _ in range(n):
                        a=parent(a)
                        assert a is not None
                    assert a==((root,),)
    print('Exact levels n=0,1,2: |W_n(a)|=1,2,32 and unique recursive decoding')
    # Independent brute force over all 4x4 arrays, not using the forward generation.
    actual=level(2,0)|level(2,1)
    reverse=set()
    for bits in product((0,1),repeat=16):
        b=tuple(tuple(bits[4*i:4*i+4]) for i in range(4))
        p=parent(b)
        if p is None:continue
        q=parent(p)
        if q is not None:
            reverse.add(b)
    assert actual==reverse and len(actual)==64
    print('All 65,536 four-by-four arrays independently tested: exactly 64 aligned 2-supertiles')
    for root in (0,1):
        blocks=level(2,root)
        for shift in ((0,1),(1,0),(1,1)):
            witnessed=[b for b in blocks if false_phase_witness(b,shift) is not None]
            assert len(witnessed)==8,(root,shift,len(witnessed))
            b=witnessed[0]
            assert false_phase_witness(b,shift)
            print('root',root,'wrong phase',shift,'interior two-two violation: 8/32 blocks')
    for n in (1,2):
        for root in (0,1):
            for b in level(n,root):
                # Repeat b as a 2^n-periodic field, and test the next 2 hierarchy levels
                L=len(b)
                N=4*L
                q=tuple(tuple(b[i%L][j%L] for j in range(N)) for i in range(N))
                p=q
                for _ in range(n+2):
                    p=parent(p)
                    assert p is not None
                assert all(v==root for row in p for v in row)
    print('Every level-1 and level-2 supertile passes higher-level periodic-extension checks')
    return True

if __name__=='__main__':
    test()
    print('PASS')
