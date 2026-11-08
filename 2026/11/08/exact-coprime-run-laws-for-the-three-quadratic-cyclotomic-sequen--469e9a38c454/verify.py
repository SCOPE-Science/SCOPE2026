"""Exact finite checks for consecutive quadratic cyclotomic gcd profiles.

Requires Python 3 standard library only. All evidence is integer arithmetic.
The general statements rely on the separately supplied symbolic proof.
"""
from collections import Counter
from math import gcd


def polynomial(m, n):
    if m == 3:
        return n*n+n+1
    if m == 4:
        return n*n+1
    if m == 6:
        return n*n-n+1
    raise ValueError(m)


def predicted_edges(m, n):
    if m == 6:
        return predicted_edges(3, n-1)
    if m == 3:
        result = {}
        for i in range(3):
            if (n+i) % 7 == 2:
                result[(i,i+2)] = 7
        for i in range(2):
            if (n+i) % 3 == 1:
                result[(i,i+3)] = 3
        if n % 19 == 7:
            result[(0,4)] = 19
        return result
    result = {}
    for i in range(2):
        if (n+i) % 5 == 2:
            result[(i,i+1)] = 5
    if n % 2 == 1:
        result[(0,2)] = 2
    return result


def direct_edges(m, n):
    H = 5 if m in (3,6) else 3
    a = [polynomial(m, n+i) for i in range(H)]
    return {(i,j):gcd(a[i],a[j]) for i in range(H)
            for j in range(i+1,H) if gcd(a[i],a[j]) > 1}


def max_run(m, n):
    H = 6 if m in (3,6) else 4
    a = [polynomial(m, n+i) for i in range(H)]
    for L in range(1,H):
        if any(gcd(a[L],a[i]) > 1 for i in range(L)):
            return L
    raise AssertionError('contradicts universal cutoff')


def proper_divisors(k):
    return [d for d in range(1,k+1) if k%d==0]


def verify():
    expected = {3:({2:57,3:152,4:118,5:72}, {0:72,1:202,2:119,3:6},399),
                4:({1:2,2:5,3:3},{0:3,1:5,2:2},10),
                6:({2:57,3:152,4:118,5:72}, {0:72,1:202,2:119,3:6},399)}
    for m in (3,4,6):
        run_counts, graph_counts, period = expected[m]
        runs = [max_run(m,n) for n in range(1,period+1)]
        graphs = []
        for n in range(1,period+1):
            actual = direct_edges(m,n)
            assert actual == predicted_edges(m,n), (m,n,actual,predicted_edges(m,n))
            graphs.append(len(actual))
        assert dict(Counter(runs)) == run_counts
        assert dict(Counter(graphs)) == graph_counts
        for d in proper_divisors(period)[:-1]:
            assert any(runs[k] != runs[(k+d)%period] for k in range(period))
        for n in range(period+1, 20000, 37):
            assert direct_edges(m,n) == predicted_edges(m,n)
            assert max_run(m,n) == runs[(n-1)%period]
        print('PROFILE_OK', 'index=',m, 'period=',period,
              'run_counts=', dict(sorted(run_counts.items())),
              'graph_edges=',dict(sorted(graph_counts.items())))
    print('VERIFY_OK', 'exact_residue_periods=True', 'large_integer_spotchecks=True',
          'general_infinite_proof_separate=True', 'independent_audit=False')

if __name__ == '__main__':
    verify()
