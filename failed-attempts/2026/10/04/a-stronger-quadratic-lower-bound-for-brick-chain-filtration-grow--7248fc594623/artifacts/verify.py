#!/usr/bin/env python3
import math
from math import factorial, lgamma


def hook_direct(n: int) -> int:
    # Rectangle with 2n rows and n columns.
    h = 1
    rows, cols = 2*n, n
    for i in range(rows):
        for j in range(cols):
            h *= (rows - i) + (cols - j) - 1
    return h


def hook_factorial(n: int) -> int:
    # H((n)^(2n)) = product_{i=0}^{2n-1} (n+i)!/i!.
    num = 1
    den = 1
    for i in range(2*n):
        num *= factorial(n+i)
        den *= factorial(i)
    return num // den


def log_lower_bound(n: int) -> float:
    d = 2*n*n
    log_h = sum(lgamma(n+i+1) - lgamma(i+1) for i in range(2*n))
    return d*math.log(6.0) + lgamma(d+1) - 2.0*log_h


def main() -> None:
    for n in range(1, 11):
        hd = hook_direct(n)
        hf = hook_factorial(n)
        assert hd == hf

    coeff = 4.0 + 8.0*math.log(2.0) - 7.0*math.log(3.0)
    normalized = coeff / 121.0
    source_endpoint = (1.0 - math.log(2.0)) / 25.0
    assert coeff > 0.0
    assert normalized > source_endpoint

    print('RECTANGLE_HOOK_CHECK_OK n=1..10')
    print(f'COEFFICIENT={coeff:.15f}')
    print(f'NORMALIZED_CONSTANT={normalized:.15f}')
    print(f'SOURCE_Q3_ENDPOINT={source_endpoint:.15f}')
    print(f'RELATIVE_IMPROVEMENT_OVER_SOURCE={(normalized/source_endpoint-1.0):.12f}')
    for n in (10, 25, 50, 100, 200):
        scaled = log_lower_bound(n)/(n*n)
        norm_scaled = log_lower_bound(n)/(121.0*n*n)
        print(f'n={n} LOG_L_OVER_N2={scaled:.12f} NORMALIZED={norm_scaled:.12f}')
    # Dimension-vector and composition-length identities for the chosen family.
    for n in range(1, 21):
        a, b, q = 2*n, n, 7
        alpha = (a + (q-1)*b, a+b)
        assert alpha == (8*n, 3*n)
        assert sum(alpha) == 11*n
    print('DIMENSION_VECTOR_CHECK_OK n=1..20')
    print('CHECK_OK')


if __name__ == '__main__':
    main()
