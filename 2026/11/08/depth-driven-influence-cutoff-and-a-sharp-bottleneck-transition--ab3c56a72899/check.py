"""Exact finite checks for the layered DeGroot influence-response formulas.

No non-standard packages, source downloads or external data are needed.
"""
from fractions import Fraction as Q
from math import comb


def update(layers, rates, matrices):
    d = len(rates)
    n = len(layers[0])
    answer = []
    for i in range(d):
        answer.append([
            (1-rates[i]) * sum(matrices[i][k][j]*layers[i][j]
                                for j in range(n)) + rates[i]*layers[i+1][k]
            for k in range(n)
        ])
    answer.append([
        sum(matrices[d][k][j]*layers[d][j] for j in range(n))
        for k in range(n)
    ])
    return answer


def geometric_cdf(rates, horizon):
    coefficients = [Q(1)] + [Q(0)]*horizon
    for p in rates:
        next_coefficients = [Q(0)]*(horizon+1)
        for a in range(horizon+1):
            if coefficients[a]:
                for k in range(1, horizon-a+1):
                    next_coefficients[a+k] += (
                        coefficients[a]*p*(1-p)**(k-1)
                    )
        coefficients = next_coefficients
    return sum(coefficients)


def binomial_tail(trials, successes, p):
    return sum(Q(comb(trials, k))*p**k*(1-p)**(trials-k)
               for k in range(successes, trials+1))


def main():
    for n in (2, 3):
        complete = [[Q(1, n)]*n for _ in range(n)]
        identity = [[Q(int(j == k)) for j in range(n)] for k in range(n)]
        for depth in range(1, 6):
            for case in range(3):
                if case == 0:
                    rates = [Q(2, 5)]*depth
                else:
                    rates = [Q(1, 3), Q(2, 5), Q(3, 4),
                             Q(1, 2), Q(1, 4)][:depth]
                matrices = [complete if (i+case)%2 else identity
                            for i in range(depth+1)]
                state = [[Q(0)]*n for _ in range(depth)] + [[Q(1)]*n]
                for t in range(16):
                    expected = geometric_cdf(rates, t)
                    assert all(value == expected for value in state[0]), (
                        n, depth, case, t, state[0], expected
                    )
                    if case == 0:
                        assert expected == binomial_tail(t, depth, rates[0])
                    state = update(state, rates, matrices)
    print('PASS: exact multiplex updates, geometric waiting-time convolutions, and binomial tails.')


if __name__ == '__main__':
    main()
