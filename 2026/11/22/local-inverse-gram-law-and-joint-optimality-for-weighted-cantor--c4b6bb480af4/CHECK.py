#!/usr/bin/env python3
"""Independent finite-matrix checks for binary-digit Fourier sampling."""
import itertools
import math
import numpy as np


def make_matrix(base, gap, steps, probs):
    n = len(steps)
    assert len(probs) == n
    bits = list(itertools.product((0, 1), repeat=n))
    points = [gap * sum(digit / (base ** (j + 1)) for j, digit in enumerate(word)) for word in bits]
    freqs = [sum(steps[j] * word[j] * (base ** j) for j in range(n)) for word in bits]
    weights = [math.prod(probs[j] if digit == 0 else 1 - probs[j]
                         for j, digit in enumerate(word)) for word in bits]
    return np.exp(2j * math.pi * np.outer(freqs, points)) * np.sqrt(weights)[None, :]


def inverse_trace_pred(base, gap, steps, probs):
    return math.prod(1.0 / (2*p*(1-p)*math.sin(math.pi*gap*t/base)**2)
                     for t,p in zip(steps, probs))


def is_singular_digit(base, gap, steps):
    return any((gap*t) % base == 0 for t in steps)


def check():
    count = 0
    for base, gap in [(3, 2), (4, 1), (5, 2), (6, 2), (7, 3), (8, 2), (9, 3), (10, 4)]:
        good_steps = [t for t in range(1, base) if gap*t % base != 0]
        for n in range(1, 5):
            for r in range(8):
                steps = [good_steps[(r+j*3) % len(good_steps)] for j in range(n)]
                probs = [0.22 + 0.14*((r+j*2) % 5) for j in range(n)]
                mat = make_matrix(base, gap, steps, probs)
                inv = np.linalg.inv(mat)
                direct = float(np.linalg.norm(inv, 'fro')**2)
                predicted = inverse_trace_pred(base, gap, steps, probs)
                assert np.isclose(direct, predicted, rtol=2e-6, atol=1e-7), (base,gap,n,r,direct,predicted)
                count += 1
                spatial_bits = list(itertools.product((0, 1), repeat=n))
                actual_diag = np.sum(np.abs(inv)**2, axis=1)
                predicted_diag = [math.prod(1.0 / (2*(probs[j] if bit == 0 else 1-probs[j])*
                                                  math.sin(math.pi*gap*steps[j]/base)**2)
                                            for j, bit in enumerate(word))
                                  for word in spatial_bits]
                assert np.allclose(actual_diag, predicted_diag, rtol=2e-6, atol=1e-7), (base,gap,n,r)
                count += 1
                det = abs(np.linalg.det(mat))
                assert np.isclose(direct/(2**n), det**(-4/(2**n)), rtol=2e-6,atol=1e-7), (base,gap,n,r,det)
                count += 1
                assert np.isclose(np.linalg.norm(mat,'fro')**2, 2**n, atol=1e-10)
                count += 1
                q = base // math.gcd(base,gap)
                s_q = 1.0 if q % 2 == 0 else math.cos(math.pi/(2*q))
                assert direct/(2**n) >= s_q**(-2*n)-1e-9
                count += 1
        for t in range(1,base):
            if (gap*t)%base == 0:
                assert np.linalg.matrix_rank(make_matrix(base,gap,[t],[0.5]),tol=1e-8)==1
                count += 1
    # Special canonical odd-base example, depth five.
    for n in range(1,6):
        mat=make_matrix(3,2,[1]*n,[0.5]*n)
        direct=np.linalg.norm(np.linalg.inv(mat),'fro')**2/(2**n)
        assert np.isclose(direct,(4/3)**n,rtol=1e-8)
        count += 1
    # Exhaust the finite digit-choice optimizers at depths 1,2,3 for moderate bases.
    for base,gap in [(3,2),(4,1),(5,2),(6,2),(7,3),(8,2)]:
        q=base//math.gcd(base,gap)
        s_q=1 if q%2==0 else math.cos(math.pi/(2*q))
        for n in (1,2,3):
            best=math.inf
            for steps in itertools.product(range(1,base),repeat=n):
                if is_singular_digit(base,gap,steps):continue
                val=math.prod(math.sin(math.pi*gap*t/base)**(-2) for t in steps)
                best=min(best,val)
                assert val >= s_q**(-2*n)-1e-10
                count += 1
            assert math.isclose(best,s_q**(-2*n),rel_tol=1e-10)
            count += 1
    print('INDEPENDENT_WEIGHTED_CANTOR_INVERSE_TRACE_CHECKS_PASSED',count)
if __name__ == '__main__':
    check()
