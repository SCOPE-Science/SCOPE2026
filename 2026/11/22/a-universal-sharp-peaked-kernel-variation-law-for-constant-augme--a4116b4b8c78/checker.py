"""Finite numerical checks for sharp localized-kernel variation asymptotics.

Python 3 standard library only. This is illustrative, not a proof of the limit.
"""
import math
import random


def solve(a, b):
    a = [list(map(float, row)) + [float(v)] for row, v in zip(a, b)]
    n = len(a)
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(a[i][k]))
        assert abs(a[p][k]) > 1e-12
        a[k], a[p] = a[p], a[k]
        inv = 1.0 / a[k][k]
        for j in range(k, n + 1):
            a[k][j] *= inv
        for i in range(n):
            if i == k:
                continue
            t = a[i][k]
            for j in range(k, n + 1):
                a[i][j] -= t * a[k][j]
    return [a[i][-1] for i in range(n)]


def interpolant(nodes, values, scale, profile):
    n = len(nodes)
    mat = [[profile(scale * abs(x-z)) for z in nodes] + [1.0] for x in nodes]
    mat.append([1.0] * n + [0.0])
    c = solve(mat, values + [0.0])
    def evaluate(x):
        return c[-1] + sum(c[i]*profile(scale*abs(x-nodes[i])) for i in range(n))
    return evaluate


def numerical_var(f, nodes, samples_per_cell=5000):
    z = [nodes[0]]
    for a,b in zip(nodes,nodes[1:]):
        z.extend(a+(b-a)*i/samples_per_cell for i in range(1,samples_per_cell+1))
    v = [f(x) for x in z]
    return sum(abs(b-a) for a,b in zip(v,v[1:]))


def predicted(n):
    return 4*(n*n//4)/n - 1


def check():
    profiles = {
        'Gaussian': lambda t: math.exp(-t*t),
        'Laplace': lambda t: math.exp(-t),
    }
    grids = {
       2: [0., 1.3],
       3: [0., 0.7, 2.1],
       4: [0., 0.9, 1.8, 3.3],
       5: [0., 0.65, 1.5, 2.6, 3.9],
       6: [0., 0.55, 1.3, 2.2, 3.2, 4.4],
       7: [0., 0.6, 1.35, 2.2, 3.35, 4.25, 5.7],
       8: [0., 0.6, 1.4, 2.2, 3.1, 4.0, 5.2, 6.5],
    }
    random.seed(3211)
    for kind,profile in profiles.items():
        for n,nodes in grids.items():
            # Effective width is much less than the smallest gap.
            h = min(b-a for a,b in zip(nodes,nodes[1:]))
            scale = 12.0 / h
            vals = [1.] * n
            ident = interpolant(nodes, vals, scale, profile)
            assert max(abs(ident(x)-1.) for x in nodes) < 2e-10
            step_variations = []
            for j in range(1,n):
                y = [0.]*j+[1.]*(n-j)
                f = interpolant(nodes,y,scale,profile)
                assert max(abs(f(x)-v) for x,v in zip(nodes,y)) < 2e-10
                step_variations.append(numerical_var(f,nodes,1800))
            k = max(step_variations)
            goal = predicted(n)
            assert abs(k-goal) < 0.035, (kind,n,k,goal)
            assert max(range(1,n),key=lambda j:step_variations[j-1]) in [n//2,(n+1)//2]
            # A fixed-scale finite-dimensional linear operator is maximized by a step.
            for _ in range(5):
                y = [random.uniform(-1,1) for _ in nodes]
                f = interpolant(nodes,y,scale,profile)
                v0 = sum(abs(y[i+1]-y[i]) for i in range(n-1))
                assert numerical_var(f,nodes,1800) <= (k+1e-8)*v0
            print(kind, n, f'finite_scale_norm={k:.6f}', f'limit={goal:.6f}')
    print('ALL_LOCALIZED_KERNEL_VARIATION_CHECKS_PASS')

if __name__ == '__main__':
    check()
