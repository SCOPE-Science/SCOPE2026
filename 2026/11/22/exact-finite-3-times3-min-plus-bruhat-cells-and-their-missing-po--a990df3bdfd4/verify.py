"""Exact integer checks for 3x3 min-plus upper-triangular double-coset criteria.

The proof for arbitrary real entries is in RESULT.md; this program tests
integer samples, exhaustive small boxes and a boundary counterexample.
"""
from itertools import product
from random import Random


def defects(A):
    (a,b,c),(d,e,f),(g,h,i) = A
    return (d+h-e-g, d+i-f-g, a+h-b-g, a+i-c-g, b+f-c-e)


def belongs(A, permutation):
    d1,d2,d3,d4,d5 = defects(A)
    if permutation == (3,2,1):
        return min(d1,d2,d3,d4)>=0 and (d5>=0 or d2==0 or d3==0)
    if permutation == (2,3,1):
        return d1==0 and min(d2,d3,d4)>=0
    raise ValueError('Only permutations mapping row 3 to column 1 are possible for finite matrices')


def factors(A, permutation):
    (a,b,c),(d,e,f),(g,h,i) = A
    u,v,w = g,h,i
    big_c,big_d = a-g,d-g
    if permutation==(3,2,1):
        if b==big_c+v:
            little_b=max(b-e,c-f)
            y=f
        else:
            little_b=b-e
            y=max(f,c-little_b)
        return (little_b,big_c,big_d),(u,v,w,e,y,c)
    if permutation==(2,3,1):
        return (c-f,big_c,big_d),(u,v,w,b,c,f)
    raise ValueError('Unsupported permutation')


def multiply(B,C,permutation):
    b,c,d=B
    u,v,w,x,y,z=C
    if permutation==(3,2,1):
        return ((c+u,min(b+x,c+v),min(z,b+y,c+w)),
                (d+u,min(x,d+v),min(y,d+w)),(u,v,w))
    if permutation==(2,3,1):
        return ((c+u,min(x,c+v),min(y,b+z,c+w)),
                (d+u,d+v,min(z,d+w)),(u,v,w))
    raise ValueError('Unsupported permutation')


def run():
    rng=Random(20261120)
    for p in ((3,2,1),(2,3,1)):
        for _ in range(100000):
            B=[rng.randint(-8,8) for _ in range(3)]
            C=[rng.randint(-8,8) for _ in range(6)]
            A=multiply(B,C,p)
            assert belongs(A,p)
            assert multiply(*factors(A,p),p)==A
        for _ in range(100000):
            A=tuple(tuple(rng.randint(-8,8) for _ in range(3)) for _ in range(3))
            if belongs(A,p):
                assert multiply(*factors(A,p),p)==A
        for values in product(range(-1,2),repeat=9):
            A=(values[:3],values[3:6],values[6:9])
            if belongs(A,p):
                assert multiply(*factors(A,p),p)==A
        print('PASS cell',p,'100000 forward, 100000 inverse, 19683 exhaustive inputs')
    excluded=((0,-3,-1),(0,-2,-3),(0,0,0))
    assert defects(excluded)==(2,3,3,1,-3)
    assert not belongs(excluded,(3,2,1))
    assert not belongs(excluded,(2,3,1))
    # The four defects involving the bottom-left entry do not suffice.
    for ps,d in (((3,2,1),(1,0,3,0,-2)),((3,2,1),(1,3,0,0,-2)),
                 ((2,3,1),(0,3,3,0,-6))):
        d1,d2,d3,d4,d5=d
        # Realize any four specified defects by choosing the bottom row/first column zero.
        A=((0,-d3,-d4),(0,-d1,-d2),(0,0,0))
        assert defects(A)==d and belongs(A,ps)
        assert multiply(*factors(A,ps),ps)==A
    print('PASS excluded example and all three boundary-wing witnesses')

if __name__=='__main__':
    run()
