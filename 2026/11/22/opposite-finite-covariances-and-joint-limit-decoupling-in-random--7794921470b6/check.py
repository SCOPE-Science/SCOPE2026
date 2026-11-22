"""Exact small-size checks for threshold-digraph covariance and asymptotic scaling.

This finite checker tests identities; asymptotic limits rely on the analytic proof.
Run: python check.py
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, comb


def closed(n):
    beta = Fraction(factorial(n - 1) * factorial(n - 2), factorial(2 * n - 2))
    return {
        'E_S': Fraction(1),
        'E_T': Fraction(1),
        'E_R': Fraction(comb(n, 2), 4),
        'Var_R': Fraction(3 * comb(n, 2), 16) + Fraction(7 * comb(n, 3), 24),
        'Cov_SR': Fraction(-n * (n - 1), 2 * (n + 2)),
        'Cov_TR': Fraction(-n * (n - 1), 2 * (n + 2)),
        'Cov_ST': Fraction(2 * n - 1, n * (n - 1)) - n * beta,
    }


def enumerate_moments(n):
    acc = {key: 0 for key in ('S', 'T', 'R', 'R2', 'SR', 'TR', 'ST')}
    den = factorial(2 * n)
    for order in permutations(range(2 * n)):
        rank = [0] * (2 * n)
        for r, tag in enumerate(order):
            rank[tag] = r
        incoming = [0] * n
        outgoing = [0] * n
        mutual = 0
        for i in range(n):
            for j in range(n):
                if i != j and rank[i] > rank[n + j]:
                    outgoing[i] += 1
                    incoming[j] += 1
        for i in range(n):
            for j in range(i + 1, n):
                if rank[i] > rank[n + j] and rank[j] > rank[n + i]:
                    mutual += 1
        s = outgoing.count(0)
        t = incoming.count(0)
        acc['S'] += s
        acc['T'] += t
        acc['R'] += mutual
        acc['R2'] += mutual ** 2
        acc['SR'] += s * mutual
        acc['TR'] += t * mutual
        acc['ST'] += s * t
    ex = {k: Fraction(v, den) for k, v in acc.items()}
    return {
        'E_S': ex['S'],
        'E_T': ex['T'],
        'E_R': ex['R'],
        'Var_R': ex['R2'] - ex['R'] ** 2,
        'Cov_SR': ex['SR'] - ex['S'] * ex['R'],
        'Cov_TR': ex['TR'] - ex['T'] * ex['R'],
        'Cov_ST': ex['ST'] - ex['S'] * ex['T'],
    }


def main():
    comparisons = 0
    for n in range(2, 5):
        exact = enumerate_moments(n)
        theory = closed(n)
        for key in theory:
            assert exact[key] == theory[key], (n, key, exact[key], theory[key])
            comparisons += 1
        assert theory['Cov_SR'] < 0
        assert theory['Cov_ST'] > 0
        comparisons += 2
        print(f'n={n}: E[R]={theory["E_R"]}, Var[R]={theory["Var_R"]}, '
              f'Cov(S,R)={theory["Cov_SR"]}, Cov(S,T)={theory["Cov_ST"]}')
    for n in range(2, 400):
        z = closed(n)
        assert z['Cov_SR'] < 0 and z['Cov_TR'] < 0 and z['Cov_ST'] > 0
        comparisons += 3
    print(f'PASS {comparisons} exact assertions. Infinite limits are not tested by enumeration.')


if __name__ == '__main__':
    main()
