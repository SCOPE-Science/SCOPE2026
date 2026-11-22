"""Exact rational checks for a three-population, stage-specific ecological map.

No external packages required; run `python verify.py`.
"""
from fractions import Fraction as Q
from itertools import product


def update(h, x, y, r, Rj, Ra):
    new_h = r*h / ((1+x)*(1+y+(r-1)*h))
    new_x = Rj*x*new_h
    new_y = Ra*y*h/(1+y)
    return (new_h, new_x, new_y)


def wedge_equilibrium(r, Rj, Ra):
    return (Q(1)/Rj, r*Rj/(Ra+r-1)-1, Ra/Rj-1)


def check():
    count = 0
    for r, Rj, Ra in product((Q(3,2), Q(2), Q(3), Q(5)),
                             (Q(5,4), Q(2), Q(4)),
                             (Q(1,2), Q(3,2), Q(5,2), Q(3), Q(5), Q(9))):
        h,x,y = Q(1,3), Q(2,7), Q(3,11)
        for t in range(8):
            hn,xn,yn = update(h,x,y,r,Rj,Ra)
            assert xn == Rj*x*hn
            q = h*y/x
            qn = hn*yn/xn
            assert qn == (Ra/Rj)*q/(1+y)
            assert 0 < hn <= 1
            assert 0 < xn <= Rj
            h,x,y = hn,xn,yn
            count += 1
        he,xe,ye = wedge_equilibrium(r,Rj,Ra)
        admissible = Rj>1 and Rj < Ra < 1+r*(Rj-1)
        assert (he > 0 and xe > 0 and ye > 0) == admissible
        if admissible:
            assert update(he,xe,ye,r,Rj,Ra) == (he,xe,ye)
    assert wedge_equilibrium(Q(3),Q(2),Q(3)) == (Q(1,2),Q(1,5),Q(1,2))
    assert update(Q(1,2),Q(1,5),Q(1,2),Q(3),Q(2),Q(3)) == (Q(1,2),Q(1,5),Q(1,2))
    # Check the generic non-Beverton--Holt algebra with a monotone, positive
    # density-dependent response satisfying its carrying-capacity normalization.
    # F(z)=2/(1+z^2); F(1)=1 and F(z)*z<=1 on (0,1].
    count_generic = 0
    for Rj,Ra in product((Q(1,2),Q(2),Q(4)),(Q(1,2),Q(1),Q(3))):
        h,x,y=Q(1,3),Q(2,7),Q(1,5)
        for _ in range(6):
            z=h/(1+y)
            G=Q(2)*z/(1+z*z)
            hn=G/(1+x)
            xn=Rj*x*G/(1+x)
            yn=Ra*y*h/(1+y)
            assert xn==Rj*x*hn
            assert hn*yn/xn==(Ra/Rj)*(h*y/x)/(1+y)
            assert hn<=1 and xn<=Rj
            h,x,y=hn,xn,yn
            count_generic += 1
    print(f'PASS: {count} Beverton--Holt rational transitions; '
          f'{count_generic} generic-response rational transitions; '
          'positive-equilibrium wedge and witness verified')

if __name__ == '__main__':
    check()
