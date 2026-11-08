#!/usr/bin/env python3
"""Elementary exact checks for the four-generator zonotope equality classification.
Requires only Python 3 standard library. The proof in RESULT.md is analytic;
this executable checks finite identities and concrete witnesses, not infinity.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def vec_add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def vec_sum(vectors):
    vectors=list(vectors)
    return tuple(sum(v[i] for v in vectors) for i in range(3))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def zonotope_volume(p):
    return sum(abs(det3(*tri)) for tri in combinations(p,3))


def circumradius_sq_direct(p):
    return max(sum(sum(signs[i]*p[i][j] for i in range(4))**2 for j in range(3))/4
               for signs in product((-1,1),repeat=4))


def balanced(p):
    return [vec_sum(tuple(signs[i]*p[i][j] for j in range(3)) for i in range(4))
            for signs in [(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)]]


def classify(q,v,R2):
    # Exact rational inequalities describing the parameter region Omega_R.
    v2=dot(v,v)
    # -v belongs to conv(q_1,...,q_4) iff q_i.v <= R^2/4 for each i.
    return (4*v2 <= R2 and all(4*dot(x,v)<=R2 for x in q)
            and all(dot(tuple(v[j]-x[j] for j in range(3)),
                        tuple(v[j]-x[j] for j in range(3)))<=R2 for x in q))


def test_exact():
    q=[(Q(1),Q(1),Q(1)),(Q(1),Q(-1),Q(-1)),
       (Q(-1),Q(1),Q(-1)),(Q(-1),Q(-1),Q(1))]
    assert sum(det3(*tri)!=0 for tri in combinations(q,3))==4
    for v in [(Q(0),Q(0),Q(0)),(Q(1,10),Q(0),Q(0)),
              (Q(-1,10),Q(1,20),Q(-1,30))]:
        assert classify(q,v,Q(4))
        p=[vec_add(x,v) for x in q]
        w=balanced(p)
        assert [dot(x,x) for x in w]==[Q(16)]*3
        assert all(dot(w[i],w[j])==0 for i in range(3) for j in range(i+1,3))
        assert zonotope_volume(p)==Q(16)
        assert circumradius_sq_direct(p)==Q(4)
        assert abs(det3(*w))==4*zonotope_volume(p)
    v=(Q(1,10),Q(0),Q(0))
    p=[vec_add(x,v) for x in q]
    lengths_sq=[dot(x,x) for x in p]
    assert len(set(lengths_sq))==2
    assert lengths_sq==[Q(321,100),Q(321,100),Q(281,100),Q(281,100)]
    return lengths_sq


def oriented_generators(p):
    # Signed maximal minors form a kernel vector of the 3-by-4 generator matrix.
    cof=[(-1)**i*det3(*(p[j] for j in range(4) if j!=i)) for i in range(4)]
    return [tuple((-1 if cof[i]<0 else 1)*x for x in p[i]) for i in range(4)]


def test_random():
    rng=Random(394201)
    margins=[]
    for _ in range(4000):
        p=[tuple(Q(rng.randint(-20,20),10) for _ in range(3)) for i in range(4)]
        w=balanced(p)
        rsq=circumradius_sq_direct(p)
        # Universal inequality vol <= 2 R^3; squared to compare rationals exactly:
        V=zonotope_volume(p)
        assert V*V <= 4*rsq*rsq*rsq
        # All balanced sums must be bounded by 4 R^2.
        assert all(dot(x,x)<=4*rsq for x in w)
        # After kernel-based orientation, determinant identity is exact.
        po=oriented_generators(p)
        assert zonotope_volume(po)==V
        assert abs(det3(*balanced(po)))==4*V
        margins.append(float(4*rsq**3-V*V))
    return len(margins),min(margins)


if __name__=='__main__':
    print('Exact witness squared edge lengths:',test_exact())
    print('Exact random rational checks (count, min squared slack):',test_random())
    print('FOUR_GENERATOR_ZONOTOPE_EQUALITY_CHECKS_PASSED')
