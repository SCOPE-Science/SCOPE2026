"""Direct finite-matrix checks for the coordinate--Fourier erasure theorem.

Requires Python 3 and NumPy. Exact statements are proved in RESULT.md;
these tests are supplementary finite computations with tolerance 2e-9.
"""
import itertools
import math
import numpy as np

TOL = 2e-9
count = 0
count_two_two = 0

def prime(n):
    return all(n % d for d in range(2, math.isqrt(n) + 1))

for n in range(5, 14):
    j = np.arange(n)
    fourier = np.exp(2j * np.pi * np.outer(j, j) / n) / np.sqrt(n)
    frame = np.concatenate((np.eye(n, dtype=complex), fourier), axis=1)
    observed = {k: [3.0, 0] for k in range(1, 5)}
    for k in range(1, 5):
        for erased in itertools.combinations(range(2 * n), k):
            u = frame[:, erased]
            gram_eig = np.linalg.eigvalsh(u.conj().T @ u)
            lower = 2 - float(gram_eig[-1])
            rows = [t for t in erased if t < n]
            cols = [t - n for t in erased if t >= n]
            r, s = len(rows), len(cols)
            if r == 0 or s == 0:
                expected_lower = 1.0
            elif min(r, s) == 1:
                expected_lower = 1 - math.sqrt(r * s / n)
            else:
                assert (k, r, s) == (4, 2, 2)
                t = ((rows[0] - rows[1]) * (cols[0] - cols[1])) % n
                plus = math.sqrt((2 + 2 * abs(math.cos(math.pi * t / n))) / n)
                minus = math.sqrt((2 - 2 * abs(math.cos(math.pi * t / n))) / n)
                expected_lower = 1 - plus
                direct_spectrum = sorted([2 - float(x) for x in gram_eig] + [2.0] * (n - 4))
                predicted_spectrum = sorted([1-plus, 1+plus, 1-minus, 1+minus] + [2.0] * (n-4))
                assert max(abs(x-y) for x, y in zip(direct_spectrum, predicted_spectrum)) < TOL
                count_two_two += 1
            assert abs(lower - expected_lower) < TOL, (n, erased, lower, expected_lower)
            if lower < observed[k][0] - TOL:
                observed[k] = [lower, 1]
            elif abs(lower - observed[k][0]) < TOL:
                observed[k][1] += 1
            count += 1
    if prime(n):
        sigma = 2 * math.cos(math.pi / (2*n)) / math.sqrt(n)
        count4 = n*n*(n-1)//2
    else:
        sigma = 2 / math.sqrt(n)
        numerator = n*n*sum(math.gcd(h, n)-1 for h in range(1,n))
        assert numerator % 4 == 0
        count4 = numerator//4
    expected = [1., 1-1/math.sqrt(n), 1-math.sqrt(2/n), 1-sigma]
    expected_counts = [2*n, n*n, n*n*(n-1), count4]
    for k in range(1,5):
        assert abs(observed[k][0]-expected[k-1]) < TOL
        assert observed[k][1] == expected_counts[k-1], (n,k,observed[k][1],expected_counts[k-1])
    assert observed[4][0]>0
    print(f'N={n} four_erasure_min={observed[4][0]:.12f} attaining_masks={observed[4][1]}')

n=4
j=np.arange(n)
fourier=np.exp(2j*np.pi*np.outer(j,j)/n)/np.sqrt(n)
frame=np.concatenate((np.eye(n,dtype=complex),fourier),axis=1)
u=frame[:,[0,2,n,n+2]]
assert abs(2 - np.linalg.eigvalsh(u.conj().T@u)[-1]) < TOL
print(f'CHECK_OK total_masks={count} two_plus_two_spectra={count_two_two} dimension_four_boundary=singular')
