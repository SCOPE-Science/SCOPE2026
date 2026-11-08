"""Finite computation checks of the critical product-hazard SIS coefficient.

No data files or third-party packages are required. The theorem is analytic;
these computations check its algebra on small connected graphs and its asymptotic
predictions for representative graphs, not its universally quantified proof.
"""
import itertools
import math


def connected(A):
    n = len(A)
    seen = {0}
    frontier = [0]
    for i in frontier:
        for j, a in enumerate(A[i]):
            if a and j not in seen:
                seen.add(j)
                frontier.append(j)
    return len(seen) == n


def perron(A):
    # A+I is primitive for a connected undirected loopless graph.
    n = len(A)
    v = [1 / math.sqrt(n)] * n
    for _ in range(2500):
        y = [v[i] + sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        norm = math.sqrt(sum(x*x for x in y))
        y = [x / norm for x in y]
        if max(abs(y[i] - v[i]) for i in range(n)) < 1e-14:
            v = y
            break
        v = y
    rho = sum(v[i] * sum(A[i][j] * v[j] for j in range(n)) for i in range(n))
    residual = max(abs(sum(A[i][j] * v[j] for j in range(n)) - rho*v[i]) for i in range(n))
    assert residual < 3e-11, ('PF residual', residual)
    return rho, v


def exact_quadratic(A, v, beta, delta):
    n = len(A)
    return sum(v[i] * ((1-delta) * beta * v[i] * sum(A[i][j] * v[j] for j in range(n))
        + beta*beta * sum(v[j]*v[k] for j in range(n) for k in range(j+1, n)
            if A[i][j] and A[i][k])) for i in range(n))


def next_state(A, x, delta, beta):
    y = []
    for i in range(len(A)):
        survive = 1.0 - (1.0 - delta) * x[i]
        for j in range(len(A)):
            if A[i][j]:
                survive *= 1.0 - beta * x[j]
        y.append(1.0 - survive)
    return y


def graph(n, edges):
    A = [[0] * n for _ in range(n)]
    for i, j in edges:
        A[i][j] = A[j][i] = 1
    return A


def run():
    tested = 0
    for n in range(2, 6):
        edges = list(itertools.combinations(range(n), 2))
        for mask in range(1, 1 << len(edges)):
            A = graph(n, [e for i, e in enumerate(edges) if (mask >> i) & 1])
            if not connected(A):
                continue
            rho, v = perron(A)
            for delta in (0.15, 0.32, 0.55, 0.83):
                beta = delta/rho
                actual = exact_quadratic(A, v, beta, delta)
                predicted = delta * (1-delta*(1+1/rho)/2) * sum(x**3 for x in v)
                assert abs(actual - predicted) < 1e-11, (n, mask, delta, actual, predicted)
                # Direct nonlinear map quadratic coefficient; noninteger interpolation.
                eps = 0.00002
                x = [eps*a for a in v]
                y = next_state(A, x, delta, beta)
                linear = [(1-delta)*x[i] + beta*sum(A[i][j]*x[j] for j in range(n)) for i in range(n)]
                drift = sum(v[i]*(linear[i]-y[i]) for i in range(n))/eps**2
                assert abs(drift-predicted) < 0.00013, (n, mask, drift, predicted)
                tested += 1

    samples = [
        ('edge', graph(2, [(0,1)])),
        ('three-vertex path', graph(3, [(0,1),(1,2)])),
        ('triangle', graph(3, [(0,1),(1,2),(2,0)])),
        ('four-leaf star', graph(5, [(0,1),(0,2),(0,3),(0,4)])),
        ('five-vertex path', graph(5, [(0,1),(1,2),(2,3),(3,4)]))
    ]
    delta = 0.4
    for name, A in samples:
        rho, v = perron(A)
        beta = delta/rho
        K = delta*(1-delta*(1+1/rho)/2)*sum(x**3 for x in v)
        # Nonaligned initial states, to check independence of starting profile.
        x = [0.11 + 0.31*(i+1)/(len(A)+1) for i in range(len(A))]
        T = 100000
        for _ in range(T):
            x = next_state(A, x, delta, beta)
        assert max(abs(T*x[i]/(v[i]/K) - 1) for i in range(len(A))) < 0.006, (name, x)
        assert 0 < K < delta * sum(z**3 for z in v)
        print('%s: rho=%.10f, K=%.10f, worst_relative_error_at_100000=%.7f'
            % (name, rho, K, max(abs(T*x[i]/(v[i]/K)-1) for i in range(len(A)))))
    print('PASS: %d graph-parameter coefficient and Taylor checks; 5 nonaligned critical asymptotic tests.' % tested)

if __name__ == '__main__':
    run()
