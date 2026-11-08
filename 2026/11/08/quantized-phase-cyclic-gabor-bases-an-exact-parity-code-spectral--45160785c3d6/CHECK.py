"""Direct-matrix finite reproducibility tests for discrete phase-alphabet Gabor fibers.
Run: python CHECK.py (requires numpy; see REQUIREMENTS.txt).
The finite tests corroborate, but do not prove, all-order identities.
"""
from itertools import product
from math import cos, pi, sin
import random
import numpy as np

checks = 0
for q in range(2, 9):
    for p in range(2, 6):
        counts = {}
        best = -1.0
        count_best = 0
        count_basis = 0
        trials = 0
        levels = [-0.11, 0.01, 0.19, 0.39, 0.61, 0.83, 1.11]
        for t in levels:
            counts[t] = 0
        for c in product(range(q), repeat=p):
            k = [(c[0] + c[-1]) % q] + [
                (c[r] - c[r - 1]) % q for r in range(1, p)
            ]
            A = 1 - max(abs(cos(pi * v / q)) for v in k)
            trials += 1
            if A > 1e-10:
                count_basis += 1
            if A > best + 1e-10:
                best, count_best = A, 1
            elif abs(A - best) < 1e-10:
                count_best += 1
            for t in levels:
                if A > t + 1e-10:
                    counts[t] += 1
        predicted_basis = (q-1)**p + ((-1)**p if q % 2 == 0 else 0)
        assert count_basis == predicted_basis, (p, q, count_basis)
        checks += 1
        if q % 2:
            predicted_best = 1 - sin(pi / (2*q))
            predicted_best_count = 2**p
        elif q % 4 == 0 or p % 2 == 0:
            predicted_best = 1.0
            predicted_best_count = 2
        elif q == 2:
            predicted_best = 0.0
            predicted_best_count = q**p
        else:
            predicted_best = 1 - sin(pi/q)
            predicted_best_count = 3**p + 1
        assert abs(predicted_best - best) < 1e-9
        assert count_best == predicted_best_count, (p, q, count_best, predicted_best_count)
        checks += 2
        for t in levels:
            K = [v for v in range(q) if 1-abs(cos(pi*v/q)) > t + 1e-10]
            D = sum((-1)**v for v in K)
            pred_count = len(K)**p + (D**p if q%2 == 0 else 0)
            assert pred_count == counts[t], (p, q, t, pred_count, counts[t])
            checks += 1

random.seed(846991)
for p in (2,3,4,5,7):
    N = 2*p
    for q in (2,3,4,6,7):
        for _ in range(18):
            x = [random.randrange(q) for _ in range(N)]
            g = np.array([np.exp(2j*pi*x[r]/q) for r in range(N)]) / np.sqrt(N)
            G = np.stack([
                np.array([np.exp(2j*pi*2*ell*j/N)*g[(j-k)%N] for j in range(N)])
                for k in (0,1) for ell in range(p)
            ], axis=1)
            eigenvalues = np.linalg.eigvalsh(G@G.conj().T)
            c = [(x[r]-x[r+p])%q for r in range(p)]
            k = [(c[0]+c[-1])%q] + [(c[r]-c[r-1])%q for r in range(1,p)]
            m = max(abs(cos(pi*v/q)) for v in k)
            assert abs(eigenvalues[0] - (1-m)) < 3e-12
            assert abs(eigenvalues[-1] - (1+m)) < 3e-12
            assert abs(eigenvalues.sum()-N) < 3e-12
            checks += 3
print(f'QUANTIZED_GABOR_TESTS_PASSED {checks}')
