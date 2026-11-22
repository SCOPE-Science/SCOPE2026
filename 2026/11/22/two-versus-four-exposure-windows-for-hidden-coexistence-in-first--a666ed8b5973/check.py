"""Reproduce the exact counterexample and invert the four-window ecological first-arrival model.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from math import exp, log, sqrt, isclose
from random import Random


def first_winner_probabilities(z, pa, pb, pab, n=4):
    """Return pairs (A_wins_by_j, B_wins_by_j), j=1..n."""
    out = []
    for j in range(1, n + 1):
        F = 1 - z**j
        out.append(( (pa+pab)*F - pab*F*F/2,
                     (pb+pab)*F - pab*F*F/2 ))
    return out


def inverse_unbalanced(a1,b1,a2,b2):
    delta1 = a1 - b1
    assert abs(delta1) > 1e-15
    z = (a2 - b2)/delta1 - 1
    assert 0 < z < 1
    F1, F2 = 1-z, 1-z*z
    q = 2*(a1/F1 - a2/F2)/(F2-F1)
    u = a1/F1 + q*F1/2
    v = b1/F1 + q*F1/2
    return z, 1-u-v+q, u-q, v-q, q


def inverse_balanced(a):
    assert len(a) >= 4
    b1,b2,b3,b4 = a[0],a[1]-a[0],a[2]-a[1],a[3]-a[2]
    det = b1*b3-b2*b2
    assert det > 0
    S = (b1*b4-b2*b3)/det
    z = (sqrt(1+4*S)-1)/2
    assert 0 < z < 1
    c = (b2-z*z*b1)/(z-z*z)
    d = (z*b1-b2)/(z-z*z)
    pa = c/(1-z)
    pab = 2*d/(1-z*z)
    return z, 1-2*pa-pab, pa, pa, pab


def close(x,y,rel=1e-7,abs_=1e-9):
    return isclose(float(x),float(y),rel_tol=rel,abs_tol=abs_)


def main():
    I = (Fraction(1,2), Fraction(9,50), Fraction(33,100), Fraction(33,100), Fraction(4,25))
    II = (Fraction(3,5), Fraction(43,256), Fraction(11,64), Fraction(11,64), Fraction(125,256))
    for data in (I,II):
        z,p00,pa,pb,pab=data
        assert min(data[1:]) > 0 and p00+pa+pb+pab == 1
        assert p00 == 1-pa-pb-pab
    a = first_winner_probabilities(I[0],I[2],I[3],I[4])
    b = first_winner_probabilities(II[0],II[2],II[3],II[4])
    for j,expected in enumerate((Fraction(9,40),Fraction(129,400),Fraction(147,400))):
        assert a[j]==(expected,expected)==b[j]
    assert a[3] == (Fraction(249,640),)*2
    assert b[3] == (Fraction(9741,25000),)*2
    assert b[3][0]-a[3][0] == Fraction(231,400000)
    cov1=I[4]-(I[2]+I[4])*(I[3]+I[4])
    cov2=II[4]-(II[2]+II[4])*(II[3]+II[4])
    assert cov1 == -Fraction(801,10000)
    assert cov2 == Fraction(3439,65536)
    counts = [0,0]
    rng = Random(112407)
    for _ in range(10000):
        xs=[rng.random()+0.05 for _ in range(4)]; total=sum(xs); p00,pa,pb,pab=(x/total for x in xs)
        z=0.12+0.75*rng.random()
        observed=first_winner_probabilities(z,pa,pb,pab)
        if abs(pa-pb) > 0.012:
            inv=inverse_unbalanced(observed[0][0],observed[0][1],observed[1][0],observed[1][1]);
            for have,want in zip(inv,(z,p00,pa,pb,pab)):
                assert close(have,want,rel=3e-7,abs_=3e-8),(have,want)
            counts[0]+=1
        # Balanced co-occupancy (independent of the unbalanced draw).
        pa=pb=(rng.random()+0.01)/5
        pab=(rng.random()+0.01)/5
        p00=1-2*pa-pab
        assert p00 >0
        obs=first_winner_probabilities(z,pa,pb,pab)
        inv=inverse_balanced([row[0] for row in obs])
        for have,want in zip(inv,(z,p00,pa,pb,pab)):
            assert close(have,want,rel=6e-7,abs_=5e-8),(have,want)
        counts[1]+=1
    print('Exact three-window counterexample: PASS')
    print('Opposite latent association signs: PASS')
    print('Fourth-window separation: PASS')
    print('Randomized unbalanced and balanced reconstructions:',counts,'PASS')

if __name__=='__main__':
    main()
