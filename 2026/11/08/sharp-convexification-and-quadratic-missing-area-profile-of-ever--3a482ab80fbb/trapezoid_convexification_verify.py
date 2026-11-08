"""Exact-rational spot checks for convexification of trapezoid vertex sets.

Run with Python 3: python trapezoid_convexification_verify.py
The universal result is proved in RESULT.md; finite checks are corroboration only.
"""
from fractions import Fraction as F


def inside_trapezoid(x, y, t):
    return F(0) <= y <= F(1) and abs(x) <= F(1) - (F(1)-t)*y


def actual_membership(x, y, t, lam):
    beta=lam/(1+lam)
    vertices=[(-F(1),F(0)),(F(1),F(0)),(-t,F(1)),(t,F(1))]
    return any(inside_trapezoid((x-(1-beta)*vx)/beta,
                                (y-(1-beta)*vy)/beta, t)
               for vx,vy in vertices)


def predicted_membership(x,y,t,lam):
    if t == 1 or lam >= 2-t:
        return True
    beta=lam/(1+lam)
    y0=(2*beta-1)/(1-t)
    y1=1-beta
    return not(y0 < y < y1 and abs(x) < (1-t)*(y-y0))


def verify():
    count=0
    for t in [F(1,7),F(1,4),F(1,2),F(2,3),F(4,5),F(1)]:
        for lam in [F(1), (F(1)+(2-t))/2, 2-t, (2-t)+F(1,5)]:
            for iy in range(33):
                y=F(iy,32)
                for ix in range(-32,33):
                    x=F(ix,32)
                    if not inside_trapezoid(x,y,t):
                        continue
                    got=actual_membership(x,y,t,lam)
                    predicted=predicted_membership(x,y,t,lam)
                    assert got==predicted, (t,lam,x,y,got,predicted)
                    count+=1
            # Confirm a counterexample at every tested strictly subcritical lambda.
            if t < 1 and lam < 2-t:
                beta=lam/(1+lam)
                y0=(2*beta-1)/(1-t)
                y1=1-beta
                yw=(y0+y1)/2
                assert inside_trapezoid(F(0),yw,t)
                assert not actual_membership(F(0),yw,t,lam)
                count+=1
    for t in [F(1,7),F(1,4),F(1,2),F(2,3),F(4,5)]:
        for lam in [F(1),(F(1)+2-t)/2,2-t]:
            b=lam/(1+lam)
            top=1-b
            bottom=(2*b-1)/(1-t)
            height=top-bottom
            assert height>=0
            # Area from integrating the exact cross-section gap, twice the halfwidth.
            integral_gap_area=(1-t)*height*height
            area_formula=(2-t-lam)**2/((1-t)*(1+lam)**2)
            assert integral_gap_area==area_formula
            assert area_formula/(1+t)==(2-t-lam)**2/((1-t*t)*(1+lam)**2)
            count+=3
    print('EXACT_RATIONAL_OK',count)


if __name__=='__main__':
    verify()
