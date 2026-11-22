#!/usr/bin/env python3
"""Finite field checks for irreducible cubic tripotent/square-zero fibers."""
from itertools import product


def gf_mul(a, b, poly, degree):
    out=0
    for _ in range(degree):
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= poly
    return out


def mat_mul(x, y, mul):
    return tuple(tuple(mul(x[i][0],y[0][j]) ^ mul(x[i][1],y[1][j]) ^ mul(x[i][2],y[2][j]) for j in range(3)) for i in range(3))


def mat_add(x, y):
    return tuple(tuple(x[i][j]^y[i][j] for j in range(3)) for i in range(3))


def outer(u, v, mul):
    return tuple(tuple(mul(u[i],v[j]) for j in range(3)) for i in range(3))


def poly_eval_cubic(b,c,d,x,mul):
    return mul(mul(x^b,x)^c,x)^d


def projective_vectors(q,mul):
    # Normalize by the first nonzero coordinate.
    inverses={a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    return [u for u in product(range(q),repeat=3) if any(u) and u[next(i for i,x in enumerate(u) if x)]==1]


def test_field(degree, modulus):
    q=1<<degree
    mul=lambda a,b:gf_mul(a,b,modulus,degree)
    vv=list(product(range(q), repeat=3))
    proj=projective_vectors(q,mul)
    ident=((1,0,0),(0,1,0),(0,0,1))
    zero=((0,0,0),(0,0,0),(0,0,0))
    count_polys=0; counts_by_trace={}; checks=0
    for a,b,c in product(range(q),repeat=3):
        if c==0 or any(poly_eval_cubic(a,b,c,t,mul)==0 for t in range(q)):
            continue
        count_polys += 1
        A=((0,0,c),(1,0,b),(0,1,a))
        got=set()
        # For each projective image line, enumerate all possible functionals annihilating the image.
        for u in proj:
            for v in vv:
                if not any(v) or (mul(u[0],v[0])^mul(u[1],v[1])^mul(u[2],v[2])):
                    continue
                N=outer(u,v,mul)
                assert mat_mul(N,N,mul)==zero
                T=mat_add(A,N)
                if mat_mul(mat_mul(T,T,mul),T,mul)==T:
                    got.add(N)
                checks+=1
        expected=q*q+q+1 if a==0 else 0
        assert len(got)==expected, (q,(a,b,c),len(got),expected)
        counts_by_trace[a]=counts_by_trace.get(a,0)+1
    assert count_polys == (q**3-q)//3
    print('GF(%s): irreducible cubics=%s, trace histogram=%s, projective lines=%s, all decompositions checked, rank-one candidates checked=%s' %(q,count_polys,counts_by_trace,len(proj),checks))

if __name__=='__main__':
    test_field(1,0b11)
    test_field(2,0b111)
    print('IRREDUCIBLE_CUBIC_TRIPOTENT_FIBERS_OK')
