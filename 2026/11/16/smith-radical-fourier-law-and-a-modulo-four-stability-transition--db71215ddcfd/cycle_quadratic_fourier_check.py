"""Exact cyclotomic-integer checker for quadratic-cycle Fourier projections.

Run: python cycle_quadratic_fourier_check.py
The code uses only Python's standard library and exact integer arithmetic.
"""
from itertools import product


def radical_order(n, k, b):
    N = 1 << k
    if b % N == 0:
        return N ** n
    v = (b & -b).bit_length() - 1
    if n % 2:
        return 1 << (n * v + 1)
    if n % 4 == 2:
        return 1 << (n * v + 2)
    return 1 << (v * (n - 2) + 2 * k)


def sqnorm_of_phase_counts(counts):
    """Compute the exact squared norm in Z[zeta_(2^k)] as a basis vector.

    A primitive 2^k-th root satisfies zeta^(N/2)=-1; for k=1,
    the return vector has length one.
    """
    N = len(counts) * 2
    half = N // 2
    out = [0] * half
    for i, ai in enumerate(counts):
        if ai:
            for j, aj in enumerate(counts):
                if aj:
                    index = (i - j) % N
                    sign = -1 if index >= half else 1
                    out[index % half] += sign * ai * aj
    return out


def check_case(n, k):
    N = 1 << k
    G = list(product(range(N), repeat=n))
    phase_points = [(x, sum(x[i] * x[(i + 1) % n] for i in range(n)) % N) for x in G]
    actual_nonzero = 0
    expected_nonzero = 0
    sum_magnitudes_sq = 0
    for b in range(N):
        rad = radical_order(n, k, b)
        assert (N ** n) % rad == 0
        expected_per_b = (N ** n) // rad
        found_per_b = 0
        target_sq = N ** n * rad
        for a in G:
            coeff = [0] * (N // 2)
            for x, quadratic in phase_points:
                e = (b * quadratic + sum(a[i] * x[i] for i in range(n))) % N
                if e < N // 2:
                    coeff[e] += 1
                else:
                    coeff[e - N // 2] -= 1
            is_nonzero = any(coeff)
            # An exact cyclotomic equality and exact squared magnitude test.
            if is_nonzero:
                val = sqnorm_of_phase_counts(coeff)
                assert val[0] == target_sq and all(v == 0 for v in val[1:]), (n, k, a, b, val, target_sq)
                found_per_b += 1
                actual_nonzero += 1
                sum_magnitudes_sq += target_sq
        assert found_per_b == expected_per_b, (n, k, b, found_per_b, expected_per_b)
        expected_nonzero += expected_per_b
    assert expected_nonzero == actual_nonzero
    # Parseval for the unnormalized Fourier transform of a size-N^n set in N^(n+1) states.
    assert sum_magnitudes_sq == N ** (2 * n + 1)
    return f"PASS n={n},k={k},nonzero={actual_nonzero},ambient={N**(n+1)}"


def check_adjacency_kernel(n, k):
    """Count kernels of the cycle adjacency without using Smith normal form."""
    N = 1 << k
    for b in range(N):
        actual = sum(all((b * (x[(i-1) % n] + x[(i+1) % n])) % N == 0 for i in range(n))
                     for x in product(range(N), repeat=n))
        assert actual == radical_order(n, k, b), (n, k, b, actual)




def check_general_quadratic(c, N):
    """Check the radical law for a non-cycle quadratic form modulo N.

    The tested N are 2, 3, 4, or 5, so exact reduction uses a simple
    cyclotomic integral basis. No floating point operations are used.
    """
    d = len(c)
    points = list(product(range(N), repeat=d))
    def Q(x):
        return sum(c[i][j] * x[i] * x[j] for i in range(d) for j in range(i, d)) % N
    def polarization(h,y):
        return (Q(tuple((h[i]+y[i])%N for i in range(d))) - Q(h) - Q(y)) % N
    def sqnorm(phase_counts):
        cyc=[0]*N
        for i,ai in enumerate(phase_counts):
            for j,aj in enumerate(phase_counts):
                cyc[(i-j)%N] += ai*aj
        if N in (2,4):
            red=[cyc[i]-cyc[i+N//2] for i in range(N//2)]
        else:
            red=[cyc[i]-cyc[N-1] for i in range(N-1)]
        return red
    for b in range(N):
        rad=sum(all((b*polarization(h,y))%N==0 for y in points) for h in points)
        count=0
        for a in points:
            phases=[0]*N
            for x in points:
                phases[(sum(a[i]*x[i] for i in range(d))+b*Q(x))%N] += 1
            val=sqnorm(phases)
            if any(val):
                assert val[0] == N**d*rad and all(v==0 for v in val[1:])
                count+=1
        assert count == N**d//rad, (c,N,b,rad,count)
    return f"PASS general-form d={d},N={N}"


def main():
    for n, k in [(3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (5, 1), (6, 1), (8, 1)]:
        print(check_case(n, k))
        check_adjacency_kernel(n, k)
    for c,N in [([[1,1],[0,1]],2), ([[1,1],[0,1]],3),
                ([[2,3],[0,1]],4), ([[0,1,2],[0,0,1],[0,0,3]],5)]:
        print(check_general_quadratic(c,N))
    print('CYCLE_QUADRATIC_FOURIER_EXACT_PASS')


if __name__ == '__main__':
    main()
