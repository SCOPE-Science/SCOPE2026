"""Reproducible tests for the parameterized cardinal cubic interpolation variation theorem.

Run with Python 3 standard library: python verify.py
Numerical checks supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction
import math
import random


def predicted_gain(lam):
    edge = 16 * abs(lam) / 27
    if lam < 0:
        q = math.sqrt((3-lam)/(3*(1-lam)))
        core = -1 + (2/3)*(3-lam)*q
    elif lam <= 3:
        core = 1.0
    else:
        q = math.sqrt((lam-3)/(3*(lam-1)))
        core = 1 + (2/3)*(lam-3)*q
    return edge + core


def cubic_value(coeff, t):
    a,b,c,d = coeff
    return ((a*t+b)*t+c)*t+d


def cubic_variation(coeff):
    a,b,c,_ = coeff
    qa,qb,qc = 3*a, 2*b, c
    roots = []
    if abs(qa) <= 1e-13:
        if abs(qb) > 1e-13:
            roots = [-qc/qb]
    else:
        disc = qb*qb - 4*qa*qc
        if disc >= 0:
            sq = math.sqrt(disc)
            roots = [(-qb-sq)/(2*qa), (-qb+sq)/(2*qa)]
    nodes = [0.] + sorted(r for r in roots if 1e-12 < r < 1-1e-12) + [1.]
    nodes2=[nodes[0]]
    for t in nodes[1:]:
        if abs(t-nodes2[-1])>1e-10: nodes2.append(t)
    return sum(abs(cubic_value(coeff,v)-cubic_value(coeff,u)) for u,v in zip(nodes2,nodes2[1:]))


def hermite_cell(y0, y1, d0, d1):
    return (2*y0-2*y1+d0+d1, -3*y0+3*y1-2*d0-d1, d0, y0)


def full_variation(signal, lam):
    n=len(signal)
    def y(k):
        return signal[0] if k<0 else signal[-1] if k>=n else signal[k]
    total=0.
    for i in range(-1,n):
        d0=lam*(y(i+1)-y(i-1))
        d1=lam*(y(i+2)-y(i))
        total += cubic_variation(hermite_cell(y(i),y(i+1),d0,d1))
    return total


def run():
    assert Fraction(1,1)+Fraction(16,27)*Fraction(1,2) == Fraction(35,27)
    assert Fraction(1,1)+Fraction(16,27)*3 == Fraction(25,9)
    rng=random.Random(20261115)
    count=0
    for lam in [-30,-10,-5,-2,-1,-0.2,-0.0001,0,0.00001,0.25,0.5,1,2.5,3,3.0001,4,8,20]:
        pred=predicted_gain(lam)
        spike=[0.]*7+[1.]*7
        step_gain=full_variation(spike,lam)
        assert abs(step_gain-pred)<=3e-9*max(1,pred), ('step',lam,step_gain,pred)
        for _ in range(120):
            n=rng.randrange(3,26)
            y=[rng.uniform(-3,3) for _ in range(n)]
            vd=sum(abs(y[i+1]-y[i]) for i in range(n-1))
            v=full_variation(y,lam)
            assert v<=pred*vd+1e-8*max(1,pred*vd), ('bound',lam,v,pred*vd)
            count+=1
    # Core derivative regime classification and stationary point identities.
    for lam in [-20,-1,-0.00001,3.00001,4,20]:
        q=math.sqrt((3-lam)/(3*(1-lam)))
        a=(1-q)/2
        p=(2*lam-2)*a**3+(3-3*lam)*a*a+lam*a
        expected=0.5+(lam-3)*q/6
        assert abs(p-expected)<1e-8
        assert abs(lam+6*(1-lam)*a*(1-a))<1e-8
    print('EXACT_FRACTION_CLASSICAL_AND_CRITICAL_CONSTANTS_PASS')
    print('SINGLE_STEP_ATTAINS_ALL_18_PARAMETER_GAINS_PASS')
    print('RANDOM_SEQUENCE_VARIATION_BOUNDS_PASS',count)
    print('ALL_REGIME_STATIONARY_FORMULAS_PASS')
    print('ALL_PARAMETRIC_CUBIC_VARIATION_CHECKS_PASS')

if __name__=='__main__': run()
