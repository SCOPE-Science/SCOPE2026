import math
import random


def exact_values(a, c, alpha):
    t = alpha * a
    r = 1.0 / (1.0 + t)
    var_inf = c*c * t / (2.0 + t)
    gap_inf = 0.5 * a * var_inf
    return t, r, var_inf, gap_inf


def simulate(a=3.0, c=2.0, alpha=0.4, steps=500, paths=200000, seed=12345):
    rng = random.Random(seed)
    t, r, var_inf, gap_inf = exact_values(a, c, alpha)
    xs = [0.37] * paths
    b = (1.0-r)*c
    for _ in range(steps):
        for i in range(paths):
            xi = 1.0 if rng.random() < 0.5 else -1.0
            xs[i] = r*xs[i] + b*xi
    mean = sum(xs)/paths
    second = sum(x*x for x in xs)/paths
    empirical_gap = 0.5*a*second
    return t, r, var_inf, gap_inf, mean, second, empirical_gap


def check_support_threshold():
    # Images of [-c,c] under T_-(x)=r x-(1-r)c and T_+(x)=r x+(1-r)c.
    c = 1.0
    for r in (0.4, 0.5, 0.6):
        left = (-c, c*(2*r-1))
        right = (c*(1-2*r), c)
        if r < 0.5:
            assert left[1] < right[0]
        elif r == 0.5:
            assert abs(left[1]-right[0]) < 1e-15
        else:
            assert left[1] > right[0]
            assert left[0] == -c and right[1] == c
    return True


def main():
    # Algebraic checks in direct floating form for several parameter values.
    for a, c, alpha in [(1.0,1.0,0.2),(2.0,3.0,0.5),(7.0,0.4,1.3)]:
        t, r, var_inf, gap_inf = exact_values(a,c,alpha)
        assert 0.0 < r < 1.0
        lhs = c*c*(1-r)/(1+r)
        assert math.isclose(lhs, var_inf, rel_tol=1e-14, abs_tol=1e-14)
        assert math.isclose(gap_inf, 0.5*a*var_inf, rel_tol=1e-14, abs_tol=1e-14)
        assert (r < 0.5) == (t > 1.0)
        assert (r > 0.5) == (t < 1.0)
    check_support_threshold()

    t, r, var_inf, gap_inf, mean, second, empirical_gap = simulate()
    # Monte Carlo is only a replay sanity check; the proof is algebraic.
    assert abs(mean) < 0.01
    assert abs(second-var_inf) < 0.02
    assert abs(empirical_gap-gap_inf) < 0.04
    print('VERIFY_OK')
    print(f't={t:.12f} r={r:.12f}')
    print(f'exact_second_moment={var_inf:.12f} empirical={second:.12f}')
    print(f'exact_gap={gap_inf:.12f} empirical_gap={empirical_gap:.12f}')

if __name__ == '__main__':
    main()
