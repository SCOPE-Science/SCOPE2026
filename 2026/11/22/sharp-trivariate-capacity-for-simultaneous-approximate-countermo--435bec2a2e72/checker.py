"""Exact rational checks for the explicit trivariate uniform coupling.

The analytic arguments in RESULT.md, not a finite test suite, establish
all real-tolerance and all-coupling statements.
"""
from fractions import Fraction as F
from itertools import permutations


def base_segments():
    """Six affine images of a uniform parameter in [1, 3/2]."""
    b = ((F(1), F(3, 2)), (F(-1, 2), F(0)),
         (F(-1), F(-1, 2)), (F(-3, 2), F(-1)),
         (F(0), F(1, 2)), (F(1, 2), F(1)))
    return sorted(b)


def verify_partition():
    segs = base_segments()
    assert len(segs) == 6
    assert segs[0][0] == F(-3, 2)
    assert segs[-1][1] == F(3, 2)
    for i, (left, right) in enumerate(segs):
        assert right - left == F(1, 2)
        if i:
            assert segs[i-1][1] == left
    # Under a uniform permutation and equiprobable sign, each component
    # is selected with weight 1/6.  Each component has density 2 on
    # its half-unit interval, giving density (1/6)*2 = 1/3.
    assert F(1, 6) * F(2) == F(1, 3)
    return 7


def base_vector(a):
    return (a, 1-a, a-2)


def verify_success_support():
    count = 0
    # Each pair-sum is affine in a, so endpoint bounds control all a.
    for a in (F(1), F(3, 2)):
        for s in (-1, 1):
            v = tuple(s*x for x in base_vector(a))
            for p in permutations(v):
                for i, j in ((0, 1), (0, 2), (1, 2)):
                    assert abs(p[i]+p[j]) <= 1
                    count += 1
    return count


def verify_mixture(eps):
    assert F(0) < eps <= F(1, 3)
    p = 3*eps
    width = 3*eps
    left = F(1, 2) - F(3, 2)*eps
    right = F(1, 2) + F(3, 2)*eps
    assert F(0) <= left < right <= F(1)
    assert right-left == width
    assert p * (1/width) == 1  # central marginal density
    if p < 1:
        assert (1-p)/(1-width) == 1  # outside marginal density
    for a in (F(1), F(7, 6), F(5, 4), F(4, 3), F(3, 2)):
        for s in (-1, 1):
            for v in permutations(tuple(s*x for x in base_vector(a))):
                u = tuple(F(1, 2)+eps*x for x in v)
                assert all(left <= x <= right for x in u)
                assert all(abs(u[i]+u[j]-1) <= eps
                           for i, j in ((0, 1), (0, 2), (1, 2)))
    return 2+5*2*6*6


def main():
    n = verify_partition()+verify_success_support()
    for eps in (F(1, 1000), F(1, 20), F(1, 7), F(1, 4), F(1, 3)):
        n += verify_mixture(eps)
    # The upper bound uses the exact algebraic identity
    # 2 v1=(v1+v2)+(v1+v3)-(v2+v3).
    for v in ((F(1, 5), F(-1, 8), F(3, 7)),
              (F(-9, 10), F(1, 11), F(5, 4))):
        assert 2*v[0] == (v[0]+v[1])+(v[0]+v[2])-(v[1]+v[2])
        n += 1
    print(f"PASS: {n} exact rational assertions/groups; analytic proof remains essential")


if __name__ == '__main__':
    main()
