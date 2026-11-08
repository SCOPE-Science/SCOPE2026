"""Independent numerical diagnostics for the even-grid Fourier heat-kernel theorem.

Requires Python 3 and mpmath. The asymptotic theorem is proved analytically;
these computations test formulas and finite-grid illustrations only.
"""
import mpmath as mp

mp.mp.dps = 110


def truncated_kernel(n, j, t):
    assert n >= 4 and n % 2 == 0 and 0 <= j < n
    kmax = n // 2
    theta = 2 * mp.pi * j / n
    s = mp.mpf(1) + 2 * sum(
        mp.exp(-(k*k)*t) * mp.cos(k*theta) for k in range(1, kmax)
    ) + mp.exp(-(kmax*kmax)*t) * (-1)**j
    return s / n


def full_theta(t, x):
    return mp.sqrt(mp.pi / t) * sum(
        mp.exp(-(x - 2*mp.pi*k)**2 / (4*t)) for k in range(-12, 13)
    )


def assert_small(actual, expected, tol=mp.mpf('1e-70')):
    assert abs(actual - expected) < tol, (actual, expected)


def main():
    count = 0
    for n in (8, 12, 16, 20, 32, 48, 64, 80):
        for c in (mp.mpf('2.8'), mp.mpf('3.5')):
            t = c / n
            # The Fourier representation and periodized Gaussian are identical.
            for j in (0, 1, n//4, n//2):
                x = 2 * mp.pi * j / n
                fourier_theta = 1 + 2*sum(
                    mp.exp(-k*k*t)*mp.cos(k*x) for k in range(1, 750)
                )
                assert_small(full_theta(t, x), fourier_theta)
                count += 1
            # The circulant propagation preserves mass exactly.
            assert_small(sum(truncated_kernel(n,j,t) for j in range(n)), 1)
            count += 1
            # Quantified correction bound for the omitted high frequencies.
            for j in (0, 1, n//2):
                x = 2 * mp.pi * j / n
                difference = abs(full_theta(t,x) - n*truncated_kernel(n,j,t))
                bound = mp.exp(-n*n*t/4)*mp.coth(n*t/2)
                assert difference < bound * (1+mp.mpf('1e-65'))
                count += 1
        j_even_near_antipode = 2*(n//4)
        if n >= 12:
            assert truncated_kernel(n, j_even_near_antipode, mp.mpf('2.8')/n) < 0
            count += 1
        for j in range(n):
            assert truncated_kernel(n, j, mp.mpf('3.5')/n) > 0
            count += 1
    for n in (40, 80, 160, 320):
        c = mp.mpf('2.8')
        x = 2*mp.pi*(2*(n//4))/n
        B = 1+2*sum(mp.exp(-c*l-c*l*l/n)*mp.cos(l*x)
                    for l in range(1, 150))
        # Convergence to the positive limiting excluded-tail coefficient.
        assert B > 0 and abs(B-mp.tanh(c/2)) < mp.mpf('4')/n
        count += 1
    print('PASS:', count, 'high-precision checks')
    for n in (12, 32, 64, 80):
        j = 2*(n//4)
        print('N=', n, 'j=', j, 'negative=',
              mp.nstr(truncated_kernel(n,j,mp.mpf('2.8')/n), 10),
              'positive=', mp.nstr(truncated_kernel(n,j,mp.mpf('3.5')/n), 10))


if __name__ == '__main__':
    main()
