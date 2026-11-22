"""Supplementary finite checks for a four-site median-relaxation theorem.

Run: python verification/check.py
These tests do not replace the infinite-parameter analytic proof.
"""
from fractions import Fraction as F
from itertools import permutations


def update(x, gamma):
    return [(1-gamma)*x[i]+gamma*sorted((x[(i-1)%4],x[i],x[(i+1)%4]))[1]
            for i in range(4)]


def opposite_low(x):
    pair=sorted(range(4), key=lambda i:x[i])[:2]
    return abs(pair[0]-pair[1])==2


def test_all_orderings():
    count=0
    for gamma in (0.1, 0.25, 0.5):
        for p in permutations(range(4)):
            x=list(map(float,p))
            target=(sorted(x)[1]+sorted(x)[2])/2
            c=opposite_low(x)
            for _ in range(1000):
                x=update(x,gamma)
            diam=max(x)-min(x)
            if c:
                assert diam<1e-9, (gamma,p,diam)
                assert max(abs(z-target) for z in x)<1e-9, (gamma,p,x,target)
            else:
                assert diam>0.5, (gamma,p,diam)
            count+=1
    return count


def test_exact_witness():
    x=list(map(F, (0,3,2,5)))
    gamma=F(2,3)
    y=update(x,gamma)
    assert y==[F(2),F(7,3),F(8,3),F(3)],y
    assert max(y[:2])<min(y[2:])
    for _ in range(100):
        y=update(y,gamma)
        assert max(y[:2])<min(y[2:])
    # Family of exact rational first-step certificates for all subcritical widths.
    trials=0
    for gamma in (F(51,100),F(2,3),F(3,4),F(9,10),F(99,100)):
        r=(2*gamma-1)/(1-gamma)
        a=b=2*r+1
        x=[F(0),a+1,a,a+1+b]
        y=update(x,gamma)
        assert y[0]<y[1]<y[2]<y[3],(gamma,y)
        assert y[2]-y[1]==(2*gamma-1)
        trials+=1
    return trials


def test_conservation():
    count=0
    for gamma in (F(1,10),F(1,4),F(1,2)):
        for p in permutations(range(4)):
            x=list(map(F,p))
            if not opposite_low(x):
                continue
            for _ in range(8):
                if max(x[0],x[2])<min(x[1],x[3]):
                    aplus=max(x[0],x[2]); bminus=min(x[1],x[3])
                    y=update(x,gamma)
                    assert max(y[0],y[2])+min(y[1],y[3])==aplus+bminus
                elif max(x[1],x[3])<min(x[0],x[2]):
                    aplus=max(x[1],x[3]); bminus=min(x[0],x[2])
                    y=update(x,gamma)
                    assert max(y[1],y[3])+min(y[0],y[2])==aplus+bminus
                else:
                    break # possible equality at gamma=1/2
                x=y
                count+=1
    return count


if __name__=='__main__':
    a=test_all_orderings()
    b=test_exact_witness()
    c=test_conservation()
    print('PASS: orderings={}, rational_witnesses={}, invariance_steps={}'.format(a,b,c))
