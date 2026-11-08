#!/usr/bin/env python3
"""Exact rational certificate for four positive fixed points of a two-species
mixture Beverton-Holt competition map. Requires Python standard library only.
"""
from fractions import Fraction as F

P1 = ((F(63,50), F(1579,50), F(9,100)),
      (F(17,25), F(2,25), F(731,100)))
P2 = ((F(253,100), F(12717,100), F(13,25)),
      (F(291,50), F(1774,25), F(9549,100)))

def phi(P,x,y):
    return sum((r/(1+a*x+b*y) for r,a,b in P), F(0))

# x, lower and upper rational bounds for the unique positive nullcline point y=Y(x).
TESTS = [
    (F(1,10000), F(324927,100000), F(324928,100000), -1),
    (F(1,200), F(182960,100000), F(182961,100000), +1),
    (F(1,50), F(25319,100000), F(25320,100000), -1),
    (F(3,50), F(2715,100000), F(2716,100000), +1),
    (F(9,100), F(62,100000), F(63,100000), -1),
]

def main():
    for i,(x,lo,hi,sgn) in enumerate(TESTS):
        assert F(0)<x and F(0)<lo<hi
        assert phi(P1,x,lo)>1, (i, 'lower nullcline bound')
        assert phi(P1,x,hi)<1, (i, 'upper nullcline bound')
        # Phi_2 is decreasing in y; a sign at the worst endpoint certifies it on all [lo,hi].
        cert=phi(P2,x,hi)-1 if sgn>0 else 1-phi(P2,x,lo)
        assert cert>F(1,1000), (i,'sign separation',cert)
        print('probe',i+1,'x=',x,'lo=',lo,'hi=',hi,'sign',sgn,'gap_gt_1/1000', cert>F(1,1000))
    assert all(TESTS[i][0]<TESTS[i+1][0] for i in range(4))
    a,b=P1
    det=a[1]*b[2]-a[2]*b[1]
    assert det!=0 and a[0]>0 and b[0]>0
    # Q1 = (U-rI)(V-rS)-rS*rI is an irreducible rectangular hyperbola
    # in the independent affine coordinates U=1+a*x+b*y, V=1+c*x+d*y.
    # Q2 cannot share that factor since it is nonzero at the 5 probed
    # points of Q1. The two conics therefore have at most four intersections
    # (Bezout). The four alternating signs give at least four.
    print('VERIFY_OK: five exact sign brackets certify exactly four positive fixed points')

if __name__ == '__main__':
    main()
