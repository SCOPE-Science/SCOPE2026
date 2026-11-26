"""Exact-rational finite sanity checks for the affine parallel-road identity.

The proof of the all-parameter theorem is analytical, not the finite tests below.
Run with Python 3: python fleet_symmetrization_checker.py
"""
from fractions import Fraction as Q
from random import Random


def wardrop(a, b, demand):
    assert len(a) == len(b) and all(x > 0 for x in b) and demand >= 0
    if demand == 0:
        return [Q(0) for _ in a]
    indices = sorted(range(len(a)), key=lambda i: a[i])
    for k in range(1, len(a) + 1):
        active = indices[:k]
        level = (demand + sum((a[i] / b[i] for i in active), Q(0))) / sum(
            (1 / b[i] for i in active), Q(0)
        )
        if k == len(a) or level <= a[indices[k]]:
            flows = [max(Q(0), (level - a[i]) / b[i]) for i in range(len(a))]
            assert sum(flows, Q(0)) == demand
            return flows
    raise AssertionError('unreachable')


def verify(a, b, demand, share):
    low = wardrop(a, b, (1 - share) * demand)
    high = wardrop(a, b, (1 + share) * demand)
    selfish = low
    fleet = [(high[i] - low[i]) / 2 for i in range(len(a))]
    total = [(high[i] + low[i]) / 2 for i in range(len(a))]
    assert all(x >= 0 for x in fleet)
    assert sum(selfish, Q(0)) == (1 - share) * demand
    assert sum(fleet, Q(0)) == share * demand
    assert sum(total, Q(0)) == demand
    delay = [a[i] + b[i] * total[i] for i in range(len(a))]
    marginal = [delay[i] + b[i] * fleet[i] for i in range(len(a))]
    if share < 1:
        min_delay = min(delay)
        assert all(not selfish[i] or delay[i] == min_delay for i in range(len(a)))
    if share > 0:
        min_marginal = min(marginal)
        assert all(not fleet[i] or marginal[i] == min_marginal for i in range(len(a)))
    return total


def verify_two_road_example():
    for beta_n in range(1, 9):
        beta = Q(beta_n, 3)
        for tau_n in range(1, 9):
            tau = Q(tau_n, 10)
            for s_n in range(0, 21):
                share = Q(s_n, 20)
                f = verify([Q(0), tau], [Q(1), beta], Q(1), share)
                if share <= 1 - tau:
                    f1 = (beta + tau) / (1 + beta)
                else:
                    f1 = (tau + 2 * beta + 1 - share) / (2 * (1 + beta))
                assert f[0] == f1
                cost = f[0] ** 2 + f[1] * (tau + beta * f[1])
                opt_f1 = (tau + 2 * beta) / (2 * (1 + beta))
                opt_f2 = 1 - opt_f1
                opt_cost = opt_f1 ** 2 + opt_f2 * (tau + beta * opt_f2)
                deficit = min(tau, 1 - share) ** 2 / (4 * (1 + beta))
                assert cost - opt_cost == deficit


def main():
    rng = Random(42143)
    for _ in range(2100):
        n = rng.randint(2, 9)
        a = [Q(rng.randint(0, 40), rng.randint(1, 10)) for _ in range(n)]
        b = [Q(rng.randint(1, 25), rng.randint(1, 10)) for _ in range(n)]
        d = Q(rng.randint(1, 70), rng.randint(1, 15))
        s = Q(rng.randint(0, 30), 30)
        verify(a, b, d, s)
    verify_two_road_example()
    print('PASS: 2100 exact multi-road equilibria; 1344 exact two-road formula/cost cases')


if __name__ == '__main__':
    main()
