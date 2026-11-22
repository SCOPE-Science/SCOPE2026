"""Independent exact checks for seed-vertex degree covariance in clique-grown random k-trees.

Run with Python 3: python CHECK.py
All finite enumerations inspect graph edges directly, not the analytic face recurrences.
"""
from fractions import Fraction
from itertools import combinations
from math import gamma, pi


def products(k, steps):
    a, b = k - 1, k - 2
    values = {}
    for s in (a, b, 2 * a):
        p = Fraction(1)
        for t in range(steps):
            total = k + 1 + k * t
            p *= Fraction(total + s, total)
        values[s] = p
    return values


def exact_moments(k, steps):
    a = k - 1
    p = products(k, steps)
    mean_a = k * p[a]
    mean_b = (k - 1) * p[k - 2]
    correction = Fraction(a * a, k)
    mixed = (k * k + correction * (k - 1)) * p[2*a] - correction * mean_b
    second = k * (2 * k - 1) * p[2*a] - a * mean_a
    mean_degree = k + (mean_a - k) / a
    cov_degree = (mixed - mean_a**2) / a**2
    var_degree = (second - mean_a**2) / a**2
    return mean_degree, cov_degree, var_degree, mean_b


def enumerate_graphs(k, steps):
    # Every history of a fixed length has the same probability: the number of
    # available k-faces is k+1+k*t at time t, independently of its history.
    adjacency = tuple(frozenset(j for j in range(k + 1) if j != i)
                      for i in range(k + 1))
    total_histories = 0
    sum_degree = sum_pair = sum_square = sum_common = 0

    def rec(graph, left):
        nonlocal total_histories, sum_degree, sum_pair, sum_square, sum_common
        if left == 0:
            total_histories += 1
            x, y = len(graph[0]), len(graph[1])
            sum_degree += x
            sum_pair += x*y
            sum_square += x*x
            sum_common += sum(1 for face in combinations(range(len(graph)), k)
                              if 0 in face and 1 in face and all(
                                  j in graph[i] for i, j in combinations(face, 2)))
            return
        n = len(graph)
        for face in combinations(range(n), k):
            if all(j in graph[i] for i, j in combinations(face, 2)):
                fs = frozenset(face)
                next_graph = tuple(graph[i] | frozenset((n,)) if i in fs
                                   else graph[i] for i in range(n)) + (fs,)
                rec(next_graph, left - 1)

    rec(adjacency, steps)
    E1 = Fraction(sum_degree, total_histories)
    E12 = Fraction(sum_pair, total_histories)
    E11 = Fraction(sum_square, total_histories)
    EB = Fraction(sum_common, total_histories)
    return total_histories, E1, E12-E1*E1, E11-E1*E1, EB


def run():
    assertions = 0
    expected_histories = [(2,4,945), (3,4,3640), (4,3,585), (5,3,1056)]
    # Determine the total history count from products as a separate check.
    for k, steps, _ in expected_histories:
        count, avg, cov, var, common = enumerate_graphs(k, steps)
        target_histories = 1
        for t in range(steps):
            target_histories *= (k + 1 + k*t)
        assert count == target_histories, (k,steps,count,target_histories)
        assertions += 1
        expectation, covariance, variance, b = exact_moments(k, steps)
        for observed, predicted in [(avg, expectation),(cov,covariance),
                                    (var,variance),(common,b)]:
            assert observed == predicted,(k,steps, observed,predicted)
            assertions += 1
    for k in range(2, 16):
        for steps in range(1, 80):
            expectation, covariance, variance, common = exact_moments(k, steps)
            assert covariance < 0,(k,steps,covariance)
            assert variance > 0,(k,steps,variance)
            assertions += 2
        assert exact_moments(k, 1)[1] == Fraction(-1,(k+1)**2)
        assertions += 1
    for steps in range(1,200):
        mean,cov,var,_=exact_moments(2,steps)
        assert cov == Fraction(3*steps+4,1)-mean**2
        assert var == Fraction(4*steps+6,1)-mean-mean**2
        assertions += 2
    # These floating checks concern gamma constants only; not infinite-proof substitutes.
    k=2
    asymptotic_corr=(3-pi)/(4-pi)
    mean,cov,var,_=exact_moments(k,5000)
    assert abs(float(cov/var)-asymptotic_corr)<0.006
    assertions+=1
    print('PASS:',assertions,'independent exact or numerical assertions')
    print('K2: mean and covariance at four insertions:',exact_moments(2,4)[:2])
    print('K2: limiting correlation:',asymptotic_corr)


if __name__ == '__main__':
    run()
