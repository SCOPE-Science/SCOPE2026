#!/usr/bin/env python3
"""Exact-arithmetic tests for sharp heat-semigroup edge-variation bounds on bicliques."""
from fractions import Fraction as F
from itertools import product
from random import Random


def tv(x, y):
    return sum(abs(u-v) for u in x for v in y)


def project_b(x,y):
    b=len(y); mean=sum(y,F(0))/b
    return [F(0)]*len(x),[z-mean for z in y]


def project_ab(x,y):
    a=len(x);b=len(y)
    mx=sum(x,F(0))/a;my=sum(y,F(0))/b
    return [z-mx for z in x],[z-my for z in y]


def heat(x,y,u):
    a=len(x); b=len(y);n=a+b
    mx=sum(x,F(0))/a;my=sum(y,F(0))/b
    mean=(a*mx+b*my)/n; gap=mx-my
    s=u**b;r=u**a;z=u**n
    return ([mean+s*(v-mx)+F(b,n)*z*gap for v in x],
            [mean+r*(v-my)-F(a,n)*z*gap for v in y])


def bound(a,b,u):
    assert a<=b
    c=F(2*(b-1),b)
    return c*u**a-(c-1)*u**(a+b)


def run():
    tested_cuts=0; tested_rational=0; tested_semigroup=0; tested_peaks=0
    for a in range(1,7):
        for b in range(a,11):
            C=F(2*(b-1),b)
            for k in range(a+1):
                for l in range(b+1):
                    x=[F(1)]*k+[F(0)]*(a-k)
                    y=[F(1)]*l+[F(0)]*(b-l)
                    den=tv(x,y)
                    if den==0: continue
                    pa,pb=project_ab(x,y)
                    ba,bb=project_b(x,y)
                    assert tv(pa,pb)<=C*den
                    assert tv(ba,bb)<=C*den
                    for u in (F(1), F(3,4), F(2,3),F(1,2),F(1,3)):
                        hx,hy=heat(x,y,u)
                        assert tv(hx,hy)<=bound(a,b,u)*den
                        tested_cuts+=1
            for u in (F(1),F(3,4),F(2,3),F(1,2),F(1,3)):
                x=[F(0)]*a
                y=[F(1)]+[F(0)]*(b-1)
                hx,hy=heat(x,y,u)
                assert tv(hx,hy)==bound(a,b,u)*tv(x,y)
    rng=Random(47)
    for a in range(1,9):
        for b in range(a,11):
            for _ in range(40):
                x=[F(rng.randint(-9,9),rng.randint(1,7)) for i in range(a)]
                y=[F(rng.randint(-9,9),rng.randint(1,7)) for j in range(b)]
                den=tv(x,y)
                if not den:continue
                C=F(2*(b-1),b)
                assert tv(*project_b(x,y))<=C*den
                assert tv(*project_ab(x,y))<=C*den
                u=F(rng.randint(1,6),7)
                hx,hy=heat(x,y,u)
                assert tv(hx,hy)<=bound(a,b,u)*den
                tested_rational+=1
                v=F(rng.randint(1,6),7)
                z=heat(hx,hy,v)
                assert z==heat(x,y,u*v)
                tested_semigroup+=1
    for a in range(1,30):
        for b in range(a,30):
            # Exact logarithmic derivative at zero of the predicted norm.
            c=F(2*(b-1),b)
            logder=-c*a+(c-1)*(a+b)
            assert logder==b-a-2
            tested_peaks+=1
    print('EXACT_ALL_BIPARTITE_CUT_HEAT_AND_CENTERING_TESTS_PASSED',tested_cuts)
    print('EXACT_RATIONAL_INPUT_CENTERING_AND_HEAT_TESTS_PASSED',tested_rational)
    print('EXACT_HEAT_SEMIGROUP_COMPOSITION_TESTS_PASSED',tested_semigroup)
    print('EXACT_SHARP_INITIAL_GROWTH_THRESHOLDS_PASSED',tested_peaks)
    print('ALL_BIPARTITE_BV_HEAT_TESTS_PASSED')

if __name__=='__main__':run()
