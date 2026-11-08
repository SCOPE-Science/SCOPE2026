"""Exact rational checks for finite-depth delayed-argument witnesses.

The general theorem and its algebraic equality case are proved in RESULT.md.
This program checks representative rational parameter instances and the
piecewise-linear history construction using only Python's standard library.
"""
from fractions import Fraction as Q


def make_example(i, q):
    assert i >= 3 and 0 < q < 1
    eta = q / 2
    eps = sig = Q(1, 100)
    y = [-Q(1)]
    for _ in range(i - 2):
        x = y[-1]
        y.append(-Q(1) - eta*(eps + sig*(x + 1)))
    assert len(set(y)) == i - 1
    sep = min(abs(a-b) for j,a in enumerate(y) for b in y[j+1:])
    radius = sep / 100
    slope = [-Q(2)]*(i-2) + [Q(2)]
    def baseline(x):
        return eps + sig*(x+1)
    def phi(x):
        for a, v in zip(y, slope):
            h = x-a
            if abs(h) <= radius:
                return baseline(a)+v*h
            if abs(h) <= 5*radius:
                outer=(5*sig-v)/4
                mag = v*radius+outer*(abs(h)-radius)
                return baseline(a)+(mag if h>0 else -mag)
        return baseline(x)
    points=[Q(-2),Q(0)]
    for a in y:
        points.extend([a-5*radius,a-radius,a,a+radius,a+5*radius])
    assert all(Q(-2)<a<Q(0) for a in y)
    assert 5*radius < min(min(a+2,-a) for a in y)
    assert max(abs(phi(x)) for x in points) < Q(1)
    # Every segment has slope either sigma, +/-2 or (5*sigma - (+/-2))/4.
    assert all(abs(v) <= 2 for v in [sig,Q(2),-Q(2),*( (5*sig-v)/4 for v in slope)])
    # At the initial time all arguments are in the initial-history interval.
    def delayed(t):
        d=t-1
        ds=[d]
        for _ in range(i-1):
            d=t-1-eta*phi(d)
            ds.append(d)
        return ds
    assert delayed(Q(0))[:i-1] == y
    # Short enough that all arguments remain in their assigned affine cores.
    step = radius/(100*i)
    trial = delayed(step)
    for d,a in zip(trial[:i-1],y):
        assert abs(d-a)<radius
    expected = Q(1)-sum((q**k for k in range(1,i)),Q(0))
    assert (trial[i-1]-delayed(Q(0))[i-1])/step == expected
    # The fixed-point implicit delayed argument is increasing by the source theorem.
    return expected, len(points), max(abs(phi(x)) for x in points)


def main():
    tests=[(3,Q(3,4)),(4,Q(2,3)),(5,Q(3,5)),(6,Q(11,20)),(7,Q(21,40))]
    checks=0
    for i,q in tests:
        derivative, points, magnitude=make_example(i,q)
        assert derivative<0
        checks+=points+8
        print(f'i={i} q={q} d_i_prime={derivative} history_max_at_breaks={magnitude}')
    for i in range(3,9):
        derivative, points, magnitude=make_example(i,Q(1,2))
        assert derivative>0
        checks+=points+8
    print(f'VERIFY_OK exact_rational_checks={checks} witness_depths=3..7 additional_below_threshold=3..8')


if __name__ == '__main__':
    main()
