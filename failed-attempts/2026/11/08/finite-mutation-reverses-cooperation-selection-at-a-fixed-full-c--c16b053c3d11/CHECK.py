"""Exact-rational verification for finite-mutation, three-player public-goods selection.

Only Python's standard library is required. No simulation or numerical tolerance is used.
"""
from fractions import Fraction as F
from math import comb

N = 4
GROUP = 3


def expected_differences(returns):
    """Condition on the focal player; sample its two co-players without replacement."""
    out = []
    den = comb(N - 1, GROUP - 1)
    for i in range(1, N):
        pc, pd = F(0), F(0)
        for j in range(GROUP):
            if 0 <= j <= i - 1 and 0 <= GROUP - 1 - j <= N - i:
                prob = F(comb(i - 1, j) * comb(N - i, GROUP - 1 - j), den)
                pc += prob * (F(j + 1, GROUP) * returns[j + 1] - 1)
            if 0 <= j <= i and 0 <= GROUP - 1 - j <= N - i - 1:
                prob = F(comb(i, j) * comb(N - i - 1, GROUP - 1 - j), den)
                pd += prob * F(j, GROUP) * returns[j]
        out.append(pc - pd)
    return out


def stationary(returns, mutation, logistic):
    """Exact stationary mean under independent uniform model selection with replacement.

    logistic maps the payoff difference at each transient count to a rational
    Fermi imitation probability. It can encode selection intensity 9*log(2)
    whenever nine times each difference is an integer.
    """
    differences = expected_differences(returns)
    forward, backward = [], []
    for i in range(N + 1):
        l = logistic(differences[i - 1]) if 0 < i < N else F(1, 2)
        contact = (1 - mutation) * F(i * (N - i), N * N)
        forward.append(mutation * F(N - i, N) + contact * l)
        backward.append(mutation * F(i, N) + contact * (1 - l))
    weights = [F(1)]
    for i in range(1, N + 1):
        weights.append(weights[-1] * forward[i - 1] / backward[i])
    z = sum(weights)
    return sum(F(i, N) * weights[i] for i in range(N + 1)) / z


def power_two_fermi(d):
    exponent = 9 * d
    assert exponent.denominator == 1
    n = int(exponent)
    return F(2**n, 1 + 2**n) if n >= 0 else F(1, 1 + 2**(-n))


def exact_derivative(returns, mutation):
    """Differentiate detailed-balance stationary weights exactly at delta=0."""
    differences = expected_differences(returns)
    up, down, dup, ddown = [], [], [], []
    for i in range(N + 1):
        contact = (1 - mutation) * F(i * (N - i), N * N)
        up.append(mutation * F(N - i, N) + contact / 2)
        down.append(mutation * F(i, N) + contact / 2)
        d = differences[i - 1] if 0 < i < N else F(0)
        dup.append(contact * d / 4)
        ddown.append(-contact * d / 4)
    weights, logder = [F(1)], [F(0)]
    for i in range(1, N + 1):
        weights.append(weights[-1] * up[i - 1] / down[i])
        logder.append(logder[-1] + dup[i - 1] / up[i - 1] - ddown[i] / down[i])
    z = sum(weights)
    mean = sum(F(i, N) * weights[i] for i in range(N + 1)) / z
    return sum(weights[i] * (F(i, N) - mean) * logder[i] for i in range(N + 1)) / z


def theorem_derivative(mutation, r2):
    return F(2, 3) * mutation * (1 - mutation) * (r2 - 5) / ((3 + 13 * mutation) * (1 + 15 * mutation))


def main():
    trials = 0
    for mutation in [F(1, 29), F(1, 17), F(1, 8), F(1, 3), F(1, 2), F(3, 4), F(7, 8), F(15, 16)]:
        for r2 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            ret = [0, 1, r2, 9]
            assert expected_differences(ret) == [F(-8, 9), F(2 * r2 - 10, 9), F(18 - 2 * r2, 9)]
            assert exact_derivative(ret, mutation) == theorem_derivative(mutation, r2)
            if r2 == 5:
                assert stationary(ret, mutation, power_two_fermi) == F(1, 2)
            trials += 1
    negative = stationary([0, 1, 1, 9], F(1, 2), power_two_fermi)
    positive = stationary([0, 1, 8, 9], F(1, 2), power_two_fermi)
    assert negative == F(599130841, 1318051952), negative
    assert positive == F(141053, 264124), positive
    assert negative < F(1, 2) < positive
    print('PASS:', trials, 'exact payoff/derivative comparisons and exact finite-selection witnesses')
    print('negative:', negative, 'positive:', positive)


if __name__ == '__main__':
    main()
