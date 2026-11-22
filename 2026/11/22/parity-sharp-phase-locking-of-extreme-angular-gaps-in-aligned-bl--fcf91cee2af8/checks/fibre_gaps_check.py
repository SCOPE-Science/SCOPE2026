"""Finite numerical diagnostics for the boundary-fibre gap theorem.

The theorem itself is analytic; these computations test normalization,
branch choices, arbitrary aligned zero lists, and cusp coefficients.
"""
import math
import random

PI = math.pi
TWO_PI = 2.0 * PI


def F_base(theta, zeros):
    """Continuous boundary phase on [-pi,pi]."""
    assert -PI - 1e-12 <= theta <= PI + 1e-12
    return sum(2.0 * math.atan2((1 + a) * math.sin(theta / 2),
                                (1 - a) * math.cos(theta / 2)) for a in zeros)


def phase(theta, zeros):
    """Continuous extension with phase(theta+2pi)=phase(theta)+2pi*N."""
    k = math.floor((theta + PI) / TWO_PI)
    t = theta - TWO_PI * k
    return TWO_PI * len(zeros) * k + F_base(t, zeros)


def phase_inverse(u, zeros):
    n = len(zeros)
    k = math.floor((u + n * PI) / (TWO_PI * n))
    target = u - TWO_PI * n * k
    lo, hi = -PI, PI
    for _ in range(68):
        mid = 0.5 * (lo + hi)
        if F_base(mid, zeros) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) + TWO_PI * k


def speed(theta, zeros):
    return sum((1 - a*a) / (1 - 2*a*math.cos(theta) + a*a) for a in zeros)


def gap_profile(center, zeros):
    return phase_inverse(center + PI, zeros) - phase_inverse(center - PI, zeros)


def gaps(phi, zeros):
    n = len(zeros)
    roots = sorted((phase_inverse(phi + TWO_PI*j, zeros) % TWO_PI)
                   for j in range(n))
    return [roots[j+1] - roots[j] for j in range(n-1)] + [roots[0] + TWO_PI - roots[-1]]


def wrapped(x):
    return (x + PI) % TWO_PI - PI


def test():
    random.seed(30421)
    num = 0
    groups = [[0.0, 0.4], [0.0, 0.0, 0.65], [0.19, 0.5, 0.7],
              [0.0, 0.2, 0.4, 0.7, 0.93]]
    for _ in range(30):
        n = random.randrange(2, 10)
        aa = [random.uniform(0, 0.93) for _ in range(n)]
        aa[random.randrange(n)] = random.uniform(0.05, 0.90)
        groups.append(aa)
    for aa in groups:
        n = len(aa)
        d_pack = phase_inverse(TWO_PI, aa)
        d_cover = PI - phase_inverse((n-2)*PI, aa)
        assert 0.0 < d_pack <= TWO_PI / n + 1e-9
        assert d_cover >= TWO_PI / n - 1e-9
        assert abs(gap_profile(PI, aa) - d_pack) < 1e-10
        assert abs(gap_profile((n-1)*PI, aa) - d_cover) < 1e-10
        assert abs(phase(d_pack, aa) - TWO_PI) < 1e-10
        num += 5
        for k in range(41):
            phi = TWO_PI * k / 41
            ds = gaps(phi, aa)
            d = abs(wrapped(phi))
            e = abs(wrapped(phi - n*PI))
            profile_min = gap_profile(PI-d, aa)
            profile_max = gap_profile((n-1)*PI+e, aa)
            assert abs(min(ds)-profile_min) < 3e-10
            assert abs(max(ds)-profile_max) < 3e-10
            assert min(ds) <= d_pack + 5e-10
            assert max(ds) >= d_cover - 5e-10
            assert abs(sum(ds) - TWO_PI) < 1e-11
            num += 5
        eps = 1e-4
        cusp_pack = 1/speed(d_pack, aa)-1/speed(0, aa)
        direct_pack = (d_pack-min(gaps(eps,aa)))/eps
        assert abs(cusp_pack-direct_pack) < 5e-3
        cusp_cover = 1/speed(PI, aa)-1/speed(PI-d_cover, aa)
        direct_cover = (max(gaps((n%2)*PI+eps,aa))-d_cover)/eps
        assert abs(cusp_cover-direct_cover) < 5e-3
        num += 2
    print('PASS', num, 'finite checks across', len(groups), 'aligned-zero lists')
    print('Example N=3:', 'pack',round(phase_inverse(TWO_PI,[0.,0.,.7]),10),
          'cover', round(PI-phase_inverse(PI,[0.,0.,.7]),10))


if __name__ == '__main__':
    test()
